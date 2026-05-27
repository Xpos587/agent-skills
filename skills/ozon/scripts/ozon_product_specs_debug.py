#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Debug: check for specs/details/title/seller widgets in entrypoint API."""

import json
import sys
import urllib.parse
from helpers.browser_utils import launch_browser, close_browser, random_delay

_EP_API = "https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2"
PRODUCT_URL = "https://www.ozon.ru/product/asus-fa608uh-rv004-igrovoy-noutbuk-16-00-amd-ryzen-7-260-ram-16-gb-ssd-512-gb-nvidia-geforce-rtx-3127658629"

cm, page = launch_browser()
try:
    page.goto(PRODUCT_URL, wait_until="domcontentloaded", timeout=30000)
    random_delay(2, 3)
    encoded = urllib.parse.quote(PRODUCT_URL, safe="")
    resp = page.context.request.get(f"{_EP_API}?url={encoded}")
    data = resp.json()
    ws = data.get("widgetStates", {})
    for key in sorted(ws.keys()):
        kl = key.lower()
        if any(kw in kl for kw in ["spec", "character", "detail", "prop", "descr", "title", "seller", "carousel"]):
            value = ws[key]
            val_str = json.dumps(json.loads(value) if isinstance(value, str) else value, ensure_ascii=False)[:800]
            print(f"\n=== {key} ===", file=sys.stderr)
            print(val_str, file=sys.stderr)
finally:
    close_browser(cm)
