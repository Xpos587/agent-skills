---
name: skills-managing
description: Use when user asks to find, install, remove, update, review, list, or move skills for AI coding agents, or says "is there a skill for X", "search for skills", "install skill", "check for updates", or "how do I do X" where X may have an existing skill
---

Manage skills across AI coding agents. List, search, install, review, delete, move, and copy skills.

## Scopes

| Scope | Path | Visibility |
|-------|------|------------|
| User | `~/.agents/skills/` | All projects, all agents |
| Project | `.agents/skills/` | This repository only |

`~/.claude/skills/` → symlink to `~/.agents/skills/` (Claude Code compatibility).
User scope takes precedence over project scope for same-name skills.

## Quick Reference

| Task | Command | Details |
|------|---------|---------|
| List | `python3 <skill-dir>/scripts/list_skills.py` | [managing](references/managing.md) |
| Show | `python3 <skill-dir>/scripts/show_skill.py <name>` | [managing](references/managing.md) |
| Review | `python3 <skill-dir>/scripts/review_skill.py <name>` | [reviewing](references/reviewing.md) |
| Delete | `python3 <skill-dir>/scripts/delete_skill.py <name>` | [managing](references/managing.md) |
| Move scope | `python3 <skill-dir>/scripts/move_skill.py <name> user\|project` | [managing](references/managing.md) |
| Find | `curl skillsmp.com/api/v1/skills/search?q=…` or `skills find` | [discovering](references/discovering.md) |
| Install | `skills add <owner/repo@skill> -g -y` | [discovering](references/discovering.md) |
| Remove | `skills remove <name> -g -y` | [discovering](references/discovering.md) |
| Update | `skills check` then `skills update` | [discovering](references/discovering.md) |
| Detect agents | `python3 <skill-dir>/scripts/detect_agents.py` | [agents-registry](references/agents-registry.md) |
| Copy to agent | `python3 <skill-dir>/scripts/copy_skill.py <name> --from X --to Y` | [managing](references/managing.md) |
| Move to agent | `python3 <skill-dir>/scripts/move_skill_agent.py <name> --from X --to Y` | [managing](references/managing.md) |
| Install to agent | `python3 <skill-dir>/scripts/install_skill.py /path --agent X` | [managing](references/managing.md) |

## When NOT to Use

- Creating a skill from scratch → `/writing-skills`
- Editing skill content → edit SKILL.md directly
- Configuring agent hooks/settings → `/settings-management`

## Important Notes

- **Restart required** after add/remove/move. Edits to existing content work without restart.
- **Always update all agents** when changing local skills: `python3 <skill-dir>/scripts/install_skill.py /path --all -s global --force`
- **Always confirm** before deleting or removing skills.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Editing `~/.claude/skills/` only | That's a symlink → `~/.agents/skills/`. Use `install_skill.py --all` for multi-agent |
| Deleting via script but skill was `skills add`-installed | `skills remove` first, then `delete_skill.py` for cleanup |
| Not restarting after install/remove | Restart the agent |
| Installing without checking overlap | Run `list_skills.py` first |