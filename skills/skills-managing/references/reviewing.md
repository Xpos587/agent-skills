# Reviewing Skills

Audit a skill against best practices and suggest improvements.

## Review Command

```bash
python3 <skill-dir>/scripts/review_skill.py <name>         # Review with text output
python3 <skill-dir>/scripts/review_skill.py <name> -f json # JSON output
```

## Checks Performed

| Check | What it validates |
|-------|-------------------|
| Name format | Lowercase, hyphens, max 64 chars, gerund form preferred |
| Description quality | Starts with "Use when", third person, specific triggers |
| Body length | Warns if >500 lines |
| Time-sensitive content | Flags dates, relative time references |
| Path format | No Windows backslashes |
| Reference depth | Should be one level deep |
| Table of contents | Recommended for long files |

## After Reviewing

Read the skill's SKILL.md and apply the suggested fixes directly.

## Remote Skill Assessment

When evaluating skills from the ecosystem before installation, see [remote-skill-assessment.md](remote-skill-assessment.md) for the full framework including quality signals, red flags, and verdict assignment.