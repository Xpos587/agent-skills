# Magnific (Freepik) API Reference

**Base URL**: `https://api.magnific.com`
**Auth**: `x-magnific-api-key: $MAGNIFIC_API_KEY` header
**Docs**: https://docs.magnific.com/llms.txt

## Search

```
GET /v1/resources
```

### Parameters

| Param | Location | Required | Values |
|-------|----------|----------|--------|
| `term` | query | no | Search query |
| `page` | query | no | Page number (1–100) |
| `limit` | query | no | Results per page |
| `order` | query | no | `relevance` (default), `recent` |
| `Accept-Language` | header | no | ISO 639-1 + ISO 3166-1, e.g. `en-US` |
| `filters[orientation][landscape]` | query | no | `1` to enable |
| `filters[orientation][portrait]` | query | no | `1` to enable |
| `filters[orientation][square]` | query | no | `1` to enable |
| `filters[orientation][panoramic]` | query | no | `1` to enable |
| `filters[content_type][photo]` | query | no | `1` to enable |
| `filters[content_type][vector]` | query | no | `1` to enable |
| `filters[content_type][psd]` | query | no | `1` to enable |
| `filters[license][freemium]` | query | no | `1` — free with attribution |
| `filters[license][premium]` | query | no | `1` — paid |
| `filters[color]` | query | no | `black`, `blue`, `gray`, `green`, `orange`, `red`, `white`, `yellow`, `purple`, `cyan`, `pink` |
| `filters[ai_generated][excluded]` | query | no | `1` — exclude AI |
| `filters[ai_generated][only]` | query | no | `1` — AI only |

### Response

```json
{
  "data": [
    {
      "id": 770011,
      "title": "Sports car",
      "url": "https://www.freepik.com/free-icon/sports-car_770011.htm",
      "filename": "sports-car.zip",
      "image": {
        "type": "photo",
        "orientation": "square",
        "source": { "url": "https://img.freepik.com/...", "key": "large", "size": "128x128" }
      },
      "author": { "id": 744082, "name": "flaticon", "avatar": "...", "slug": "flaticon", "assets": 0 },
      "licenses": [{ "type": "freemium", "url": "https://www.freepik.com/profile/license/pdf/770011?lang=en" }],
      "stats": { "downloads": 52527, "likes": 137 },
      "meta": { "is_new": true, "published_at": "2022-01-14T20:45:28.000Z" }
    }
  ],
  "meta": { "current_page": 1, "last_page": 32, "per_page": 2, "total": 63 }
}
```

### Orientation Mapping

| Skill param | Magnific param |
|-------------|----------------|
| `landscape` | `filters[orientation][landscape]=1` |
| `portrait` | `filters[orientation][portrait]=1` |
| `square` | `filters[orientation][square]=1` |

### Curl Template

```bash
curl -sS -G --max-time 15 --fail "https://api.magnific.com/v1/resources" \
  --data-urlencode "term=SEARCH_QUERY" \
  -d "limit=COUNT" \
  -d "filters[orientation][ORIENTATION_FLAG]=1" \
  -d "filters[license][freemium]=1" \
  -H "x-magnific-api-key: $MAGNIFIC_API_KEY"
```

Or from config file: replace `$MAGNIFIC_API_KEY` with the key value, but NEVER display the command.

## Error Handling

| HTTP Status | Meaning |
|-------------|---------|
| 400 | Invalid parameter — check query |
| 401 | Missing or invalid API key |
| 403 | Not authorized / premium-only resource |
| 404 | Resource not found |
| 503 | Service unavailable — retry later |

## Rate Limits

Check https://docs.magnific.com for current limits. Default: not specified in API spec.

## Default Search Behavior

Default to `filters[license][freemium]=1` to return only free-with-attribution results unless user explicitly requests premium content.