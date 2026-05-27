# Writing-Research Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use subagent-driven-development (recommended) or executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a self-contained `writing-research` skill that unifies CLI-based web search (`tvly` + `exa`), GitHub code search (`gh search`), NotebookLM via `nlm` CLI (source-grounded analysis, podcasts), and Gemini Deep Research via `gdr` CLI (comprehensive multi-source web investigation, HTTP-based). All tools called via Bash — zero MCP dependencies for search.

**Architecture:** Single self-contained skill with SKILL.md (routing + workflows) + references. No bundled scripts — uses `gdr` CLI (Python, `uv tool install`) for Gemini Deep Research. Shares auth with `nlm` via `~/.notebooklm-mcp-cli/profiles/`. References `/nlm-skill` for NotebookLM.

**Tech Stack:** SKILL.md (routing), `gdr` CLI (Gemini Deep Research, Python/gemini-webapi), `nlm` CLI v0.5.13+ (NotebookLM), `tvly` CLI (Tavily search), `exa` CLI (Exa search), `gh` CLI (GitHub search).

---

## Environment (pre-plan check)

| Component | Status | Path/Version |
|-----------|--------|-------------|
| `nlm` CLI | Installed | v0.5.13 at `~/.local/bin/nlm` |
| `nlm-skill` | Installed | `~/.claude/skills/nlm-skill/` |
| `uv` | Available | v0.11.6 |
| `gdr-cli` | **Source at `~/Github/gdr-cli/`** | v0.1.0, not yet installed as tool |
| `tvly` CLI | **NOT installed** | `uv tool install tavily-cli` |
| `exa` CLI | **NOT installed** | From tobalsan/exa GitHub |
| Gemini Advanced | **Subscribed** | Full Gemini Deep Research access |

## File Structure (final state)

```
~/.claude/skills/writing-research/
├── SKILL.md                          # Routing, decision tree, chained workflows
└── references/
    └── research-stack.md             # Detailed tool comparison and decision framework
```

No bundled scripts — `gdr` CLI handles all Gemini Deep Research automation.

## Research Stack (final)

| Level | Tool | CLI | Latency |
|-------|------|-----|---------|
| **Quick lookup** | Tavily | `tvly search`, `tvly extract`, `tvly crawl` | Seconds |
| **Quick lookup (alt)** | Exa | `exa search`, `exa code`, `exa deep-search`, `exa crawl` | Seconds |
| **Code search** | GitHub | `gh search code`, `gh search repos`, `gh search issues` | Seconds |
| **Source-grounded** | NotebookLM | `nlm notebook query`, `nlm source add`, `nlm audio create` | Minutes |
| **Deep research** | Gemini DR | `gdr research "query"` | 5-30 min |

## Key Differences from Previous Plan

1. **No terrylica TypeScript scripts** — replaced by `gdr` CLI (Python, HTTP-based)
2. **No Playwright** — `gdr` uses `gemini-webapi` HTTP library, not browser automation
3. **No persistent Chromium CDP** — browser only needed briefly for `gdr login` (shares cookies with nlm)
4. **Simpler file structure** — just SKILL.md + references, no scripts/ directory
5. **Auth sharing** — `gdr login` writes to `~/.notebooklm-mcp-cli/profiles/default/` (same as nlm)

---

### Task 1: Install gdr-cli

**Files:**
- System tool via uv

- [ ] **Step 1: Install from GitHub**

```bash
uv tool install git+https://github.com/Xpos587/gdr-cli.git
```

- [ ] **Step 2: Verify installation**

```bash
gdr --version
gdr --help
```

Expected: Version string + list of commands (research, chat, chats, login, doctor).

- [ ] **Step 3: Run doctor**

```bash
gdr doctor
```

Expected: Shows auth/connectivity status. May show "not logged in" — that's expected.

---

### Task 2: Install tvly CLI (Tavily)

**Files:**
- System tool via uv

- [ ] **Step 1: Install tavily-cli**

```bash
uv tool install tavily-cli
```

- [ ] **Step 2: Verify installation**

```bash
tvly --version
tvly --status
```

Expected: Version string + auth status (will show "not authenticated").

- [ ] **Step 3: Authenticate**

```bash
tvly login --api-key tvly-YOUR_API_KEY
# Or get free key at https://tavily.com
tvly auth
```

Expected: "Authenticated" status.

- [ ] **Step 4: Test basic search**

```bash
tvly search "test query" --max-results 2
```

Expected: Search results returned.

---

### Task 3: Install exa CLI

**Files:**
- From tobalsan/exa GitHub repo

- [ ] **Step 1: Clone and build**

```bash
cd /tmp
git clone https://github.com/tobalsan/exa.git
cd exa
bun install
bun build ./src/index.ts --compile --outfile exa
cp exa ~/.local/bin/
```

- [ ] **Step 2: Configure API key**

```bash
exa config set api-key YOUR_EXA_API_KEY
# Or get key at https://exa.ai
exa status
```

Expected: "Connected" status.

- [ ] **Step 3: Test basic search**

```bash
exa search "test query" -n 2
```

Expected: Search results returned.

- [ ] **Step 4: Cleanup clone**

```bash
rm -rf /tmp/exa
```

---

### Task 4: Authenticate gdr (and nlm shared auth)

**Files:**
- No project files (auth setup)

- [ ] **Step 1: Login via gdr**

```bash
gdr login
```

Expected: Browser opens for Google OAuth. Cookies saved to `~/.notebooklm-mcp-cli/profiles/default/`.

- [ ] **Step 2: Verify gdr auth**

```bash
gdr doctor
```

Expected: Auth check passes.

- [ ] **Step 3: Verify nlm shared auth**

```bash
nlm login --check
nlm notebook list
```

Expected: Both work — cookies shared between gdr and nlm.

---

### Task 5: Test gdr research

**Files:**
- No project files (integration test)

- [ ] **Step 1: Run a short research query**

```bash
gdr research "what is uv python tool" -o /tmp/gdr-test.md --timeout 10
```

> **IMPORTANT:** Use Bash tool with `timeout: 600000` (10 minutes) for research commands.

Expected: Research plan shown, report generated and saved to `/tmp/gdr-test.md`.

- [ ] **Step 2: Verify output**

```bash
head -50 /tmp/gdr-test.md
wc -c /tmp/gdr-test.md
```

Expected: Markdown report with 1000+ characters.

---

### Task 6: Create skill directory structure

**Files:**
- Create: `~/.claude/skills/writing-research/`
- Create: `~/.claude/skills/writing-research/references/`

- [ ] **Step 1: Create directories**

```bash
mkdir -p ~/.claude/skills/writing-research/references
```

---

### Task 7: Write SKILL.md

**Files:**
- Create: `~/.claude/skills/writing-research/SKILL.md`

- [ ] **Step 1: Write the SKILL.md**

```markdown
---
name: writing-research
description: >
  Unified CLI-based research orchestration across five tools — tvly (Tavily search, extract, crawl),
  exa (Exa search, code search, deep-search), gh (GitHub code/repos/issues search), NotebookLM (nlm CLI
  for source-grounded analysis, podcasts, study materials), and Gemini Deep Research (gdr CLI,
  HTTP-based, 40k+ char reports). All tools via Bash — zero MCP search dependencies. Use when researching topics,
  investigating questions, finding code examples, searching GitHub, analyzing documents, or producing
  research reports. Triggers on 'research', 'look up', 'find out about', 'deep research', 'investigate',
  'search github', 'find implementation', 'podcast', and research-related requests.
version: "1.0.0"
metadata:
  author: michael
  requires:
    bins: [gh, nlm, gdr]
  notes: >
    Optional: tvly (uv tool install tavily-cli), exa (build from GitHub).
    Gemini Deep Research requires gdr CLI + Gemini Advanced subscription.
---

# Writing-Research — Unified CLI Research Orchestration

Self-contained skill that routes research queries to the optimal CLI tool based on complexity, time budget, and output requirements. All tools called via Bash — no MCP search dependencies.

## Research Stack Overview

| Tool | CLI | Latency | Output | Best For |
|------|-----|---------|--------|----------|
| **Tavily** | `tvly` | Seconds | Search results, extracted content | Web search, URL extraction, site crawling, URL mapping |
| **Exa** | `exa` | Seconds | Search results, code examples | Web search, code/SDK docs, deep-search, company/LinkedIn |
| **GitHub** | `gh` | Seconds | Code, repos, issues, discussions | Real implementations, best practices, open source dorking |
| **NotebookLM** | `nlm` | Minutes | Podcasts, reports, quizzes, study materials | Source-grounded analysis, content generation, learning |
| **Gemini Deep Research** | `gdr` | 5-30 min | 40k+ char markdown report | Comprehensive multi-source web investigation |

## Triage Decision Tree

```
What does the user need?
│
├─► Quick answer, code snippet, or URL content (seconds)
│   ├─► Real implementations / best practices → gh search code/repos
│   ├─► Code examples / library docs → exa code
│   ├─► Web search → tvly search or exa search
│   ├─► Full page content from URL → tvly extract or exa crawl
│   └─► DONE — answer is immediate
│
├─► Source-grounded analysis or content generation (minutes)
│   ├─► Load /nlm-skill
│   ├─► Create notebook → add sources → generate content
│   └─► DONE — podcasts, reports, study materials
│
├─► Comprehensive multi-source investigation (5-30 min)
│   ├─► gdr research "query" -o report.md
│   └─► DONE — 40k+ char report with citations
│
└─► Complex research needing multiple tools
    └─► See Chained Workflows below
```

## Quick Lookup Path (tvly + exa + gh)

Use for: factual questions, code patterns, library documentation, specific URLs, site mapping, GitHub dorking.

### tvly (Tavily) — Primary

```bash
# Web search with AI answer
tvly search "your query"
tvly search "your query" --depth advanced --max-results 10
tvly search "your query" --topic news --time-range week

# Extract content from URL(s)
tvly extract https://example.com
tvly extract https://a.com https://b.com --query "pricing info"

# Crawl a website
tvly crawl https://docs.example.com --max-depth 2 --limit 50

# Map all URLs on a site
tvly map https://example.com --select-paths "/blog/.*"

# JSON output for scripts
tvly search "query" --json
```

### exa (Exa) — Alternative / Complementary

```bash
# Web search
exa search "your query"
exa search "your query" -n 10 --max-chars 5000

# Code / SDK documentation search
exa code "React hooks documentation"
exa code "FastAPI authentication" --tokens 10000

# Deep search (query expansion)
exa deep-search "What are the latest developments in fusion energy?"

# Crawl URL content
exa crawl "https://example.com"

# Company research
exa company "OpenAI" -n 5

# LinkedIn search
exa linkedin "software engineer" -t profiles -n 5

# JSON output
exa search "query" --raw
```

### When to use tvly vs exa

| Scenario | Tool | Why |
|----------|------|-----|
| General web search | tvly | Better AI answers, domain filtering |
| Code/SDK docs | exa | `exa code` optimized for developer docs |
| URL content extraction | tvly | `tvly extract` handles JS-rendered pages |
| Site crawling | tvly | `tvly crawl` with depth/breadth control |
| URL mapping | tvly | `tvly map` discovers URLs without content |
| Company/LinkedIn research | exa | `exa company` / `exa linkedin` specialized |
| Deep search (API) | exa | `exa deep-search` with query expansion |
| News search | tvly | `--topic news --time-range week` |

### GitHub Code Search Path (gh)

Use for: finding real implementations, enterprise best practices in open source, code snippets, documentation patterns, dorking-style queries across GitHub.

**Prerequisites**: `gh` CLI installed and authenticated (`gh auth login`).

```bash
# Code search — find real implementations
gh search code "websocket connection handler" --language typescript --limit 20
gh search code "race condition mutex" --language go --limit 10

# Repo search — find projects with best practices
gh search repos "production kubernetes deployment" --stars ">100" --sort stars
gh search repos "microservice auth jwt" --language rust --stars ">50"

# Search within specific repos (dorking)
gh search code "architecture decision" --repo vercel/next.js --language markdown
gh search code "TODO fix race" --language go --repo golang/go

# Issue/discussion search — community knowledge
gh search issues "best practice authentication" --repo facebook/react
gh search issues "performance optimization" --language typescript

# Dorking query params (--stars only for repos, NOT code/issues)
gh search code "config.yaml" --filename "docker-compose"
gh search repos "ml pipeline" --topic machine-learning --pushed ">2025-01-01" --stars ">100"

# JSON output for scripts
gh search code "query" --json repository,path,textMatches --limit 5
gh search repos "topic" --json fullName,description,stargazersCount --limit 10
```

### When to use GitHub vs exa code vs tvly

| Scenario | Tool | Why |
|----------|------|-----|
| Library API docs | exa code | Optimized for documentation |
| Real code implementations | gh search code | Actual source code, not docs |
| Enterprise best practices | gh search repos | Find production-grade projects |
| GitHub-specific dorking | gh search | repo, language, stars, path filters |
| Community discussions | gh search issues | Solved problems, decisions |
| General web articles | tvly search | Blog posts, news, tutorials |

## Source-Grounded Research Path (NotebookLM)

Use for: analyzing specific sources, generating podcasts/reports/study materials, learning from uploaded content.

**Prerequisites**:
1. `nlm` CLI v0.5.13+ installed and authenticated (`nlm login`)
2. Chromium available for CDP authentication

**Delegate to**: `/nlm-skill` for full command reference.

**Quick commands**:
```bash
nlm login                                        # Authenticate
nlm notebook create "Research Topic"              # Create notebook
nlm source add <nb-id> --url "https://..."        # Add sources
nlm research start "query" --notebook-id <nb-id>  # Discover new sources
nlm audio create <nb-id> --confirm                # Generate podcast
nlm report create <nb-id> --confirm               # Generate report
```

## Deep Research Path (Gemini Deep Research via gdr)

Use for: comprehensive multi-source web investigation, when you need a thorough report with many citations.

**Prerequisites**:
1. `gdr` CLI installed (`uv tool install ~/Github/gdr-cli`)
2. Authenticated via `gdr login` (shares cookies with `nlm` at `~/.notebooklm-mcp-cli/profiles/default/`)
3. Gemini Advanced subscription

### Health Check

```bash
gdr doctor
```

### Run Research

**IMPORTANT**: Use Bash tool with `timeout: 600000` (10 minutes) for research commands. Default timeout will kill the process.

```bash
# Basic
gdr research "your research query"

# With output file
gdr research "your research query" -o /tmp/report.md

# With timeout and custom poll interval
gdr research "long topic" --timeout 60 --poll 15 -o report.md

# Auto-save to directory
gdr research "your research query" --output-dir ~/research-output

# Without auto-confirming plan (manual confirmation)
gdr research "your research query" --no-confirm
```

### gdr Chat (bonus)

`gdr` also supports interactive chat with Gemini — useful for follow-up questions after research.

```bash
# Interactive REPL
gdr chat

# Single message
gdr chat "Explain the difference between TCP and UDP"

# Continue last conversation
gdr chat -c
```

## Chained Workflows

### Workflow 1: Scoping Survey then Deep Dive

```
Step 1 (tvly, ~30s):    tvly search "topic overview" → understand landscape
Step 2 (tvly, ~60s):    tvly extract top 3-5 URLs → gather detailed context
Step 3 (gdr, 5-30m):    gdr research "refined query from Step 2" -o report.md
Step 4 (NotebookLM):    Import report as source → generate podcast
```

### Workflow 2: Code Research then Documentation

```
Step 1 (gh, ~10s):      gh search code "pattern" --language typescript → real implementations
Step 2 (exa, ~30s):     exa code "library usage patterns" → code examples
Step 3 (tvly, ~60s):    tvly search "library best practices 2026" → current guidance
Step 4 (NotebookLM):    Add URLs as sources → generate study guide
```

### Workflow 3: Exhaustive Investigation

```
Step 1 (tvly+exa, ~2min): Multiple searches to map the space
Step 2 (tvly, ~2min):     tvly extract on 5-10 URLs for deep context
Step 3 (gdr, 15-30m):     gdr research "comprehensive query" -o report.md
Step 4 (NotebookLM):      Import report + sources → report + podcast
```

### Workflow 4: Site Research Pipeline

```
Step 1 (tvly, ~30s):     tvly map https://docs.example.com → discover all URLs
Step 2 (tvly, ~2min):     tvly crawl docs --output-dir ./docs → mirror site
Step 3 (NotebookLM):      Add key docs as sources → generate briefing doc
```

## Auth Sharing (gdr + nlm)

`gdr` and `nlm` share Google authentication via cookies:

```
~/.notebooklm-mcp-cli/
├── profiles/
│   └── default/
│       ├── cookies.json       # Shared Google cookies
│       └── metadata.json
└── gdr-config.json            # gdr-specific config
```

Login once with either tool — both can use the same session:

```bash
gdr login    # or nlm login — either one works
```

## When NOT to Use This Skill

- **Simple git operations** (commit, push, branch) → use `git` directly
- **PR/issue management** → use `/github` skill
- **Complex NotebookLM workflows** (pipelines, batch, cross-notebook) → use `/nlm-skill` directly
- **Exa MCP tool calls** → do NOT use `mcp__exa__*` tools. Use `tvly` or `exa` CLI via Bash instead.
- **Quick single-command lookups** where the user specifies the tool explicitly

## Prerequisites Summary

| Tool | Prerequisites | Check Command |
|------|--------------|---------------|
| gdr | `uv tool install ~/Github/gdr-cli`, Gemini Advanced | `gdr doctor` |
| tvly | `uv tool install tavily-cli`, API key | `tvly --status` |
| exa | Build from GitHub, API key | `exa status` |
| GitHub | `gh` CLI installed, auth | `gh auth status` |
| NotebookLM | `nlm` installed, auth (shared with gdr) | `nlm login --check` |

## Error Recovery

| Error | Cause | Solution |
|-------|-------|----------|
| `gdr` auth error | Not logged in / cookies expired | `gdr login` |
| `gdr` timeout | Query too broad or Gemini rate limit | Use `--timeout`, refine query |
| `tvly` auth error | Missing/wrong API key | `tvly login --api-key tvly-KEY` |
| `exa` auth error | Missing/wrong API key | `exa config set api-key KEY` |
| `gh` auth error | Not logged in | `gh auth login` |
| `gh` rate limit | Too many requests | Wait, use `--cache 1h` |
| `nlm` auth expired | Session timeout (~20 min) | `nlm login` (or `gdr login`) |
| `nlm` browser not found | Wrong browser path | `nlm config set auth.browser /usr/bin/chromium` |

## See Also

- `/nlm-skill` — NotebookLM CLI and MCP expert guide
- `references/research-stack.md` — Detailed tool comparison and decision framework
- `~/Github/gdr-cli/` — gdr-cli source code and README
```

---

### Task 8: Write references/research-stack.md

**Files:**
- Create: `~/.claude/skills/writing-research/references/research-stack.md`

- [ ] **Step 1: Write the detailed comparison reference**

```markdown
# Research Stack — Detailed Comparison

## Tool Capabilities Matrix

| Capability | tvly | exa | GitHub | NotebookLM | Gemini DR (gdr) |
|-----------|------|-----|--------|------------|-----------------|
| Web search | Yes (AI answers) | Yes (clean content) | No | Yes (nlm research) | Yes (multi-source) |
| Code examples | No | Yes (primary) | Yes (primary) | No | Limited |
| URL extraction | Yes (JS-rendered) | Yes | No | Yes (add as source) | Yes |
| Site crawling | Yes (depth/breadth) | No | No | No | No |
| URL mapping | Yes | No | No | No | No |
| Company/LinkedIn | No | Yes | No | No | No |
| Real implementations | No | No | Yes (primary) | No | No |
| Best practices (OSS) | No | No | Yes (primary) | No | No |
| Source-grounded analysis | No | No | No | Yes (primary) | Partial |
| Podcast generation | No | No | No | Yes | No |
| Study materials | No | No | No | Yes (quiz, flashcards) | No |
| Report generation | No | No | No | Yes (briefing) | Yes (40k+ chars) |
| Deep search (API) | No | Yes (deep-search) | No | No | Yes (HTTP) |
| Chat/Q&A | No | No | No | Yes (notebook query) | Yes (gdr chat) |
| Output format | Text, JSON | Text, JSON | Text, JSON | Various artifacts | Markdown |
| Latency | 1-10s | 1-10s | 1-10s | 30s-5min | 5-30min |
| Cost | Free tier 1K/mo | API key | Free (rate limited) | Free | Gemini Advanced |
| Auth | API key | API key | `gh auth` | Google (shared with gdr) | Google (shared with nlm) |

## Decision Framework

### Choose tvly when:
- You need an AI-generated answer with search results
- Extracting content from JS-rendered pages
- Crawling a website with depth/breadth control
- Mapping all URLs on a site
- News/finance-specific search with time filtering
- Domain inclusion/exclusion filtering

### Choose exa when:
- Looking for code examples or SDK documentation (`exa code`)
- Company or LinkedIn research (`exa company`, `exa linkedin`)
- Deep search with query expansion (`exa deep-search`)
- You prefer Exa's search quality (same as Exa MCP)

### Choose NotebookLM when:
- You have specific sources to analyze
- Want generated content: podcasts, quizzes, flashcards, study guides
- Need source-grounded Q&A
- Building learning materials
- Combining multiple sources into cohesive analysis

### Choose Gemini Deep Research (gdr) when:
- Need comprehensive, multi-source investigation
- Topic requires broad web searching across many sources
- Need a long-form report (40k+ characters)
- Citation quality and source diversity matter
- Have 5-30 minutes to wait
- Want to follow up with chat (`gdr chat -c`)

### Choose GitHub search when:
- Looking for real code implementations (not documentation)
- Finding enterprise best practices in open source projects
- Dorking-style queries with language, stars, repo, path filters
- Finding community discussions and solved problems
- Comparing how different projects solve the same problem

## tvly vs exa vs gh Quick Reference

| Feature | tvly | exa | gh |
|---------|------|-----|-----|
| Install | `uv tool install tavily-cli` | Build from GitHub | `pacman -S gh` |
| Web search | `tvly search "q"` | `exa search "q"` | No |
| Code search | No | `exa code "q"` | `gh search code "q"` |
| Repo search | No | No | `gh search repos "q"` |
| Issue search | No | No | `gh search issues "q"` |
| URL extract | `tvly extract URL` | `exa crawl URL` | No |
| Site crawl | `tvly crawl URL` | No | No |
| URL map | `tvly map URL` | No | No |
| Company | No | `exa company "name"` | No |
| LinkedIn | No | `exa linkedin "query"` | No |
| Deep search | No | `exa deep-search "q"` | No |
| JSON output | `--json` | `--raw` | `--json fields` |
| AI answer | `--include-answer advanced` | No | No |
| Time filter | `--time-range week` | No | No |
| Domain filter | `--include-domains` | No | `--repo owner/repo` |
| Max results | `--max-results N` | `-n N` | `--limit N` |
| Max chars | No | `--max-chars N` | No |

## gdr vs nlm Quick Reference

| Feature | gdr | nlm |
|---------|-----|-----|
| Install | `uv tool install ~/Github/gdr-cli` | `uv tool install notebooklm-mcp-cli` |
| Auth | `gdr login` | `nlm login` |
| Auth storage | `~/.notebooklm-mcp-cli/profiles/` | `~/.notebooklm-mcp-cli/profiles/` |
| Deep research | `gdr research "query"` | No |
| Chat | `gdr chat` | `nlm notebook query` |
| Podcast | No | `nlm audio create` |
| Sources | No (web search) | `nlm source add` (specific URLs) |
| Report | Markdown file | Various formats |
| Health | `gdr doctor` | `nlm login --check` |

## Latency Budget Planning

| Workflow | Expected Time | Max Time |
|----------|--------------|----------|
| tvly search | 2-5s | 15s |
| tvly extract (single) | 3-10s | 30s |
| tvly crawl (site) | 15-60s | 150s |
| exa search | 2-5s | 15s |
| exa code | 3-8s | 20s |
| exa deep-search | 10-30s | 60s |
| gh search code | 2-5s | 15s |
| gh search repos | 2-5s | 15s |
| NotebookLM: research fast | ~30s | 60s |
| NotebookLM: podcast | 2-5min | 10min |
| gdr research | 5-15min | 30min |
| gdr chat (single) | 5-30s | 60s |
| Full chained workflow | 15-40min | 60min |
```

---

### Task 9: Cleanup

**Files:**
- Delete: `/tmp/terrylica-gdr/` (if still exists)
- Delete: `/tmp/exa/` (if still exists)
- Delete: `~/.claude/skills/writing-research/scripts/` (old terrylica scripts, if copied)

- [ ] **Step 1: Remove temporary files**

```bash
rm -rf /tmp/terrylica-gdr /tmp/exa
rm -rf ~/.claude/skills/writing-research/scripts/
```

---

### Task 10: Verify end-to-end

**Files:**
- No new files (verification only)

- [ ] **Step 1: Verify all files exist**

```bash
ls ~/.claude/skills/writing-research/SKILL.md
ls ~/.claude/skills/writing-research/references/research-stack.md
```

- [ ] **Step 2: Verify all CLI tools work**

```bash
gdr doctor
tvly --status
exa status
nlm login --check
gh auth status
```

Expected: All pass (or fail with expected auth/login errors, NOT "command not found").

- [ ] **Step 3: Restart Claude Code and test routing**

After restarting, test triggers:
1. "research the latest Python async patterns" → routes to exa code or tvly search
2. "create a podcast from these URLs" → routes to NotebookLM
3. "do a deep research investigation into quantum computing" → routes to `gdr research`
4. "research AI agents thoroughly and make me a podcast" → triggers chained workflow

---

## Task Dependency Graph

```
Task 1 (Install gdr-cli)       ─┐
Task 2 (Install tvly)          ─┤── Parallel
Task 3 (Install exa)           ─┘
        │
        ▼
Task 4 (Authenticate gdr+nlm)  ── Depends on Task 1
Task 5 (Test gdr research)     ── Depends on Task 4
        │
        ▼
Task 6 (Create directories)    ── Independent
        │
        ▼
Task 7 (Write SKILL.md)        ── Independent
Task 8 (Write research-stack)  ── Independent
        │
        ▼
Task 9 (Cleanup)               ── After file operations
        │
        ▼
Task 10 (Verify E2E)           ── Depends on all above
```

## Risks and Mitigations

1. **gdr-cli maturity**: v0.1.0, local source. May need patches. Source at `~/Github/gdr-cli/`.
2. **Gemini API changes**: `gemini-webapi` library may break if Google changes internal API. Check for updates.
3. **Auth cookie expiry**: Both gdr and nlm share cookies. Re-login with either tool fixes both.
4. **tvly/exa API keys**: User needs to register at tavily.com and exa.ai for free API keys.
5. **exa CLI maturity**: Only 1 star, very new. May need patches. tvly is more mature as primary.
6. **Gemini rate limits**: Max 3 concurrent deep research tasks.
