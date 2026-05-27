#!/usr/bin/env python3
"""Wordstat research collector for CustDev demand validation.

Collects targeted data (topRequests, associations, dynamics, regions)
for 1-10 research masks. NOT a full-depth semantic wave.

Usage:
    research_wordstat.py --query "how to improve X"
    research_wordstat.py --query "mask" --dynamics --regions-data --output-dir out
    research_wordstat.py --masks-file masks.tsv --dynamics --regions-data --output-dir out
    research_wordstat.py --token-check

Env: YANDEX_WORDSTAT_TOKEN
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

try:
    import httpx
except ImportError:
    print("ERROR: httpx required. pip install httpx", file=sys.stderr)
    sys.exit(1)

sys.path.insert(0, str(Path(__file__).parent))
from research_common import (
    require_env,
    save_json,
    save_summary,
    read_masks_file,
    slugify_mask,
    month_range,
    ensure_dir,
)

WORDSTAT_API = "https://api.wordstat.yandex.net/v1"
NUM_PHRASES_DEFAULT = 200
SLEEP_S = 0.25


def _post(token: str, method: str, body: dict) -> httpx.Response:
    return httpx.post(
        f"{WORDSTAT_API}/{method}",
        headers={"Authorization": f"Bearer {token}"},
        json=body,
        timeout=30,
    )


def check_token(token: str) -> dict:
    resp = _post(token, "userInfo", {})
    if resp.status_code == 403:
        return {"status": "blocked", "http_code": 403, "detail": "Wordstat API forbidden. Check app approval or use cloud path."}
    if resp.status_code == 401:
        return {"status": "auth_required", "http_code": 401, "detail": "Token expired or invalid. Re-authorize."}
    if resp.status_code != 200:
        return {"status": "error", "http_code": resp.status_code, "detail": resp.text[:200]}
    return {"status": "ready", "user_info": resp.json()}


def collect_mask(
    token: str, mask: str, regions: list[int], num_phrases: int,
    do_dynamics: bool, do_regions: bool, output_dir: Path,
) -> dict:
    stub = slugify_mask(mask)
    result: dict = {"mask": mask}

    # topRequests + associations
    try:
        resp = _post(token, "wordstat", {
            "phrase": mask, "numPhrases": num_phrases, "regions": regions,
        })
        resp.raise_for_status()
        payload = resp.json()
        save_json(output_dir / f"top_requests_{stub}.json", payload)
        result["total_count"] = payload.get("totalCount", 0)
        result["top_requests_count"] = len(payload.get("topRequests", []))
        result["associations_count"] = len(payload.get("associations", []))
        result["status"] = "ok"
    except Exception as e:
        (output_dir / f"error_top_{stub}.txt").write_text(str(e))
        result["status"] = "error"
        result["error"] = str(e)[:200]

    time.sleep(SLEEP_S)

    # dynamics (seasonality)
    if do_dynamics:
        from_date, to_date = month_range(6)
        try:
            resp = _post(token, "dynamics", {
                "phrase": mask, "period": "monthly",
                "fromDate": from_date, "toDate": to_date, "regions": regions,
            })
            resp.raise_for_status()
            payload = resp.json()
            save_json(output_dir / f"dynamics_{stub}.json", payload)
            result["dynamics_points"] = len(payload.get("dynamics", []))
            result["dynamics_status"] = "ok"
        except Exception as e:
            (output_dir / f"error_dyn_{stub}.txt").write_text(str(e))
            result["dynamics_status"] = "error"
            result["dynamics_error"] = str(e)[:200]
        time.sleep(SLEEP_S)

    # regions (geography)
    if do_regions:
        try:
            resp = _post(token, "regions", {
                "phrase": mask, "regions": regions,
            })
            resp.raise_for_status()
            payload = resp.json()
            save_json(output_dir / f"regions_{stub}.json", payload)
            result["regions_count"] = len(payload.get("regions", []))
            result["regions_status"] = "ok"
        except Exception as e:
            (output_dir / f"error_regions_{stub}.txt").write_text(str(e))
            result["regions_status"] = "error"
            result["regions_error"] = str(e)[:200]

    return result


def main() -> int:
    p = argparse.ArgumentParser(description="Wordstat research collector")
    p.add_argument("--query", help="Single research mask")
    p.add_argument("--masks-file", help="TSV with mask/intent columns")
    p.add_argument("--output-dir", default="research/wordstat")
    p.add_argument("--regions", default="225", help="Region IDs (default: 225=Russia)")
    p.add_argument("--num-phrases", type=int, default=NUM_PHRASES_DEFAULT)
    p.add_argument("--dynamics", action="store_true", help="Collect seasonality")
    p.add_argument("--regions-data", action="store_true", help="Collect geography")
    p.add_argument("--token-check", action="store_true", help="Verify token only")
    args = p.parse_args()

    token = require_env("YANDEX_WORDSTAT_TOKEN", "https://oauth.yandex.ru")

    if args.token_check:
        s = check_token(token)
        print(json.dumps(s, indent=2, ensure_ascii=False))
        return 0 if s["status"] == "ready" else 1

    if not args.query and not args.masks_file:
        print("ERROR: --query or --masks-file required", file=sys.stderr)
        return 2

    output_dir = Path(args.output_dir)
    ensure_dir(output_dir)
    region_ids = [int(r.strip()) for r in args.regions.split(",") if r.strip()]

    masks = read_masks_file(Path(args.masks_file)) if args.masks_file else [{"mask": args.query, "intent": "research"}]
    if len(masks) > 10:
        print(f"WARNING: {len(masks)} masks. Research mode recommends <=5.", file=sys.stderr)

    preflight = check_token(token)
    save_json(output_dir / "_preflight.json", preflight)
    if preflight["status"] != "ready":
        print(f"ERROR: Wordstat {preflight['status']}", file=sys.stderr)
        return 1

    print(f"Wordstat research: {len(masks)} mask(s), regions={region_ids}")
    results = []
    for i, m in enumerate(masks, 1):
        print(f"  [{i}/{len(masks)}] {m['mask']}")
        r = collect_mask(token, m["mask"], region_ids, args.num_phrases, args.dynamics, args.regions_data, output_dir)
        r["intent"] = m.get("intent", "research")
        results.append(r)

    save_summary(output_dir, {
        "masks": len(masks),
        "config": {"num_phrases": args.num_phrases, "regions": region_ids, "dynamics": args.dynamics, "regions_data": args.regions_data},
        "results": results,
    })

    ok = sum(1 for r in results if r.get("status") == "ok")
    print(f"\nDone: {ok}/{len(masks)} ok. Summary: {output_dir / '_summary.json'}")
    return 0 if ok == len(masks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
