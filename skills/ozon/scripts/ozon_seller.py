#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Ozon seller info — extract seller details from a product page.

Usage: uv run scripts/ozon_seller.py --url "https://www.ozon.ru/product/..." --output seller.json
"""

from __future__ import annotations

import argparse
import re
import sys
from urllib.parse import unquote

from helpers.browser_utils import (
    close_browser, launch_browser, print_json, random_delay,
    safe_goto, save_json,
)

_SELLER_RATING_RE = re.compile(r"(\d[,.]\d)")


def _seller_name_from_url(href: str) -> str:
    m = re.search(r"/seller/([^/?]+)", href)
    if not m:
        return ""
    slug = m.group(1)
    # Remove erid and trailing numbers
    slug = re.split(r"\?|$", slug)[0]
    # Decode and split by hyphens, take name parts (before company type words)
    parts = unquote(slug).split("-")
    stop_words = {"ooo", "ao", "ip", "llc", "ofitsialnyy", "magazin", "aktsionernoe", "obschestvo"}
    name_parts = [p for p in parts if p.lower() not in stop_words and not p.isdigit()]
    if not name_parts:
        name_parts = [parts[0]] if parts else []
    name = " ".join(p[0].upper() + p[1:] if p else "" for p in name_parts)
    return name


def parse_seller_info(page, product_url: str) -> dict:
    safe_goto(page, product_url)
    random_delay(1, 2)

    # Seller link from product page
    seller_name, seller_url = "", ""
    seller_link = page.query_selector('a[href*="/seller/"]')
    if seller_link:
        href = seller_link.get_attribute("href") or ""
        seller_url = f"https://www.ozon.ru{href}" if href.startswith("/") else href
        seller_name = seller_link.inner_text().strip()
        if not seller_name:
            seller_name = _seller_name_from_url(href)

    # Brand detection
    is_official = False
    brand_link = page.query_selector('a[href*="/brand/"]')
    if brand_link:
        is_official = True
        brand = brand_link.inner_text().strip()
        if not seller_name:
            seller_name = brand
    else:
        full_text = page.inner_text("body")
        if "Оригинальный товар" in full_text:
            is_official = True

    result = {
        "product_url": product_url,
        "seller_name": seller_name,
        "seller_url": seller_url,
        "seller_rating": "",
        "is_official_store": is_official,
        "trust_signals": [],
        "risk_signals": [],
    }

    if is_official:
        result["trust_signals"].append("Оригинальный товар")

    # Navigate to seller page for rating
    if seller_url:
        try:
            safe_goto(page, seller_url)
            random_delay(1, 2)
            seller_text = page.locator("body").inner_text()

            # Find "отзыв" and look in a window before it for the rating
            rev_idx = seller_text.find("отзыв")
            if rev_idx > 0:
                window = seller_text[max(0, rev_idx - 100):rev_idx]
                # Find last decimal number in the window before "отзыв"
                rating_candidates = list(_SELLER_RATING_RE.finditer(window))
                if rating_candidates:
                    rating = rating_candidates[-1].group(1).replace(",", ".")
                    try:
                        val = float(rating)
                        if 0 <= val <= 5:
                            result["seller_rating"] = rating
                    except ValueError:
                        pass

                # Extract reviews text: find the count before "отзыв"
                # The line before "отзыв" typically has the count like "590 K"
                lines_before = window.strip().split("\n")
                last_line = lines_before[-1].strip().replace("\u202f", "") if lines_before else ""
                reviews_word = seller_text[rev_idx:rev_idx + 10].strip()
                nl = reviews_word.find("\n")
                if nl > 0:
                    reviews_word = reviews_word[:nl]
                result["seller_reviews_text"] = f"{last_line} {reviews_word}" if last_line else reviews_word
        except Exception:
            pass

    try:
        rating = float(result["seller_rating"] or "0")
        if rating >= 4.5:
            result["trust_signals"].append(f"Высокий рейтинг ({rating})")
        elif 0 < rating < 3.5:
            result["risk_signals"].append(f"Низкий рейтинг ({rating})")
    except ValueError:
        pass

    if not result["seller_name"]:
        result["risk_signals"].append("Не удалось определить продавца")

    return result


def main() -> None:
    p = argparse.ArgumentParser(description="Parse Ozon seller info")
    p.add_argument("--url", required=True)
    p.add_argument("--output", help="Output JSON file path")
    args = p.parse_args()

    cm, page = launch_browser()
    try:
        print(f"[ozon-seller] Parsing seller: {args.url}", file=sys.stderr)
        seller = parse_seller_info(page, args.url)
        if args.output:
            save_json(seller, args.output)
            print(f"[ozon-seller] Saved to {args.output}", file=sys.stderr)
        else:
            print_json(seller)
    finally:
        close_browser(cm)


if __name__ == "__main__":
    main()
