#!/usr/bin/env python3
"""Shared utilities for search demand research scripts."""

from __future__ import annotations

import csv
import json
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

CACHE_DIR = Path.home() / ".cache" / "search-demand-research"
TRENDS_CACHE_DAYS = 7


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def require_env(name: str, help_url: str) -> str:
    value = os.environ.get(name, "")
    if not value:
        print(f"ERROR: {name} environment variable not set.", file=sys.stderr)
        print(f"Get it at: {help_url}", file=sys.stderr)
        sys.exit(2)
    return value


def cache_path(key: str, subdir: str = "") -> Path:
    d = CACHE_DIR / subdir if subdir else CACHE_DIR
    ensure_dir(d)
    safe = key.replace(" ", "_").replace("/", "_").replace('"', "").replace("'", "")[:120]
    return d / f"{safe}.json"


def load_cache(path: Path, max_age_days: int) -> dict[str, Any] | None:
    if max_age_days <= 0:
        return None
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        cached_at = datetime.fromisoformat(data.get("_cached_at", "2000-01-01"))
        if datetime.now() - cached_at < timedelta(days=max_age_days):
            return data
    except (json.JSONDecodeError, ValueError):
        pass
    return None


def save_cache(path: Path, data: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    data["_cached_at"] = datetime.now().isoformat()
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def save_json(path: Path, data: dict[str, Any] | list[Any]) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def save_summary(output_dir: Path, summary: dict[str, Any]) -> None:
    ensure_dir(output_dir)
    save_json(output_dir / "_summary.json", summary)


def read_masks_file(path: Path) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for row in reader:
            mask = (row.get("mask") or "").strip()
            if not mask:
                continue
            intent = (row.get("intent") or "research").strip()
            rows.append({"mask": mask, "intent": intent})
    return rows


def slugify_mask(mask: str) -> str:
    return " ".join(mask.strip().split()).replace(" ", "_").lower()[:70]


def to_iso_date(d: datetime) -> str:
    return f"{d.year}-{d.month:02d}-{d.day:02d}"


def month_range(months_back: int = 6) -> tuple[str, str]:
    now = datetime.now()
    from_d = datetime(now.year, now.month - months_back, 1)
    to_d = datetime(now.year, now.month, 1) - timedelta(days=1)
    return to_iso_date(from_d), to_iso_date(to_d)