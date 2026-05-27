# Discovering & Installing Skills

Search, install, remove, and update skills from the open agent skills ecosystem.

## Table of Contents

- [Find Skills](#find-skills)
  - [SkillsMP API](#skillsmp-api-preferred)
  - [Skills CLI](#skills-cli-fallback)
  - [When to Search](#when-to-search)
  - [Common Search Categories](#common-search-categories)
- [Install](#install-from-ecosystem)
- [List](#list-ecosystem-skills)
- [Remove](#remove-ecosystem-skills)
- [Check & Update](#check--update)
- [Review & Compare](#review--compare-results)
- [No Results](#no-results)

## Find Skills

### SkillsMP API (preferred)

REST API over 1.2M skills. Supports keyword + semantic search, category/occupation filters.

**Keyword search:**
```bash
curl -s "https://skillsmp.com/api/v1/skills/search?q=react+performance&limit=10&sortBy=stars" | jq .
# Results in .data.skills[]
```

**Semantic search** (uses `$SKILLSMP_API_KEY`):
```bash
curl -s -H "Authorization: Bearer $SKILLSMP_API_KEY" \
  "https://skillsmp.com/api/v1/skills/ai-search?q=how+to+handle+auth+errors+in+React+Router" | jq .
# Results in .data.data[] (different structure from keyword)
```

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `q` | string | Search query (required) |
| `page` | number | Page number (default: 1) |
| `limit` | number | Items per page (default: 20, max: 100) |
| `sortBy` | string | `stars` or `recent` (default: recent) |
| `category` | string | Category slug (e.g. `data-ai`, `devops`) |
| `occupation` | string | SOC occupation slug (e.g. `software-developers-151252`) |

**Rate limits:** 50 req/day anonymous, 500 req/day with `$SKILLSMP_API_KEY`.

**Response fields** (`keyword` search, `.data.skills[]`):

| Field | Meaning | Install use |
|-------|---------|-------------|
| `name` | Skill slug | `@name` in install command |
| `author` | Owner/organization | `owner` in `owner/repo@name` |
| `githubUrl` | GitHub tree URL | Parse `owner/repo` from path |
| `stars` | Star count | Quality signal |
| `description` | Full description | Relevance check |
| `skillUrl` | SkillsMP page | Deep-link for manual review |

**From result to install** (`keyword` search):

1. Pick skill from `.data.skills[]`
2. Parse `owner/repo` from `githubUrl` (`https://github.com/owner/repo/tree/…`)
3. Install: `skills add <owner>/<repo>@<name> -g -y`
4. Alternative: `skills add <owner>/<repo> -s "<name>" -g -y` (same result, different syntax)
5. Or use `githubUrl` directly: `skills add <githubUrl> -g -y` (CLI resolves it)

**Example:**

```bash
# Search
curl -s "https://skillsmp.com/api/v1/skills/search?q=art-direction&limit=3&sortBy=stars" | jq '.data.skills[] | {name, author, githubUrl, stars}'

# Response snippet:
# {
#   "name": "art-direction",
#   "author": "rampstackco",
#   "githubUrl": "https://github.com/rampstackco/claude-skills/tree/main/skills/art-direction",
#   "stars": 154
# }

# Install → owner=rampstackco, repo=claude-skills, name=art-direction
skills add rampstackco/claude-skills@art-direction -g -y
```

### Skills CLI (fallback)

```bash
skills find [query]              # Interactive search
skills find react performance    # Keyword search
```

### When to Search

Use search when the user:
- Asks "how do I do X" where X is a common task
- Says "find a skill for X" or "is there a skill for X"
- Wants specialized capabilities (design, testing, deployment, etc.)

### Common Search Categories

| Category | Example queries |
|----------|----------------|
| Web Dev | react, nextjs, typescript, tailwind |
| Testing | testing, jest, playwright, e2e |
| DevOps | deploy, docker, kubernetes, ci-cd |
| Docs | docs, readme, changelog, api-docs |
| Quality | review, lint, refactor, best-practices |
| Design | ui, ux, design-system, accessibility |
| Productivity | workflow, automation, git |

## Install from Ecosystem

```bash
skills add <owner/repo@skill> -g -y    # Install globally, skip prompts
skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y
```

## List Ecosystem Skills

```bash
skills list                      # List all installed ecosystem skills
skills ls                        # Alias
skills list -g                   # Global skills only
skills list -a cursor            # Skills for a specific agent
```

## Remove Ecosystem Skills

Uninstalls skills installed via `skills add`. For locally-created skills, use `python3 <skill-dir>/scripts/delete_skill.py` instead.

**Always confirm with the user before removing.**

```bash
skills remove <name> -g -y       # Remove a global skill, skip prompt
skills rm <name>                 # Alias, with confirmation prompt
skills remove <name> -a cursor   # Remove from specific agent
skills remove --all -g -y        # Remove all global ecosystem skills
```

## Check & Update

```bash
skills check                     # Check for available updates
skills update                    # Update all installed skills
```

When the user asks to "update skills", "are my skills up to date?", or "check for updates":

1. Run `skills check` first to show what has updates available
2. If updates exist, confirm with user before running `skills update`
3. After updating, remind user to restart the agent for changes to take effect

## Review & Compare Results

**Always offer to review found skills before installing.** When there are 2+ results, proactively offer to fetch and assess the top candidates.

**Always offer review when:**
- Any search returns results
- 3+ results returned
- Multiple results with similar names or overlapping descriptions
- User asks to compare, review, evaluate, or pick the best
- A result has suspicious metrics (niche topic with very high installs)

**Process:**
1. Present the search results summary first
2. Ask the user if they want you to review/compare the top candidates
3. If yes: fetch skills.sh pages for top 3-6 candidates
4. Evaluate quality signals: install count, agent distribution, age, description, relevance, overlap with installed skills
5. Assign verdict: Recommended / Consider / Skip
6. Present ranked summary with 1-2 sentence assessments

See [remote-skill-assessment.md](remote-skill-assessment.md) for the full assessment framework including red flags and scoring signals.

## No Results

If no skills found: offer to help directly, then suggest `skills init <name>` to create a custom skill.