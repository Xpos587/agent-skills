#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

"""FIPS register document viewer.

Looks up IP documents by registration number.
Search by registration number, publication date, or MKPO index.

Note: fips.ru uses DDoS-Guard. Use --cookie to pass browser cookies,
or --cdp to auto-extract from a running Chromium instance.
"""

import argparse
import json
import sys
import re

import httpx
from bs4 import BeautifulSoup

BASE = "https://fips.ru"
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"

# FIPS register database codes
DB_CODES = {
    "rude": "RUDE",        # Industrial designs (промышленные образцы)
    "rutm": "RUTM",        # Trademarks (товарные знаки)
    "rupat": "RUPAT",      # Inventions (изобретения)
    "rupm": "RUPM",        # Utility models (полезные модели)
    "evm": "EVM",          # Computer programs (программы для ЭВМ)
    "rugp": "RUGP",        # Geographical indications (ГУ/НМПТ)
    "rudeap": "RUDEAP",    # Design applications
    "vz": "VZ",            # Topographies (топологии ИМС)
    "pravo": "PRAVO",      # Legal documents
}

EPilog = """\
examples:
  %(prog)s get 106651 -d rude                              # Industrial design (no cookie needed)
  %(prog)s get 123456 -d rutm --cookie "..."              # Trademark
  %(prog)s get 123456 -d rutm --cdp                        # Trademark (auto-extract cookies)
  %(prog)s get 2761234 -d rupat --cookie "..."            # Invention patent
  %(prog)s search number 106651 -d rude --cookie "..."    # Search (experimental, may be empty)
  %(prog)s dbs                                              # List databases
"""

SEARCH_PARAMS = {
    "number": "par_15",    # Registration number
    "date": "par_4",       # Publication date
    "mkpo": "par_8",      # MKPO index (International Classification for Industrial Designs)
}

# NOTE: FIPS search uses Java servlet session state. HTTP search
# may return empty results. Prefer `get` for known document numbers.


def _parse_cookies(cookie_str: str) -> dict:
    return dict(p.strip().split("=", 1) for p in cookie_str.split(";") if "=" in p)


def _get_cookies_cdp(cdp_url: str = "http://localhost:9222") -> dict:
    """Extract fips.ru cookies from running Chromium via CDP."""
    import subprocess
    try:
        result = subprocess.run(
            ["npx", "playwright-cli", "--raw", "cookie-list", "--domain=fips.ru"],
            capture_output=True, text=True, timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return _parse_cookies(result.stdout.strip())
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    print("CDP cookie extraction failed. Is Chromium running with fips.ru open?", file=sys.stderr)
    return {}


def _make_client(cookies: dict | None = None) -> httpx.Client:
    client = httpx.Client(
        base_url=BASE,
        headers={"User-Agent": UA, "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8"},
        follow_redirects=True,
        timeout=30.0,
    )
    if cookies:
        for k, v in cookies.items():
            client.cookies.set(k, v, domain="fips.ru")
    else:
        resp = client.get("/registers-web/")
        if resp.status_code == 451:
            print("DDoS-Guard blocked. Use --cookie from browser.", file=sys.stderr)
    return client


def get_document(client: httpx.Client, db: str, doc_number: int | str,
                 rn: int = 147, type_file: str = "html") -> dict:
    """Fetch a document from FIPS register by doc number."""
    resp = client.get(
        "/registers-doc-view/fips_servlet",
        params={"DB": db, "rn": str(rn), "DocNumber": str(doc_number), "TypeFile": type_file},
    )
    if resp.status_code == 451:
        print("DDoS-Guard blocked. Use --cookie from browser.", file=sys.stderr)
    resp.raise_for_status()
    return _parse_document(resp.text, doc_number, db)


def search_by_param(client: httpx.Client, db: str, param: str, value: str,
                    rn: int = 147) -> dict:
    """Search FIPS register via HTTP (may return empty results)."""
    param_code = SEARCH_PARAMS.get(param)
    if not param_code:
        print(f"Error: unknown param '{param}'. Use: number, date, mkpo", file=sys.stderr)
        sys.exit(1)

    resp = client.get(
        "/registers-web/action",
        params={"acName": "clickRegister", "regName": db},
    )
    if resp.status_code == 451:
        print("DDoS-Guard blocked. Use --cookie from browser.", file=sys.stderr)
    resp.raise_for_status()

    form_data = {
        "searchPar": param_code,
        "searchParValue": value,
        "DB": db,
        "DocNumber": "0",
        "TypeFile": "html",
    }

    resp = client.post(
        "/registers-web/action",
        data=form_data,
        headers={"Referer": f"{BASE}/registers-web/action?acName=clickRegister&regName={db}"},
    )
    if resp.status_code == 451:
        print("DDoS-Guard blocked. Use --cookie from browser.", file=sys.stderr)
    resp.raise_for_status()

    return _parse_search_results(resp.text, db)



def _parse_document(html: str, doc_number: str, db: str) -> dict:
    """Parse a FIPS document page into structured data."""
    soup = BeautifulSoup(html, "html.parser")

    result = {"db": db, "doc_number": str(doc_number)}

    # Title
    title = soup.find("title")
    if title:
        result["title"] = title.get_text(strip=True)

    # Extract text content from mainDoc div
    main_doc = soup.select_one("div#mainDoc")
    if main_doc:
        text = main_doc.get_text(separator="\n", strip=True)
        # Truncate to reasonable size
        result["text"] = text[:5000] if len(text) > 5000 else text

    # Extract tables for key-value data
    tables = soup.select("table")
    data_pairs = {}
    for table in tables:
        for row in table.select("tr"):
            cells = row.find_all("td")
            if len(cells) == 2:
                key = cells[0].get_text(strip=True)
                val = cells[1].get_text(strip=True)
                if key and val and len(key) < 100:
                    data_pairs[key] = val

    if data_pairs:
        result["fields"] = data_pairs

    return result


def _parse_search_results(html: str, db: str) -> dict:
    """Parse FIPS search results page."""
    soup = BeautifulSoup(html, "html.parser")

    results = []

    # Find document links
    for link in soup.select("a[href*='DocNumber']"):
        href = link.get("href", "")
        doc_m = re.search(r"DocNumber=(\d+)", href)
        if doc_m:
            text = link.get_text(strip=True)
            results.append({
                "doc_number": doc_m.group(1),
                "url": href if href.startswith("http") else f"{BASE}{href}",
                "description": text,
            })

    # Pagination info
    pagination = soup.select_one("div.pagination, div.pager, span.pageInfo")
    meta = {}
    if pagination:
        meta["pagination_text"] = pagination.get_text(strip=True)

    return {"db": db, "results": results, "meta": meta}


def cmd_get(args):
    db = DB_CODES.get(args.db.lower(), args.db)
    if args.cdp:
        cookie_dict = _get_cookies_cdp()
    elif args.cookie:
        cookie_dict = _parse_cookies(args.cookie)
    else:
        cookie_dict = None
    client = _make_client(cookie_dict)

    try:
        doc = get_document(client, db, args.number, rn=args.rn, type_file=args.type)
    except httpx.HTTPStatusError as e:
        print(f"Error: {e.response.status_code} — {e.response.text[:200]}", file=sys.stderr)
        sys.exit(1)

    if args.format == "short":
        print(f"DB: {doc.get('db', '?')} | Doc: {doc.get('doc_number', '?')} | Title: {doc.get('title', 'N/A')}")
        if doc.get("fields"):
            for k, v in list(doc["fields"].items())[:10]:
                print(f"  {k}: {v}")
        if doc.get("text"):
            lines = doc["text"].split("\n")
            for line in lines[:20]:
                if line.strip():
                    print(f"  {line.strip()}")
    else:
        json.dump(doc, sys.stdout, ensure_ascii=False, indent=2)
        print()

    client.close()


def cmd_search(args):
    db = DB_CODES.get(args.db.lower(), args.db)
    if args.cdp:
        cookie_dict = _get_cookies_cdp()
    elif args.cookie:
        cookie_dict = _parse_cookies(args.cookie)
    else:
        cookie_dict = None
    client = _make_client(cookie_dict)

    try:
        result = search_by_param(client, db, args.param, args.value, rn=args.rn)
    except httpx.HTTPStatusError as e:
        print(f"Error: {e.response.status_code} — {e.response.text[:200]}", file=sys.stderr)
        sys.exit(1)

    client.close()

    if args.format == "short":
        for r in result.get("results", []):
            print(f"{r['doc_number']:>10s}  {r['description']}")
        if result.get("meta", {}).get("pagination_text"):
            print(f"\n{result['meta']['pagination_text']}")
    else:
        json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
        print()

    client.close()


def cmd_dbs(args):
    """List available register databases."""
    for code, name in DB_CODES.items():
        print(f"  {code:10s}  {name}")


def main():
    p = argparse.ArgumentParser(
        description="FIPS register document viewer",
        epilog=EPilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="command", required=True)

    # get - fetch document by number
    g = sub.add_parser("get", help="Fetch document by registration number",
                        epilog=EPilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    g.add_argument("number", help="Document/registration number (e.g. 106651)")
    g.add_argument("-d", "--db", default="rude", choices=list(DB_CODES.keys()),
                   help="Register database (default: rude)")
    g.add_argument("--rn", type=int, default=147, help="Result number (default: 147)")
    g.add_argument("--type", dest="type", default="html", choices=["html", "pdf"],
                   help="Document format (default: html)")
    g.add_argument("--cookie", help="Cookie header from browser DevTools")
    g.add_argument("--cdp", action="store_true",
                    help="Auto-extract cookies from Chromium via CDP")
    g.add_argument("-f", "--format", default="short", choices=["short", "full"])
    g.set_defaults(func=cmd_get)

    # search - search by parameter (experimental)
    s = sub.add_parser("search", help="Search register (experimental — prefer 'get' for known numbers)",
                       epilog=EPilog, formatter_class=argparse.RawDescriptionHelpFormatter)
    s.add_argument("param", choices=["number", "date", "mkpo"],
                   help="Search parameter: number (reg number), date (publication date), mkpo (MKPO index)")
    s.add_argument("value", help="Search value")
    s.add_argument("-d", "--db", default="rude", choices=list(DB_CODES.keys()),
                   help="Register database (default: rude)")
    s.add_argument("--rn", type=int, default=147)
    s.add_argument("--cookie", help="Cookie header from browser DevTools")
    s.add_argument("--cdp", action="store_true",
                    help="Auto-extract cookies from Chromium via CDP")
    s.add_argument("-f", "--format", default="short", choices=["short", "full"])
    s.set_defaults(func=cmd_search)

    # dbs - list databases
    d = sub.add_parser("dbs", help="List available register databases")
    d.set_defaults(func=cmd_dbs)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()