#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Debug: check if entrypoint API returns search product data."""

import json
import sys
import urllib.parse
from helpers.browser_utils import launch_browser, close_browser, random_delay

_EP_API = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2"
SEARCH_URL = "https://www.ozon.ru/search/?text=ноутбук+asus&from_global=true"

cm, page = launch_browser()
try:
    page.goto(SEARCH_URL, wait_until="domcontentloaded", timeout=30000)
    random_delay(2, 3)

    encoded = urllib.parse.quote(SEARCH_URL, safe="")
    api_ctx = page.context.request
    resp = api_ctx.get(f"{_EP_API}?url={encoded}")
    data = resp.json()
    ws = data.get("widgetStates", {})

    print(f"[debug] Total widget states: {len(ws)}", file=sys.stderr)

    # Look for product-related widgets
    for key in sorted(ws.keys()):
        if any(kw in key.lower() for kw in ["tile", "product", "search", "listing", "grid", "catalog"]):
            value = ws[key]
            val_str = str(value)[:200]
            print(f"\n=== {key} === (len={len(str(value))})", file=sys.stderr)
            print(val_str, file=sys.stderr)

    # Also check for any widget with product URLs
    for key, value in ws.items():
        if isinstance(value, str) and "/product/" in value:
            print(f"\n=== {key} === contains /product/", file=sys.stderr)
            print(str(value)[:500], file=sys.stderr)

finally:
    close_browser(cm)
