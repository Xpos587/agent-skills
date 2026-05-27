# Tech Topic Mind Map Template

> ⚠️ **This template generates bitmap (PNG)**, not XMind / MindNode / mermaid mindmap editable mind maps.
> For editable diagrams use XMind / MindNode / Excalidraw / mermaid mindmap.

This file is used for generating "engineering-style tech topic mind maps":

- Tech stack overviews (frontend / backend / data / DevOps panorama)
- Interview knowledge mind maps (standard questions / system design / algorithms)
- Research mind maps (summaries after researching a field)
- Learning roadmaps
- Topic dictionaries / concept relationship diagrams

Characteristics:

- Central node = topic (rounded rectangle / ellipse, with accent color)
- Primary branches = main categories (4-8, radially distributed)
- Secondary / tertiary branches = sub-topics (indented or nested)
- Different branches use different colors (role coding)
- Dark grid + monospace font (following visual system)

## Scope

- Tech stack panorama diagrams
- Interview preparation mind maps
- Research / learning summary mind maps
- Knowledge system organization
- Concept relationship networks

## When to use

- User mentions "mind map / knowledge system / learning roadmap / tech stack overview"
- User wants standard "center + radial" mind map structure
- User accepts bitmap output

Do NOT use for:

- User wants "engineering system architecture" → use `technical-diagrams/system-architecture.md`
- User wants "ER data model" → use `technical-diagrams/er-diagram.md`
- User wants "hierarchical flowchart / step-by-step" → use `infographics/step-by-step-infographic.md`
- User wants "outline / list-style slide" → use `slides-and-visual-docs/`

## Missing Information Priority Question Order

1. Topic (center node content, "Frontend Engineer Tech Stack 2026 / System Design Interview Essentials")
2. Number of primary branches (recommend 4-8)
3. Sub-nodes under each primary branch (3-7 secondary per primary)
4. Whether tertiary / quaternary nesting is needed
5. Aspect ratio (default 16:9 landscape; can use 3:4 portrait when branches are numerous)
6. Whether to highlight certain "key / must-know" nodes

## Main Template: Standard Radial Tech Mind Map

📖 Description

The entire image has a topic node at the center, with 4-8 primary branches radiating outward, each primary branch expanding into 3-7 sub-nodes, with tertiary nodes expanded as needed. Each primary branch uses one color family throughout all its sub-nodes.

📝 Prompt

```json
{
  "type": "Engineering-style tech mind map (radial mind map)",
  "goal": "Generate a radial mind map as a visualization for knowledge organization / interview preparation / learning roadmap / tech stack panorama",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"Frontend Engineer Tech Stack\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"2026 edition\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "central_node": {
    "label": "{argument name=\"central_label\" default=\"Frontend\\nEngineer\"}",
    "shape": "rounded rectangle (corner radius 16px) or ellipse",
    "size": "260×120px",
    "fill": "amber #FBBF24 × 18% opacity",
    "border": "2px solid amber #FBBF24",
    "label_style": "mono bold 16pt, centered, light text",
    "position": "image center"
  },
  "primary_branches": {
    "count": "{argument name=\"primary_count\" default=\"6\"}",
    "items": [
      { "id": "B1", "label": "Languages", "color": "cyan #22D3EE", "angle_position": "top-left" },
      { "id": "B2", "label": "Frameworks", "color": "blue #60A5FA", "angle_position": "top-right" },
      { "id": "B3", "label": "State & Data", "color": "emerald #34D399", "angle_position": "right" },
      { "id": "B4", "label": "Build & Tooling", "color": "violet #A78BFA", "angle_position": "bottom-right" },
      { "id": "B5", "label": "Testing", "color": "rose #FB7185", "angle_position": "bottom-left" },
      { "id": "B6", "label": "Performance", "color": "orange #FB923C", "angle_position": "left" }
    ],
    "branch_node_style": {
      "shape": "rounded rectangle (corner radius 10px)",
      "size": "180×56px",
      "fill": "branch color × 14% opacity",
      "border": "1.5px solid branch color",
      "label": "mono bold 13pt, centered, light text",
      "position": "evenly distributed around central node, ~ radius 380-440px"
    },
    "connector_style": "thick branch-colored line 2px from central node to primary node, slight curve"
  },
  "secondary_nodes": {
    "rule": "Each primary has 3-7 secondary nodes, branching out tree-like along the primary branch direction",
    "items_per_primary_example": {
      "B1_Languages": ["TypeScript", "JavaScript (ES2024+)", "WebAssembly", "CSS / Sass"],
      "B2_Frameworks": ["React 19", "Next.js 15", "Vue 3", "Svelte 5", "Solid"],
      "B3_State_Data": ["TanStack Query", "Zustand", "Jotai", "URQL / Apollo", "tRPC"],
      "B4_Build_Tooling": ["Vite", "Turbopack", "Bun", "pnpm + Turborepo", "Biome"],
      "B5_Testing": ["Vitest", "Playwright", "Storybook", "MSW"],
      "B6_Performance": ["Core Web Vitals", "RUM", "Bundle analysis", "Image / Font opt"]
    },
    "secondary_node_style": {
      "shape": "rounded rectangle (corner radius 8px)",
      "size": "auto-fit text + 12px padding, ~ 140×40px typical",
      "fill": "branch color × 8% opacity",
      "border": "1.2px solid branch color (slightly desaturated)",
      "label": "mono regular 11pt"
    },
    "connector_style": "thin branch-colored line 1.2px from primary to secondary, curved"
  },
  "tertiary_nodes": {
    "enabled": "{argument name=\"tertiary_enabled\" default=\"false\"}",
    "rule": "if true, secondary nodes can further expand into 2-3 tertiary nodes (smaller rounded rectangles + thinner lines), but avoid visual explosion; recommend expanding only under 1-2 secondary nodes"
  },
  "highlights": {
    "must_know": {
      "enabled": "{argument name=\"must_know_enabled\" default=\"false\"}",
      "rule": "if true, add '★' prefix to key / must-know nodes + thicken border to 2.5px",
      "examples": ["★ React 19", "★ TypeScript", "★ Vite"]
    }
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "branch color → category mapping, star → must-know",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "Central node is unique and centered",
      "Primary branches evenly distributed around the center (avoid clustering on one side)",
      "Each branch color family persists through all its child nodes",
      "Secondary nodes strictly hang in the extension direction of their parent primary",
      "Dark grid background + monospace font",
      "Node sizes follow hierarchy (central > primary > secondary > tertiary)",
      "Connection lines do not cross (unless unavoidable)"
    ],
    "avoid": [
      "All nodes same size → loses hierarchy",
      "Primaries clustered on one side → visual imbalance",
      "Secondary colors inconsistent with their parent primary",
      "Massive line crossings → readability collapse",
      "Using emoji as node icons (unless theme requires it)",
      "More than 8 primaries (crowded; consider splitting into sub-maps)",
      "All tertiary and below expanded → visual explosion",
      "Using 3D / gradients / glass textures",
      "Claiming this is an editable SVG"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, `central_label`, primary branch list (with names), secondary list under each primary
- **Can default**: `background` (dark grid), `primary_branches.color` (default 6-color combo), `tertiary_enabled` (false), `must_know_enabled` (false)
- **Can randomize**: each primary's angle_position (auto-distributed evenly based on count), slight node position adjustments to avoid overlap

### Auto-Fill Strategy

- User provides "topic + 4-6 branches" → auto-use default secondary count (4 per branch)
- User provides "I want a frontend tech stack mind map" → use default 6 branches (Languages / Frameworks / State&Data / Build / Testing / Performance)
- User doesn't specify colors → auto-assign 6-color combo by role order
- User says "add key markers" → enable `must_know_enabled`
- User wants light mode → use Variant 1

## Variant 1: Light Mind Map

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "node_fill": "branch color × 6% opacity",
    "node_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "connector_color": "branch color (deeper shade)",
    "vibe": "white-background documentation / print-friendly"
  }
}
```

## Variant 2: Hierarchical Tree Diagram (Left-to-Right)

```json
{
  "modify": {
    "layout": "Replace radial with 'left-to-right tree': central node at far left, primaries vertically arranged in the second column, secondaries in the third column, and so on",
    "use_case": "Better suited for 'learning roadmap / knowledge hierarchy' (rather than 'panorama overview')",
    "vibe": "More like XMind's logical chart view"
  }
}
```

Suitable for: learning roadmaps, knowledge hierarchies, decision-tree style knowledge.

## Variant 3: Organization / Team Structure Mind Map

```json
{
  "modify": {
    "central_label": "team / company / org name",
    "primary_branches": "Departments / Functions (Engineering / Design / Product / Ops / Marketing)",
    "secondary_nodes": "Specific roles / team members (using 'Name · Title' format)",
    "highlights_extra": "Team leads marked with ★ + bold border",
    "use_case": "Team introduction decks, organizational charts"
  }
}
```

Suitable for: team / organizational structure displays, new member onboarding documents.

## Things to Avoid

- Primary branches concentrated on one side of the canvas → visual imbalance
- All nodes the same size → loses hierarchy
- Massive line crossings → unreadable
- Secondary node colors inconsistent with their primary → visual chaos
- Tertiary and below all expanded → visual explosion
- Using emoji as node icons (unless topic-related, e.g. "food mind map")
- More than 8 primary branches → crowded, consider splitting the topic
- Using 3D / gradients / glass textures
- Central node not in center / not unique
- Making "system architecture / ER diagram" into a mind map (semantic mismatch)
- Font size too small / mono font lost (breaks engineering feel)