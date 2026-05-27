#!/usr/bin/env python3
"""Google Trends research collector for CustDev demand validation.

Collects RELATED_QUERIES, RELATED_TOPICS, TIMESERIES, GEO_MAP via SerpApi.

Usage:
    research_trends.py --query "X training" --data-type RELATED_QUERIES
    research_trends.py --query "X,Y,Z" --full --output-dir out
    research_trends.py --token-check

Env: SERPAPI_KEY
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import httpx
except ImportError:
    print("ERROR: httpx required. pip install httpx", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from research_common import (
    require_env,
    cache_path,
    load_cache,
    save_cache,
    save_json,
    save_summary,
    ensure_dir,
)

SERPAPI_BASE = "https://serpapi.com/search"
TRENDS_CACHE_DAYS = 7

DATA_TYPES = ["RELATED_QUERIES", "RELATED_TOPICS", "TIMESERIES", "GEO_MAP_0", "GEO_MAP"]


def trends_request(params: dict, api_key: str, use_cache: bool = True) -> dict | None:
    cache_key = f"{params.get('q','')}_{params.get('data_type','')}_{params.get('geo','')}_{params.get('date','')}"
    cp = cache_path(cache_key, subdir="trends")

    if use_cache:
        cached = load_cache(cp, TRENDS_CACHE_DAYS)
        if cached:
            return cached

    params["engine"] = "google_trends"
    params["api_key"] = api_key

    resp = httpx.get(SERPAPI_BASE, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    if data.get("search_metadata", {}).get("status") != "Success":
        error = data.get("error", "Unknown SerpApi error")
        print(f"  [error] {params.get('data_type')}: {error}", file=sys.stderr)
        return None

    if use_cache:
        save_cache(cp, data)
    return data


def collect_full(query: str, api_key: str, geo: str, date: str, output_dir: Path) -> list[dict]:
    """Run full research: RELATED_QUERIES + RELATED_TOPICS + TIMESERIES."""
    results = []
    calls = [
        ("RELATED_QUERIES", {"q": query, "data_type": "RELATED_QUERIES", "date": date}),
        ("RELATED_TOPICS", {"q": query, "data_type": "RELATED_TOPICS", "date": date}),
        ("TIMESERIES", {"q": query, "data_type": "TIMESERIES", "date": "today 12-m"}),
    ]
    if geo:
        for p in calls:
            p[1]["geo"] = geo

    for label, params in calls:
        print(f"  [{label}]")
        data = trends_request(params, api_key)
        if data:
            safe = label.lower()
            save_json(output_dir / f"{safe}_{query.replace(',','_').replace(' ','_')[:50]}.json", data)
            results.append({"type": label, "status": "ok", "keys": list(data.keys())})
        else:
            results.append({"type": label, "status": "error"})

    return results


def main() -> int:
    p = argparse.ArgumentParser(description="Google Trends research collector")
    p.add_argument("--query", required=False, help="1-5 comma-separated terms (max 100 chars each)")
    p.add_argument("--data-type", choices=DATA_TYPES, help="Single data type (ignored if --full)")
    p.add_argument("--full", action="store_true", help="Collect RELATED_QUERIES + TOPICS + TIMESERIES")
    p.add_argument("--geo", default="", help="Geographic filter (US, GB, etc.)")
    p.add_argument("--date", default="today 3-m", help="Time range (default: today 3-m)")
    p.add_argument("--output-dir", default="research/trends")
    p.add_argument("--no-cache", action="store_true", help="Skip cache, force fresh API calls")
    p.add_argument("--token-check", action="store_true", help="Verify API key only")
    args = p.parse_args()

    api_key = require_env("SERPAPI_KEY", "https://serpapi.com/ (free tier: 250 requests/month)")

    if args.token_check:
        resp = httpx.get(SERPAPI_BASE, params={
            "engine": "google_trends", "q": "test", "data_type": "RELATED_QUERIES", "api_key": api_key,
        }, timeout=15)
        data = resp.json()
        status = data.get("search_metadata", {}).get("status")
        if status == "Success":
            print(json.dumps({"status": "ready"}, indent=2))
            return 0
        error = data.get("error", f"HTTP {resp.status_code}")
        print(json.dumps({"status": "error", "detail": error}, indent=2))
        return 1

    if not args.query:
        print("ERROR: --query required", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)

    if args.full:
        print(f"Trends research (full): {args.query}")
        results = collect_full(args.query, api_key, args.geo, args.date, output_dir)
    elif args.data_type:
        params = {"q": args.query, "data_type": args.data_type, "date": args.date}
        if args.geo:
            params["geo"] = args.geo
        print(f"Trends research: {args.data_type} for '{args.query}'")
        data = trends_request(params, api_key, use_cache=not args.no_cache)
        if data:
            safe = args.data_type.lower()
            save_json(output_dir / f"{safe}_{args.query.replace(',','_').replace(' ','_')[:50]}.json", data)
            results = [{"type": args.data_type, "status": "ok"}]
        else:
            results = [{"type": args.data_type, "status": "error"}]
    else:
        print("ERROR: specify --data-type or --full", file=sys.stderr)
        return 2

    save_summary(output_dir, {
        "query": args.query,
        "geo": args.geo or "worldwide",
        "date": args.date,
        "results": results,
    })

    ok = sum(1 for r in results if r["status"] == "ok")
    print(f"\nDone: {ok}/{len(results)} ok. Summary: {output_dir / '_summary.json'}")
    return 0 if ok == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
