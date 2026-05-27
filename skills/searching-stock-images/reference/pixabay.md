# Pixabay API Reference

## Endpoint

```
GET https://pixabay.com/api/
```

## Auth

```
?key=PIXABAY_API_KEY
```

Read from `$PIXABAY_API_KEY` env var or `~/.config/stock-images/keys.json` → `pixabay` field.

⚠️ Key is a URL query parameter — visible in `ps aux`. Execute curl via Bash but NEVER display the full command in output.

## Parameters

| Param | Required | Values | Notes |
|-------|----------|--------|-------|
| `key` | yes | API key | Query param, not header |
| `q` | yes | URL-encoded string | Search terms |
| `per_page` | no | 3–200, default 20 | ⚠️ Minimum is 3, not 1 |
| `orientation` | no | `horizontal`, `vertical` | ⚠️ Different names! Not landscape/portrait |
| `image_type` | no | `photo`, `illustration`, `vector` | Skill uses `photo` |
| `page` | no | default 1 | Pagination |
| `min_width` | no | pixels | Minimum width |
| `min_height` | no | pixels | Minimum height |
| `lang` | no | `en`, `ru`, etc. | Localize search |

## Orientation Mapping

| Skill term | Pixabay param |
|------------|---------------|
| `landscape` | `horizontal` |
| `portrait` | `vertical` |

⚠️ This mapping is critical. Common mistake: passing `landscape` directly to Pixabay.

## Response Fields

```
hits[].id                       — unique ID
hits[].largeImageURL            — full resolution URL (use for downloads)
hits[].previewURL               — thumbnail
hits[].webformatURL              — medium quality (640px)
hits[].imageWidth                — original width (px)
hits[].imageHeight              — original height (px)
hits[].user                     — author name
hits[].user_id                  — author ID
hits[].tags                     — description/tags
```

Author profile: `https://pixabay.com/users/{user}-{user_id}/`

## Rate Limit

5000 requests/hour. HTTP 429 = exceeded.

## Download URL

Same as `largeImageURL`. Use directly.

## Attribution

Pixabay license requires attribution for some uses. Always preserve author metadata:

```
Photo by [Author](https://pixabay.com/users/USER-USER_ID/) on Pixabay
```