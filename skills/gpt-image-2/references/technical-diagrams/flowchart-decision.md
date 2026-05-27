# Flowchart / Decision Diagram Template

> ⚠️ **This template generates bitmap (PNG)**, not mermaid / draw.io editable flowcharts.
> For editable diagrams use mermaid / draw.io / excalidraw / Figma.

This file is used for generating "engineering-style business flowcharts / decision diagrams":

- Business flowcharts (user registration flow, payment flow, order lifecycle)
- Decision tree flowcharts (with Yes / No branches)
- Algorithm / data processing flows
- Internal approval / ticket / application workflows
- Exception handling / error recovery flows

Characteristics:

- Standard BPMN-like shape semantics:
  - Circle / fully rounded rectangle = start / end
  - Rectangle = process step
  - Diamond = decision point (with Yes / No branches)
  - Parallelogram = input / output
- Top-down OR left-to-right
- Dark grid background + monospace font (following technical-diagrams visual system)
- Decision branch color coding (Yes green, No red / gray)

## Scope

- Business flowcharts
- Decision tree flows
- Algorithm / data flows
- Error handling / exception flows
- Documentation / blog illustrations

## When to use

- User mentions "flowchart / decision diagram / decision tree / business flow / algorithm flow"
- User wants "BPMN standard shape semantics, with Yes/No decision branches"
- User accepts bitmap output

Do NOT use for:

- User wants "step-by-step tutorial illustration" (warm, cartoon feel) → use `infographics/step-by-step-infographic.md`
- User wants "sequence diagram" (actor + messages) → use `technical-diagrams/sequence-diagram.md`
- User wants "state machine" (state + transition) → use `technical-diagrams/state-machine.md`
- User wants "system architecture" (multi-component deployment) → use `technical-diagrams/system-architecture.md`
- User wants "comic storyboard flow" → use `storyboards-and-sequences/recipe-process-flowchart.md`

## Missing Information Priority Question Order

1. Flow name ("user registration flow / refund flow / XX algorithm flow")
2. Start point / end point (what triggers? what ends?)
3. Main steps (recommend 5-12 steps, more than that consider sub-processes)
4. Decision points (where branching is needed? branch conditions?)
5. Whether there are exception branches / failure loops
6. Flow direction (top-down / left-to-right)
7. Aspect ratio (top-down uses 3:4 or 9:16; left-right uses 16:9)

## Main Template: Standard BPMN-Style Flowchart

📖 Description

The entire image flows in "start → process → decision → end" BPMN shape semantics, laid out top-down, with decision points using diamonds + dual-direction branches, arrows labeled Yes/No. Overall presented with engineering feel on a dark grid background.

📝 Prompt

```json
{
  "type": "Engineering-style flowchart / decision diagram",
  "goal": "Generate a business flowchart drawn with BPMN standard shape semantics, usable as README / blog / documentation illustration",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"3:4 portrait\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"User Registration Flow\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"with email verification\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "flow_direction": "{argument name=\"flow_direction\" default=\"top-to-bottom\"}",
  "shape_legend": {
    "start_end": {
      "shape": "filled solid circle (start) and target / bullseye circle (end), or fully rounded pill rectangle with label 'Start' / 'End'",
      "color": "cyan #22D3EE for start, rose #FB7185 for end"
    },
    "process": {
      "shape": "rectangle with corner radius 8px",
      "color": "emerald #34D399 border + 12% fill"
    },
    "decision": {
      "shape": "diamond (rotated square)",
      "color": "amber #FBBF24 border + 12% fill",
      "labels": "Yes / No on outgoing arrows; arrow color: emerald for Yes, slate for No"
    },
    "io": {
      "shape": "parallelogram (skewed rectangle)",
      "color": "violet #A78BFA border + 12% fill",
      "use_for": "user input, data write, external API input/output"
    },
    "subprocess": {
      "shape": "rectangle with corner radius 8px and a smaller secondary rectangle inside (BPMN sub-process notation)",
      "color": "blue #60A5FA border + 12% fill",
      "use_for": "encapsulated sub-processes, to keep the main diagram from getting too large"
    }
  },
  "nodes": {
    "count": "{argument name=\"node_count\" default=\"9\"}",
    "items": [
      { "id": "S", "type": "start_end", "label": "Start" },
      { "id": "N1", "type": "io", "label": "User submits email + password" },
      { "id": "N2", "type": "process", "label": "Validate input format" },
      { "id": "N3", "type": "decision", "label": "Email already exists?" },
      { "id": "N4a", "type": "process", "label": "Show error: account exists" },
      { "id": "N4b", "type": "process", "label": "Create user record" },
      { "id": "N5", "type": "process", "label": "Send verification email" },
      { "id": "N6", "type": "decision", "label": "User clicks link within 24h?" },
      { "id": "N7a", "type": "process", "label": "Mark account verified" },
      { "id": "N7b", "type": "process", "label": "Soft-delete record" },
      { "id": "E", "type": "start_end", "label": "End" }
    ]
  },
  "edges": {
    "rule": "Edges follow the main axis orthogonally (vertical when top-to-bottom), decision branches extend horizontally",
    "items": [
      { "from": "S", "to": "N1" },
      { "from": "N1", "to": "N2" },
      { "from": "N2", "to": "N3" },
      { "from": "N3", "to": "N4a", "label": "Yes" },
      { "from": "N3", "to": "N4b", "label": "No" },
      { "from": "N4a", "to": "E" },
      { "from": "N4b", "to": "N5" },
      { "from": "N5", "to": "N6" },
      { "from": "N6", "to": "N7a", "label": "Yes" },
      { "from": "N6", "to": "N7b", "label": "No" },
      { "from": "N7a", "to": "E" },
      { "from": "N7b", "to": "E" }
    ],
    "edge_style": {
      "default": "solid line 1.5px slate #64748B with filled triangle arrowhead",
      "yes_branch": "thin solid line in emerald #34D399 + label 'Yes' near origin in mono 9pt",
      "no_branch": "thin solid line in slate #64748B + label 'No'",
      "exception_branch": {
        "enabled": "{argument name=\"exception_branch_enabled\" default=\"false\"}",
        "style": "dashed rose #FB7185 line, label 'Exception' / 'Error'"
      }
    }
  },
  "swim_lanes": {
    "enabled": "{argument name=\"swim_lanes_enabled\" default=\"false\"}",
    "rule": "if true, divide canvas into vertical / horizontal lanes labeled by actor (e.g. 'User', 'Frontend', 'Backend', 'Email Service'); place each node in its actor's lane"
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "shape → role mapping (start/end, process, decision, io, subprocess) and edge → meaning",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "BPMN shape semantics strictly followed",
      "Decision nodes must have ≥ 2 branches",
      "Each decision branch must be labeled 'Yes' / 'No' or with a specific condition",
      "Edges routed orthogonally, labels must not overlap edges",
      "Dark background + monospace font",
      "At least 1 start and 1 end",
      "Legend must be drawn"
    ],
    "avoid": [
      "Using emoji nodes",
      "Drawing decision points as circles / rectangles (must be diamonds)",
      "Drawing processes as diamonds (semantic confusion)",
      "Diagonal lines flying everywhere / edges crossing through nodes",
      "More than 15 nodes (split into sub-processes)",
      "Decision branches without labels",
      "Using fancy fonts / gradient fills",
      "Making the flowchart look like an illustration (use step-by-step-infographic for tutorial steps)",
      "Claiming this is an editable SVG (it is a bitmap)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, start + end points, node list (with type), decision point branch conditions
- **Can default**: `flow_direction` (top-to-bottom), `background` (dark grid), `shape_legend`, `legend_enabled` (true)
- **Can randomize**: node positions (auto-layout based on flow_direction)

### Auto-Fill Strategy

- User provides 5-7 steps but no decisions → default to no decisions (pure linear flow)
- User says "with exception handling" → enable `exception_branch_enabled` + add dashed rose line
- User says "multi-actor / cross-department / cross-service" → enable `swim_lanes_enabled`
- User says "flow is long, more than 12 steps" → ask whether to split into multiple sub-processes
- User wants light mode → use Variant 1

## Variant 1: Light Flowchart

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "node_fill": "shape role color × 8% opacity",
    "node_border": "1.5px solid full opacity (use deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "edge_color": "slate #475569",
    "vibe": "suitable for white-background documentation sites / print editions"
  }
}
```

## Variant 2: Swim Lanes Cross-Actor Flowchart

```json
{
  "modify": {
    "swim_lanes_enabled": true,
    "lane_layout": "vertical lanes (each actor a vertical column)",
    "lane_labels": ["User", "Frontend", "Backend API", "Database", "Email Service"],
    "rule": "Each node placed in its corresponding actor's lane; cross-lane edges use bold arrows",
    "use_case": "Cross-department approval, cross-service interaction, multi-actor user-system flows"
  }
}
```

Suitable for: cross-department approval flows, cross-service interaction flows, flows that need to clearly show "who does what."

## Variant 3: Algorithm Pseudocode Visualization Flow

```json
{
  "modify": {
    "title": "Algorithm: <name>",
    "node_label_format": "Node labels use pseudocode snippets rather than natural language",
    "rule_extra": "Keep loop nodes (loop-back curved arrows for loops), variable assignments use ← notation",
    "vibe": "suitable as a visual version of paper algorithm boxes"
  }
}
```

Suitable for: algorithm visualization, visual versions of paper algorithm sections, teaching handouts.

## Things to Avoid

- Drawing decision diamonds as squares or circles (semantic confusion)
- Decision branches without Yes / No labels
- More than 15 nodes (visual explosion, recommend splitting)
- Using emoji as node icons
- Diagonal edges / edges crossing through nodes / label collisions
- Using illustration-style cartoon graphics (use `step-by-step-infographic.md` instead)
- Using 3D / gradients / glass textures
- Multiple start or end points not clearly marked
- In swim lane mode, drawing cross-lane arrows inconspicuously
- Cramming "system architecture" into a flowchart (nodes should be actions not components)