---
name: finding-datasets
description: |
  Use when the user needs datasets for machine learning, data science, research, or analysis. Also when they ask "where to find data about X", "need a dataset for Y", "sources for Z", or want public/government/financial/health/geospatial data. No trigger for synthetic data generation, private data requests, or API integration tasks.
compatibility: Requires aria2c and optionally rclone for cloud storage downloads.
allowed-tools: Bash(aria2c), Bash(rclone)
---

# Finding Datasets

Curated catalog of data sources across domains. Start with domain, then pick a source.

## Table of Contents

- [Workflow](#workflow)
- [Categories](#categories)
- [Quick Commands](#quick-commands)
- [Workspace Layout](#workspace-layout)
- [Tips](#tips)
- [When to Look Elsewhere](#when-to-look-elsewhere)

## Workflow

Four-phase workflow for dataset discovery:

| Phase           | Action                                           | Goal                 |
| --------------- | ------------------------------------------------ | -------------------- |
| **1. Scope**    | Clarify domain, modality, size, license          | Focus search         |
| **2. Search**   | Query 2-3 sources from [Categories](#categories) | Build candidate list |
| **3. Preview**  | Peek metadata + sample rows before download      | Avoid wrong data     |
| **4. Download** | Pull full data after user confirms               | Save to workspace    |

### Scope checklist

- Domain: ML, finance, health, geospatial, climate, NLP, social networks...
- Modality: image, text, tabular, audio, graph, time series
- Size: small (<10K), medium (10K-1M), large (>1M)
- License: permissive (MIT/Apache/CC-BY), any, specific

### Search commands

```bash
# Kaggle search (API v1 — no auth needed)
aria2c --summary-interval=0 -d /tmp -o kaggle_search.json \
  "https://www.kaggle.com/api/v1/datasets/list?search=climate&sortBy=hottest&page=1"

# Data.gov catalog API
aria2c --summary-interval=0 -d /tmp -o datagov.json \
  "https://data.gov/search/?q=climate"

# Hugging Face datasets API
aria2c --summary-interval=0 -d /tmp -o hf_datasets.json \
  "https://huggingface.co/api/datasets?search=medical&limit=5"

# Google Dataset Search (browse)
aria2c --summary-interval=0 -d /tmp -o gds.html \
  "https://datasetsearch.research.google.com/search?query=health"
```

### Preview commands

```bash
# HF dataset preview (first rows API)
aria2c --summary-interval=0 -d /tmp -o hf_preview.json \
  "https://datasets-server.huggingface.co/first-rows?dataset=stanfordnlp/imdb&config=plain_text&split=train"

# Data.gov dataset page (browse)
aria2c --summary-interval=0 -d /tmp -o datagov_meta.html \
  "https://data.gov/dataset/usgs-elevation"
```

### Download workflow

```bash
# Create workspace
mkdir -p ~/Datasets/finding/{domain}_{source}/

# Parallel segmented download (16 connections to same server, 4 file segments)
# -x = max-connection-per-server (default 1)
# -s = split file into N segments (default 5)
aria2c -x 16 -s 4 -d ~/Datasets/finding/health_who -o data.csv \
  "https://example.com/data.csv"

# Resume interrupted download
aria2c -c -x 16 -s 4 -d ~/Datasets/finding/health_who -o data.csv \
  "https://example.com/data.csv"

# Download multiple URLs from list file (one URL per line)
aria2c -x 16 -s 4 -i urls.txt -d ~/Datasets/finding/ml_kaggle/

# Cloud storage via rclone (70+ backends)
# List remote directory tree (2 levels deep, show sizes)
rclone tree gdrive-advanced:FSAnno -s --level 2

# Sync dataset from cloud to local (modifies dest only)
rclone sync gdrive-advanced:MyDataset ~/Datasets/finding/ml_gdrive/

# Parallel transfers (default 4, increase for many small files)
rclone copy --transfers 16 gdrive-advanced:BigDataset ~/Datasets/finding/ml_gdrive/
```

## Categories

| Domain                 | Source           | Search URL / How to query                                                                                          | Use When                   |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| ML / Data Science      | Kaggle           | `https://www.kaggle.com/datasets/search?search=<query>&sort=votes`                                                 | Datasets for training      |
| ML / Data Science      | UCI              | `https://archive.ics.uci.edu/ml/datasets.php?format=csv` (browse)                                                  | Classic ML benchmarks      |
| ML / Data Science      | Papers with Code | `https://paperswithcode.com/datasets?q=<query>`                                                                    | SOTA datasets              |
| ML / Data Science      | Hugging Face     | `https://huggingface.co/datasets?search=<query>`                                                                   | NLP, vision, audio         |
| ML / Data Science      | ModelScope       | `https://www.modelscope.cn/datasets?search=<query>`                                                                | Chinese + multilingual     |
| Government / Open Data | data.gov (US)    | `https://data.gov` (browse, search box)                                                                            | US federal data            |
| Government / Open Data | EU Open Data     | `https://data.europa.eu/data/datasets?query=<query>`                                                               | European data              |
| Government / Open Data | World Bank       | `https://api.worldbank.org/v2/indicator/NY.GDP.MKTP.CD?format=json` (API) or `https://data.worldbank.org` (browse) | Economic indicators        |
| Government / Open Data | UN Data          | `https://data.un.org/Data.aspx` (browse by topic)                                                                  | Global statistics          |
| Finance / Economics    | Yahoo Finance    | `https://finance.yahoo.com/quote/<ticker>/history`                                                                 | Stock historical prices    |
| Finance / Economics    | FRED             | `https://fred.stlouisfed.org/searchresults/?st=<query>`                                                            | Economic time series       |
| Finance / Economics    | NASDAQ           | `https://data.nasdaq.com/search?query=<query>`                                                                     | Market data                |
| Finance / Economics    | Quandl           | `https://www.quandl.com/search?query=<query>` (requires signup)                                                    | Financial datasets         |
| Finance / Economics    | OECD             | `https://stats.oecd.org/` (browse by topic)                                                                        | Cross-country stats        |
| Health / Medical       | WHO              | `https://www.who.int/data/gho` (Global Health Observatory, browse themes)                                          | Global health data         |
| Health / Medical       | CDC              | `https://www.cdc.gov/rdc/` (restricted access)                                                                     | US health statistics       |
| Health / Medical       | HealthData.gov   | `https://healthdata.gov/browse` (browse)                                                                           | US health datasets         |
| Health / Medical       | MIMIC            | `https://physionet.org/content/mimiciv/` (requires credentialed access)                                            | Clinical ICU data          |
| Geospatial             | OpenStreetMap    | `https://overpass-api.de/api/interpreter` (Overpass API)                                                           | Maps, POI, routes          |
| Geospatial             | NASA EarthData   | `https://cmr.earthdata.nasa.gov/search/concepts` (CMR API)                                                         | Satellite imagery          |
| Geospatial             | USGS             | `https://earthexplorer.usgs.gov/` (browse)                                                                         | Terrain, elevation         |
| Geospatial             | Natural Earth    | `https://www.naturalearthdata.com/downloads/` (direct download)                                                    | Cultural, physical vectors |
| Climate / Weather      | NOAA             | `https://www.ncei.noaa.gov/access/search/dataset-search`                                                           | Weather stations, climate  |
| Climate / Weather      | WorldClim        | `https://www.worldclim.org/data.html` (direct download)                                                            | Historical climate rasters |
| Climate / Weather      | Wunderground     | `https://www.wunderground.com/history` (browse by station)                                                         | Local weather history      |
| NLP / Text             | Common Crawl     | `https://index.commoncrawl.org/` (index by year)                                                                   | Web-scale text corpora     |
| NLP / Text             | DBpedia          | `https://www.dbpedia.org/resources/ontology/`                                                                      | Structured Wikipedia       |
| NLP / Text             | WordNet          | `https://wordnet.princeton.edu/download/` (direct download)                                                        | Lexical database           |
| NLP / Text             | Wiki Dumps       | `https://dumps.wikimedia.org/` (download XML dumps)                                                                | Raw Wikipedia              |
| Social Networks        | Stanford SNAP    | `https://snap.stanford.edu/data/index.html` (browse collections)                                                   | Academic graph datasets    |
| Social Networks        | Internet Archive | `https://archive.org/details/datasets` (browse)                                                                    | Historical web datasets    |
| Social Networks        | Twitter/X        | Academic API required — apply at `https://developer.twitter.com/`                                                  | Social media data          |
| Images / CV            | ImageNet         | `https://www.image-net.org/download.php` (requires login)                                                          | Object classification      |
| Images / CV            | COCO             | `https://cocodataset.org/#download`                                                                                | Object detection           |
| Images / CV            | Open Images      | `https://storage.googleapis.com/openimages/web/index.html` (browse)                                                | Multi-label images         |
| Images / CV            | LFW              | `http://vis-www.cs.umass.edu/lfw/` (direct download)                                                               | Face recognition           |
| Time Series            | UCR              | `https://www.cs.ucr.edu/~eamonn/time_series_data_2018/`                                                            | Classification benchmarks  |
| Time Series            | Yahoo Finance    | `https://finance.yahoo.com/quote/<ticker>/history`                                                                 | Stock/crypto prices        |
| Time Series            | FRED             | `https://fred.stlouisfed.org/searchresults/?st=<query>`                                                            | Macroeconomic indicators   |
| Energy                 | Pecan Street     | `https://dataport.pecanstreet.org/` (login required)                                                               | Residential smart meter    |
| Energy                 | AMPds            | `https://ampds.org/` (direct download)                                                                             | Appliance-level power      |
| Energy                 | REDD             | `https://redd.csail.mit.edu/` (download MATLAB files)                                                              | Low-power device traces    |
| Transport / Logistics  | OpenFlights      | `https://openflights.org/data` (direct download)                                                                   | Airports, routes, airlines |
| Transport / Logistics  | BTS              | `https://www.transtats.bts.gov/DL_SelectFields.aspx` (select form)                                                 | US flight on-time data     |
| Transport / Logistics  | NYC Taxi         | `https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page` (parquet)                                           | Ride-hailing records       |
| Customs / Trade        | UN Comtrade      | `https://comtrade.un.org/data/doc/API/` (bulk API)                                                                 | Import/export by country   |
| Customs / Trade        | National customs | `https://customs.gov.ru/` (Russia), `https://www.customs.go.jp/` (Japan), etc.                                     | National trade statistics  |
| GitHub Repositories    | GitHub Search    | `https://github.com/search?q=<query>+topic:dataset&type=repositories`                                              | Code + data bundles        |
| GitHub Repositories    | Awesome Lists    | `https://github.com/search?q=awesome+public+datasets`                                                              | Curated lists              |

## Quick Commands

### Government portals by country

| Country   | URL              |
| --------- | ---------------- |
| USA       | `data.gov`       |
| UK        | `data.gov.uk`    |
| EU        | `data.europa.eu` |
| Canada    | `open.canada.ca` |
| Australia | `data.gov.au`    |
| Brazil    | `dados.gov.br`   |
| India     | `data.gov.in`    |
| Russia    | `data.gov.ru`    |

### APIs with data

| Source         | Endpoint                                     | Key Required |
| -------------- | -------------------------------------------- | ------------ |
| World Bank     | `api.worldbank.org/v2/country/all/indicator` | No           |
| FRED           | `api.stlouisfed.org/fred/series`             | Yes          |
| NASA EarthData | `cmr.earthdata.nasa.gov/search/granules`     | Yes          |
| OpenStreetMap  | `overpass-api.de/api/interpreter`            | No           |
| WHO            | `ghoapi.azureedge.net/api`                   | No           |

## Workspace Layout

```
~/Datasets/finding/                         # default workspace
  search-{YYYY-MM-DD}.json                   # search results log
  {domain}_{source}/
    metadata.json                              # API metadata
    README.md                                  # human-readable summary
    sample.jsonl                               # sample rows
    data/                                      # full downloaded data
```

## Tips

- **Always preview before download** — fetch metadata and sample rows first.
- **Parallel downloads** — aria2c `-x 16 -s 4` opens 16 connections to the same server and splits the file into 4 segments downloaded concurrently.
- **Resume interrupted downloads** — aria2c `-c` continues from partial file.
- **Cloud storage** — rclone supports 70+ backends: Google Drive, S3, Dropbox, Azure, SFTP.
- **Parallel transfers** — rclone `--transfers 16` speeds up many small files (default 4).
- **Kaggle** — search via API v1 (no auth). Download via `kaggle datasets download` CLI (needs `kaggle.json` auth).
- **UCI Repository** — direct download, no auth.
- **Government portals** — look for CSV/JSON/API formats, avoid PDFs for analysis.
- **Academic datasets** — check license (CC0, ODbL, custom).
- **Large datasets** — prefer segmented download with aria2c; rclone sync for cloud sources.
- **Geospatial** — prefer GeoJSON/Shapefile; GeoTIFF for raster.
- **Time series** — ensure consistent frequency and timezone before merging.
- **Deduplicate** — when searching multiple sources, same dataset may appear under different names.

## When to Look Elsewhere

- Need real-time streaming data → look for WebSocket/SSE APIs, not static datasets.
- Need proprietary/enterprise data → commercial providers (Bloomberg, Reuters, Statista).
- Need synthetic data → use `faker`, `synth`, or generative models.
