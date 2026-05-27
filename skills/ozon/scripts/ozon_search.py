#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Ozon search — collect product cards from search results.

Usage: uv run scripts/ozon_search.py --query "ноутбук ASUS" --max-results 10 --output results.json
"""

from __future__ import annotations

import argparse
import re
import sys

from helpers.browser_utils import (
    close_browser, is_blocked, launch_browser, print_json, random_delay,
    safe_goto, safe_screenshot, save_json, scroll_down,
)

OZON_SEARCH_URL = "https://www.ozon.ru/search/?text={query}&from_global=true"

_TILE_ROOT_RE = re.compile(r"tile-root", re.I)
_PRODUCT_LINK_RE = re.compile(r"/product/")
_PRICE_RE = re.compile(r"(\d[\d\s]*)\s*\u20bd")
_RATING_RE = re.compile(r"(?<!\d)([1-5])\s*[,\.]\s*(\d)(?!\d)")
_REV_COUNT_RE = re.compile(r"(\d+)\s*отзыв", re.I)
_DISCOUNT_RE = re.compile(r"−(\d+)%")
_DELIV_RE = re.compile(
    r"(\d+\s+(?:марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря|января|февраля))"
)
_TILE_NOISE_RE = re.compile(
    r"^\d+\s*(баллов?|бонусов?) за отзыв|Распродажа$|Новинка$|Цена что надо$|Хит продаж$|"
    r"^\d+\s*шт осталось$|Оригинал$|до \d+ дней$|^\d+% до",
    re.I,
)


def _extract_tile_title(tile_el) -> str:
    spans = tile_el.query_selector_all("span")
    for s in spans:
        cls = s.get_attribute("class") or ""
        if "tsBody500Medium" in cls:
            text = s.inner_text().strip()
            if len(text) > 15 and not _TILE_NOISE_RE.match(text):
                return text
    link = tile_el.query_selector('a[href*="/product/"]')
    if link:
        text = link.inner_text().strip()
        if len(text) > 15 and not _TILE_NOISE_RE.match(text):
            return text
    full = tile_el.inner_text().strip()
    lines = full.split("  ")
    candidates = [
        l.strip() for l in lines
        if len(l.strip()) > 20
        and not re.match(r"^[\d\s]+\u20bd", l.strip())
        and not _TILE_NOISE_RE.match(l.strip())
        and "отзыв" not in l.strip()
    ]
    return max(candidates, key=len) if candidates else ""


def extract_product_cards(page, max_results: int = 10) -> list[dict]:
    products: list[dict] = []
    scroll_down(page, times=3)
    random_delay(1, 2)

    if is_blocked(page):
        safe_screenshot(page, "ozon_blocked.png")
        print("[ozon-search] BLOCKED by Ozon anti-bot!", file=sys.stderr)
        return products

    tiles = page.query_selector_all('[class*="tile-root"]')
    seen_urls: set[str] = set()

    for tile in tiles:
        if len(products) >= max_results:
            break

        link = tile.query_selector('a[href*="/product/"]')
        if not link:
            continue
        href = (link.get_attribute("href") or "").split("?")[0]
        url = f"https://www.ozon.ru{href}" if href.startswith("/") else href
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)

        title = _extract_tile_title(tile)
        if not title:
            continue

        full_text = tile.inner_text()
        price_matches = _PRICE_RE.findall(full_text)
        prices = [p.replace(" ", "") for p in price_matches]

        img = tile.query_selector("img")
        image = ""
        if img:
            image = img.get_attribute("src") or img.get_attribute("data-src") or ""

        rating_m = _RATING_RE.search(full_text)
        rating = f"{rating_m.group(1)}.{rating_m.group(2)}" if rating_m else ""

        rev_m = _REV_COUNT_RE.search(full_text)
        reviews_count = rev_m.group(1) if rev_m else ""

        disc_m = _DISCOUNT_RE.search(full_text)
        discount_pct = disc_m.group(1) if disc_m else ""

        deliv_m = _DELIV_RE.search(full_text)
        delivery = deliv_m.group(1) if deliv_m else ""

        products.append({
            "title": title[:200],
            "price": prices[0] if prices else "",
            "old_price": prices[1] if len(prices) >= 2 else "",
            "discount_pct": discount_pct,
            "url": url,
            "rating": rating,
            "reviews_count": reviews_count,
            "image": image,
            "delivery": delivery,
        })

    return products[:max_results]


def search_ozon(query: str, max_results: int = 10) -> list[dict]:
    cm, page = launch_browser()
    try:
        url = OZON_SEARCH_URL.format(query=query.replace(" ", "+"))
        print(f"[ozon-search] Searching: {url}", file=sys.stderr)
        safe_goto(page, url)
        products = extract_product_cards(page, max_results)
        if not products:
            safe_screenshot(page, "ozon_search_debug.png")
            print(f"[ozon-search] Page title: {page.title()}", file=sys.stderr)
            print("[ozon-search] WARNING: No products found.", file=sys.stderr)
        return products
    finally:
        close_browser(cm)


def main() -> None:
    p = argparse.ArgumentParser(description="Search Ozon for products")
    p.add_argument("--query", required=True)
    p.add_argument("--max-results", type=int, default=10)
    p.add_argument("--output", help="Output JSON file path")
    args = p.parse_args()

    products = search_ozon(args.query, args.max_results)
    if args.output:
        save_json(products, args.output)
        print(f"[ozon-search] Saved {len(products)} products to {args.output}", file=sys.stderr)
    else:
        print_json(products)


if __name__ == "__main__":
    main()
