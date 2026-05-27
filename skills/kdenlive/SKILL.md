---
name: editing-video-kdenlive
description: "Use when editing video via CLI, generating Kdenlive/MLT XML projects programmatically, automating video editing tasks, or scripting clip assembly, filtering, and export. Triggers on: video editing, clip assembly, kdenlive, MLT XML, video automation, timeline editing, video filtering, melt rendering"
---

# Kdenlive CLI

CLI for programmatic video editing. Generates JSON project files → MLT XML for Kdenlive/melt.

## Setup Gates

| Gate | Check | If Fail |
|------|-------|---------|
| Binary | `which cli-anything-kdenlive` returns path | Install: `uv tool install` from repo |
| Version | Auto-save present: `grep auto_save $(which cli-anything-kdenlive)` or test `bin import` persists | Reinstall from `/home/michael/Github/CLI-Anything/kdenlive/agent-harness` |
| Project | Project file exists and is valid JSON | Run `project new` first |

## When to Use

- Assembling video from clips programmatically
- Generating Kdenlive project files (.kdenlive XML)
- Automating: trim, split, filter, transition, export
- Batch video project creation

**Not for:** Interactive editing (use Kdenlive GUI), real-time playback, rendering (use `melt`)

## Core Workflow

```
project new → bin import → timeline add-track → timeline add-clip → (filter/transition) → export xml
```

Each CLI call auto-saves mutations to project file (v1.0+ with `auto_save_on_exit`). No explicit `project save` needed unless you want a named snapshot. See [reference/workflows.md](reference/workflows.md) for complete examples.

## Quick Reference

| Group | Key Commands | Details |
|-------|-------------|---------|
| **project** | `new`, `save`, `profiles`, `info`, `json` | [reference/commands.md](reference/commands.md) |
| **bin** | `import SOURCE`, `list`, `get`, `remove` | Always `-d DURATION` on import |
| **timeline** | `add-track`, `add-clip`, `trim`, `split`, `move`, `list` | TRACK_ID=int, CLIP_ID="clip0" |
| **filter** | `add`, `remove`, `set`, `list`, `available` | 13 filters: brightness→chroma_key |
| **transition** | `add`, `remove`, `set`, `list` | Between tracks |
| **guide** | `add`, `remove`, `list` | Position in seconds |
| **export** | `xml`, `presets` | h264/h265/webm/prores/lossless/gif/audio_only |
| **session** | `undo`, `redo`, `history`, `status` | Up to 50 undo levels |

Full command flags and filter/preset tables: [reference/commands.md](reference/commands.md)

## Agent Rules

1. **Always `--json`** — parseable output, no table scraping
2. **Always absolute paths** — relative paths break cross-directory
3. **Always `-d DURATION`** on `bin import` — defaults to 0.0
4. **Check exit codes** — 0 = success, non-zero = JSON error
5. **Verify version** — if `bin import` doesn't persist, reinstall from repo (see Setup Gates)

## Common Mistakes

### Old version without auto-save

**PyPI v1.0.0 lacks `auto_save_on_exit`.** Mutations lost between calls. Symptom: `bin import` returns clip but `bin list` = `[]`.

**Fix:** Reinstall from repo: `cd /home/michael/Github/CLI-Anything/kdenlive/agent-harness && uv tool install --force .`

### Missing `-d` duration

Duration defaults to `0.0`. Clip won't play. Always specify `-d SECONDS`.

### Track ID vs Clip ID vs Clip Index

Three different ID types:
- **CLIP_ID**: string (`"clip0"`) — used in `add-clip` and `bin` commands
- **TRACK_ID**: integer (`0, 1, 2`) — used in `add-clip`, `trim`, `split`, `filter add`
- **CLIP_INDEX**: integer (`0, 1`) — position within track, used in `filter add`, `trim`, `split`

`clip0` ≠ index `0`. Clip ID = bin identifier. Clip index = position in track.

### Profile at creation time

Set profile at `project new` with `-p hd1080p30`. Cannot change after clips placed.