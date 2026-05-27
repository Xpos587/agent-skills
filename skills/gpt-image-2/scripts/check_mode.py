#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""Detect gpt-image-2 runtime mode (A / B-or-C)."""

import json
import os
import sys

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent))
from shared import load_ambient_env, DEFAULT_MODEL, TRUTHY

load_ambient_env()

raw_flag = os.environ.get("ENABLE_GARDEN_IMAGEGEN", "").strip().lower()
garden_enabled = raw_flag in TRUTHY

api_key = os.environ.get("FAL_KEY", "") or os.environ.get("FAL_API_KEY", "")
model = os.environ.get("OPENAI_IMAGE_MODEL", DEFAULT_MODEL)

if garden_enabled and api_key:
    mode = "A"
    recommendation = "garden"
    summary = "MODE A: Use generate.py / edit.py via fal.ai to generate images and save to disk."
elif garden_enabled and not api_key:
    mode = "A?"
    recommendation = "garden-missing-key"
    summary = "ENABLE_GARDEN_IMAGEGEN is on but FAL_KEY is missing. Ask user for key or fallback to B/C."
else:
    mode = "B-or-C"
    recommendation = "host-or-advisor"
    summary = "MODE B/C: Garden not enabled. If host has image tools (image_generation/dalle/mcp__*image*) → B: pass prompt to host. If no image tools → C: output high-quality prompt only."

result = {
    "mode": mode,
    "recommendation": recommendation,
    "garden_mode_enabled": garden_enabled,
    "has_api_key": bool(api_key),
    "model": model,
    "env_flag_value": raw_flag or "(unset)",
    "summary": summary,
}

if "--json" in sys.argv:
    print(json.dumps(result, indent=2))
else:
    pad = lambda s: s.ljust(24)
    print("--- gpt-image-2 runtime mode ---")
    for k, v in result.items():
        if k == "summary":
            continue
        print(f"{pad(k)}: {v}")
    print()
    print(result["summary"])