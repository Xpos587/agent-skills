# Search Reference

## Extracting Search Parameters

From user request, extract:

| Parameter | Required | Default | How to infer |
|-----------|----------|---------|--------------|
| `query` | yes | — | Direct from user |
| `count` | no | 5 | "few" → 3, "many" → 10, number if specified, max 20 |
| `orientation` | no | all | hero/banner → `landscape`, avatar/profile → `portrait`, thumbnail/icon → `square` |
| `provider` | no | all configured | If user names a provider, use it. Otherwise search all |

## Search Flow

1. Run setup detection (see SKILL.md)
2. Extract parameters from user request
3. For each configured provider, run curl in parallel (separate Bash calls)
4. Parse JSON responses
5. Preserve full results for follow-up "download image #N"
6. Present results, ask if user wants to download

## Curl Templates

### Pexels

```bash
curl -sS -G --max-time 15 --fail "https://api.pexels.com/v1/search" \
  --data-urlencode "query=SEARCH_QUERY" \
  -d "per_page=COUNT" \
  -d "orientation=ORIENTATION" \
  -H "Authorization: $PEXELS_API_KEY"
```

Or from config file: replace `$PEXELS_API_KEY` with the key value, but NEVER display the command.

### Unsplash

```bash
curl -sS -G --max-time 15 --fail "https://api.unsplash.com/search/photos" \
  --data-urlencode "query=SEARCH_QUERY" \
  -d "per_page=COUNT" \
  -d "orientation=ORIENTATION" \
  -H "Authorization: Client-ID $UNSPLASH_ACCESS_KEY"
```

### Pixabay

```bash
curl -sS -G --max-time 15 --fail "https://pixabay.com/api/" \
  -d "key=$PIXABAY_API_KEY" \
  --data-urlencode "q=SEARCH_QUERY" \
  -d "per_page=COUNT" \
  -d "orientation=ORIENTATION" \
  -d "image_type=photo"
```

⚠️ Pixabay orientation mapping: `landscape` → `horizontal`, `portrait` → `vertical`
⚠️ Pixabay per_page minimum is 3
⚠️ NEVER display Pixabay curl command in output (key visible in process list)

### Magnific (Freepik)

```bash
curl -sS -G --max-time 15 --fail "https://api.magnific.com/v1/resources" \
  --data-urlencode "term=SEARCH_QUERY" \
  -d "limit=COUNT" \
  -d "filters[orientation][ORIENTATION_FLAG]=1" \
  -d "filters[license][freemium]=1" \
  -H "x-magnific-api-key: $MAGNIFIC_API_KEY"
```

⚠️ Magnific orientation mapping: `landscape` → `landscape`, `portrait` → `portrait`, `square` → `square`
⚠️ Default to `filters[license][freemium]=1` unless user explicitly wants premium
⚠️ NEVER display Magnific curl command in output (key in header)

## Error Handling

| Error | Action |
|-------|--------|
| curl non-zero / timeout | Skip provider, continue |
| HTTP 401 | Key invalid — suggest re-setup |
| HTTP 429 | Rate limit — wait or try other provider |
| Empty/malformed JSON | Skip provider, continue |
| All providers return 0 results | Suggest alternative search terms |
| Malformed keys.json | Inform user, offer to recreate |

## Presenting Results

Present in user's language. Format:

```
## Results for "query" (N images)

### Pexels
1. "Description" — by [Author](profile_url)
   URL: https://...
   Resolution: WxH

### Unsplash
2. ...
```

Number each result. Include author attribution link. Ask if user wants to download any.