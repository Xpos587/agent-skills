# System Architecture Diagram Template

> ⚠️ **This template generates bitmap (PNG), not editable SVG / draw.io / mermaid diagrams**.
> If you need editable, alignable, version-controlled engineering diagrams, use mermaid / draw.io / excalidraw / Figma.
> If you need "README header / blog illustration / document figure / PPT cover" level visual presentation, this template is suitable.

This file is used for generating "engineering-style system architecture diagrams":

- Overall system architecture (frontend + backend + DB + cache + queue + external services)
- Microservice architecture overview
- Multi-region / multi-zone deployment architecture
- AI system / data pipeline architecture
- Cloud-native architecture diagrams

Characteristics:

- Dark background (#0F172A slate-900) + fine grid
- Nodes = rounded rectangles + semi-transparent dark fill + 1.5px border + monospace font labels
- Color coding by "role" (user layer / business layer / data layer / infrastructure / security / middleware / external)
- Directed data flow arrows: solid arrow = sync, dashed = async / callback
- Regions enclosed by large dashed boxes (VPC / cloud zone / trust boundary)
- Font: JetBrains Mono / SF Mono monospace

## Scope

- System overview architecture diagrams
- Microservice / distributed system architecture
- Multi-region / multi-cloud deployment architecture
- Data pipeline / AI system architecture
- Documentation / blog illustrations / README header images

## When to use

- User mentions "system architecture / microservice / distributed / deployment architecture / data pipeline / AI system architecture / cloud architecture"
- User wants the visual "engineering feel, dark, grid, like baoyu-diagram style"
- User accepts this is a bitmap (doesn't require editable)

Do NOT use for:

- User wants "business flowchart / decision diagram" → use `technical-diagrams/flowchart-decision.md`
- User wants "sequence diagram / API call flow" → use `technical-diagrams/sequence-diagram.md`
- User wants "network topology" (server room / routers / devices) → use `technical-diagrams/network-topology.md`
- User wants "ER diagram / data model" → use `technical-diagrams/er-diagram.md`
- User wants "paper method pipeline" → use `academic-figures/method-pipeline-overview.md`
- User wants "neural network architecture" → use `academic-figures/neural-network-architecture.md`

## Missing Information Priority Question Order

1. System name + one-sentence positioning ("we need to draw the overall architecture of XX platform")
2. Main layers / regions (e.g. "frontend / gateway / business services / data layer / infrastructure")
3. Nodes in each layer (max 8-15 total nodes, more will be crowded)
4. Main data flow direction (user request → ... → response)
5. Whether there are external services (third-party APIs / SaaS)
6. Whether there are "security / auth / monitoring" related components that need separate marking
7. Theme color preference (default dark; whether light variant is needed)
8. Aspect ratio (default 16:9 landscape; architecture diagrams are rarely portrait)

## Main Template: Layered Dark System Architecture Diagram

📖 Description

The entire image is divided by layers / regions, each layer is a group of nodes with the same color scheme, connected by arrows expressing data flow, overall presented with engineering feel on a dark grid background.

📝 Prompt

```json
{
  "type": "Tech system architecture diagram (dark engineering style)",
  "goal": "Generate an engineering-style system architecture diagram for README / blog / design documentation",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "{argument name=\"background\" default=\"deep slate #0F172A with subtle 1px grid lines #1E293B at 32px spacing\"}",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"System Architecture Overview\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"v1.0 · 2026\"}",
    "position": "top-left, large mono font (JetBrains Mono / SF Mono), light gray text"
  },
  "color_semantics": {
    "rule": "Color coded by 'role', not by 'technology'",
    "palette": [
      { "role": "User / Client / Edge", "color": "cyan #22D3EE", "use_for": "End users, Web, Mobile, CLI" },
      { "role": "Gateway / API / BFF", "color": "blue #60A5FA", "use_for": "API gateway, load balancer, CDN, BFF" },
      { "role": "Business Services", "color": "emerald #34D399", "use_for": "Microservices, application layer, business logic" },
      { "role": "Data / Persistence", "color": "violet #A78BFA", "use_for": "Databases, cache, object storage, search" },
      { "role": "Middleware / Queue", "color": "orange #FB923C", "use_for": "MQ, Kafka, Redis Stream, Pub/Sub" },
      { "role": "Infra / Platform", "color": "amber #FBBF24", "use_for": "K8s, container runtime, cloud platform" },
      { "role": "Security / Auth", "color": "rose #FB7185", "use_for": "Authentication, secrets, audit, firewall" },
      { "role": "External / 3rd Party", "color": "slate #94A3B8", "use_for": "External SaaS, third-party APIs" }
    ]
  },
  "regions": {
    "rule": "Use large dashed boxes to surround nodes belonging to the same 'deployment unit', with region label above the box",
    "items": [
      { "id": "R1", "label": "{argument name=\"region1_label\" default=\"Public Edge\"}", "color_border": "cyan dashed" },
      { "id": "R2", "label": "{argument name=\"region2_label\" default=\"VPC · ap-northeast-1\"}", "color_border": "amber dashed" },
      { "id": "R3", "label": "{argument name=\"region3_label\" default=\"Data Plane\"}", "color_border": "violet dashed" }
    ]
  },
  "nodes": {
    "count_total": "{argument name=\"node_count\" default=\"10\"}",
    "items": [
      { "id": "N1", "label": "Web App", "role": "User / Client", "region": "R1" },
      { "id": "N2", "label": "Mobile App", "role": "User / Client", "region": "R1" },
      { "id": "N3", "label": "CDN", "role": "Gateway / API", "region": "R1" },
      { "id": "N4", "label": "API Gateway", "role": "Gateway / API", "region": "R2" },
      { "id": "N5", "label": "Auth Service", "role": "Security / Auth", "region": "R2" },
      { "id": "N6", "label": "Order Service", "role": "Business Services", "region": "R2" },
      { "id": "N7", "label": "User Service", "role": "Business Services", "region": "R2" },
      { "id": "N8", "label": "Kafka", "role": "Middleware / Queue", "region": "R2" },
      { "id": "N9", "label": "PostgreSQL", "role": "Data / Persistence", "region": "R3" },
      { "id": "N10", "label": "Redis", "role": "Data / Persistence", "region": "R3" }
    ]
  },
  "node_style": {
    "shape": "rounded rectangle, corner radius 8px",
    "size": "auto-fit text + 24px horizontal padding, ~ 140px wide × 56px tall typical",
    "fill": "background color of role × 12% opacity (semi-transparent)",
    "border": "1.5px solid in role color (full opacity)",
    "label": "label text in JetBrains Mono / SF Mono 12pt, color = role color (lighter shade) for readability on dark bg",
    "icon": "small icon in top-left corner of node (optional, generic geometric glyph for the role — circle for service, cylinder for DB, hex for queue)"
  },
  "edges": {
    "sync_call": {
      "style": "solid line 1.5px in slate #64748B, with small filled triangle arrowhead at the target end",
      "use_for": "Synchronous requests / calls"
    },
    "async_event": {
      "style": "dashed line 1.5px in slate #64748B, with hollow triangle arrowhead",
      "use_for": "Asynchronous events / message pub-sub / callbacks"
    },
    "data_flow_label": {
      "rule": "Optionally add small labels on edges (e.g. 'POST /orders' / 'order.created event'), using mono font 9pt, background blends with canvas"
    },
    "rule_routing": "Primarily orthogonal (horizontal / vertical) routing; if diagonal lines are necessary, keep ≤ 30°; edges must not cross through nodes"
  },
  "legend": {
    "enabled": "{argument name=\"legend_enabled\" default=\"true\"}",
    "position": "bottom-right",
    "content": "color → role mapping (8 swatches), and edge style → meaning (sync solid vs async dashed)",
    "style": "small panel with semi-transparent background, mono font 10pt"
  },
  "constraints": {
    "must_keep": [
      "Dark background + fine grid",
      "Color coded by role, not by technology brand (e.g. PostgreSQL uses violet because it is data, not because PG's official blue)",
      "Nodes unified corner radius and size baseline",
      "Monospace font throughout the diagram",
      "Edges must not cross through nodes, labels must not overlap edges",
      "Region dashed box colors match region semantics",
      "Legend must be drawn (even if simplified)"
    ],
    "avoid": [
      "Rainbow / high-saturation neon colors (all colors except cyan should be muted)",
      "Using emoji as node icons (use minimalist geometric glyphs)",
      "Pasting technology logos directly (unless for trademark reference purposes)",
      "3D cubes / perspective effects / glass textures",
      "Same color used for both 'security' and 'business'",
      "More than 15 nodes (split into multiple sub-diagrams)",
      "Claiming this diagram is editable / exportable as SVG (it is a bitmap)",
      "Using fancy fonts / handwriting fonts (breaks engineering feel)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, node list (with each node's role assignment), main edges
- **Can default**: `background` (dark grid), `color_semantics` (8-role color palette), `node_style`, `legend_enabled` (true)
- **Can randomize**: node placement positions (auto-layout based on region / role), icon glyph specific rendering

### Auto-Fill Strategy

- User provides "Web + API + DB" three-layer simplified → auto-use 3 regions (Edge / Service / Data) + 5-7 nodes
- User doesn't mention regions → auto-cluster by role + add region boxes
- User doesn't mention light variant → default dark; switch to Variant 1 when user requests light
- User provides specific technologies ("uses PostgreSQL") → node label directly shows technology name, but color still selected by role

## Variant 1: Light / Light Mode System Architecture Diagram

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC with very faint grid #E2E8F0",
    "node_fill": "role color × 8% opacity",
    "node_border": "1.5px solid role color (full opacity)",
    "label_color": "role color (full opacity, dark enough for white bg) — e.g. cyan label uses cyan-700 not cyan-300",
    "title_color": "deep slate #0F172A",
    "edges_color": "slate #475569",
    "vibe": "Looks like a light theme documentation illustration (suitable for Notion / GitHub / white-background docs)"
  }
}
```

Suitable for: white-background document sites, print documents, light alternative to the dark version.

## Variant 2: Minimal Monochrome System Architecture Diagram

```json
{
  "modify": {
    "color_semantics": "all roles use slate #94A3B8 except 'highlight current focus' uses single accent (e.g. cyan #22D3EE)",
    "use_case": "Emphasize structure itself, not role classification (e.g. teaching explanations, conceptual diagrams)",
    "vibe": "Restrained, non-distracting, like The Verge / Stripe blog minimalist illustrations"
  }
}
```

Suitable for: conceptual illustrations (no need to emphasize roles), blog hero images, teaching.

## Variant 3: Hero / Marketing Style System Architecture Diagram

```json
{
  "modify": {
    "background": "Gradient deep blue-purple + distant star dots + main nodes with soft glow",
    "node_style": "Nodes retain rounded corners and monospace font, but add subtle glow (drop shadow + glow)",
    "title": "Larger, with sub-slogan",
    "use_case": "Product website hero / investor deck / launch event keynote image",
    "vibe": "Stripe / Linear / Vercel website-style visual impact"
  }
}
```

Suitable for: product websites, tech brand website hero images, product launch keynote visuals.

## Things to Avoid

- More than 15 nodes → visual congestion, recommend splitting into multiple diagrams ("high-level architecture" + "detail module diagrams")
- Using PostgreSQL / Redis / Kafka real logos → risk of copyright infringement + breaks unified visual
- Color coding by "technology" (e.g. PG blue, Redis red) → loses role semantics
- Using emoji as node icons
- 3D perspective / glass textures / gradient-filled nodes
- Edges crossing through nodes / label collisions / diagonal lines flying everywhere
- No legend → readers don't know what colors mean
- No region boxes (even when logically layered) → loses "deployment unit" information
- Pretending this is an exportable editable SVG → don't mislead users
- Cramming neural network structures / business flows / sequences into this diagram (use corresponding templates)