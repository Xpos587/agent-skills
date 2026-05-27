---
name: exploring-codebase
description: "Use when exploring unfamiliar code, finding functions/classes, tracing call chains, understanding architecture, or navigating codebase structure. Triggers: where is X defined, who calls Y, how does Z work, codebase exploration, code navigation."
---

# Exploring Codebase

Navigate codebases via knowledge graph MCP tools. Start graph → fall back to Grep/Read only when graph lacks data.

## When to Use

- Exploring unfamiliar codebase
- Finding where function/class defined
- Tracing callers, callees, imports
- Understanding architecture or module structure
- Finding execution flows (request handling, data pipeline)

## When NOT to Use

- Simple text search for string literals → Grep
- Reading known file → Read directly
- No code-review-graph MCP available → standard tools

## Workflow

```
Task → get_minimal_context(task) → drill down → done
         │
         ├─ architecture? → get_architecture_overview
         ├─ find symbol?  → semantic_search_nodes
         ├─ trace calls?  → query_graph(callers_of/callees_of)
         ├─ module?       → list_communities → get_community
         ├─ flow?         → list_flows → get_flow
         └─ structure?    → children_of / find_large_functions
```

## Quick Reference

| Goal | Tool | Pattern/Args |
|------|------|-------------|
| Start any task | `get_minimal_context` | `task="<description>"` |
| Architecture | `get_architecture_overview` | — |
| Find symbol | `semantic_search_nodes` | `query="..."` |
| Who calls X | `query_graph` | `pattern="callers_of", node="X"` |
| What X calls | `query_graph` | `pattern="callees_of", node="X"` |
| Imports of X | `query_graph` | `pattern="imports_of", node="X"` |
| Test coverage | `query_graph` | `pattern="tests_for", node="X"` |
| Module details | `list_communities` → `get_community` | — |
| Execution flow | `list_flows` → `get_flow` | — |
| File contents | `children_of` | `node="path/to/file"` |
| Complex code | `find_large_functions` | — |
| Stats | `list_graph_stats` | — |

## Token Efficiency

- **ALWAYS** start with `get_minimal_context(task="...")` before other graph calls
- Use `detail_level="minimal"` — escalate to `"standard"` only when minimal insufficient
- Target: ≤5 tool calls, ≤800 output tokens per task

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Skipping `get_minimal_context` | Always call first — saves 2-3 calls |
| Using `detail_level="standard"` by default | Default to `"minimal"`, escalate only |
| Drilling without overview | Start broad (stats/architecture) then narrow |
| Searching graph for string literals | Use Grep for literal text, graph for structure |
| Ignoring `list_flows` for runtime paths | Flows show execution order graph can't |