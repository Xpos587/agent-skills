# Rospatent Search Platform API

Base URL: `https://searchplatform.rospatent.gov.ru`

Public API — no authentication required for search. Session created automatically.

## Endpoints

### Search Patents/Trademarks/Designs

```
POST /search?t=<timestamp>
Content-Type: application/json
```

**Request body:**

```json
{
  "qn": "<search query>",
  "offset": 0,
  "limit": 10,
  "pre_tag": "<span style='background: yellow' class=\"marked-element\">",
  "post_tag": "</span>",
  "include_facets": 0,
  "sort": "relevance",
  "highlight": { "profiles": ["_searchquery_"] },
  "countStatistics": true,
  "datasets": ["ru_since_1994", "ru_till_1994"],
  "preffered_lang": "ru"
}
```

**Key parameters:**

| Parameter | Values | Notes |
|---|---|---|
| `qn` | Free text query | Supports Cyrillic and Latin |
| `offset` | 0+ | Pagination offset |
| `limit` | 1–100 | Results per page |
| `sort` | `"relevance"` or `"date_desc"` | Sort order |
| `include_facets` | 0 or 1 | Include facet counts |
| `datasets` | See sources below | Which databases to search |
| `preffered_lang` | `"ru"` or `"en"` | Response language (note: typo is in API) |

**Dataset IDs for Russian IP:**

| ID | Description |
|---|---|
| `ru_since_1994` | Russian patents from 1994 (inventions, utility models) |
| `ru_till_1994` | Russian patents before 1994 (USSR legacy) |
| `dsgn_ru` | Russian industrial designs |
| `programs` | Computer programs (search via /integral path) |
| `topologies` | IC layouts (search via /integral path) |
| `copyrights_db` | Copyright-protected databases (via /integral) |
| `related_rights_db` | Related rights databases (via /integral) |

**International datasets:** `cn`, `us`, `ep`, `de`, `fr`, `gb`, `jp`, `kr`, `ch`, `at`, `au`, `ca`, `pct`, `ap`, `cis`, `others`, `dsgn_kr`, `dsgn_cn`, `dsgn_jp`

**Response structure:**

```json
{
  "total": 3328,
  "available": 1000,
  "hits": [
    {
      "id": "FR0000828733A_19380527",
      "index": "may22_fr",
      "dataset": "fr",
      "similarity": 86.68,
      "similarity_norm": 0.989,
      "common": {
        "publishing_office": "RU",
        "document_number": "...",
        "kind": "A",
        "publication_date": "2024.01.15",
        "classification": {
          "cpc": [{ "fullname": "A63K17/00" }],
          "ipc": [{ "fullname": "A63K17/00" }]
        },
        "application": {
          "number": "...",
          "filing_date": "2023.06.01"
        },
        "priority": [{ "number": "...", "filing_date": "...", "publishing_office": "RU" }]
      },
      "biblio": {
        "ru": { "title": "...", "applicant": [{ "name": "..." }] },
        "en": { "title": "...", "applicant": [{ "name": "..." }] }
      },
      "snippet": {
        "title": "...",
        "description": "...highlighted text..."
      }
    }
  ],
  "timings": { ... }
}
```

### Autocomplete (SGS)

```
GET /sgs?q=<query>&search_type=patent&t=<timestamp>
```

Returns: `{"suggests": [{"text": "...", "type": "..."}]}`

Often returns empty for specific queries. Use for broad term suggestions only.

### Sources Tree

```
GET /sources/tree?t=<timestamp>
```

Returns patent/trademark dataset hierarchy (categories + datasets).

```
GET /sources/tree/integral?t=<timestamp>
```

Returns non-patent IP sources (programs, topologies, databases).

### Session

```
POST /api/session_current?t=<timestamp>
Body: {}
```

Returns: `{"username": null}` for anonymous access.

## CLI Usage

```bash
# Search Russian patents (since 1994)
curl -s 'https://searchplatform.rospatent.gov.ru/search' \
  -H 'Content-Type: application/json' \
  -d '{"qn":"нейронная сеть","offset":0,"limit":10,"sort":"relevance","include_facets":0,"highlight":{"profiles":["_searchquery_"]},"countStatistics":true,"datasets":["ru_since_1994"],"preffered_lang":"ru"}' \
  | jq '{total, available, hits: [.hits[] | {id, dataset, similarity_norm, title: .biblio.ru.title, applicant: [.biblio.ru.applicant[].name], date: .common.publicution_date, ipc: [.common.classification.ipc[].fullname]}]}'

# Search trademarks (use dsgn_ru for designs, ru_since_1994 includes TZ in some queries)
curl -s 'https://searchplatform.rospatent.gov.ru/search' \
  -H 'Content-Type: application/json' \
  -d '{"qn":"Сбер","offset":0,"limit":5,"sort":"relevance","include_facets":0,"highlight":{"profiles":["_searchquery_"]},"countStatistics":true,"datasets":["ru_since_1994"],"preffered_lang":"ru"}'

# Search computer programs
curl -s 'https://searchplatform.rospatent.gov.ru/search' \
  -H 'Content-Type: application/json' \
  -d '{"qn":"антивирус","offset":0,"limit":10,"sort":"relevance","include_facets":0,"highlight":{"profiles":["_searchquery_"]},"countStatistics":true,"datasets":["programs"],"preffered_lang":"ru"}'

# Get sources list
curl -s 'https://searchplatform.rospatent.gov.ru/sources/tree' | jq '.[].children[] | {id, name_ru}'
curl -s 'https://searchplatform.rospatent.gov.ru/sources/tree/integral' | jq '.[] | {id, name_ru}'
```

## Common Search Patterns

| What you're looking for | `datasets` | `qn` example |
|---|---|---|
| Russian patents (1994+) | `["ru_since_1994"]` | `"способ лечения"` |
| USSR/early RF patents | `["ru_till_1994"]` | `"композитный материал"` |
| Industrial designs (RF) | `["dsgn_ru"]` | `"дизайн упаковки"` |
| Computer programs | `["programs"]` | `"бухгалтерская программа"` |
| IC topologies | `["topologies"]` | `"процессор"` |
| International patents | `["us","ep","cn"]` | `"machine learning training"` |
| Broad search across all | All datasets | `"фигурное катание"` |

## Limitations

- No authentication → anonymous access, rate limits may apply
- `available` cap at 1000 results per query — use `offset` + `limit` for pagination
- `preffered_lang` typo is in the API (not our typo)
- Some datasets may have limited biblio fields (especially older patents)
- No direct document download — only search and biblio metadata

---

# kad.arbitr.ru API (Court for Intellectual Property — СИП)

Base URL: `https://kad.arbitr.ru`

**DDoS-Guard protected** — requires browser cookies. Pass via `--cookie` flag.

## Endpoint

```
POST /Kad/SearchInstances
Content-Type: application/json
X-Requested-With: XMLHttpRequest
x-date-format: iso
```

## Request Body

```json
{
  "Page": 1,
  "Count": 25,
  "Courts": ["SIP"],
  "DateFrom": null,
  "DateTo": null,
  "Sides": [{"Name": "Сбербанк", "Type": -1, "ExactMatch": false}],
  "Judges": [],
  "CaseNumbers": [],
  "WithVKSInstances": false
}
```

| Field | Type | Values | Notes |
|---|---|---|---|
| `Page` | int | 1+ | Page number |
| `Count` | int | 1–25 | Results per page (max 25) |
| `Courts` | string[] | `"SIP"`, `"VS_RF"`, etc. | Court filter. Omit for all |
| `Sides[].Name` | string | Any | Party name search |
| `Sides[].Type` | int | -1, 0, 1 | -1=any, 0=plaintiff, 1=respondent |
| `Sides[].ExactMatch` | bool | | Exact name match |
| `Judges` | string[] | Judge surnames | Judge filter |
| `DateFrom/DateTo` | string | ISO date | `"2024-01-01"` format |

## Response

HTML table (not JSON). Parsed by `sip.py` into structured output.

**Case types** (from CSS class): `administrative`, `civil`, `civil_simple`

**Pagination**: hidden inputs `#documentsTotalCount`, `#documentsPagesCount`, `#documentsPage`

## CLI Usage

```bash
# Search by party name (auto-extract cookies via CDP)
python3 scripts/sip.py search -p "Сбербанк" --cdp

# Search by party name (manual cookies)
python3 scripts/sip.py search -p "Сбербанк" --cookie "key=val; key2=val2"

# Filter by court (default: sip)
python3 scripts/sip.py search -p "Ровио" -c sip --cdp

# Full JSON output
python3 scripts/sip.py search -p "Сбербанк" -f full --cdp

# By judge
python3 scripts/sip.py search --judge "Пашкова" --cdp

# Date range
python3 scripts/sip.py search -p "Сбербанк" --date-from 2024-01-01 --date-to 2025-12-31 --cdp
```

## Getting Cookies

### Method 1: Auto-extract via CDP (recommended)

Launch Chromium with remote debugging, navigate to kad.arbitr.ru, pass DDoS-Guard check, then use `--cdp`:

```bash
# 1. Launch Chromium with CDP
chromium --remote-debugging-port=9222 --no-first-run &
# Or attach to running browser:
# playwright-cli attach --cdp=chromium

# 2. Open kad.arbitr.ru and pass DDoS-Guard check (browser does this automatically)

# 3. Use --cdp flag — auto-extracts cookies
python3 scripts/sip.py search -p "Сбербанк" --cdp
```

### Method 2: Manual extraction from DevTools

1. Open `kad.arbitr.ru` in browser
2. Open DevTools > Network tab
3. Perform a search
4. Find the `SearchInstances` request
5. Copy the `Cookie` header value
6. Pass as `--cookie "..."`

Cookies expire with browser session (~20 min).

## Limitations

- DDoS-Guard requires browser cookies — no fully automated access
- Response is HTML, not JSON — parsed by BeautifulSoup
- Max 25 results per page
- CaseNumbers field in API body appears non-functional
- Card detail page (individual case) not scraped — only search results

---

# FIPS Register API

Base URL: `https://fips.ru`

`get` works without cookies. `search` is **experimental** — FIPS search uses Java servlet session state that is difficult to replicate programmatically. Prefer `get` for known document numbers. `--cookie` may help if blocked.

## Register Databases

| Code | Name | Description |
|---|---|---|
| `RUPAT` | Inventions | Изобретения |
| `RUPM` | Utility models | Полезные модели |
| `RUDE` | Industrial designs | Промышленные образцы |
| `RUTM` | Trademarks | Товарные знаки и знаки обслуживания |
| `EVM` | Computer programs | Программы для ЭВМ |
| `RUGP` | Geographical indications | ГУ/НМПТ |
| `RUDEAP` | Design applications | Заявки на промышленные образцы |
| `VZ` | IC topologies | Топологии интегральных микросхем |
| `PRAVO` | Legal documents | Правовые акты |

## Endpoints

### Document Viewer

```
GET /registers-doc-view/fips_servlet?DB=RUDE&rn=147&DocNumber=106651&TypeFile=html
```

| Parameter | Values | Notes |
|---|---|---|
| `DB` | See table above | Register database |
| `rn` | int | Result number (usually 147) |
| `DocNumber` | int | Registration/patent number |
| `TypeFile` | `html`, `pdf` | Document format |

Returns: HTML document page with registration details (status, dates, holders, claims).

### Register Navigation

```
GET /registers-web/action?acName=clickRegister&regName=RUTM
```

Loads the search form for the specified register.

### Search Parameters

| Parameter | Code | Description |
|---|---|---|
| Registration number | `par_15` | Номер регистрации |
| Publication date | `par_4` | Дата публикации |
| MKPO index | `par_8` | Индекс МКПО |

## CLI Usage

```bash
# List available databases
python3 scripts/fips.py dbs

# Fetch document by registration number
python3 scripts/fips.py get 106651 -d rude --cookie "..."
python3 scripts/fips.py get 106651 -d rude --cdp               # Auto-extract cookies
python3 scripts/fips.py get 2761234 -d rupat --cookie "..."    # Invention patent
python3 scripts/fips.py get 123456 -d rutm --cookie "..."       # Trademark

# Search by parameter
python3 scripts/fips.py search number 106651 -d rude --cookie "..."
python3 scripts/fips.py search number 106651 -d rude --cdp
python3 scripts/fips.py search date 16.01.2018 -d rude --cookie "..."
python3 scripts/fips.py search mkpo 11 -d rude --cookie "..."

# Full JSON output
python3 scripts/fips.py get 106651 -d rude -f full --cookie "..."
```

## Getting Cookies

1. Open `fips.ru` in browser
2. Navigate to a register (e.g., "Открытые реестры" → "Промышленные образцы")
3. Open DevTools > Network tab
4. Copy the `Cookie` header from any `fips.ru` request
5. Pass as `--cookie "..."`

## Limitations

- DDoS-Guard may require browser cookies for some operations
- `search` command is experimental — FIPS uses Java servlet session state; results may be empty
- Search by registration number/date/MKPO only — no free-text search
- No full-text search by title/owner — use `rospatent.py` for keyword search
- Document pages are HTML (windows-1251 encoded), parsed by BeautifulSoup