# Agent Skills — Development Guide

Single-plugin marketplace + cross-agent skill collection. Same `skills/` dir read by `npx skills add` and Claude Code plugin install.

## Repository structure

```
agent-skills/
├── .claude-plugin/
│   ├── marketplace.json    ← single-plugin marketplace, source: "./"
│   └── plugin.json
├── skills/                  ← canonical Agent Skills layout
│   └── <skill-name>/SKILL.md
├── README.md
├── CLAUDE.md
└── LICENSE
```

## Adding a new skill

1. Create `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`).
2. Add optional `README.md`, `references/`, `scripts/`, `assets/`.
3. Update the relevant section in `README.md`.
4. Bump `version` in both `.claude-plugin/*.json` (minor for new skill).
5. Commit, tag, release.

## When to tag/release

Only when skill or plugin files change. README/CLAUDE.md/doc-only changes don't need a release.

## Versioning

Semver: MAJOR = breaking interface changes, MINOR = new skills, PATCH = fixes/tweaks.

## Release process

1. Bump version in `.claude-plugin/plugin.json` AND `.claude-plugin/marketplace.json`.
2. Commit.
3. `git tag -a vX.Y.Z -m "Version X.Y.Z" && git push origin vX.Y.Z`
4. `gh release create vX.Y.Z --title "vX.Y.Z" --notes "..."`
