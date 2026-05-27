#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""GPT Image 2 — generate and edit via fal.ai (Mode A only).

Usage:
  gpt-image-2.py generate --prompt "..." [--output out.png]
  gpt-image-2.py edit --image src.png --prompt "..." [--output out.png]
  gpt-image-2.py edit --image src.png --mask mask.png --prompt "..."
"""

import argparse
import json
import os
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from shared import (
    FAL_GENERATE_URL,
    FAL_EDIT_URL,
    build_default_image_path,
    download_url,
    ensure_files_exist,
    extract_fal_images,
    load_ambient_env,
    post_fal_json,
    read_prompt_input,
    resolve_output,
    save_image,
    save_prompt,
    slugify,
    upload_to_fal_cdn,
)


def add_common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--prompt", help="Prompt text")
    p.add_argument("--prompt-file", dest="prompt_file", help="Load prompt from file")
    p.add_argument("--prompt-output", help="Save final prompt to specific file")
    p.add_argument("--output", help="Output image path")
    p.add_argument("--image-size", default=None, help="Image size preset or WxH (e.g. landscape_4_3, square, 1024x1024)")
    p.add_argument("--num-images", type=int, default=1, help="Number of images (1-4, default: 1)")
    p.add_argument("--quality", default="auto", help="auto|low|medium|high (default: auto)")
    p.add_argument("--output-format", help="png|jpeg|webp")
    p.add_argument("--sync", type=bool, default=True, help="Use sync_mode (default: true)")
    p.add_argument("--json", action="store_true", help="Print structured JSON output")


def cmd_generate(args: argparse.Namespace) -> None:
    prompt = read_prompt_input(args.prompt, args.prompt_file)
    name_hint = slugify(" ".join(prompt.split()[:8]), "generated-image")
    prompt_path = save_prompt(prompt, args.prompt_output, name_hint)
    output_path = resolve_output(args.output, build_default_image_path("generate", name_hint))

    payload: dict = {"prompt": prompt}
    if args.image_size:
        payload["image_size"] = args.image_size
    if args.num_images and args.num_images > 1:
        payload["num_images"] = args.num_images
    if args.quality and args.quality != "auto":
        payload["quality"] = args.quality
    if args.output_format:
        payload["output_format"] = args.output_format

    resp = post_fal_json(FAL_GENERATE_URL, payload, sync_mode=args.sync)
    images = extract_fal_images(resp)

    saved = save_all_images(images, output_path, args.num_images)

    print_result(saved, prompt_path, FAL_GENERATE_URL, resp, args)


def cmd_edit(args: argparse.Namespace) -> None:
    if not args.image:
        print("Error: --image is required for edit. Provide source image path.", file=sys.stderr)
        sys.exit(1)

    files_to_check = [args.image]
    if args.mask:
        files_to_check.append(args.mask)
    ensure_files_exist(files_to_check, "Image file")

    prompt = read_prompt_input(args.prompt, args.prompt_file)
    name_hint = slugify(" ".join(prompt.split()[:8]), "edited-image")
    prompt_path = save_prompt(prompt, args.prompt_output, name_hint)
    output_path = resolve_output(args.output, build_default_image_path("edit", name_hint))

    print(f"Uploading {args.image} to fal.ai CDN...", file=sys.stderr)
    image_url = upload_to_fal_cdn(args.image)

    payload: dict = {
        "prompt": prompt,
        "image_urls": [image_url],
    }
    if args.mask:
        print(f"Uploading mask {args.mask} to fal.ai CDN...", file=sys.stderr)
        mask_url = upload_to_fal_cdn(args.mask)
        payload["mask_url"] = mask_url
    if args.image_size:
        payload["image_size"] = args.image_size
    if args.num_images and args.num_images > 1:
        payload["num_images"] = args.num_images
    if args.quality and args.quality != "auto":
        payload["quality"] = args.quality
    if args.output_format:
        payload["output_format"] = args.output_format

    resp = post_fal_json(FAL_EDIT_URL, payload, sync_mode=args.sync)
    images = extract_fal_images(resp)

    saved = save_all_images(images, output_path, args.num_images)

    print_result(saved, prompt_path, FAL_EDIT_URL, resp, args)


def save_all_images(images: list[dict], base_path: str, num_requested: int) -> list[str]:
    """Save all returned images. Returns list of saved paths."""
    saved = []
    for i, img_info in enumerate(images):
        img_url = img_info["url"]
        img_bytes = download_url(img_url)
        if len(images) == 1:
            target = base_path
        else:
            p = pathlib.Path(base_path)
            target = str(p.parent / f"{p.stem}-{i + 1}{p.suffix}")
        save_image(target, img_bytes)
        saved.append(target)

    if num_requested > 1 and len(images) < num_requested:
        print(
            f"Warning: requested {num_requested} images but got {len(images)}.",
            file=sys.stderr,
        )
    return saved


def print_result(
    saved: list[str],
    prompt_path: str,
    request_url: str,
    resp: dict,
    args: argparse.Namespace,
) -> None:
    if args.json:
        print(json.dumps({
            "savedImages": saved,
            "savedPrompt": prompt_path,
            "requestUrl": request_url,
            "imageCount": len(saved),
            "apiResponse": resp,
        }, indent=2))
    elif len(saved) == 1:
        print(saved[0])
    else:
        for p in saved:
            print(p)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="GPT Image 2 — generate and edit via fal.ai (Mode A)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    gen = sub.add_parser("generate", help="Generate image from text prompt")
    add_common_args(gen)

    edt = sub.add_parser("edit", help="Edit existing image")
    edt.add_argument("--image", required=True, help="Source image path (required for edit)")
    edt.add_argument("--mask", help="Mask image path for inpainting")
    add_common_args(edt)

    args = parser.parse_args()
    load_ambient_env()

    if args.command == "generate":
        cmd_generate(args)
    elif args.command == "edit":
        cmd_edit(args)


if __name__ == "__main__":
    main()
