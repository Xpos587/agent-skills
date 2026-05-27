#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Ozon reviews parser — extract and analyze product reviews via entrypoint API.

Usage: uv run scripts/ozon_reviews.py --url "https://www.ozon.ru/product/..." --max-reviews 30 --output reviews.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from datetime import datetime, timezone

from helpers.browser_utils import (
    close_browser, launch_browser, print_json,
    random_delay, save_json,
)

_EP_API = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2"


def _extract_product_id(url: str) -> str | None:
    m = re.search(r"/product/[^/]*?(\d+)/?$", url)
    return m.group(1) if m else None


def _fetch_entrypoint(page, encoded_url: str, retries: int = 2) -> dict:
    """Fetch Ozon entrypoint API using Playwright request context (no page navigation)."""
    url = f"{_EP_API}?url={encoded_url}"
    for attempt in range(retries + 1):
        try:
            api_ctx = page.context.request
            resp = api_ctx.get(url)
            if resp.ok:
                try:
                    return {"ok": True, "status": resp.status, "data": resp.json()}
                except Exception:
                    return {"ok": False, "error": f"Invalid JSON: status {resp.status}"}
            return {"ok": False, "error": f"HTTP {resp.status}"}
        except Exception as e:
            if attempt < retries:
                print(f"[ozon-reviews] Retry {attempt + 1}/{retries}: {e}", file=sys.stderr)
                random_delay(1, 2)
            else:
                return {"ok": False, "error": str(e)}
    return {"ok": False, "error": "max retries"}


def _get_sh_hash(page) -> str | None:
    return page.evaluate("""
        () => {
            for (const s of document.querySelectorAll('script')) {
                const m = s.textContent?.match(/sh=([^"'\\\\&]+)/);
                if (m) return m[1];
            }
            return null;
        }
    """)


def _parse_review(r: dict) -> dict:
    content = r.get("content", {})
    author = r.get("author", {})
    useful = r.get("usefulness", {})
    comment = content.get("comment", "")
    positive = content.get("positive", "")
    negative = content.get("negative", "")
    score = content.get("score")

    text_parts = [p for p in (positive, negative, comment) if p]
    text = " | ".join(text_parts) if len(text_parts) > 1 else (text_parts[0] if text_parts else "")

    published = r.get("publishedAt")
    date_str = ""
    if published:
        try:
            dt = datetime.fromtimestamp(published, tz=timezone.utc)
            date_str = dt.strftime("%Y-%m-%d")
        except (OSError, ValueError):
            date_str = ""

    photos = [
        {"url": p.get("url", ""), "uuid": p.get("UUID", "")}
        for p in content.get("photos", [])
    ]
    videos = [
        {"url": v.get("url", ""), "preview": v.get("previewUrl", ""), "duration": v.get("duration", "")}
        for v in content.get("videos", [])
    ]

    return {
        "id": r.get("uuid", ""),
        "author": author.get("firstName", ""),
        "rating": score,
        "date": date_str,
        "text": text[:1000],
        "positive": positive[:500],
        "negative": negative[:500],
        "useful_count": useful.get("useful", 0),
        "useless_count": useful.get("unuseful", 0),
        "comments_count": r.get("comments", {}).get("totalCount", 0),
        "photos": photos,
        "videos": videos,
    }


def parse_reviews(page, product_url: str, max_reviews: int = 30) -> dict:
    product_url = product_url.rstrip("/")
    product_id = _extract_product_id(product_url)
    if not product_id:
        print(f"[ozon-reviews] Cannot extract product ID from URL: {product_url}", file=sys.stderr)
        return _empty_result(product_url)

    print(f"[ozon-reviews] Product ID: {product_id}", file=sys.stderr)

    # Intercept composer API responses for rating distribution (lazy-loaded widget)
    composer_score_data: dict | None = None

    def on_response(response):
        nonlocal composer_score_data
        if "webReviewProductScore" in response.url and "composer" in response.url:
            try:
                body = response.json()
                composer_score_data = body.get("state", {})
            except Exception:
                pass

    page.on("response", on_response)

    page.goto(product_url, wait_until="domcontentloaded", timeout=30000)
    random_delay(2, 3)

    product_score = _extract_product_score(page)
    if product_score:
        print(f"[ozon-reviews] Product score: {product_score}", file=sys.stderr)

    # Scroll to reviews section to trigger lazy-loaded webReviewProductScore widget
    for i in range(3):
        page.evaluate(f"window.scrollTo(0, document.body.scrollHeight * {(i + 1) * 0.15})")
        random_delay(1, 2)
    try:
        page.evaluate("""() => {
            const links = document.querySelectorAll('a[href*="/reviews"]');
            for (const a of links) { a.click(); break; }
        }""")
        random_delay(3, 5)
    except Exception:
        pass

    # Remove listener after scrolling
    page.remove_listener("response", on_response)

    if composer_score_data:
        print("[ozon-reviews] Rating distribution captured via intercept", file=sys.stderr)

    sh = _get_sh_hash(page)
    if not sh:
        print("[ozon-reviews] Warning: no sh hash found, pagination may fail", file=sys.stderr)

    reviews: list[dict] = []
    seen_ids: set[str] = set()

    # Step 1: Fetch pdpReviews to get initial reviews + rating + paginator
    review_url = f"{product_url}/?layout_container=pdpReviews&layout_page_index=2"
    if sh:
        review_url += f"&sh={sh}"
    encoded = urllib.parse.quote(review_url, safe="")

    print("[ozon-reviews] Fetching initial review page...", file=sys.stderr)
    try:
        result = _fetch_entrypoint(page, encoded)
    except Exception as e:
        print(f"[ozon-reviews] Initial fetch error: {e}", file=sys.stderr)
        return _empty_result(product_url)
    if not result.get("ok"):
        print(f"[ozon-reviews] Failed to fetch pdpReviews: {result.get('error', result.get('status'))}", file=sys.stderr)
        return _empty_result(product_url)

    data = result["data"]
    widget_states = data.get("widgetStates", {})

    # Extract reviews from webListReviews widget
    _extract_reviews_from_states(widget_states, reviews, seen_ids)

    # Extract rating distribution from webReviewTabs (basic total count)
    rating_dist = _extract_rating_from_states(widget_states)

    # Merge rating distribution from intercepted composer API response
    if composer_score_data:
        scores = composer_score_data.get("score", [])
        if scores:
            rating_dist = {
                "total": composer_score_data.get("reviewsCount", rating_dist.get("total")),
                "total_score": composer_score_data.get("totalScore"),
                "distribution": {
                    5: next((s["value"] for s in scores if "5" in s.get("title", "")), 0),
                    4: next((s["value"] for s in scores if "4" in s.get("title", "")), 0),
                    3: next((s["value"] for s in scores if "3" in s.get("title", "")), 0),
                    2: next((s["value"] for s in scores if "2" in s.get("title", "")), 0),
                    1: next((s["value"] for s in scores if "1" in s.get("title", "")), 0),
                },
            }
            print(f"[ozon-reviews] Rating distribution: {rating_dist}", file=sys.stderr)

    # Find paginator nextPage
    next_page_url = None
    for key, value in widget_states.items():
        if key.startswith("paginator"):
            state = json.loads(value) if isinstance(value, str) else value
            next_page_url = state.get("nextPage")
            break

    # Step 2: Follow paginator chain
    # The initial pdpReviews page often has NO reviews — first batch is in pdpReviews2
    page_fetches = 0
    max_fetches = max(15, (max_reviews // 3) + 5)

    while next_page_url and len(reviews) < max_reviews and page_fetches < max_fetches:
        if sh and "sh=" not in next_page_url:
            next_page_url += f"&sh={sh}"
        encoded_next = urllib.parse.quote(next_page_url, safe="")
        print(f"[ozon-reviews] Fetching page {page_fetches + 1} ({len(reviews)} reviews so far)...", file=sys.stderr)

        try:
            result = _fetch_entrypoint(page, encoded_next)
        except Exception as e:
            print(f"[ozon-reviews] Pagination fetch error: {e}", file=sys.stderr)
            break
        if not result.get("ok"):
            print(f"[ozon-reviews] Pagination failed: {result.get('error', result.get('status'))}", file=sys.stderr)
            break

        ws = result["data"].get("widgetStates", {})
        count_before = len(reviews)
        _extract_reviews_from_states(ws, reviews, seen_ids)
        print(f"[ozon-reviews]   Page {page_fetches + 1}: +{len(reviews) - count_before} reviews (total: {len(reviews)})", file=sys.stderr)

        # Find next paginator
        next_page_url = None
        for key, value in ws.items():
            if key.startswith("paginator"):
                state = json.loads(value) if isinstance(value, str) else value
                next_page_url = state.get("nextPage")
                break

        page_fetches += 1
        if len(reviews) == count_before:
            break  # no new reviews, stop

    reviews = reviews[:max_reviews]
    ratings = [r["rating"] for r in reviews if isinstance(r["rating"], (int, float))]
    avg = sum(ratings) / len(ratings) if ratings else 0
    positive = sum(1 for r in ratings if r >= 4)

    bot_flags = _detect_bot_patterns(reviews)

    return {
        "product_url": product_url,
        "product_id": product_id,
        "total_extracted": len(reviews),
        "summary": {
            "total": len(reviews),
            "avg_rating": round(avg, 2),
            "positive_pct": round(positive / len(ratings) * 100, 1) if ratings else 0,
            "total_on_page": rating_dist.get("total"),
            "rating_distribution": rating_dist,
            "product_score": product_score,
            "bot_flags": bot_flags,
        },
        "reviews": reviews,
        "extracted_at": datetime.now(timezone.utc).isoformat(),
    }


def _extract_reviews_from_states(widget_states: dict, reviews: list[dict], seen_ids: set[str]) -> None:
    for key, value in widget_states.items():
        if "webListReviews" not in key:
            continue
        state = json.loads(value) if isinstance(value, str) else value
        for r in state.get("reviews", []):
            uuid = r.get("uuid", "")
            if uuid in seen_ids:
                continue
            seen_ids.add(uuid)
            reviews.append(_parse_review(r))


def _extract_rating_from_states(widget_states: dict) -> dict[str, int]:
    """Extract total review count from webReviewTabs."""
    for key, value in widget_states.items():
        if "webReviewTabs" not in key:
            continue
        state = json.loads(value) if isinstance(value, str) else value
        for tab in state.get("tabs", []):
            if tab.get("value") == "reviews":
                try:
                    return {"total": int(tab.get("counter", 0))}
                except (ValueError, TypeError):
                    pass
    return {}


def _extract_product_score(page) -> float | None:
    """Extract overall product score (e.g. 4.9) from webSingleProductScore widget."""
    try:
        text = page.evaluate("""() => {
            const el = document.querySelector('[data-widget="webSingleProductScore"]');
            return el ? el.innerText : '';
        }""")
        m = re.search(r"(\d[.,]\d)", text)
        if m:
            return float(m.group(1).replace(",", "."))
    except Exception:
        pass
    return None


def _detect_bot_patterns(reviews: list[dict]) -> list[str]:
    """Detect potential bot/fake review patterns."""
    flags: list[str] = []
    if len(reviews) < 3:
        return flags

    # 1. Review velocity: all reviews within 48 hours
    dates = []
    for r in reviews:
        if r.get("date"):
            try:
                dates.append(datetime.strptime(r["date"], "%Y-%m-%d"))
            except ValueError:
                pass
    if len(dates) >= 3:
        dates.sort()
        span_hours = (dates[-1] - dates[0]).total_seconds() / 3600
        if span_hours <= 48:
            flags.append("reviews_burst_48h")
        elif span_hours <= 168:  # 1 week
            flags.append("reviews_burst_1w")

    # 2. Cloned reviews: identical or near-identical text
    texts = [r.get("text", "").strip().lower() for r in reviews if r.get("text", "").strip()]
    if len(texts) >= 3:
        seen: dict[str, int] = {}
        for t in texts:
            # Normalize: strip punctuation, collapse whitespace
            normalized = re.sub(r"[^\w\s]", "", t)
            normalized = re.sub(r"\s+", " ", normalized).strip()
            if len(normalized) < 20:
                continue
            seen[normalized] = seen.get(normalized, 0) + 1
        clones = sum(1 for c in seen.values() if c > 1)
        if clones >= 2:
            flags.append(f"cloned_reviews({clones} groups)")

    # 3. Repetitive author names (same first name in many reviews)
    authors = [r.get("author", "").strip() for r in reviews if r.get("author", "").strip()]
    if len(authors) >= 5:
        name_counts: dict[str, int] = {}
        for a in authors:
            # Take first name only
            first = a.split()[0] if a else ""
            name_counts[first] = name_counts.get(first, 0) + 1
        max_name_count = max(name_counts.values())
        if max_name_count >= len(authors) * 0.4:
            flags.append("repetitive_authors")

    # 4. All reviews are 5-star with short text
    review_ratings = [r["rating"] for r in reviews if isinstance(r["rating"], (int, float))]
    if len(review_ratings) >= 5:
        five_star_pct = sum(1 for r in review_ratings if r == 5) / len(review_ratings) * 100
        short_pct = sum(1 for t in texts if len(t) < 50) / len(texts) * 100 if texts else 0
        if five_star_pct == 100 and short_pct >= 70:
            flags.append("all_5star_short_text")

    return flags


def _empty_result(product_url: str) -> dict:
    return {
        "product_url": product_url,
        "total_extracted": 0,
        "summary": {"total": 0, "avg_rating": 0, "positive_pct": 0, "rating_distribution": {}, "product_score": None},
        "reviews": [],
        "extracted_at": datetime.now(timezone.utc).isoformat(),
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Parse Ozon product reviews via API")
    p.add_argument("--url", required=True)
    p.add_argument("--max-reviews", type=int, default=30)
    p.add_argument("--output", help="Output JSON file path")
    args = p.parse_args()

    cm, page = launch_browser()
    try:
        print(f"[ozon-reviews] Parsing reviews: {args.url}", file=sys.stderr)
        result = parse_reviews(page, args.url, args.max_reviews)
        if args.output:
            save_json(result, args.output)
            print(f"[ozon-reviews] Saved {result['total_extracted']} reviews to {args.output}", file=sys.stderr)
        else:
            print_json(result)
    finally:
        close_browser(cm)


if __name__ == "__main__":
    main()
