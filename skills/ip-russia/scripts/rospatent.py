#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
# ]
# ///

"""Rospatent Search Platform CLI.

Search patents, trademarks, programs, topologies, designs.
No authentication required — public API.
"""

import argparse
import json
import sys
import time

import httpx

BASE = "https://searchplatform.rospatent.gov.ru"

DATASETS = {
    "patents_ru": ["ru_since_1994", "ru_till_1994"],
    "designs_ru": ["dsgn_ru"],
    "programs": ["programs"],
    "topologies": ["topologies"],
    "copyrights_db": ["copyrights_db"],
    "related_rights_db": ["related_rights_db"],
    "patents_all": ["ru_since_1994", "ru_till_1994", "us", "ep", "cn", "de", "fr", "gb", "jp", "kr", "pct"],
}

FMT_FIELDS = {
    "short": ["id", "title", "applicant", "date", "ipc"],
    "full": None,
}

ROOT_EPILOG = """\
examples:
  %(prog)s search "нейронная сеть" -d patents_ru           # Russian patents
  %(prog)s search "антивирус" -d programs                    # Computer programs
  %(prog)s sources                                           # List datasets
  %(prog)s sources --integral                                # Non-patent sources
  %(prog)s suggest "нейро"                                   # Autocomplete
"""

SEARCH_EPILOG = """\
examples:
  %(prog)s "нейронная сеть" -d patents_ru           # Russian patents
  %(prog)s "антивирус" -d programs                    # Computer programs
  %(prog)s "Сбер" -d patents_ru -f full              # Full output
  %(prog)s "дизайн упаковки" -d designs_ru            # Industrial designs
"""


def _client() -> httpx.Client:
    return httpx.Client(base_url=BASE, timeout=30.0)


def search(qn: str, datasets: list[str], lang: str = "ru", limit: int = 10,
           offset: int = 0, sort: str = "relevance") -> dict:
    body = {
        "qn": qn,
        "offset": offset,
        "limit": limit,
        "sort": sort,
        "include_facets": 0,
        "highlight": {"profiles": ["_searchquery_"]},
        "countStatistics": True,
        "datasets": datasets,
        "preffered_lang": lang,
    }
    with _client() as c:
        resp = c.post(f"/search?t={int(time.time()*1000)}", json=body)
        resp.raise_for_status()
        return resp.json()


def format_hit(hit: dict, fields: list[str] | None) -> dict:
    biblio_ru = hit.get("biblio", {}).get("ru", {})
    biblio_en = hit.get("biblio", {}).get("en", {})
    common = hit.get("common", {})

    full = {
        "id": hit.get("id", ""),
        "dataset": hit.get("dataset", ""),
        "similarity": round(hit.get("similarity_norm", 0), 3),
        "title": biblio_ru.get("title") or biblio_en.get("title") or "",
        "applicant": [a.get("name", "") for a in biblio_ru.get("applicant", [])]
                     or [a.get("name", "") for a in biblio_en.get("applicant", [])],
        "date": common.get("publication_date", ""),
        "filing_date": common.get("application", {}).get("filing_date", ""),
        "ipc": [c.get("fullname", "") for c in common.get("classification", {}).get("ipc", [])],
        "kind": common.get("kind", ""),
        "office": common.get("publishing_office", ""),
        "snippet": (hit.get("snippet", {}).get("description", "") or "")[:500],
    }

    if fields is None:
        return full
    return {k: v for k, v in full.items() if k in fields}


def _print_short(result):
    for h in result.get("hits", []):
        applicants = ", ".join(h.get("applicant", [])[:2]) if isinstance(h.get("applicant"), list) else str(h.get("applicant", ""))
        ipc_list = h.get("ipc", [])
        ipc = ", ".join(ipc_list[:2]) if isinstance(ipc_list, list) else str(ipc_list)
        print(f"{h.get('id', '?')[:40]:40s} {h.get('date', ''):12s} {h.get('title', '')[:60]}")
        if applicants:
            print(f"{'':40s} {'':12s}   {applicants}")
        if ipc:
            print(f"{'':40s} {'':12s}   IPC: {ipc}")
    print(f"\nTotal: {result.get('total', 0)} | Available: {result.get('available', 0)}")


def cmd_search(args):
    datasets = DATASETS.get(args.dataset, [args.dataset])
    if args.extra_datasets:
        datasets.extend(args.extra_datasets)

    try:
        result = search(args.query, datasets, lang=args.lang, limit=args.limit,
                        offset=args.offset, sort=args.sort)
    except httpx.HTTPStatusError as e:
        print(f"Error: {e.response.status_code} — {e.response.text[:200]}", file=sys.stderr)
        sys.exit(1)

    hits = [format_hit(h, FMT_FIELDS.get(args.format)) for h in result.get("hits", [])]
    output = {"total": result.get("total", 0), "available": result.get("available", 0), "hits": hits}

    if args.format == "short":
        _print_short(output)
    else:
        json.dump(output, sys.stdout, ensure_ascii=False, indent=2)
        print()


def cmd_sources(args):
    with _client() as c:
        path = "/sources/tree/integral" if args.integral else "/sources/tree"
        resp = c.get(f"{path}?t={int(time.time()*1000)}")
        resp.raise_for_status()
        data = resp.json()

    def flatten(nodes):
        for node in nodes:
            if node.get("type") == "dataset":
                print(f"  {node['id']:20s} {node.get('name_ru', '')}")
            if "children" in node:
                flatten(node["children"])

    flatten(data)


def cmd_suggest(args):
    with _client() as c:
        resp = c.get(f"/sgs?q={args.query}&search_type=patent&t={int(time.time()*1000)}")
        resp.raise_for_status()
        result = resp.json()
    for s in result.get("suggests", []):
        print(s if isinstance(s, str) else s.get("text", ""))


def main():
    parser = argparse.ArgumentParser(
        description="Rospatent Search Platform CLI",
        epilog=ROOT_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    s = sub.add_parser("search", help="Search patents, programs, designs",
                        epilog=SEARCH_EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    s.add_argument("query", help="Search query (Cyrillic and Latin supported)")
    s.add_argument("-d", "--dataset", default="patents_ru",
                   choices=list(DATASETS.keys()),
                   help="Dataset group (default: patents_ru)")
    s.add_argument("--extra-datasets", nargs="*", help="Additional dataset IDs")
    s.add_argument("-l", "--limit", type=int, default=10)
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--sort", default="relevance", choices=["relevance", "date_desc"])
    s.add_argument("--lang", default="ru", choices=["ru", "en"])
    s.add_argument("-f", "--format", default="short", choices=["short", "full"],
                   help="Output format: short (table) or full (JSON)")
    s.set_defaults(func=cmd_search)

    sr = sub.add_parser("sources", help="List available datasets")
    sr.add_argument("--integral", action="store_true", help="Non-patent sources (programs, topologies, DBs)")
    sr.set_defaults(func=cmd_sources)

    sg = sub.add_parser("suggest", help="Autocomplete suggestions")
    sg.add_argument("query", help="Partial query")
    sg.set_defaults(func=cmd_suggest)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()