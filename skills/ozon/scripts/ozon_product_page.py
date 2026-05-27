#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Ozon product page parser — extract full product details.

Usage: uv run scripts/ozon_product_page.py --url "https://www.ozon.ru/product/..." --output product.json
"""

from __future__ import annotations

import argparse
import re
import sys

from helpers.browser_utils import (
    close_browser, launch_browser, print_json, random_delay,
    safe_goto, save_json, scroll_down,
)

_PRICE_RE = re.compile(r"(\d[\d\s]*)\s*\u20bd")
_RATING_RE = re.compile(r"(?<!\d)([1-5])\s*[,\.]\s*(\d)(?!\d)")
_REV_COUNT_RE = re.compile(r"(\d+)\s*отзыв", re.I)


def _extract_price_from_widget(widget_text: str) -> tuple[str, str]:
    """Extract (price, old_price) from webPrice widget text."""
    lines = [l.strip() for l in widget_text.strip().split("\n") if l.strip()]
    prices = []
    for line in lines:
        m = _PRICE_RE.match(line)
        if m:
            prices.append(m.group(1).replace(" ", ""))
    if not prices:
        return "", ""
    return prices[0], prices[-1] if len(prices) >= 2 else ""


def parse_product_page(page, url: str) -> dict:
    safe_goto(page, url)
    scroll_down(page, times=3)
    random_delay(1, 2)

    # Title
    h1 = page.query_selector("h1")
    title = h1.inner_text().strip() if h1 else ""

    # Price from webPrice widget
    price, old_price = "", ""
    price_widget = page.query_selector('[data-widget="webPrice"]')
    if price_widget:
        price, old_price = _extract_price_from_widget(price_widget.inner_text())

    # Rating & reviews from webReviewProductScore
    full_text = page.locator("body").inner_text()
    rating_m = _RATING_RE.search(full_text)
    rating = f"{rating_m.group(1)}.{rating_m.group(2)}" if rating_m else ""
    rev_m = _REV_COUNT_RE.search(full_text)
    reviews_count = rev_m.group(1) if rev_m else ""

    # Seller
    seller_name, seller_url = "", ""
    seller_link = page.query_selector('a[href*="/seller/"]')
    if seller_link:
        href = seller_link.get_attribute("href") or ""
        seller_url = f"https://www.ozon.ru{href}" if href.startswith("/") else href
        seller_name = seller_link.inner_text().strip()
        if not seller_name:
            from urllib.parse import unquote
            m = re.search(r"/seller/([^/?]+)", href)
            if m:
                slug = m.group(1)
                slug = re.split(r"\?|$", slug)[0]
                parts = unquote(slug).split("-")
                stop_words = {"ooo", "ao", "ip", "llc", "ofitsialnyy", "magazin", "aktsionernoe", "obschestvo"}
                name_parts = [p for p in parts if p.lower() not in stop_words and not p.isdigit()]
                if not name_parts:
                    name_parts = [parts[0]] if parts else []
                seller_name = " ".join(p[0].upper() + p[1:] if p else "" for p in name_parts)

    # Brand — look for "Оригинальный товар" marker or /brand/ link
    brand = ""
    brand_link = page.query_selector('a[href*="/brand/"]')
    if brand_link:
        brand = brand_link.inner_text().strip()
    elif "Оригинальный товар" in full_text:
        brand = "Оригинал"

    # Specs — dl elements
    specs = {}
    for dl in page.query_selector_all("dl"):
        dt = dl.query_selector("dt")
        dd = dl.query_selector("dd")
        if dt and dd:
            k, v = dt.inner_text().strip(), dd.inner_text().strip()
            if k and v and v != "Не указано":
                specs[k] = v

    # Try to expand hidden specs
    for btn in page.query_selector_all('button, [role="button"]'):
        txt = btn.inner_text().strip()
        if "Все характеристики" in txt:
            btn.click()
            random_delay(1, 2)
            for dl in page.query_selector_all("dl"):
                dt = dl.query_selector("dt")
                dd = dl.query_selector("dd")
                if dt and dd:
                    k, v = dt.inner_text().strip(), dd.inner_text().strip()
                    if k and v and v != "Не указано" and k not in specs:
                        specs[k] = v
            break

    # Breadcrumbs
    breadcrumbs = []
    bc_widget = page.query_selector('[data-widget="breadCrumbs"]')
    if bc_widget:
        breadcrumbs = [t.strip() for t in bc_widget.inner_text().strip().split("\n") if t.strip()]

    return {
        "url": url,
        "title": title,
        "brand": brand,
        "price": price,
        "old_price": old_price,
        "currency": "RUB",
        "rating": rating,
        "reviews_count": reviews_count,
        "seller_name": seller_name,
        "seller_url": seller_url,
        "specs": specs,
        "breadcrumbs": breadcrumbs,
    }


def main() -> None:
    p = argparse.ArgumentParser(description="Parse Ozon product page")
    p.add_argument("--url", required=True)
    p.add_argument("--output", help="Output JSON file path")
    args = p.parse_args()

    cm, page = launch_browser()
    try:
        print(f"[ozon-product] Parsing: {args.url}", file=sys.stderr)
        product = parse_product_page(page, args.url)
        if args.output:
            save_json(product, args.output)
            print(f"[ozon-product] Saved to {args.output}", file=sys.stderr)
        else:
            print_json(product)
    finally:
        close_browser(cm)


if __name__ == "__main__":
    main()
