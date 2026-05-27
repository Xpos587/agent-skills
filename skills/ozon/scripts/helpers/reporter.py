#!/usr/bin/env -S uv run --script
"""Report generator — combine analysis results into a Markdown report.

Usage: uv run scripts/helpers/reporter.py --input results/ --output report.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def load_json_files(directory: str | Path) -> dict:
    data: dict = {}
    dirpath = Path(directory)
    if not dirpath.exists():
        print(f"[reporter] Directory not found: {directory}", file=sys.stderr)
        return data

    for f in sorted(dirpath.glob("*.json")):
        try:
            with open(f, "r", encoding="utf-8") as fh:
                data[f.stem] = json.load(fh)
        except Exception as e:
            print(f"[reporter] Failed to load {f}: {e}", file=sys.stderr)
    return data


def generate_report(data: dict, query: str = "") -> str:
    lines: list[str] = []
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines.append(f"# Отчёт анализа Ozon")
    lines.append(f"**Дата**: {now}")
    if query:
        lines.append(f"**Запрос**: {query}")
    lines.append("")

    search_data = None
    products: dict = {}
    reviews: dict = {}
    sellers: dict = {}

    for key, val in data.items():
        if key in ("search", "results"):
            search_data = val if isinstance(val, list) else val.get("products", [])
        elif key.startswith("product_"):
            products[key] = val
        elif key.startswith("reviews_"):
            reviews[key] = val
        elif key.startswith("seller_"):
            sellers[key] = val

    if products:
        for idx, (key, product) in enumerate(products.items(), 1):
            lines.extend(_format_product_section(idx, product, reviews, sellers))
    elif search_data:
        lines.append("## Результаты поиска")
        lines.append("")
        for idx, item in enumerate(search_data, 1):
            lines.append(f"### {idx}. {item.get('title', 'Без названия')}")
            lines.append(f"- **Цена**: {item.get('price', '?')} ₽")
            if item.get("rating"):
                lines.append(f"- **Рейтинг**: {item['rating']}")
            if item.get("reviews_count"):
                lines.append(f"- **Отзывы**: {item['reviews_count']}")
            if item.get("url"):
                lines.append(f"- **Ссылка**: {item['url']}")
            lines.append("")

    return "\n".join(lines)


def _format_product_section(idx: int, product: dict, reviews: dict, sellers: dict) -> list[str]:
    lines: list[str] = []
    title = product.get("title", "Без названия")
    price = product.get("price", "?")

    verdict = _determine_verdict(product, reviews, sellers)
    emoji = {"safe": "✅", "warning": "⚠️", "danger": "🔴"}.get(verdict["level"], "❓")

    lines.append(f"## {idx}. {title}")
    lines.append(f"**{price} ₽** {emoji} {verdict['label']}")
    lines.append(f"**Оценка доверия**: {verdict['score']}/10")
    lines.append("")

    # Seller
    seller_data = _find_matching_seller(product, sellers)
    if seller_data:
        s_name = seller_data.get("seller_name", "Неизвестно")
        s_rating = seller_data.get("seller_rating", "?")
        s_reviews = seller_data.get("seller_reviews_text", "")
        if s_reviews:
            lines.append(f"- **Продавец**: {s_name} (рейтинг {s_rating}, {s_reviews})")
        else:
            lines.append(f"- **Продавец**: {s_name} (рейтинг {s_rating})")
    elif product.get("seller_name"):
        lines.append(f"- **Продавец**: {product['seller_name']}")

    # Reviews
    rev_data = _find_matching_reviews(product, reviews)
    if rev_data:
        summary = rev_data.get("summary", {})
        total = summary.get("total", 0)
        total_on_page = summary.get("total_on_page", 0)
        positive_pct = summary.get("positive_pct", 0)
        avg_rating = summary.get("avg_rating", 0)
        product_score = summary.get("product_score")

        review_parts = []
        if product_score:
            review_parts.append(f"рейтинг {product_score}/5")
        if total_on_page:
            review_parts.append(f"всего {total_on_page}")
        if total:
            review_parts.append(f"изучено {total}")
        if positive_pct:
            review_parts.append(f"{positive_pct}% положительных")

        lines.append(f"- **Отзывы**: {', '.join(review_parts)}")

        # Rating distribution
        rd = summary.get("rating_distribution", {})
        dist = rd.get("distribution")
        if dist:
            parts = [f"{k}★: {v}" for k, v in sorted(dist.items(), reverse=True)]
            lines.append(f"- **Распределение оценок**: {', '.join(parts)}")

        bot_flags = summary.get("bot_flags", [])
        if bot_flags:
            lines.append(f"- **Признаки накрутки**: {', '.join(bot_flags)}")

    # Specs
    specs = product.get("specs", {})
    if specs:
        lines.append("- **Характеристики**:")
        for k, v in list(specs.items())[:8]:
            lines.append(f"  - {k}: {v}")

    # Flags
    all_flags: list[str] = []
    if seller_data:
        all_flags.extend(seller_data.get("risk_signals", []))
    if rev_data:
        summary = rev_data.get("summary", {})
        all_flags.extend(summary.get("bot_flags", []))
    all_flags.extend(verdict.get("flags", []))
    lines.append(f"- **Красные флаги**: {'; '.join(all_flags) if all_flags else 'Нет'}")

    spec_warnings = verdict.get("spec_warnings", [])
    if spec_warnings:
        lines.append(f"- **Предупреждения по характеристикам**: {'; '.join(spec_warnings)}")
    lines.append("")
    return lines


def _determine_verdict(product: dict, reviews: dict, sellers: dict) -> dict:
    score = 7
    flags: list[str] = []
    spec_warnings: list[str] = []

    specs = product.get("specs", {})

    # Universal spec validation — detect placeholder/vague specs regardless of category
    _validate_specs(specs, flags, spec_warnings)

    # Seller check
    seller = _find_matching_seller(product, sellers)
    if seller:
        score -= len(seller.get("risk_signals", []))
        if seller.get("is_official_store"):
            score += 2
    elif not product.get("seller_name"):
        score -= 1
        flags.append("no_seller_info")

    # Reviews check
    rev = _find_matching_reviews(product, reviews)
    if rev:
        summary = rev.get("summary", {})
        bot_flags = summary.get("bot_flags", [])
        score -= len(bot_flags) * 2
        if summary.get("positive_pct", 0) > 95 and summary.get("total", 0) > 10:
            score -= 1
            flags.append("suspiciously_perfect_reviews")

        # Rating distribution anomaly: >95% are 5-star
        rd = summary.get("rating_distribution", {})
        dist = rd.get("distribution")
        if dist:
            total_votes = sum(dist.values())
            if total_votes >= 10:
                five_star_pct = dist.get(5, 0) / total_votes * 100
                if five_star_pct > 95:
                    score -= 1
                    flags.append("suspicious_rating_distribution")
    else:
        try:
            rc = int(product.get("reviews_count", "0"))
            if 0 < rc < 5:
                score -= 1
                flags.append("few_reviews")
        except ValueError:
            pass

    score -= len(spec_warnings)
    score = max(0, min(10, score))

    if score >= 7:
        level, label = "safe", "Рекомендация"
    elif score >= 4:
        level, label = "warning", "Исследовать подробнее"
    else:
        level, label = "danger", "Высокий риск скама"

    return {"score": score, "level": level, "label": label, "flags": flags, "spec_warnings": spec_warnings}


_NO_MODEL_SPEC = re.compile(
    r"современный|есть|не указано|нет данных|установлен|неизвестно", re.I
)

# Spec keys that should have specific model numbers, not placeholders
_SPEC_KEYS_REQUIRING_MODEL = [
    "процессор", "cpu", "видеокарт", "gpu", "оперативн", "ram",
    "модель", "бренд", "материал", "размер", "вес", "ёмк",
]


def _validate_specs(specs: dict, flags: list[str], spec_warnings: list[str]) -> None:
    """Check for vague/placeholder specs regardless of product category."""
    for key, val in specs.items():
        kl = key.lower()
        vl = str(val).strip()

        if len(vl) <= 3:
            continue

        matches_key = any(pattern in kl for pattern in _SPEC_KEYS_REQUIRING_MODEL)
        if matches_key and _NO_MODEL_SPEC.search(vl):
            spec_warnings.append(f"Характеристика без конкретного значения: {key} — \"{vl}\"")
            flags.append("vague_spec")


def _extract_product_id(url: str) -> str | None:
    m = re.search(r"/product/[^/]*?(\d+)/?$", url)
    return m.group(1) if m else None


def _find_matching_reviews(product: dict, reviews: dict) -> dict | None:
    pid = _extract_product_id(product.get("url", ""))
    if not pid:
        return next(iter(reviews.values()), None)
    for key, val in reviews.items():
        if pid in key or val.get("product_id") == pid:
            return val
    return next(iter(reviews.values()), None)


def _find_matching_seller(product: dict, sellers: dict) -> dict | None:
    pid = _extract_product_id(product.get("url", ""))
    if not pid:
        return next(iter(sellers.values()), None)
    for key, val in sellers.items():
        if pid in key:
            return val
    return next(iter(sellers.values()), None)


def main() -> None:
    p = argparse.ArgumentParser(description="Generate Markdown report from analysis data")
    p.add_argument("--input", required=True, help="Directory with JSON files or single JSON file")
    p.add_argument("--output", help="Output Markdown file path")
    p.add_argument("--query", default="", help="Search query for report header")
    args = p.parse_args()

    if os.path.isdir(args.input):
        data = load_json_files(args.input)
    else:
        with open(args.input, "r", encoding="utf-8") as f:
            data = {"single": json.load(f)}

    report = generate_report(data, args.query)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"[reporter] Report saved to {args.output}", file=sys.stderr)
    else:
        print(report)


if __name__ == "__main__":
    main()
