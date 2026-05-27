---
name: finding-docs
description: Use when user asks about a library, framework, SDK, or CLI tool. Activate for API syntax, config options, version migration, "how do I" questions mentioning a library, or debugging library-specific behavior. Prefer over web search for docs and API details.
---

# finding-docs

Fetch current library docs via `ctx7` CLI. Training data cutoff makes APIs stale — always verify against current docs.

## When to Use

- API syntax or signature questions
- Configuration options for specific library
- Version migration issues
- "How do I" with library/framework name
- Debugging library-specific behavior

When NOT to use:
- General web search → `tavily-cli` or `using-websearch`
- Finding skills/MCP setup → `skills-management`, `mcp-management`

## Quick Reference

```bash
# Step 1: resolve library ID
ctx7 library <name> <query>

# Step 2: fetch docs
ctx7 docs <libraryId> <query>

# Step 3 (optional): deep research
ctx7 docs <libraryId> <query> --research
```

## Common Mistakes

- Library IDs need `/` prefix: `/facebook/react`, `/android/camera-samples`
- Always run `ctx7 library` first to resolve ID
- Use descriptive queries, not single words
- `CameraX` → try `android/camera-samples` or `jetpack-camera-app` (not a direct match)
- Never include sensitive data in queries

## Fallback Strategy

If `ctx7 library` fails:
1. Try alternative library names (e.g. `camerax` → `android/camera-samples`, `jetpack-camera-app`)
2. If auth error → `ctx7 login`
3. If all ctx7 attempts fail → fall back to `using-websearch` or `tavily-cli`
