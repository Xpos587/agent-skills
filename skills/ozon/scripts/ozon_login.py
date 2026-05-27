#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Ozon login — open browser with persistent profile for manual authentication.

Opens a non-headless Camoufox browser pointing to Ozon login page.
Log in manually, then close the browser. Profile is saved to
~/.config/ozon-shopper/profile/ and reused by all other scripts.

Usage: uv run scripts/ozon_login.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from helpers.browser_utils import OZON_PROFILE_DIR, launch_browser, close_browser

OZON_LOGIN_URL = "https://www.ozon.ru/my/login"


def main() -> None:
    OZON_PROFILE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[ozon-login] Profile dir: {OZON_PROFILE_DIR}", file=sys.stderr)
    print("[ozon-login] Opening browser for manual login...", file=sys.stderr)
    print("[ozon-login] Log in to Ozon, then close the browser window.", file=sys.stderr)

    cm, page = launch_browser(headless=False)
    page.goto(OZON_LOGIN_URL, wait_until="domcontentloaded", timeout=30000)

    print("[ozon-login] Browser opened. Waiting for user to close...", file=sys.stderr)

    try:
        page.wait_for_event("close", timeout=300_000)
    except Exception:
        pass

    close_browser(cm)
    print("[ozon-login] Profile saved. All scripts will now use this session.", file=sys.stderr)


if __name__ == "__main__":
    main()
