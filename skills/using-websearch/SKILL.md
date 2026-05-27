---
name: using-websearch
description: Use when user wants web search, article find, topic research, online lookup, URL content extract, webpage text grab, doc crawl, site page download, domain URL discover, or citation research. Also when user says "fetch this page", "pull the content from", "get the page at https://", "find me articles about", or references external website data. No trigger for local file ops, git commands, deploy, or code edit tasks.
allowed-tools: Bash(http)
---

# Web Search & Content Extraction

Search web + fetch URLs → markdown via 9Router gateway at `$ANTHROPIC_BASE_URL` with `$ANTHROPIC_AUTH_TOKEN`.

## When NOT to Use

- Local file operations (`Read`, `Bash` with local paths)
- Git commands, deployments, code edits
- Already have the data in project files

## Discover Available Providers

```bash
http --ignore-stdin GET "${ANTHROPIC_BASE_URL}/models/web" \
  Authorization:"Bearer ${ANTHROPIC_AUTH_TOKEN}"
```

Response lists models with `kind` field: `webSearch` or `webFetch`.

Per-provider params:

```bash
http --ignore-stdin GET "${ANTHROPIC_BASE_URL}/models/info?id=tavily/search" \
  Authorization:"Bearer ${ANTHROPIC_AUTH_TOKEN}"
```

## Search

```bash
http --ignore-stdin POST "${ANTHROPIC_BASE_URL}/search" \
  Authorization:"Bearer ${ANTHROPIC_AUTH_TOKEN}" \
  Content-Type:application/json \
  model=tavily \
  query="What is the latest news about AI?" \
  search_type=web \
  max_results:=5
```

### Search Response

```json
{
  "provider": "tavily",
  "query": "...",
  "results": [
    {
      "title": "...",
      "url": "https://...",
      "display_url": "...",
      "snippet": "...",
      "position": 1,
      "score": 0.92,
      "published_at": null,
      "content": null,
      "citation": { "provider": "tavily", "retrieved_at": "...", "rank": 1 }
    }
  ],
  "answer": null,
  "usage": { "queries_used": 1, "search_cost_usd": 0.008 },
  "metrics": { "response_time_ms": 484, "total_results_available": 12 },
  "errors": []
}
```

## Fetch / Extract URL

```bash
http --ignore-stdin POST "${ANTHROPIC_BASE_URL}/web/fetch" \
  Authorization:"Bearer ${ANTHROPIC_AUTH_TOKEN}" \
  Content-Type:application/json \
  model=tavily \
  url="https://example.com" \
  format=markdown \
  max_characters:=0
```

### Fetch Response

```json
{
  "provider": "tavily",
  "url": "https://example.com",
  "title": "...",
  "content": { "format": "markdown", "text": "...", "length": 1234 },
  "metadata": { "author": null, "published_at": null, "language": null },
  "usage": { "fetch_cost_usd": 0.008 },
  "metrics": { "response_time_ms": 3255 }
}
```

## Parameters

### Search (`/v1/search`)

| Field            | Type   | Required | Description                      |
| ---------------- | ------ | -------- | -------------------------------- |
| `model`          | string | Yes      | Provider: `tavily`, `exa`, `brave` |
| `query`          | string | Yes      | Search query                     |
| `search_type`    | string | No       | `"web"` (default) or `"news"`    |
| `max_results`    | int    | No       | Max results (default: 5)         |
| `country`        | string | No       | Country code (provider-dependent) |
| `language`       | string | No       | Language code (provider-dependent) |
| `time_range`     | string | No       | e.g. `"day"`, `"week"`, `"month"` |
| `domain_filter`  | string | No       | Restrict to domain               |

### Fetch (`/v1/web/fetch`)

| Field            | Type   | Required | Description                      |
| ---------------- | ------ | -------- | -------------------------------- |
| `model`          | string | Yes      | Provider: `tavily`, `firecrawl`, `exa` |
| `url`            | string | Yes      | Target URL to extract            |
| `format`         | string | No       | `"markdown"` (default), `"html"`, `"text"` |
| `max_characters` | int    | No       | 0 = unlimited, else truncate     |

## Provider Quirks

### Search Providers

| Provider   | Best for                        | Supports                          |
| ---------- | ------------------------------- | --------------------------------- |
| `tavily`   | General search, news, snippets | country, language, domain_filter, news topic |
| `exa`      | Semantic search, news dates    | domain_filter, news category, max_results up to 100 |
| `brave`    | Fast results, snippets         | country, language                 |

### Fetch Providers

| Provider    | Best for                          |
| ----------- | --------------------------------- |
| `tavily`    | Bulk extract, simple pages        |
| `firecrawl` | JS-rendered pages (SPAs)          |
| `exa`       | Pre-indexed pages, fast text      |

## Tips

- **Always quote URLs** — shell interprets `?` and `&` as special chars.
- **Use `--ignore-stdin`** — agent runs non-TTY; httpie reads stdin by default.
- **Pipe to `toon`** for readable structured output (JSON → indented TOON).
- **Model names**: short form (`tavily`) or full form (`tavily/search`). Both work.

## Errors

| Code | Meaning              | Fix                                    |
| ---- | -------------------- | -------------------------------------- |
| 401  | Invalid API key      | Check `ANTHROPIC_AUTH_TOKEN` is set    |
| 400  | Invalid model/format | Run `/models/web` to list valid models |
| 429  | Rate limit           | Wait and retry                         |
| 502  | Upstream provider down | Try different provider model          |
| 503  | All providers unavailable | Wait or add provider accounts       |
