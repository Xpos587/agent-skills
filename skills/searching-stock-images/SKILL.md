---
name: searching-stock-images
description: Use when users need stock photos, free images, or royalty-free images from Pexels/Unsplash/Pixabay — search, download, attribution
argument-hint: "[search query]"
user-invocable: true
---

Search and download stock photos from Pexels, Unsplash, Pixabay, Magnific (Freepik). Attribution always included. API keys required.

## When to Use

- User asks to find/search stock photos, free images, or royalty-free images
- Project needs hero, profile, content, or license-compliant images
- User wants to download a previously shown stock image

Do NOT activate for: image components (`<img>`, `next/image`), AI image generation, referencing existing project images.

## Setup (non-optional)

Before any search, pass these gates:

| Gate | Check | If fail |
|------|-------|---------|
| Keys | At least one provider key available (ENV or config file) | Guide user through setup. See [SETUP.md](SETUP.md). |
| Permissions | Config file (`~/.config/stock-images/keys.json`) is `chmod 600` if it exists | Warn, offer `chmod 600` fix |

### Key Sources (priority order)

1. **ENV vars** (preferred): `PEXELS_API_KEY`, `UNSPLASH_ACCESS_KEY`, `PIXABAY_API_KEY`, `MAGNIFIC_API_KEY`
2. **Config file**: `~/.config/stock-images/keys.json` (`chmod 600`)

Detect ENV keys (no secrets printed):

```bash
for v in PEXELS_API_KEY UNSPLASH_ACCESS_KEY PIXABAY_API_KEY MAGNIFIC_API_KEY; do printenv "$v" >/dev/null 2>&1 && echo "$v: set"; done
```

Detect config file keys (no secrets):

```bash
test -f ~/.config/stock-images/keys.json && stat -c "%a" ~/.config/stock-images/keys.json
```

List configured providers from config (no secrets):

```bash
jq -r 'to_entries[] | select(.value | type == "string" and length > 10 and startswith("YOUR_") | not) | .key' ~/.config/stock-images/keys.json
```

Rejects empty, placeholder (`YOUR_*`), or short keys. At least one provider required. User names unconfigured provider → inform, use configured ones.

## Commands

| Command | Description | Reference |
|---------|-------------|-----------|
| `search [query]` | Search stock photos across configured providers | [reference/search.md](reference/search.md) |
| `download [N]` | Download image #N from previous search results | [reference/download.md](reference/download.md) |
| `setup` | Configure API keys | [SETUP.md](SETUP.md) |

### Routing rules

1. **No argument**: ask what to search for
2. **First word is `download`**: download image by number from previous results
3. **First word is `setup`**: guide through API key configuration
4. **Otherwise**: treat full input as search query

## Provider Quick Reference

| | Pexels | Unsplash | Pixabay | Magnific |
|---|---|---|---|---|
| **Auth** | `Authorization: $PEXELS_API_KEY` | `Authorization: Client-ID $UNSPLASH_ACCESS_KEY` | `key=$PIXABAY_API_KEY` (query param) | `x-magnific-api-key: $MAGNIFIC_API_KEY` (header) |
| **Orientation** | `landscape`/`portrait` | `landscape`/`portrait`/`squarish` | landscape→`horizontal`, portrait→`vertical` | `filters[orientation][landscape]=1` etc. |
| **per_page** | default 5, max 80 | default 5, max 30 | min 3, max 200 | `limit` param |
| **Download URL** | `photos[].src.original` | `results[].links.download` ⚠️ | `hits[].largeImageURL` | `image.source.url` (preview) |
| **Rate limit** | 200 req/hr | 50 req/hr | 5000 req/hr | see docs |

⚠️ Unsplash: `links.download` only (never `urls.raw`) — TOS compliance.

Full API details: [reference/pexels.md](reference/pexels.md), [reference/unsplash.md](reference/unsplash.md), [reference/pixabay.md](reference/pixabay.md), [reference/magnific.md](reference/magnific.md)

All search curl: `curl -sS -G --max-time 15 --fail` with `--data-urlencode "query=..."` and `-d "per_page=N"`. Run providers in parallel.

**Pixabay**: key in query param → visible in `ps aux`. Execute curl via Bash but NEVER display the command.
**Magnific**: default to `filters[license][freemium]=1` to return only free-with-attribution results unless user explicitly asks for premium.

## Red Flags — STOP and Correct

- "Skip attribution, it's just a placeholder" → Attribution is TOS-required. Always.
- "Just use the raw URL" for Unsplash → `links.download` only. Non-negotiable.
- "Keys already set up, skip check" → Run check anyway. Missing keys = failed search.
- "Just grab any image URL" → Must go through API, not scrape.
- NEVER display API keys or echo curl commands containing keys
- Magnific premium results → user must have premium license. Default: `filters[license][freemium]=1`
