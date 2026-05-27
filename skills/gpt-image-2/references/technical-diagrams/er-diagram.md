# ER Diagram / Data Model Diagram Template

> ⚠️ **This template generates bitmap (PNG)**, not dbdiagram.io / draw.io editable ER diagrams.
> For editable diagrams use dbdiagram.io / draw.io / DBeaver.

This file is used for generating "engineering-style ER diagrams / data model diagrams":

- Database table structure diagrams (PG / MySQL / SQLite)
- Domain model diagrams (DDD entities + relationships)
- Document database schema (MongoDB / DynamoDB)
- API data contract schema diagrams
- Microservice boundary + data ownership diagrams

Characteristics:

- Entity boxes = rounded rectangles, split into upper and lower zones: upper zone for table name / lower zone for field list
- Field rows = field name + type + primary key PK / foreign key FK markers
- Relationship lines = 1:1 / 1:N / N:M (using crow's foot or UML multiplicity)
- Dark grid + monospace font (following visual system)

## Scope

- Database table structures
- Domain models / DDD entities
- API schema documentation
- Database design reviews
- Microservice data ownership diagrams

## When to use

- User mentions "ER diagram / Entity-Relationship / data model / database design / schema diagram / table structure"
- User wants standard "entity + field + relationship" ER diagram style
- User accepts bitmap output

Do NOT use for:

- User wants "system architecture" → use `technical-diagrams/system-architecture.md`
- User wants "class diagram / UML class diagram" (with methods) → no dedicated template yet, can adapt this template by adding method rows
- User wants "mind map" → use `technical-diagrams/mind-map-tech.md`

## Missing Information Priority Question Order

1. Database / domain name ("e-commerce data model / SaaS user management schema")
2. Entity list (recommend 4-12, more than that consider splitting into sub-diagrams)
3. Fields for each entity (field name + type + PK/FK + whether nullable)
4. Relationships between entities (1:1 / 1:N / N:M, whether cascading)
5. Whether to include enums / indexes / constraints
6. Aspect ratio (default 4:3 or 16:9)

## Main Template: Standard ER Diagram (Dark Engineering Style)

📖 Description

The entire image is composed of several entity boxes, each showing the table name + table label (📦 entity) in the upper half, and listing fields in the lower half (with type + PK/FK markers), connected by relationship lines between entities, with crow's foot at endpoints expressing 1 / N.

📝 Prompt

```json
{
  "type": "Engineering-style ER diagram / data model diagram",
  "goal": "Generate an engineering-style ER diagram as database design documentation / API schema / domain model review illustration",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"4:3\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"E-commerce Data Model\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"core entities · v1.0\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "entities": {
    "count": "{argument name=\"entity_count\" default=\"6\"}",
    "items": [
      {
        "id": "E1",
        "name": "users",
        "category": "user",
        "fields": [
          { "name": "id", "type": "uuid", "marker": "PK" },
          { "name": "email", "type": "varchar(255)", "marker": "UQ" },
          { "name": "password_hash", "type": "varchar(255)", "marker": "" },
          { "name": "created_at", "type": "timestamp", "marker": "" },
          { "name": "updated_at", "type": "timestamp", "marker": "" }
        ]
      },
      {
        "id": "E2",
        "name": "orders",
        "category": "transaction",
        "fields": [
          { "name": "id", "type": "uuid", "marker": "PK" },
          { "name": "user_id", "type": "uuid", "marker": "FK→users.id" },
          { "name": "status", "type": "enum", "marker": "" },
          { "name": "total_cents", "type": "bigint", "marker": "" },
          { "name": "created_at", "type": "timestamp", "marker": "" }
        ]
      },
      {
        "id": "E3",
        "name": "order_items",
        "category": "transaction",
        "fields": [
          { "name": "id", "type": "uuid", "marker": "PK" },
          { "name": "order_id", "type": "uuid", "marker": "FK→orders.id" },
          { "name": "product_id", "type": "uuid", "marker": "FK→products.id" },
          { "name": "quantity", "type": "int", "marker": "" },
          { "name": "unit_price_cents", "type": "bigint", "marker": "" }
        ]
      },
      {
        "id": "E4",
        "name": "products",
        "category": "catalog",
        "fields": [
          { "name": "id", "type": "uuid", "marker": "PK" },
          { "name": "sku", "type": "varchar(64)", "marker": "UQ" },
          { "name": "name", "type": "varchar(255)", "marker": "" },
          { "name": "price_cents", "type": "bigint", "marker": "" },
          { "name": "stock", "type": "int", "marker": "" }
        ]
      },
      {
        "id": "E5",
        "name": "categories",
        "category": "catalog",
        "fields": [
          { "name": "id", "type": "uuid", "marker": "PK" },
          { "name": "name", "type": "varchar(128)", "marker": "" },
          { "name": "parent_id", "type": "uuid", "marker": "FK→categories.id (self)" }
        ]
      },
      {
        "id": "E6",
        "name": "product_categories",
        "category": "join",
        "fields": [
          { "name": "product_id", "type": "uuid", "marker": "PK,FK→products.id" },
          { "name": "category_id", "type": "uuid", "marker": "PK,FK→categories.id" }
        ]
      }
    ]
  },
  "entity_style": {
    "shape": "rounded rectangle, corner radius 6px",
    "fill": "category color × 10% opacity",
    "border": "1.5px solid in category color",
    "header_strip": "topmost ~28px height: filled with category color × 25% opacity, contains table name in bold mono 12pt + small icon glyph",
    "field_row_style": "below header: each field row = 'field_name : type [marker]' in mono 10pt, alternating row tint for readability",
    "marker_color": "PK = amber bold, FK = blue, UQ = violet, NN = subtle gray"
  },
  "category_color_map": {
    "user": "cyan #22D3EE",
    "transaction": "emerald #34D399",
    "catalog": "violet #A78BFA",
    "join": "slate #94A3B8",
    "system": "amber #FBBF24",
    "external": "rose #FB7185"
  },
  "relationships": {
    "items": [
      { "from": "E1", "to": "E2", "cardinality": "1:N", "label": "places" },
      { "from": "E2", "to": "E3", "cardinality": "1:N", "label": "contains" },
      { "from": "E4", "to": "E3", "cardinality": "1:N", "label": "appears_in" },
      { "from": "E4", "to": "E6", "cardinality": "1:N", "label": "" },
      { "from": "E5", "to": "E6", "cardinality": "1:N", "label": "" },
      { "from": "E5", "to": "E5", "cardinality": "0..1:N", "label": "parent_of (self)" }
    ],
    "line_style": {
      "default": "solid line 1.5px slate #94A3B8",
      "endpoint_notation": "use crow's foot notation: '1' = single perpendicular tick, 'N' = three-pronged 'crow's foot', '0..1' = open circle + tick, '0..N' = open circle + crow's foot",
      "label_format": "relationship verb in mono 9pt placed near the middle of the line, e.g. 'places' / 'contains'"
    },
    "rule_routing": "lines avoid crossing entities; orthogonal routing preferred; self-relations curve to the side"
  },
  "extras": {
    "indices_section": {
      "enabled": "{argument name=\"indices_enabled\" default=\"false\"}",
      "rule": "if true, below each entity add a small 'Indices' section listing index names (e.g. 'idx_users_email')"
    },
    "color_legend": {
      "enabled": true,
      "position": "bottom-right",
      "content": "category color → role mapping + marker meaning (PK / FK / UQ / NN) + cardinality notation"
    }
  },
  "constraints": {
    "must_keep": [
      "Entity box shape unified (rounded rectangle + header strip)",
      "Field rows use monospace font, type right-aligned or colon-separated",
      "PK / FK / UQ markers clear (color + text)",
      "Relationship lines use crow's foot or UML multiplicity to express 1:1 / 1:N / N:M",
      "FK fields must mark FK→target_table.field within the table",
      "Dark grid background + monospace font",
      "Legend must be drawn"
    ],
    "avoid": [
      "Using diamond shapes for entities (semantic error)",
      "Field rows using proportional fonts (breaks alignment)",
      "FK without target → relationship loses context",
      "Relationship lines without cardinality endpoints",
      "More than 12 entities (crowded; split by sub-domain)",
      "Join tables using same color as regular tables (should use 'join' gray to distinguish)",
      "Using emoji as field markers",
      "Claiming this is an editable SVG"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, entity list (with fields + PK/FK markers), relationship list (with cardinality)
- **Can default**: `background` (dark grid), `category_color_map`, `indices_enabled` (false)
- **Can randomize**: entity placement positions (auto-layout to minimize edge crossings)

### Auto-Fill Strategy

- User provides "e-commerce schema" → use default 6 entities
- User doesn't specify cardinality → ask back (relationship semantics cannot be guessed)
- User doesn't categorize by category → auto-categorize by table name (users → user, orders → transaction, products → catalog, *_join → join)
- User wants light mode → use Variant 1
- User says "include indexes" → enable `indices_enabled`

## Variant 1: Light ER Diagram

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "entity_fill": "category color × 8% opacity",
    "entity_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "vibe": "friendly for white-background documentation sites"
  }
}
```

## Variant 2: DDD Domain Model Diagram (with Methods / Behaviors)

```json
{
  "modify": {
    "entity_label_format": "<<entity / value object / aggregate root>> add stereotype label above table name",
    "field_section_split": "Inside the entity, split into two parts: fields above, methods below (separated by a '——' divider), method format 'methodName(args): returnType'",
    "category_color_map_extra": "aggregate root = amber, entity = emerald, value object = violet, domain service = cyan",
    "use_case": "DDD tactical design review, domain modeling workshop"
  }
}
```

Suitable for: DDD project domain modeling, UML class diagrams, business modeling.

## Variant 3: Microservice Data Ownership Diagram (Bounded Context)

```json
{
  "modify": {
    "extras": "Use large dashed boxes (bounded context) to surround entities belonging to the same service, label boxes with 'User Service' / 'Order Service' etc.",
    "cross_service_relations": "Cross-service relationships use red dashed lines (indicating anti-pattern or explicit service boundary crossing)",
    "use_case": "Microservice splitting, bounded context design, Conway's Law alignment"
  }
}
```

Suitable for: microservice design, bounded context partitioning, data ownership reviews.

## Things to Avoid

- Using proportional fonts for field rows → types / markers won't align
- FK without target → relationship context lost
- Relationship lines without cardinality → completely loses ER semantics
- More than 12 entities → visual explosion, must split
- Using diamond shapes for entities → semantic error
- Using emoji as field markers
- Join tables same color as regular tables
- Claiming this is an editable SVG
- Cramming "system architecture" into ER diagram (use the corresponding template)
- Omitting field types → loses engineering value