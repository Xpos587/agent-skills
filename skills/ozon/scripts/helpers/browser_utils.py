#!/usr/bin/env -S uv run --script
# /// script
# dependencies = [
#   "camoufox[geoip]",
# ]
# ///
"""Browser utilities for Ozon scraping via Camoufox (Playwright-based anti-detect Firefox)."""

from __future__ import annotations

import json
import random
import shutil
import sys
import time
from pathlib import Path
from typing import Generator

OZON_PROFILE_DIR = Path.home() / ".config" / "ozon-shopper" / "profile"


def random_delay(min_sec: float = 2.0, max_sec: float = 5.0) -> None:
    time.sleep(random.uniform(min_sec, max_sec))


def launch_browser(headless: bool = True):
    """Launch Camoufox browser (headless by default). Returns (browser_context, page).

    Uses persistent profile from ~/.config/ozon-shopper/profile/ if it exists
    (preserves cookies, localStorage, session). Run ozon_login.py first to set up.
    """
    from camoufox.sync_api import Camoufox

    kwargs: dict = {
        "headless": headless,
        "humanize": True,
        "geoip": True,
    }

    profile = OZON_PROFILE_DIR
    if profile.exists():
        kwargs["persistent_context"] = True
        kwargs["user_data_dir"] = str(profile)

    cm = Camoufox(**kwargs)
    ctx = cm.__enter__()

    page = ctx.new_page() if hasattr(ctx, "new_page") else ctx
    return cm, page


def close_browser(cm) -> None:
    """Close Camoufox context manager."""
    try:
        cm.__exit__(None, None, None)
    except Exception:
        pass


def safe_goto(page, url: str, timeout: int = 30, max_retries: int = 2) -> None:
    for attempt in range(max_retries + 1):
        random_delay(1, 2)
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout * 1000)
        except Exception as e:
            if attempt < max_retries:
                wait = 2 ** attempt * 3
                print(f"[browser] Retry {attempt + 1}/{max_retries}: {e} (wait {wait}s)", file=sys.stderr)
                time.sleep(wait)
                continue
            raise

        if is_blocked(page):
            if attempt < max_retries:
                wait = 2 ** attempt * 5
                print(f"[browser] Blocked/captcha detected, retry {attempt + 1}/{max_retries} (wait {wait}s)", file=sys.stderr)
                time.sleep(wait)
                continue
            raise RuntimeError(f"Access blocked after {max_retries + 1} attempts: {url}")

        random_delay(3, 6)
        return


def safe_screenshot(page, path: str = "debug.png") -> None:
    try:
        page.screenshot(path=path)
    except Exception:
        pass


def scroll_down(page, times: int = 3) -> None:
    for _ in range(times):
        distance = random.randint(300, 800)
        page.evaluate(f"window.scrollBy(0, {distance})")
        random_delay(0.5, 1.5)


def is_blocked(page) -> bool:
    try:
        title = page.title().lower()
        if any(w in title for w in ("ограничен", "blocked", "captcha", "antibot", "challenge")):
            return True
        content = page.content()
        if "Доступ ограничен" in content or "Antibot Challenge" in content:
            return True
    except Exception:
        pass
    return False


def get_page_content(page) -> str:
    return page.content()


def get_page_text(page) -> str:
    return page.evaluate("() => document.body.innerText")


def click_element(page, selector: str) -> bool:
    try:
        el = page.query_selector(selector)
        if el:
            el.click()
            return True
    except Exception:
        pass
    return False


def click_by_text(page, text: str) -> bool:
    try:
        el = page.query_selector(f"text=\"{text}\"")
        if el:
            el.click()
            return True
    except Exception:
        pass
    return False


def wait_for_content(page, ms: int = 3000) -> None:
    page.wait_for_timeout(ms)


def save_json(data, output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def print_json(data) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))
