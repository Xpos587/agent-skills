---
name: ov-this
description: Use when session produced tool calls, file changes, decisions, bugs fixed, or non-obvious knowledge worth preserving across sessions
version: "2.1"
author: almaz
tags: [ov-this, autosave, openviking, session-management]
---

# ov-this

Auto-save session knowledge to OpenViking. Iron Rule: never ask "should I save?" — always think "where in OV does this belong?"

## When to Use

ANY one triggers pipeline:
- tool_calls >= 5
- commands >= 3 unique
- files_modified >= 1
- decisions >= 1 (architectural or procedural)
- bugs_fixed >= 1
- knowledge_discovered: non-obvious workaround, API quirk, tool behavior
- cross_session_relevance: knowledge useful for future sessions

## When NOT to Use

- Pure Q&A with no code or decisions
- Transient debugging (tried X, didn't work, moved on — no insight gained)
- Knowledge already stored in OV

## Pipeline

1. **Scope**: `pwd` → derive agent-id (always lowercase, = last path component)
2. **Health**: `ov status` → wait if busy
3. **Structure**: `ov tree <scope_uri> -L 3`
4. **Consult**: `ov chat -m` → ask where to place knowledge
5. **Plan**: Build file list with per-file `--reason` and `--agent-id`
6. **Review**: Spawn ONE reviewer — first available in order: Claude → Qoder → Kimi
7. **Execute**: OV command with `--agent-id`, `--reason`, `--wait`, correct `--mode`
8. **Verify**: `ov tree <target_dir>`

## Mandatory Flags

| Flag | Purpose |
|------|---------|
| `--wait` | Wait for async processing |
| `--agent-id <ID>` | Logged in frontmatter |
| `--reason "<text>"` | WHY this knowledge deserves durable storage |
| `--mode create` | New files |
| `--mode replace` | Updates |

Before saving, answer: "Why does this knowledge deserve durable storage?" → use as `--reason`.

## OV Command Reference

| Command | Use For | `--reason` | `--agent-id` | `--wait` |
|---------|---------|-----------|-------------|----------|
| `ov add-resource` | Import files/dirs | CLI flag | Yes | Yes |
| `ov write` | Write text to file | Embed in content | Yes | Yes |
| `ov mkdir` | Create directory | `--description` | Yes | No |
| `ov mv` | Move/rename | Content body | Yes | No |
| `ov rm` | Remove resource | Content body | Yes | No |
| `ov add-skill` | Import skill | Content body | Yes | Yes |
| `ov add-memory` | Add memory | Content body | Yes | No |

## Project Structure

All projects: `viking://resources/projects/<project_id>/` (lowercase). Required: `README.md`, `evidence/`, `patterns/`, `cases/`, `playbooks/`, `decisions/`, `.sessions.md`. Full spec → [project-organization.md](project-organization.md).

## Red Flags — STOP and Save Now

- "I'll save later" → won't happen
- "This isn't worth saving" → if you thought about it, it is
- "Session is still young" → context fills fast, save early
- Skipping `--reason` → no provenance = no trust
- Skipping `ov status` → queue may be saturated

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Save decisions to `evidence/` | Decisions → `decisions/` |
| Missing `--reason` flag | Every save needs provenance |
| Skip health check | `ov status` first — queue may block |
| Wrong `--mode` | New = `create`, update = `replace` |
| Agent-id not lowercase | Always lowercase: `mattermost` not `MatterMost` |

## Fallback

OV unreachable or queue saturated >120s:
1. Write intent to `/tmp/ov-this-pending.log` with timestamp + scope + summary
2. Retry on next session start
3. **Never silently drop durable knowledge**
