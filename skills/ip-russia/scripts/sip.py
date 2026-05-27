#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

"""kad.arbitr.ru (СИП — Court for Intellectual Property) CLI.

Searches arbitration court cases. Returns structured JSON or compact table.

Note: kad.arbitr.ru uses DDoS-Guard. Two ways to pass cookies:
1. --cookie "..." — manually paste from browser DevTools
2. --cdp — auto-extract from running Chromium via CDP (preferred)
"""

import argparse
import json
import sys

import httpx
from bs4 import BeautifulSoup

BASE = "https://kad.arbitr.ru"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"

COURT_CODES = {"sip": "SIP", "vs_rf": "VS_RF", "all": None}

CASE_TYPES = {"administrative", "civil", "civil_simple"}

EPilog = """\
examples:
  %(prog)s search -p "Сбербанк"                              # Search by party name
  %(prog)s search -p "Сбербанк" -c sip -f full               # Full JSON output, SIP only
  %(prog)s search -p "Сбербанк" --cookie "session=..."        # With browser cookies
  %(prog)s search -p "Сбербанк" --cdp                         # Auto-extract cookies via CDP
  %(prog)s search --judge "Пашкова" --cdp                      # Search by judge with CDP cookies
  %(prog)s search -p "Яндекс" --date-from 2024-01-01          # Date-filtered search
"""


def _parse_cookies(cookie_str: str) -> dict:
    return dict(p.strip().split("=", 1) for p in cookie_str.split(";") if "=" in p)


def _get_cookies_cdp(cdp_url: str = "http://localhost:9222") -> dict:
    """Extract kad.arbitr.ru cookies from a running Chromium via CDP.

    Requires Chromium launched with --remote-debugging-port=9222
    and kad.arbitr.ru opened in a tab (DDoS-Guard must have been passed).
    """
    import subprocess

    # Find WebSocket URL via CDP endpoint
    try:
        resp = httpx.get(f"{cdp_url}/json")
        tabs = resp.json()
    except httpx.ConnectError:
        print("Cannot connect to CDP. Launch Chromium with --remote-debugging-port=9222", file=sys.stderr)
        sys.exit(1)

    # Find a tab with kad.arbitr.ru or use the first tab
    ws_url = None
    for tab in tabs:
        if "kad.arbitr.ru" in tab.get("url", ""):
            ws_url = tab.get("webSocketDebuggerUrl")
            break
    if not ws_url and tabs:
        ws_url = tabs[0].get("webSocketDebuggerUrl")

    if not ws_url:
        print("No CDP tabs found.", file=sys.stderr)
        sys.exit(1)

    # Use playwright-cli to extract cookies if available
    try:
        result = subprocess.run(
            ["npx", "playwright-cli", "--raw", "cookie-list", "--domain=kad.arbitr.ru"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return _parse_cookies(result.stdout.strip())
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: use CDP Network.getAllCookies via raw websocket
    print("Tip: use playwright-cli for easier cookie extraction.", file=sys.stderr)
    print("Run: playwright-cli --raw cookie-list --domain=kad.arbitr.ru", file=sys.stderr)
    return {}


def _make_client(cookies: dict | None = None) -> httpx.Client:
    client = httpx.Client(
        base_url=BASE,
        headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9,ru;q=0.8"},
        follow_redirects=True,
        timeout=30.0,
    )
    if cookies:
        for k, v in cookies.items():
            client.cookies.set(k, v, domain="kad.arbitr.ru")
    else:
        resp = client.get("/")
        if resp.status_code == 451:
            print("DDoS-Guard blocked. Use --cookie or --cdp.", file=sys.stderr)
    return client


def _do_search(client: httpx.Client, body: dict) -> tuple[list[dict], dict]:
    resp = client.post(
        "/Kad/SearchInstances",
        json=body,
        headers={
            "X-Requested-With": "XMLHttpRequest",
            "x-date-format": "iso",
            "Referer": f"{BASE}/",
            "Origin": BASE,
        },
    )
    if resp.status_code == 451:
        print("DDoS-Guard blocked. Use --cookie or --cdp.", file=sys.stderr)
        resp.raise_for_status()
    resp.raise_for_status()
    return _parse_results(resp.text)


def _parse_results(html: str) -> tuple[list[dict], dict]:
    soup = BeautifulSoup(html, "html.parser")
    cases = []

    for row in soup.select("tr"):
        cells = row.find_all("td")
        if len(cells) < 4:
            continue

        case = {}

        link = cells[0].select_one("a.num_case")
        if not link:
            continue
        case["number"] = link.get_text(strip=True)
        href = link.get("href", "")
        case["card_url"] = href if href.startswith("http") else f"{BASE}{href}"

        date_div = cells[0].select_one(", ".join(f"div.{t}" for t in CASE_TYPES))
        if date_div:
            title = date_div.get("title", "")
            case["date"] = title.split(" ")[0] if title else ""
            cls = date_div.get("class", [])
            case["type"] = next((t for t in CASE_TYPES if t in cls), "unknown")
        else:
            case["date"] = ""
            case["type"] = "unknown"

        judge_div = cells[1].select_one("div.judge")
        case["judge"] = judge_div.get("title", "") if judge_div else ""
        for cd in cells[1].select("div[title]"):
            if "judge" not in cd.get("class", []):
                case["court"] = cd.get("title", "")
                break

        case["plaintiffs"] = [
            s.contents[0].strip()
            for s in cells[2].select("span.js-rollover")
            if s.contents and s.contents[0].strip()
        ]
        case["respondents"] = [
            s.contents[0].strip()
            for s in cells[3].select("span.js-rollover")
            if s.contents and s.contents[0].strip()
        ]

        cases.append(case)

    meta = {}
    for fid, key in [("documentsTotalCount", "total"), ("documentsPagesCount", "pages"), ("documentsPage", "current_page")]:
        el = soup.select_one(f"#{fid}")
        if el:
            meta[key] = int(el.get("value", "0"))

    return cases, meta


def search(client: httpx.Client, courts=None, party=None, role=-1,
           exact=False, judge=None, date_from=None, date_to=None,
           page=1, count=25) -> dict:
    if courts is None:
        courts = ["SIP"]

    sides = [{"Name": party, "Type": role, "ExactMatch": exact}] if party else []

    body = {
        "Page": page,
        "Count": min(count, 25),
        "Courts": courts,
        "DateFrom": date_from,
        "DateTo": date_to,
        "Sides": sides,
        "Judges": [judge] if judge else [],
        "CaseNumbers": [],
        "WithVKSInstances": False,
    }

    cases, meta = _do_search(client, body)
    return {"cases": cases, "meta": meta}


def _print_short(result):
    for c in result["cases"]:
        pl = " | ".join(c.get("plaintiffs", [])[:2])
        print(f"{c['number']:20s} {c.get('date',''):12s} {c.get('type',''):15s} {pl}")
    m = result.get("meta", {})
    if m:
        print(f"\nTotal: {m.get('total','?')} | Page {m.get('current_page','?')}/{m.get('pages','?')}")


def cmd_search(args):
    courts = [COURT_CODES.get(c.lower(), c) or c for c in args.courts]
    courts = [c for c in courts if c]

    # Determine cookies: --cdp > --cookie > none
    cookie_dict = None
    if args.cdp:
        cookie_dict = _get_cookies_cdp()
        if not cookie_dict:
            print("Failed to extract cookies via CDP. Is Chromium running with kad.arbitr.ru open?", file=sys.stderr)
            sys.exit(1)
    elif args.cookie:
        cookie_dict = _parse_cookies(args.cookie)

    client = _make_client(cookie_dict)

    try:
        result = search(
            client, courts=courts, party=args.party, role=args.role,
            exact=args.exact, judge=args.judge,
            date_from=args.date_from, date_to=args.date_to,
            page=args.page, count=args.count,
        )
    except httpx.HTTPStatusError as e:
        print(f"Error: {e.response.status_code} — {e.response.text[:200]}", file=sys.stderr)
        sys.exit(1)

    if args.format == "short":
        _print_short(result)
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()

    client.close()


def main():
    p = argparse.ArgumentParser(
        description="kad.arbitr.ru (СИП) case search",
        epilog=EPilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("search", help="Search arbitration cases",
                        epilog=EPilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    s.add_argument("--cookie", help="Cookie header from browser DevTools")
    s.add_argument("--cdp", action="store_true",
                    help="Auto-extract cookies from Chromium via CDP (requires --remote-debugging-port)")
    s.add_argument("-p", "--party", help="Party name (plaintiff or respondent)")
    s.add_argument("--role", type=int, default=-1, help="-1=any, 0=plaintiff, 1=respondent")
    s.add_argument("--exact", action="store_true", help="Exact name match")
    s.add_argument("-c", "--courts", nargs="+", default=["sip"], help="sip, vs_rf, all")
    s.add_argument("--judge", help="Judge surname")
    s.add_argument("--date-from", help="YYYY-MM-DD")
    s.add_argument("--date-to", help="YYYY-MM-DD")
    s.add_argument("--page", type=int, default=1)
    s.add_argument("--count", type=int, default=25, help="Max 25")
    s.add_argument("-f", "--format", default="short", choices=["short", "full"])
    s.set_defaults(func=cmd_search)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
