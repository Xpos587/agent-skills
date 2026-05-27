#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""Shared utilities for gpt-image-2 scripts (fal.ai backend)."""

import os
import re
import sys
import json
import pathlib
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from urllib.parse import quote

DEFAULT_IMAGE_DIR = "garden-gpt-image-2/image"
DEFAULT_PROMPT_DIR = "garden-gpt-image-2/prompt"
DEFAULT_MODEL = "openai/gpt-image-2"
FAL_GENERATE_URL = "https://fal.run/openai/gpt-image-2"
FAL_EDIT_URL = "https://fal.run/openai/gpt-image-2/edit"
FAL_STORAGE_UPLOAD_URL = "https://api.fal.ai/v1/serverless/files/file/local"

TRUTHY = {"1", "true", "yes", "on", "y"}


def load_ambient_env() -> None:
    """Load .env / .gateway.env files into os.environ (don't overwrite existing)."""
    places = [
        pathlib.Path(os.getcwd()) / ".env",
        pathlib.Path(os.getcwd()) / ".gateway.env",
        pathlib.Path.home() / ".gateway.env",
    ]
    for p in places:
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip()
            if value.startswith(('"', "'")) and value.endswith(value[0]):
                value = value[1:-1]
            if key not in os.environ:
                os.environ[key] = value


def read_prompt_input(prompt: str | None, prompt_file: str | None) -> str:
    if prompt:
        return prompt.strip()
    if prompt_file:
        return pathlib.Path(prompt_file).resolve().read_text(encoding="utf-8").strip()
    print("Error: Prompt is required. Use --prompt or --promptfile.", file=sys.stderr)
    sys.exit(1)


_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slugify(value: str, fallback: str = "image-task") -> str:
    base = value.strip().lower()
    base = re.sub(r"[̀-ͯ]", "", base)
    base = _SLUG_RE.sub("-", base).strip("-")
    return base[:48] or fallback


def make_timestamp() -> str:
    now = datetime.now(timezone.utc).astimezone()
    return now.strftime("%Y%m%d-%H%M%S")


def build_default_image_path(kind: str, hint: str, ext: str = ".png") -> str:
    stamp = make_timestamp()
    slug = slugify(hint, "edited-image" if kind == "edit" else "generated-image")
    return str(pathlib.Path(DEFAULT_IMAGE_DIR) / f"{slug}-{stamp}{ext}")


def build_default_prompt_path(hint: str) -> str:
    stamp = make_timestamp()
    slug = slugify(hint, "prompt")
    return str(pathlib.Path(DEFAULT_PROMPT_DIR) / f"{slug}-{stamp}.md")


def resolve_output(raw: str | None, fallback_path: str) -> str:
    target = raw or fallback_path
    full = str(pathlib.Path(target).resolve())
    if not pathlib.Path(full).suffix:
        full += ".png"
    return full


def save_prompt(prompt_text: str, raw_path: str | None, hint: str) -> str:
    final_path = str(pathlib.Path(raw_path or build_default_prompt_path(hint)).resolve())
    pathlib.Path(final_path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(final_path).write_text(prompt_text.strip() + "\n", encoding="utf-8")
    return final_path


def require_fal_key() -> str:
    key = os.environ.get("FAL_KEY", "") or os.environ.get("FAL_API_KEY", "")
    if not key:
        print("Error: FAL_KEY or FAL_API_KEY is required. Set it or add to .env.", file=sys.stderr)
        sys.exit(1)
    if not os.environ.get("FAL_KEY") and os.environ.get("FAL_API_KEY"):
        os.environ["FAL_KEY"] = key
    return key


def ensure_files_exist(files: list[str], label: str) -> None:
    for f in files:
        p = pathlib.Path(f).resolve()
        if not p.exists():
            print(f"Error: {label} not found: {p}", file=sys.stderr)
            sys.exit(1)


def fal_auth_header() -> dict[str, str]:
    return {"Authorization": f"Key {require_fal_key()}"}


def post_fal_json(url: str, payload: dict, sync_mode: bool = True) -> dict:
    """POST JSON to fal.ai. Returns parsed response."""
    headers = fal_auth_header()
    headers["Content-Type"] = "application/json"
    payload = {**payload, "sync_mode": sync_mode}
    data = json.dumps(payload).encode("utf-8")
    req = Request(url, data=data, headers=headers, method="POST")
    try:
        with urlopen(req) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 401:
            hint = "Check FAL_KEY / FAL_API_KEY env var. Get key at fal.ai/dashboard/keys"
        elif e.code == 402:
            hint = "Quota exceeded. Check billing at fal.ai/dashboard"
        elif e.code == 429:
            hint = "Rate limited. Wait and retry, or reduce request frequency"
        else:
            hint = "Check model name and payload parameters"
        print(f"fal.ai API error ({e.code}): {body}\nRecovery hint: {hint}", file=sys.stderr)
        sys.exit(1)


def upload_to_fal_cdn(file_path: str) -> str:
    """Upload a local file to fal.ai CDN storage. Returns the public URL."""
    key = require_fal_key()
    file_name = pathlib.Path(file_path).name
    target_path = f"gpt-image-2/{make_timestamp()}-{file_name}"
    upload_url = f"{FAL_STORAGE_UPLOAD_URL}/{quote(target_path, safe='/')}"

    file_bytes = pathlib.Path(file_path).resolve().read_bytes()
    ext = pathlib.Path(file_path).suffix.lower()
    content_type = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif",
    }.get(ext, "application/octet-stream")

    boundary = "----FalUploadBoundary" + make_timestamp()
    body_parts: list[bytes] = []

    # file_upload field
    body_parts.append(f"--{boundary}\r\n".encode())
    body_parts.append(
        f'Content-Disposition: form-data; name="file_upload"; filename="{file_name}"\r\n'.encode()
    )
    body_parts.append(f"Content-Type: {content_type}\r\n\r\n".encode())
    body_parts.append(file_bytes)
    body_parts.append(b"\r\n")
    body_parts.append(f"--{boundary}--\r\n".encode())

    body = b"".join(body_parts)
    req = Request(
        upload_url,
        data=body,
        headers={
            "Authorization": f"Key {key}",
            "Content-Type": f"multipart/form-data; boundary={boundary}",
        },
        method="POST",
    )
    try:
        with urlopen(req) as resp:
            result = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"fal.ai upload error ({e.code}): {err_body}", file=sys.stderr)
        sys.exit(1)

    # Response contains the file URL
    url = result.get("url") or result.get("file_url") or ""
    if not url:
        url = f"https://fal.media/files/{target_path}"
        print(f"Warning: CDN upload response missing URL. Constructed fallback: {url}", file=sys.stderr)
    return url


def download_url(url: str) -> bytes:
    """Download bytes from a URL."""
    req = Request(url)
    with urlopen(req) as resp:
        return resp.read()


def extract_fal_images(data: dict) -> list[dict]:
    """Extract image info from fal.ai response. Returns list of {url, width, height}."""
    images = data.get("images")
    if not images:
        keys = list(data.keys())
        print(
            f"Error: fal.ai response missing 'images' key. Response keys: {keys}. "
            f"Check model name matches a fal.ai image model.",
            file=sys.stderr,
        )
        sys.exit(1)
    return images


def save_image(output_path: str, data_bytes: bytes) -> None:
    p = pathlib.Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data_bytes)