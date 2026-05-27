#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Full product analysis — product info + reviews + seller in one browser session.

Usage:
  uv run scripts/full_analysis.py --urls "https://www.ozon.ru/product/..." "https://..."
  uv run scripts/full_analysis.py --query "ноутбук ASUS" --max-results 5
  uv run scripts/full_analysis.py --urls "..." --output-dir results/
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from helpers.browser_utils import (
    close_browser, launch_browser, random_delay, safe_goto, save_json,
)
from ozon_product_page import parse_product_page
from ozon_reviews import parse_reviews
from ozon_seller import parse_seller_info
from ozon_search import OZON_SEARCH_URL, _extract_tile_title


def search_to_urls(page, query: str, max_results: int = 5) -> list[str]:
    """Search Ozon and return product URLs."""
    url = OZON_SEARCH_URL.format(query=query.replace(" ", "+"))
    print(f"[full-analysis] Searching: {query}", file=sys.stderr)
    safe_goto(page, url, timeout=30)
    random_delay(1, 2)

    tiles = page.query_selector_all('[class*="tile-root"]')
    urls: list[str] = []
    seen: set[str] = set()

    for tile in tiles:
        if len(urls) >= max_results:
            break
        link = tile.query_selector('a[href*="/product/"]')
        if not link:
            continue
        href = (link.get_attribute("href") or "").split("?")[0]
        full_url = f"https://www.ozon.ru{href}" if href.startswith("/") else href
        if full_url and full_url not in seen:
            seen.add(full_url)
            title = _extract_tile_title(tile)
            print(f"  {len(urls)+1}. {title[:80]} — {full_url}", file=sys.stderr)
            urls.append(full_url)

    if not urls:
        print("[full-analysis] No products found for query.", file=sys.stderr)
    return urls


def analyze_product(page, url: str, max_reviews: int = 30) -> dict:
    """Run product + reviews + seller analysis for a single URL."""
    print(f"\n{'='*50}", file=sys.stderr)
    print(f"[full-analysis] Analyzing: {url}", file=sys.stderr)

    product = parse_product_page(page, url)
    print(f"  Product: {product.get('title', '?')[:80]}", file=sys.stderr)
    print(f"  Price: {product.get('price', '?')}₽", file=sys.stderr)

    reviews = parse_reviews(page, url, max_reviews)
    summary = reviews.get("summary", {})
    print(f"  Reviews: {reviews['total_extracted']} extracted (page total: {summary.get('total_on_page', '?')})", file=sys.stderr)

    seller = parse_seller_info(page, url)
    print(f"  Seller: {seller.get('seller_name', '?')} (rating: {seller.get('seller_rating', '?')})", file=sys.stderr)

    return {
        "url": url,
        "product": product,
        "reviews": reviews,
        "seller": seller,
    }


def generate_markdown_report(results: list[dict], query: str = "") -> str:
    """Generate Markdown report from analysis results."""
    from helpers.reporter import generate_report

    data: dict = {}
    for i, r in enumerate(results, 1):
        if "error" in r:
            continue
        url = r["url"]
        slug = re.search(r"/product/[^/]*?(\d+)/?$", url)
        pid = slug.group(1) if slug else str(i)
        data[f"product_{pid}"] = r["product"]
        data[f"reviews_{pid}"] = r["reviews"]
        data[f"seller_{pid}"] = r["seller"]

    return generate_report(data, query)


def main() -> None:
    p = argparse.ArgumentParser(description="Full Ozon product analysis")
    group = p.add_mutually_exclusive_group(required=True)
    group.add_argument("--urls", nargs="+", help="Product URLs to analyze")
    group.add_argument("--query", help="Search query (finds products automatically)")
    p.add_argument("--max-results", type=int, default=5, help="Max products from search (default: 5)")
    p.add_argument("--max-reviews", type=int, default=30, help="Max reviews per product (default: 30)")
    p.add_argument("--output-dir", default="results/", help="Output directory for JSON files")
    p.add_argument("--report", help="Output Markdown report path")
    args = p.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    cm, page = launch_browser()
    try:
        # Resolve URLs
        urls = args.urls
        query = ""
        if args.query:
            query = args.query
            urls = search_to_urls(page, query, args.max_results)

        if not urls:
            print("[full-analysis] No URLs to analyze.", file=sys.stderr)
            return

        print(f"\n[full-analysis] Analyzing {len(urls)} products...", file=sys.stderr)

        results: list[dict] = []
        for i, url in enumerate(urls, 1):
            print(f"\n>>> [{i}/{len(urls)}]", file=sys.stderr)
            try:
                r = analyze_product(page, url, args.max_reviews)
                results.append(r)

                # Save individual JSONs
                slug = re.search(r"/product/[^/]*?(\d+)/?$", url)
                pid = slug.group(1) if slug else str(i)
                save_json(r["product"], out_dir / f"product_{pid}.json")
                save_json(r["reviews"], out_dir / f"reviews_{pid}.json")
                save_json(r["seller"], out_dir / f"seller_{pid}.json")
                print(f"  -> Saved to {out_dir}/", file=sys.stderr)
            except Exception as e:
                print(f"  ERROR: {e}", file=sys.stderr)
                results.append({"url": url, "error": str(e)})

        # Save combined JSON
        combined_path = out_dir / "full_analysis.json"
        save_json(results, combined_path)
        print(f"\n[full-analysis] Combined results: {combined_path}", file=sys.stderr)

        # Generate Markdown report
        md = generate_markdown_report(results, query)
        if args.report:
            Path(args.report).parent.mkdir(parents=True, exist_ok=True)
            Path(args.report).write_text(md, encoding="utf-8")
            print(f"[full-analysis] Report: {args.report}", file=sys.stderr)
        else:
            report_path = out_dir / "report.md"
            report_path.write_text(md, encoding="utf-8")
            print(f"[full-analysis] Report: {report_path}", file=sys.stderr)

    finally:
        close_browser(cm)


if __name__ == "__main__":
    main()
