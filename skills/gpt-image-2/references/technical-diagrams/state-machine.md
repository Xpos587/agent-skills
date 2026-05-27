# State Machine / Lifecycle Diagram Template

> ⚠️ **This template generates bitmap (PNG)**, not mermaid / xstate editable state machines.
> For editable diagrams use mermaid stateDiagram / xstate visualizer.

This file is used for generating "engineering-style state machines / lifecycle diagrams":

- Order state machines (pending payment / paid / shipped / completed / cancelled / refunded)
- Connection / session states (idle / connecting / connected / closing / closed)
- Workflow states (draft / submitted / approved / rejected)
- UI component states (hover / active / disabled / loading)
- Protocol state machines (TCP states, WebSocket states, HTTP cache states)

Characteristics:

- Rounded rectangles = state nodes
- Filled circle = initial pseudo-state; bullseye / double circle = final state
- Directed edges = transitions, labeled with "event / condition"
- Self-loops = state preserving itself
- Dark grid + monospace font (following visual system)

## Scope

- Business object lifecycles (orders / documents / tickets)
- Protocol / connection states
- Workflow / approval states
- UI component / interaction states
- Device / session / task states

## When to use

- User mentions "state machine / lifecycle / state diagram / state transition"
- User wants standard "state + transition" UML state diagram style
- User accepts bitmap output

Do NOT use for:

- User wants "business flowchart (with decisions, actions)" → use `technical-diagrams/flowchart-decision.md`
- User wants "sequence diagram" → use `technical-diagrams/sequence-diagram.md`

## Missing Information Priority Question Order

1. State machine name ("order state machine / TCP state machine")
2. Initial state (usually unique) + final state(s) (can be multiple)
3. Intermediate state list (recommend 4-12, more than that consider sub-state machines)
4. Transitions: for each transition "source state → target state + trigger event + guard condition + action"
5. Whether there are self-loops
6. Whether composite states (nested states) are needed
7. Aspect ratio (default 4:3 or 16:9 landscape)

## Main Template: Standard UML State Machine Diagram

📖 Description

The entire image starts from the initial pseudo-state (filled circle), flows through several state nodes (rounded rectangles) and transition arrows (labeled with events), finally reaching the final state (bullseye). State nodes can have self-loops (e.g. "retry" self-loop).

📝 Prompt

```json
{
  "type": "Engineering-style state machine / lifecycle diagram (UML state diagram)",
  "goal": "Generate a state machine diagram as business documentation / protocol specification / teaching illustration",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"Order Lifecycle State Machine\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"e-commerce order from creation to completion\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "states": {
    "count": "{argument name=\"state_count\" default=\"7\"}",
    "items": [
      { "id": "S0", "type": "initial", "label": "" },
      { "id": "S1", "type": "state", "label": "Pending\\nPayment", "category": "active" },
      { "id": "S2", "type": "state", "label": "Paid", "category": "active" },
      { "id": "S3", "type": "state", "label": "Shipped", "category": "active" },
      { "id": "S4", "type": "state", "label": "Completed", "category": "success_terminal" },
      { "id": "S5", "type": "state", "label": "Cancelled", "category": "fail_terminal" },
      { "id": "S6", "type": "state", "label": "Refunded", "category": "fail_terminal" },
      { "id": "ST", "type": "final", "label": "" }
    ]
  },
  "state_style": {
    "initial": {
      "shape": "filled solid circle, ~16px diameter",
      "color": "cyan #22D3EE solid"
    },
    "final": {
      "shape": "concentric double circle (bullseye), outer ~18px, inner solid 10px",
      "color": "rose #FB7185"
    },
    "state": {
      "shape": "rounded rectangle, corner radius 12px (more rounded than process), 160×72px typical",
      "fill": "category color × 12% opacity",
      "border": "1.5px solid in category color",
      "label": "state name in mono 12pt, centered, light text on dark fill",
      "optional_internal_label": "Can add small text at the bottom inside the state: 'entry / action' / 'do / activity' / 'exit / cleanup' (UML extension)"
    }
  },
  "category_color_map": {
    "active": "emerald #34D399",
    "waiting": "amber #FBBF24",
    "success_terminal": "blue #60A5FA",
    "fail_terminal": "rose #FB7185",
    "error": "rose #FB7185",
    "neutral": "slate #94A3B8"
  },
  "transitions": {
    "items": [
      { "from": "S0", "to": "S1", "label": "create()" },
      { "from": "S1", "to": "S2", "label": "pay() [valid card]" },
      { "from": "S1", "to": "S5", "label": "timeout / cancel()" },
      { "from": "S2", "to": "S3", "label": "ship()" },
      { "from": "S2", "to": "S6", "label": "refund() [user request]" },
      { "from": "S3", "to": "S4", "label": "deliver() [confirmed]" },
      { "from": "S3", "to": "S6", "label": "return() [defect]" },
      { "from": "S4", "to": "ST", "label": "" },
      { "from": "S5", "to": "ST", "label": "" },
      { "from": "S6", "to": "ST", "label": "" },
      { "from": "S1", "to": "S1", "label": "retry_payment", "self_loop": true }
    ],
    "transition_style": {
      "default": "thin solid arrow 1.5px slate #94A3B8 with filled triangle arrowhead",
      "self_loop": "small loop curving above the state, returning to itself",
      "label_format": "<event> [guard] / <action>, e.g. 'pay() [valid card] / lock_inventory()', mono 9-10pt labeled at edge midpoint, background blends with canvas to avoid overlap"
    },
    "rule_routing": "Primarily orthogonal or ≤ 30° diagonal lines, avoid edges crossing through nodes"
  },
  "composite_states": {
    "enabled": "{argument name=\"composite_enabled\" default=\"false\"}",
    "rule": "if true, can group sub-states inside a larger rounded rectangle labeled 'Active' / 'Suspended' etc.; sub-states are 'state' type nested within the composite border"
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "category color → meaning (active / terminal-success / terminal-fail / error), shape → role (initial filled circle / final bullseye / state rectangle), self-loop notation",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "Initial state is a filled circle / final state is a bullseye, do not mix",
      "State nodes unified shape (rounded rectangle) and size baseline",
      "Transitions must have labels (except entering final state)",
      "Guard conditions enclosed in []",
      "Actions separated by /",
      "Self-loops drawn as loops, not straight lines",
      "Category colors consistent (do not use red for success, green for fail)",
      "Dark grid + monospace font",
      "Legend must be drawn"
    ],
    "avoid": [
      "Using diamonds / parallelograms as states (confused with flowcharts)",
      "Transitions without labels",
      "Drawing final states as regular rounded rectangles",
      "Guard / action syntax non-standard (missing [] or /)",
      "More than 12 states (crowded; consider composite state or splitting)",
      "Using emoji as state icons",
      "Using 3D / gradients / glass textures",
      "Claiming this is an editable SVG"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, initial state, final state(s), intermediate state list, all transitions (with from/to/label)
- **Can default**: `background` (dark grid), `category_color_map`, `legend_enabled` (true)
- **Can randomize**: state node placement positions (auto-layout based on transition relationships to minimize edge crossings)

### Auto-Fill Strategy

- User provides "order state machine" but no details → use default 7-state version (pending payment / paid / shipped / completed / cancelled / refunded)
- User doesn't mention guard / action → label only has event name
- User provides states but no transitions → ask for key transitions (cannot fabricate business rules)
- User says "too many states" → enable `composite_enabled` + use composite to surround related states
- User wants light mode → use Variant 1

## Variant 1: Light State Machine

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "state_fill": "category color × 8% opacity",
    "state_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "transition_color": "slate #475569",
    "vibe": "white-background documentation / print edition"
  }
}
```

## Variant 2: Protocol State Machine (TCP / WebSocket / HTTP cache)

```json
{
  "modify": {
    "title_format": "<protocol> State Machine (e.g. TCP State Machine)",
    "state_label_emphasis": "Use uppercase / protocol specification terms (e.g. LISTEN / SYN_SENT / ESTABLISHED / TIME_WAIT)",
    "transition_label_emphasis": "Use 'trigger packet / send packet' format: e.g. 'recv: SYN / send: SYN+ACK'",
    "use_case": "Network protocol teaching, specification documentation, interview preparation materials"
  }
}
```

Suitable for: TCP / UDP / WebSocket / HTTP / OAuth state descriptions.

## Variant 3: UI Component States (Button / Input / Modal)

```json
{
  "modify": {
    "title_format": "<Component> Interaction States",
    "state_label_emphasis": "Use UI state terminology: default / hover / active / focus / disabled / loading / error / success",
    "transition_label_emphasis": "Use UI events: mouseenter / click / focus / blur / API resolve / API reject",
    "category_color_map_extra": "default = slate, hover = cyan, active = emerald, disabled = slate desaturated, loading = amber, error = rose, success = blue",
    "use_case": "Design system documentation, component library README, designer / developer alignment"
  }
}
```

Suitable for: design systems, component library documentation, UI / UX state specifications.

## Things to Avoid

- Using diamond / parallelogram shapes for state nodes → confused with flowcharts
- Transitions without event labels → completely loses state machine semantics
- Drawing final states as regular rectangles → non-compliant with UML
- Guard conditions not using [] → non-standard
- Using emoji as state icons
- More than 12 states → crowded, must split or use composite
- Self-loops drawn as straight lines → visual error
- Success / fail colors reversed
- Making a "state machine" into a "flowchart" (nodes should be states, not actions)
- Too many nodes / edges causing mutual overlap