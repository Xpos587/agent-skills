# Sequence Diagram Template

> ⚠️ **This template generates bitmap (PNG)**, not PlantUML / mermaid editable sequence diagrams.
> For editable diagrams use mermaid / PlantUML / draw.io.

This file is used for generating "engineering-style sequence diagrams":

- API call sequences (frontend → backend → DB)
- Authentication / OAuth / multi-step handshake sequences
- Microservice inter-message sequences
- Distributed transaction / Saga / 2PC sequences
- Client - server - third-party protocol sequences

Characteristics:

- Top row of actor boxes (with names + type icons)
- Each actor has a vertical dashed line below (lifeline)
- Horizontal message arrows connect actors (solid arrow = sync, dashed arrow = async / return)
- "Activation bars" on lifelines (thin rectangles) showing when an actor is processing
- Messages can be numbered (1, 2, 3...)
- Dark grid background + monospace font

## Scope

- API call sequences
- Authentication / OAuth flows
- Microservice message sequences
- Distributed transactions / Saga / 2PC
- Third-party protocol / SDK call flows

## When to use

- User mentions "sequence diagram / call sequence / API flow / OAuth flow / distributed transaction / call timing"
- User wants standard "actor + lifeline + message arrow" UML sequence diagram style
- User accepts bitmap output

Do NOT use for:

- User wants "business flow / decision" → use `technical-diagrams/flowchart-decision.md`
- User wants "state machine" → use `technical-diagrams/state-machine.md`
- User wants "system architecture" → use `technical-diagrams/system-architecture.md`

## Missing Information Priority Question Order

1. Sequence name ("OAuth 2.0 authorization code flow / order sequence / Saga transaction")
2. Participating actors (in left-to-right order)
3. Message sequence (in chronological order, specifying sender → receiver, message content, sync / async)
4. Whether there are failure / retry branches
5. Whether there are self-calls (actor calling its own internal method)
6. Whether message numbering is needed (papers / protocol descriptions often require it)
7. Aspect ratio (default 16:9 landscape; can use 4:3 when many actors)

## Main Template: Standard UML Sequence Diagram

📖 Description

The entire image has a row of actor boxes at the top, with a vertical dashed lifeline below each actor, horizontal message arrows connecting actors, activation bars on lifelines, and clear message numbering + labels.

📝 Prompt

```json
{
  "type": "Engineering-style sequence diagram (UML sequence diagram)",
  "goal": "Generate an engineering-style sequence diagram as a README / blog / protocol documentation illustration",
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect_ratio\" default=\"16:9\"}",
    "background": "deep slate #0F172A with subtle 1px grid #1E293B at 32px spacing",
    "outer_padding": "60px"
  },
  "title_strip": {
    "title": "{argument name=\"title\" default=\"OAuth 2.0 Authorization Code Flow\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"with PKCE\"}",
    "position": "top-left, JetBrains Mono / SF Mono, light gray"
  },
  "actors": {
    "count": "{argument name=\"actor_count\" default=\"4\"}",
    "items": [
      {
        "id": "A1",
        "name": "{argument name=\"actor1_name\" default=\"User\"}",
        "type": "{argument name=\"actor1_type\" default=\"user\"}",
        "icon_glyph": "stick figure outline"
      },
      {
        "id": "A2",
        "name": "{argument name=\"actor2_name\" default=\"Web App\"}",
        "type": "{argument name=\"actor2_type\" default=\"client\"}",
        "icon_glyph": "browser window outline"
      },
      {
        "id": "A3",
        "name": "{argument name=\"actor3_name\" default=\"Auth Server\"}",
        "type": "{argument name=\"actor3_type\" default=\"service\"}",
        "icon_glyph": "shield outline"
      },
      {
        "id": "A4",
        "name": "{argument name=\"actor4_name\" default=\"Resource Server\"}",
        "type": "{argument name=\"actor4_type\" default=\"service\"}",
        "icon_glyph": "database / server outline"
      }
    ],
    "header_box_style": {
      "shape": "rounded rectangle, corner radius 6px",
      "fill": "type-coded color × 12% opacity",
      "border": "1.5px solid type-coded color",
      "size": "160px wide × 64px tall, all headers identical size, evenly spaced",
      "label": "actor name in mono 11pt + small icon glyph above name"
    },
    "type_color_map": {
      "user": "cyan #22D3EE",
      "client": "blue #60A5FA",
      "service": "emerald #34D399",
      "database": "violet #A78BFA",
      "external": "slate #94A3B8"
    }
  },
  "lifelines": {
    "rule": "Below each actor header, draw a vertical dashed line (1px dashed slate #475569), extending from header bottom to canvas bottom",
    "spacing": "Lifelines equally spaced, gap ≥ 200px"
  },
  "messages": {
    "count": "{argument name=\"message_count\" default=\"10\"}",
    "items": [
      { "id": "M1", "from": "A1", "to": "A2", "label": "1. Click 'Sign in'", "type": "sync" },
      { "id": "M2", "from": "A2", "to": "A3", "label": "2. GET /authorize?code_challenge=...", "type": "sync" },
      { "id": "M3", "from": "A3", "to": "A1", "label": "3. Show login page", "type": "return" },
      { "id": "M4", "from": "A1", "to": "A3", "label": "4. Submit credentials", "type": "sync" },
      { "id": "M5", "from": "A3", "to": "A2", "label": "5. Redirect with auth_code", "type": "return" },
      { "id": "M6", "from": "A2", "to": "A3", "label": "6. POST /token { code, code_verifier }", "type": "sync" },
      { "id": "M7", "from": "A3", "to": "A2", "label": "7. { access_token, refresh_token }", "type": "return" },
      { "id": "M8", "from": "A2", "to": "A4", "label": "8. GET /api/data (Bearer token)", "type": "sync" },
      { "id": "M9", "from": "A4", "to": "A4", "label": "9. validate token", "type": "self" },
      { "id": "M10", "from": "A4", "to": "A2", "label": "10. { data: ... }", "type": "return" }
    ],
    "message_style": {
      "sync": "solid line 1.5px slate #94A3B8, filled triangle arrowhead at target",
      "async": "solid line 1.5px slate #94A3B8, hollow triangle arrowhead",
      "return": "dashed line 1.5px slate #64748B, hollow triangle arrowhead",
      "self": "horizontal arrow that loops out to the right and back to the same lifeline (bracket shape)"
    },
    "label_format": "<number>. <message content>, e.g. '5. Redirect with auth_code', mono 10pt, centered above the arrow"
  },
  "activation_bars": {
    "enabled": "{argument name=\"activation_bars_enabled\" default=\"true\"}",
    "rule": "Draw thin rectangles (4-6px wide) on actor lifelines covering the time period when that actor is processing a message; color uses the actor's type color, semi-transparent",
    "vertical_extent": "From when the actor receives a message to when it sends a return"
  },
  "annotations": {
    "notes": {
      "enabled": "{argument name=\"notes_enabled\" default=\"false\"}",
      "rule": "Can add yellow sticky notes (amber semi-transparent rounded rectangle) next to a sequence segment with annotations, e.g. 'PKCE prevents code interception'"
    },
    "loops_alts": {
      "enabled": "{argument name=\"loops_alts_enabled\" default=\"false\"}",
      "rule": "Can use UML alt / loop frames: rounded rectangles enclosing multiple messages, with 'alt' / 'loop' label + condition text at top-left corner"
    }
  },
  "legend": {
    "enabled": true,
    "position": "bottom-right",
    "content": "actor type → color, message style → meaning (sync solid arrow / async hollow / return dashed / self bracket)",
    "style": "small panel, semi-transparent bg, mono 10pt"
  },
  "constraints": {
    "must_keep": [
      "Actor headers equal size, equal spacing, horizontally aligned",
      "Lifelines vertical, equally spaced",
      "Messages strictly ordered top-to-bottom chronologically",
      "Each message has a number + concise label",
      "Sync / return / async distinguished by different arrow styles",
      "Dark grid background + monospace font",
      "Legend must be drawn"
    ],
    "avoid": [
      "Actor headers different sizes",
      "Messages not in chronological order",
      "Self-call drawn as a straight line (must be bracket / loop shape)",
      "Return using solid line arrow (breaks semantics)",
      "Label overlapping lifeline",
      "Using emoji as actor icons",
      "More than 6 actors (crowded; consider splitting)",
      "More than 15 messages (visual explosion; consider splitting into sub-sequences)",
      "Claiming this is an editable SVG"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: `title`, actors list, messages sequence (with from/to/label/type)
- **Can default**: `activation_bars_enabled` (true), `type_color_map`, `notes_enabled` (false), `loops_alts_enabled` (false)
- **Can randomize**: actor icon glyph specific rendering, message label font size fine-tuning

### Auto-Fill Strategy

- User provides "I want to draw OAuth flow" → default 4 actors + 10 messages (user → web → auth → resource)
- User doesn't specify sync / async → default sync; obvious callback / notification scenarios default async
- User says "with failure retry" → enable `loops_alts_enabled` + alt block enclosure
- User says "add annotation explanations" → enable `notes_enabled`
- User wants light mode → use Variant 1

## Variant 1: Light Sequence Diagram

```json
{
  "modify": {
    "background": "warm off-white #F8FAFC + faint grid #E2E8F0",
    "actor_header_fill": "type color × 8% opacity",
    "actor_header_border": "1.5px solid (deeper shade for white bg)",
    "label_color": "deep slate #0F172A",
    "lifeline_color": "slate #94A3B8 dashed",
    "vibe": "white-background documentation / print-friendly"
  }
}
```

## Variant 2: Protocol Handshake / OAuth / Authentication-Specific Style

```json
{
  "modify": {
    "messages_emphasis": "Add a lock-equivalent glyph or 'TLS' / 'signed' small label for security / token messages",
    "extras": "Additionally label HTTP method (GET/POST/PUT) on messages, with tiny mono labels",
    "annotation": "Add PKCE / nonce / state explanation notes, notes_enabled = true",
    "use_case": "OAuth 2.0 / OIDC / SAML / mTLS and other protocols"
  }
}
```

Suitable for: protocol teaching, authentication flow documentation.

## Variant 3: Distributed Transaction / Saga / 2PC Style

```json
{
  "modify": {
    "actor_types": "Typically 4-5 service actors + 1 coordinator + 1 message broker",
    "messages_emphasis": "Clearly label prepare / commit / rollback / compensate phases, using different colors (commit green, rollback red, prepare blue)",
    "loops_alts_enabled": true,
    "alt_blocks": "alt 'commit phase' / 'rollback phase' enclosing corresponding messages",
    "use_case": "Saga / 2PC / TCC / outbox pattern teaching and documentation"
  }
}
```

Suitable for: distributed transaction pattern teaching, architecture reviews, failure mode analysis.

## Things to Avoid

- Sequence diagram with messages not ordered chronologically top-to-bottom → loses sequential nature
- Using diamond / circle for actors (must be rectangular headers)
- Self-call drawn as straight line (must be bracket)
- Return using solid line (confused with sync)
- More than 6 actors → visually crowded, consider splitting
- More than 15 messages → visual explosion
- Using emoji as actor icons
- Making actor avatars into cartoon characters → loses engineering feel
- No activation bars → can't tell who's processing
- No message numbering (teaching scenarios must have it)
- Drawing a "flowchart" as a sequence diagram (nodes should be actions not actors)