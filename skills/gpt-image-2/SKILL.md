---
name: gpt-image-2
description: Use when user requests image generation or editing, needs visual content created, or asks to produce posters mockups infographics diagrams or any visual asset
---

# GPT Image 2

3 runtime modes, behavior differs significantly. **Determine mode first.**

```bash
<skill-dir>/scripts/check_mode.py        # human-readable
<skill-dir>/scripts/check_mode.py --json  # JSON output
```

> Scripts use `uv run --script` shebang. Run directly — **NEVER prefix with `python`**.

## Runtime Modes

| Condition | Mode | Scripts? | Save prompt? | Save image? |
|---|---|---|---|---|
| `ENABLE_GARDEN_IMAGEGEN=1` + FAL_KEY | **A** | ✅ `gpt-image-2.py` | ✅ auto | ✅ auto |
| `ENABLE_GARDEN_IMAGEGEN=1` + no FAL_KEY | A? | ❌ need key first | — | — |
| Not enabled + host has image tool | **B** | ❌ use host tool | optional | host decides |
| Not enabled + no image tool | **C** | ❌ | ✅ required | ❌ impossible |

**Mode A** — Garden Local: full pipeline (template → prompt → script → image).
**Mode B** — Host Delegation: render prompt → pass to host's image tool (`image_generation`/`dalle`/`mcp__*image*`).
**Mode C** — Advisor: write prompt, save to disk, display to user. **Never pretend image was generated.**

Uncertain B vs C? **Ask**: "Use your environment's image tool, or just write the prompt?"
Mode A fails (401/quota) → report error, ask "switch to B/C?"

## Config

**Env vars** (read: CLI → env → `<cwd>/.env` → `<cwd>/.gateway.env` → `~/.gateway.env`):

- `ENABLE_GARDEN_IMAGEGEN` — mode switch. Truthy → A; unset → B/C.
- `FAL_KEY` — fal.ai API key (Mode A); `FAL_API_KEY` as fallback.
- `OPENAI_IMAGE_MODEL` — default `openai/gpt-image-2`.

**Output** (`<task-slug>` auto-extracted, `<timestamp>` = `YYYYMMDD-HHmmss`):

- Prompt: `garden-gpt-image-2/prompt/<task-slug>-<timestamp>.md`
- Image: `garden-gpt-image-2/image/<task-slug>-<timestamp>.png` (Mode A only)

Prompt save: Mode A ✅ | Mode B optional | Mode C ✅. Override with `--prompt-output`.

## Quick Usage (Mode A)

```bash
<skill-dir>/scripts/check_mode.py                            # ALWAYS first
<skill-dir>/scripts/gpt-image-2.py generate --prompt "..."   # text-to-image
<skill-dir>/scripts/gpt-image-2.py generate --prompt-file p.md --num-images 3 --output out.png
<skill-dir>/scripts/gpt-image-2.py edit --image src.png --prompt "..."
<skill-dir>/scripts/gpt-image-2.py edit --image src.png --mask mask.png --prompt "..."
```

Key flags: `--image-size`, `--quality` (auto|low|medium|high), `--output-format` (png|jpeg|webp), `--json`.

Mode B/C: no CLI. Render prompt → host tool (B) or display (C).

## Template Workflow

1. Run `check_mode.py` → determine A/B/C.
2. Identify task: generate or edit.
3. Find matching category in `references/template-index.md`.
4. Read only that template file — **never scan all `references/`**.
5. JSON templates for structured tasks; natural-language where JSON constrains creativity.
6. Map user input → template params. Ask only when missing info significantly affects result.

Prompt rendered → mode fork:

- **A**: save prompt, call `gpt-image-2.py generate/edit`, save image.
- **B**: pass prompt to host image tool. Optionally save prompt.
- **C**: save prompt, display to user with usage suggestions.

Report: mode, prompt path, image path (if any).

## Common Mistakes

- Scanning entire `references/` → read only the one matching template
- Pretending image was generated in Mode C → C never produces images
- Calling scripts in Mode B/C → `gpt-image-2.py` only works in Mode A
- Copying SKILL.md content into prompts → this is agent meta-info
- Vague questions ("what style?") → ask targeted per-template-field questions

## Constraints

- Template JSON = prompt structure, not API request body.
- Final output = rendered prompt string (flattened JSON or natural language).
- Mode A: fal.ai backend. `generate` → `POST https://fal.run/openai/gpt-image-2`; `edit` → upload to CDN then `POST …/edit` with `image_urls`/`mask_url`. Response: `images[].url`. Multi-image: `--num-images N` saves `base-1.png`, `base-2.png`, etc.
- Edit workflow: local file → CDN upload → URL → JSON body. No multipart needed.