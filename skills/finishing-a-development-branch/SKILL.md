---
name: finishing-a-development-branch
description: Use when implementation is complete, tests pass, and work needs integrating back — merge, PR, or cleanup decisions with provenance safety
---

# Finishing a Development Branch

## Overview

Verify tests → hooks pass → ALL CI green → present options → execute → cleanup own resources only.

**Core principle:** Tests pass + hooks pass + ALL CI green + only delete what YOU created.

## Step 1: Verify Tests

```bash
uv run pytest / bun test / cargo test / go test ./...
```

**Fails?** Stop. Fix first. No proceeding with failing tests.

## Step 2: Verify Hooks

**STRICT: pre-commit and pre-push hooks must pass before ANY push.**

```bash
# Run pre-commit hooks manually
pre-commit run --all-files

# Or let git hooks run during commit/push (don't --no-verify)
```

**If hooks fail:**
```
Hooks failing (<N> failures). Must fix before pushing.
Cannot proceed until hooks pass.
```

**NEVER use `--no-verify` or `--skip-hooks`.** Fix the failures. Hooks exist for a reason.

**If hooks pass:** Continue to Step 3.

## Step 3: Detect Environment

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
```

| State | Menu | Cleanup |
|-------|------|---------|
| `GIT_DIR == GIT_COMMON` | 4 options | No worktree |
| `GIT_DIR != GIT_COMMON`, named branch | 4 options | ExitWorktree |
| `GIT_DIR != GIT_COMMON`, detached HEAD | 3 options (no merge) | ExitWorktree |

## Step 4: Present Options

Use `AskUserQuestion`:

**Named branch (4 options):**

```
Implementation complete. Tests pass. What next?

1. Merge to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is
4. Discard this work
```

**Detached HEAD (3 options):**

```
Implementation complete. Detached HEAD.

1. Push as new branch and create PR
2. Keep as-is
3. Discard this work
```

## Step 5: Execute Choice

### Option 1: Merge Locally

```bash
# Exit worktree first — restores CWD to main repo
ExitWorktree(action: "keep")

# Now in main repo
git checkout <base-branch>
git pull
git merge <feature-branch>

# Verify tests on merged result
<test command>

# Push merged result, verify ALL CI green
git push
gh run list --branch=<base-branch> --limit=5
```

**STRICT: ALL CI must be green before push to main-branch. No exceptions.**

After CI green, clean up:

```bash
git worktree remove <worktree-path>    # Only if YOU created it
git branch -d <feature-branch>          # Only if YOU created it
git push origin --delete <feature-branch>  # Remove remote branch if pushed
```

### Option 2: Push and Create PR

```bash
git push -u origin <feature-branch>

gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets>

## Test Plan
- [ ] <verification steps>
EOF
)"

# Wait for ALL CI green on PR before telling user it's done
gh pr checks
```

**Don't exit worktree** — user needs it for PR iteration.

**After PR is merged (by user or maintainer):**
```bash
git push origin --delete <feature-branch>   # Clean up remote branch
git branch -d <feature-branch>               # Only if YOU created local branch
```

### Option 3: Keep As-Is

Report: "Keeping branch <name>. Worktree at <path>."

No cleanup.

### Option 4: Discard

**Warning:** This permanently deletes branch `<name>` and all commits.

Confirm with user first.

```bash
ExitWorktree(action: "remove", discard_changes: true)
git branch -D <feature-branch>              # Only if YOU created it
git push origin --delete <feature-branch>   # Remove remote if pushed
```

## Provenance Check (CRITICAL)

**IF YOU DIDN'T CREATE IT → DON'T DELETE IT**

Before ANY cleanup:

### Worktree Ownership

- Only `ExitWorktree` on worktrees from THIS session's `EnterWorktree`
- Never `git worktree remove` on unknown worktrees
- **Never `git worktree prune`** — kills other agents' worktrees
- Unsure? ASK user

**Multi-agent repo:**
```bash
git worktree list   # Check before cleanup
```
Only remove worktree matching YOUR session's branch name.

### Branch Ownership

- Only delete branches matching this session's worktree name (pattern: `worktree-<name>`)
- Applies to BOTH local and remote: `git branch -d` + `git push origin --delete`
- Never delete `main`, `master`, `develop`, release branches
- Branch name doesn't match your worktree? ASK before deleting
- **Never delete branches other agents might be using** — check `git worktree list`

### When in Doubt

Preserve everything. Let user decide.

## CI & Hooks Rules

**ALL CI MUST BE GREEN. ALL HOOKS MUST PASS. No exceptions.**

- No push with failing pre-commit or pre-push hooks
- Never `--no-verify`, `--skip-hooks`, or any hook bypass
- No merge/push with failing CI checks
- No merge/push with pending CI checks
- No "probably fine" overrides
- Flaky CI? Re-run, investigate, fix. Don't skip.

## Quick Reference

| Option | Merge | Push | Keep Worktree | Delete Local Branch | Delete Remote Branch |
|--------|-------|------|---------------|---------------------|---------------------|
| 1. Merge locally | yes | yes (after CI green) | no | yes | yes |
| 2. Create PR | no | yes | yes | after merge | after merge |
| 3. Keep as-is | no | no | yes | no | no |
| 4. Discard | no | no | no | yes (force) | yes (if pushed) |

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Push before user chose (esp. before discard) | Push only in Option 2 |
| `git checkout <base>` inside worktree | ExitWorktree first, then checkout |
| `git worktree prune` in multi-agent setup | Never prune. Only ExitWorktree your own |
| Delete other agent's branch | Only delete branches matching your worktree name |
| Skip CI check | ALL CI green. Every time. No shortcuts |
| `--no-verify` to skip hooks | Fix hook failures. Never skip |
| Cleanup worktree for Option 2 | User needs it for PR iteration |
| Leave remote branch after merge/delete | Always `git push origin --delete <branch>` |

## Integration

**Used by:** executing-plans, subagent-driven-development, verification-before-completion

**Pairs with:** EnterWorktree (creates workspace this skill cleans up), verification-before-completion (ensures honest test/CI claims)
