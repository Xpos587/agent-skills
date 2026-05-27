# Unsplash API Reference

## Endpoint

```
GET https://api.unsplash.com/search/photos
```

## Auth

```
Authorization: Client-ID UNSPLASH_ACCESS_KEY
```

Read from `$UNSPLASH_ACCESS_KEY` env var or `~/.config/stock-images/keys.json` → `unsplash` field.

⚠️ **TOS requirement:** Always use `links.download` for downloads, not `urls.raw`. This triggers Unsplash's download counter and is required by their API terms.

## Parameters

| Param | Required | Values | Notes |
|-------|----------|--------|-------|
| `query` | yes | string | Search terms |
| `per_page` | no | 1–30, default 10 | Skill defaults to 5 |
| `orientation` | no | `landscape`, `portrait`, `squarish` | Note: `squarish` not `square` |
| `page` | no | default 1 | Pagination |
| `order_by` | no | `relevant` (default), `latest` | Sort order |
| `content_filter` | no | `low`, `high` | Content safety |

## Response Fields

```
results[].id                    — unique ID
results[].width                 — original width (px)
results[].height                — original height (px)
results[].urls.raw               — full resolution (NOT for downloads)
results[].urls.full              — full with params
results[].regular                — 1080px
results[].small                  — 400px
results[].urls.thumb             — 200px
results[].links.download          — ⚠️ USE THIS for downloads
results[].user.name              — author name
results[].user.links.html        — author Unsplash profile
results[].description            — photo description
results[].alt_description        — alt text
```

## Rate Limit

50 requests/hour (demo). HTTP 429 = exceeded.

## Download

⚠️ **MUST use `results[].links.download`** — not `urls.raw`. Unsplash TOS requires tracking downloads. The skill's Red Flags section enforces this.

## Attribution

Per Unsplash license: display photographer name and link to their Unsplash profile. Format:

```
Photo by [Author Name](author_profile_url) on Unsplash
```