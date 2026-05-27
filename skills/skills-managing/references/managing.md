# Managing Local Skills

List, show, delete, move, install, and copy skills across agents.

## List Skills

```bash
python3 <skill-dir>/scripts/list_skills.py              # All skills
python3 <skill-dir>/scripts/list_skills.py -s user      # User scope only
python3 <skill-dir>/scripts/list_skills.py -s project   # Project scope only
python3 <skill-dir>/scripts/list_skills.py -f json      # JSON output
```

## Show Skill Details

```bash
python3 <skill-dir>/scripts/show_skill.py <name>           # Basic info
python3 <skill-dir>/scripts/show_skill.py <name> --files   # Include file listing
python3 <skill-dir>/scripts/show_skill.py <name> -f json   # JSON output
```

## Delete Skill

**Always confirm with user before deleting.**

```bash
python3 <skill-dir>/scripts/delete_skill.py <name>              # Claude Code only, with confirmation
python3 <skill-dir>/scripts/delete_skill.py <name> --force      # Skip confirmation prompt
python3 <skill-dir>/scripts/delete_skill.py <name> -s project   # Target specific scope
python3 <skill-dir>/scripts/delete_skill.py <name> -a cursor    # Delete from specific agent
python3 <skill-dir>/scripts/delete_skill.py <name> --all-agents --force  # Delete from all agents
```

Skills installed via `skills add` may exist in multiple agent directories. Default mode deletes from Claude Code only and warns if copies remain in other agents. Use `--all-agents` to delete from every detected agent.

For ecosystem-installed skills, prefer `skills remove <name> -g -y` first. Use `delete_skill.py --all-agents` as fallback for manual cleanup.

**Note:** `~/.claude/skills/` is a symlink to `~/.agents/skills/`. The real data lives in `~/.agents/skills/`.

## Move Skill Between Scopes

```bash
python3 <skill-dir>/scripts/move_skill.py <name> user      # Project → User (personal)
python3 <skill-dir>/scripts/move_skill.py <name> project   # User → Project (share with team)
python3 <skill-dir>/scripts/move_skill.py <name> user -f   # Overwrite if exists
```

## Multi-Agent Operations

### Detect Installed Agents

```bash
python3 <skill-dir>/scripts/detect_agents.py              # List detected agents
python3 <skill-dir>/scripts/detect_agents.py --all        # Show all supported agents
python3 <skill-dir>/scripts/detect_agents.py -f json      # JSON output
```

### List Skills for Any Agent

```bash
python3 <skill-dir>/scripts/list_agent_skills.py --agent cursor           # Single agent
python3 <skill-dir>/scripts/list_agent_skills.py --agent goose -s global  # Specific scope
python3 <skill-dir>/scripts/list_agent_skills.py --all                    # All detected agents
python3 <skill-dir>/scripts/list_agent_skills.py --agent amp -f json      # JSON output
```

### Install Skill to Agents

```bash
python3 <skill-dir>/scripts/install_skill.py /path/to/skill --agent cursor              # Single agent
python3 <skill-dir>/scripts/install_skill.py /path/to/skill --agent cursor --agent amp  # Multiple agents
python3 <skill-dir>/scripts/install_skill.py /path/to/skill --all                       # All detected
python3 <skill-dir>/scripts/install_skill.py /path/to/skill --agent goose -s global     # Global scope
python3 <skill-dir>/scripts/install_skill.py /path/to/skill --agent cursor --force      # Overwrite
```

### Copy Skill Between Agents

```bash
python3 <skill-dir>/scripts/copy_skill.py my-skill --from claude-code --to cursor
python3 <skill-dir>/scripts/copy_skill.py my-skill --from claude-code --to cursor --to-scope global
python3 <skill-dir>/scripts/copy_skill.py my-skill --from claude-code --from-scope project --to amp
python3 <skill-dir>/scripts/copy_skill.py my-skill --from claude-code --to cursor --force
```

### Move Skill Between Agents

```bash
python3 <skill-dir>/scripts/move_skill_agent.py my-skill --from claude-code --to cursor
python3 <skill-dir>/scripts/move_skill_agent.py my-skill --from claude-code --to goose --force
```

For the full list of supported agent IDs and their skill directories, see [agents-registry](agents-registry.md) or run `python3 <skill-dir>/scripts/detect_agents.py --all`.