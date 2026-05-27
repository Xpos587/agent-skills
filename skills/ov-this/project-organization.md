# Project Organization (North Pole Golden Standard)

All projects: `viking://resources/projects/<project_id>/` (project_id always lowercase).

New projects MUST use `resources/projects/`. Legacy `viking://agent/` paths still valid.

## Required Structure

| Path | Role | Pattern | Required |
|------|------|---------|----------|
| `README.md` | Project card | Single file | Yes |
| `evidence/` | Raw data, research, logs | Free-form + date prefixes | Yes |
| `patterns/` | Reusable operational rules | `PT-NNN-*.md` | Yes |
| `cases/` | Test cases, validation | `TC-NNN-*.md` | Yes |
| `playbooks/` | Runbooks, procedures | `PB-NNN-*.md` | Yes |
| `decisions/` | Architecture decisions | `ADR-NNN-*.md` | Yes |
| `.sessions.md` | Session pointer table | Table format | Yes |

Golden standard reference: `viking://resources/projects/mattermost/` — use as template.

## Folder Semantics

| Folder | Question it answers | Store | Don't store |
|--------|-------------------|-------|-------------|
| evidence/ | What did we find? | Facts, logs, research, configs | Decisions |
| patterns/ | How should we always do X? | Reusable rules across sessions | One-off notes |
| cases/ | Did we prove X works? | Tests, validation, reproductions | Untested claims |
| playbooks/ | What to do when X happens? | Step-by-step procedures | General advice |
| decisions/ | Why did we choose X? | ADRs with alternatives considered | Undocumented changes |
| .sessions.md | What happened when? | Date/topic → session UUID pointers | Transcripts |

## Agent-ID Rules

- **ALWAYS lowercase**: `mattermost` not `MatterMost`
- **Projects**: agent-id = last path component, lowercased
- **Non-project scopes**:

| Data Type | Scope URI | Agent-ID |
|-----------|-----------|----------|
| Personal | `viking://user/<username>/` | default (none) |
| Project | `viking://resources/projects/<project>/` | `<project>` |
| Shared resources | `viking://resources/<project>/` | `<project>` |

## Cross-CLI Deployment

| CLI | Shim Location | Method |
|-----|--------------|--------|
| Hermes | Native | `provider: openviking` — zero shim |
| Claude Code | `~/.claude/commands/ov-this.md` | 6-line shim |
| Codex | `~/.codex/skills/ov-this/SKILL.md` | 6-line shim |
| Kimi CLI | `~/.kimi/skills/ov-this.md` | 6-line shim |
| QoderCLI | `~/.qoder/skills/ov-this/SKILL.md` | 6-line shim |

All non-Hermes shims read SSOT directly from OV via `ov read`.
