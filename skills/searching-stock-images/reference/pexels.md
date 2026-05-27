# Pexels API Reference

## Endpoint

```
GET https://api.pexels.com/v1/search
```

## Auth

```
Authorization: PEXELS_API_KEY
```

Read from `$PEXELS_API_KEY` env var or `~/.config/stock-images/keys.json` → `pexels` field.

## Parameters

| Param | Required | Values | Notes |
|-------|----------|--------|-------|
| `query` | yes | URL-encoded string | Search terms |
| `per_page` | no | 1–80, default 15 | Skill defaults to 5 |
| `orientation` | no | `landscape`, `portrait` | No `square` option |
| `page` | no | default 1 | Pagination |
| `size` | no | `original`, `large`, `medium` | Image size preference |
| `color` | no | hex or named | Filter by color |
| `locale` | no | e.g. `en-US`, `ru-RU` | Localize results |

## Response Fields

```
photos[].id                    — unique ID
photos[].width                 — original width (px)
photos[].height                — original height (px)
photos[].url                   — Pexels page URL
photos[].photographer          — author name
photos[].photographer_url      — author profile
photos[].alt                   — description
photos[].src.original          — full resolution URL
photos[].src.large             — large (max 1000px)
photos[].src.medium            — medium (max 350px)
photos[].src.small             — small (max 130px)
```

## Rate Limit

200 requests/hour. HTTP 429 = exceeded, wait or try another provider.

## Download URL

Same as `src.original`. Use directly for downloads.