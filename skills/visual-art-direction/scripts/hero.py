#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "httpx",
# ]
# ///

"""Generate art-directed images for any UI/UX surface via fal.ai GPT Image 2.

Generates images for viewport breakpoints and channel variants in one run.
Outputs WebP images + prompt file + responsive <picture> HTML snippet.

Usage:
  ./hero.py --prompt "SaaS dashboard hero" --project my-saas
  ./hero.py --prompt "Fintech hero" --breakpoints desktop,mobile,social-square
  ./hero.py --prompt "Draft concept" --quality low --json
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import httpx

FAL_GENERATE = "https://fal.run/openai/gpt-image-2"
FAL_EDIT = "https://fal.run/openai/gpt-image-2/edit"

SIZE_MAP = {
    "desktop": "landscape_16_9",
    "tablet": "landscape_4_3",
    "mobile": "portrait_4_5",
    "social-square": "square",
    "social-vertical": "portrait_9_16",
    "email-banner": "landscape_3_1",
}


def slugify(value: str, fallback: str = "project") -> str:
    base = str(value or "").strip().lower()
    ascii_str = re.sub(r"[^a-z0-9]+", "-", base.normalize("NFKD"))[:48].strip("-")
    return ascii_str or fallback


def make_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def ext_for(fmt: str) -> str:
    return ".jpg" if fmt == "jpeg" else f".{fmt}"


async def fal_generate(
    client: httpx.AsyncClient,
    prompt: str,
    breakpoint: str,
    quality: str,
    output_format: str,
    num_images: int,
) -> dict:
    api_key = os.environ.get("FAL_API_KEY") or os.environ.get("FAL_KEY", "")
    if not api_key:
        print("Error: FAL_API_KEY or FAL_KEY environment variable is required", file=sys.stderr)
        sys.exit(1)

    image_size = SIZE_MAP.get(breakpoint)
    if not image_size:
        valid = ", ".join(SIZE_MAP.keys())
        print(f"Error: unknown breakpoint '{breakpoint}'. Use: {valid}", file=sys.stderr)
        sys.exit(1)

    payload = {
        "prompt": prompt,
        "image_size": image_size,
        "quality": quality,
        "num_images": num_images,
        "output_format": output_format,
        "sync_mode": True,
    }

    resp = await client.post(
        FAL_GENERATE,
        json=payload,
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f"fal.ai error ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)

    return resp.json()


async def fal_edit(
    client: httpx.AsyncClient,
    prompt: str,
    image_urls: list[str],
    mask_url: str | None,
    image_size: str | None,
    quality: str,
    output_format: str,
    num_images: int,
) -> dict:
    api_key = os.environ.get("FAL_API_KEY") or os.environ.get("FAL_KEY", "")
    if not api_key:
        print("Error: FAL_API_KEY or FAL_KEY environment variable is required", file=sys.stderr)
        sys.exit(1)

    if not image_urls:
        print("Error: --image-urls is required for edit mode", file=sys.stderr)
        sys.exit(1)

    payload: dict = {
        "prompt": prompt,
        "image_urls": image_urls,
        "quality": quality,
        "num_images": num_images,
        "output_format": output_format,
        "sync_mode": True,
    }
    if image_size:
        payload["image_size"] = image_size
    else:
        payload["image_size"] = "auto"
    if mask_url:
        payload["mask_url"] = mask_url

    resp = await client.post(
        FAL_EDIT,
        json=payload,
        headers={
            "Authorization": f"Key {api_key}",
            "Content-Type": "application/json",
        },
        timeout=120,
    )

    if resp.status_code != 200:
        print(f"fal.ai edit error ({resp.status_code}): {resp.text}", file=sys.stderr)
        sys.exit(1)

    return resp.json()


async def download_image(client: httpx.AsyncClient, url: str, path: Path) -> None:
    resp = await client.get(url, timeout=60)
    if resp.status_code != 200:
        print(f"Failed to download image ({resp.status_code})", file=sys.stderr)
        sys.exit(1)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(resp.content)


def build_picture_html(
    results: dict[str, dict],
    alt: str,
    fmt: str,
) -> str:
    desktop_src = results.get("desktop", {}).get("images", [{}])[0].get("filename")
    tablet_src = results.get("tablet", {}).get("images", [{}])[0].get("filename")
    mobile_src = results.get("mobile", {}).get("images", [{}])[0].get("filename")
    mobile_img = results.get("mobile", {}).get("images", [{}])[0]

    mime = "image/jpeg" if fmt == "jpeg" else f"image/{fmt}"
    parts = []

    # Art-directed <picture> for viewport breakpoints
    if desktop_src and tablet_src and mobile_src:
        dims = ""
        w = mobile_img.get("width")
        h = mobile_img.get("height")
        if w and h:
            dims = f' width="{w}" height="{h}"'
        parts.append(f"""<picture>
  <source media="(min-width: 1024px)" srcset="{desktop_src}" type="{mime}">
  <source media="(min-width: 768px)" srcset="{tablet_src}" type="{mime}">
  <img src="{mobile_src}" alt="{alt}" loading="eager"{dims} style="max-width:100%;height:auto;">
</picture>""")

    # Social/channel variants as standalone <img> tags
    for bp in ["social-square", "social-vertical", "email-banner"]:
        src = results.get(bp, {}).get("images", [{}])[0].get("filename")
        if src:
            w = results.get(bp, {}).get("images", [{}])[0].get("width", "")
            h = results.get(bp, {}).get("images", [{}])[0].get("height", "")
            dims = f' width="{w}" height="{h}"' if w and h else ""
            parts.append(f"""<!-- {bp} -->
<img src="{src}" alt="{alt}"{dims} loading="lazy" style="max-width:100%;height:auto;">""")

    return "\n\n".join(parts)


async def run_generate(args: argparse.Namespace) -> None:
    project_slug = slugify(args.project or args.prompt)
    output_dir = Path(args.output_dir or f"visual-assets/{project_slug}")
    ext = ext_for(args.output_format)

    async with httpx.AsyncClient() as client:
        results: dict[str, dict] = {}

        for bp in args.breakpoints:
            print(f"Generating {bp} hero...", file=sys.stderr)
            data = await fal_generate(
                client, args.prompt, bp, args.quality, args.output_format, args.num_images
            )
            saved = []
            for img in data.get("images", []):
                filename = f"hero-{bp}{ext}"
                out_path = output_dir / filename
                await download_image(client, img["url"], out_path)
                saved.append({
                    "filename": filename,
                    "path": str(out_path),
                    "width": img.get("width"),
                    "height": img.get("height"),
                })
            results[bp] = {"images": saved}

    # Save prompt
    ts = make_timestamp()
    prompt_path = output_dir / f"prompt-{ts}.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(args.prompt.strip() + "\n")

    # HTML snippet
    alt_text = args.prompt[:100].replace('"', "&quot;")

    html = build_picture_html(results, alt_text, args.output_format)
    html_path = output_dir / "responsive.html"
    html_path.write_text(html)

    if args.json:
        print(json.dumps({"results": results, "promptPath": str(prompt_path), "htmlPath": str(html_path), "outputDir": str(output_dir)}, indent=2))
    else:
        print(f"\nDone. Output: {output_dir}/", file=sys.stderr)
        for bp in args.breakpoints:
            for img in results.get(bp, {}).get("images", []):
                print(img["path"])
        print(str(prompt_path))
        print(str(html_path))


async def run_edit(args: argparse.Namespace) -> None:
    project_slug = slugify(args.project or args.prompt, "edit")
    output_dir = Path(args.output_dir or f"visual-assets/{project_slug}")
    ext = ext_for(args.output_format)

    async with httpx.AsyncClient() as client:
        print("Editing image...", file=sys.stderr)
        data = await fal_edit(
            client, args.prompt, args.image_urls, args.mask_url,
            args.image_size, args.quality, args.output_format, args.num_images
        )
        saved = []
        for i, img in enumerate(data.get("images", [])):
            filename = f"edited-{i}{ext}" if args.num_images > 1 else f"edited{ext}"
            out_path = output_dir / filename
            await download_image(client, img["url"], out_path)
            saved.append({
                "filename": filename,
                "path": str(out_path),
                "width": img.get("width"),
                "height": img.get("height"),
            })

    # Save prompt
    ts = make_timestamp()
    prompt_path = output_dir / f"prompt-{ts}.md"
    prompt_path.parent.mkdir(parents=True, exist_ok=True)
    prompt_path.write_text(args.prompt.strip() + "\n")

    if args.json:
        print(json.dumps({"images": saved, "promptPath": str(prompt_path), "outputDir": str(output_dir)}, indent=2))
    else:
        print(f"\nDone. Output: {output_dir}/", file=sys.stderr)
        for img in saved:
            print(img["path"])
        print(str(prompt_path))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate/edit art-directed images for any UI/UX surface via fal.ai GPT Image 2")
    sub = parser.add_subparsers(dest="command")

    # Generate subcommand
    gen = sub.add_parser("generate", help="Generate images per viewport/channel variant")
    gen.add_argument("--prompt", required=True, help="Hero image prompt")
    gen.add_argument("--project", help="Project slug for output directory")
    gen.add_argument("--breakpoints", default="desktop,tablet,mobile", help="Comma-separated variants: desktop,tablet,mobile,social-square,social-vertical,email-banner (default: desktop,tablet,mobile)")
    gen.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    gen.add_argument("--output-format", default="webp", choices=["webp", "png", "jpeg"], dest="output_format")
    gen.add_argument("--num-images", type=int, default=1, help="Images per breakpoint, 1-4")
    gen.add_argument("--output-dir", help="Override output directory")
    gen.add_argument("--json", action="store_true", help="Print structured JSON output")
    gen.add_argument("--prompt-file", help="Read prompt from file")

    # Edit subcommand
    edt = sub.add_parser("edit", help="Edit existing image(s) via fal.ai GPT Image 2 /edit")
    edt.add_argument("--prompt", required=True, help="Edit instruction prompt")
    edt.add_argument("--image-urls", required=True, nargs="+", help="URL(s) of source image(s)")
    edt.add_argument("--mask-url", help="URL of mask image (white=edit, black=keep)")
    edt.add_argument("--image-size", help="Output size preset or auto (default: auto)")
    edt.add_argument("--project", help="Project slug for output directory")
    edt.add_argument("--quality", default="high", choices=["auto", "low", "medium", "high"])
    edt.add_argument("--output-format", default="webp", choices=["webp", "png", "jpeg"], dest="output_format")
    edt.add_argument("--num-images", type=int, default=1, help="Number of outputs, 1-4")
    edt.add_argument("--output-dir", help="Override output directory")
    edt.add_argument("--json", action="store_true", help="Print structured JSON output")
    edt.add_argument("--prompt-file", help="Read prompt from file")

    args = parser.parse_args()

    # Resolve prompt from file if specified
    if args.prompt_file:
        args.prompt = Path(args.prompt_file).read_text().strip()

    # Parse breakpoints for generate
    if args.command == "generate":
        args.breakpoints = [b.strip() for b in args.breakpoints.split(",")]
        asyncio_run = __import__("asyncio").run
        asyncio_run(run_generate(args))
    elif args.command == "edit":
        asyncio_run = __import__("asyncio").run
        asyncio_run(run_edit(args))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
