# Character Relationship Diagram Template

This file is used for "generating character relationship diagrams based on a work / organization":

- Anime / movie / novel character relationship diagrams
- Company / organization member relationship diagrams
- Historical event participant relationship diagrams
- Team / faction relationship diagrams

Features:

- Multiple character cards (avatar + name + label)
- Different colors / line types representing different relationships
- Clear visual hierarchy (main character large, supporting characters small)
- Emphasis on "information visualization + poster design feel"
- Overall restrained, not cluttered

## Scope

- IP character relationship diagrams
- Organization / team structure diagrams
- Historical event figure relationship diagrams
- Social media educational content

## When to Use

- User mentions "relationship diagram / relationship network / character graph / faction diagram"
- User wants a single image that clearly shows who is related to whom

Do NOT use for:

- Single image KV (use `anime-key-visual.md`)
- Character design sheets (use `portraits-and-characters/character-sheet.md`)
- General infographics (use `infographics/legend-heavy-infographic.md`)

## Missing Information Priority Question Order

1. Theme (which work / which organization)
2. Character count (recommended 6-12)
3. Who is the main character (highest visual weight)
4. Relationship types (blood / friendship / mentor-student / rival / alliance / secret crush)
5. Style: faithful to original work style / universal modern design style
6. Aspect ratio

## Main Template: Work Character Relationship Diagram Poster

📖 Description

Overall a large image, multiple character cards arranged in a relationship network, connecting lines distinguishing different relationship types, with legend and title.

📝 Prompt

```json
{
  "type": "Work Character Relationship Diagram Poster",
  "goal": "Generate a high-finish character relationship diagram usable as educational / fan / beginner guide poster",
  "ip": {
    "name": "{argument name=\"ip name\" default=\"Demon Slayer\"}",
    "tone": "{argument name=\"ip tone\" default=\"faithful to original style + poster design feel\"}"
  },
  "characters": {
    "count": "{argument name=\"character count\" default=\"9\"}",
    "auto_select": "{argument name=\"auto select\" default=\"true\"}",
    "rule": "if auto_select is true, auto-select 6-12 most representative characters based on the theme",
    "user_list": "{argument name=\"user list\" default=\"\"}",
    "card_design": {
      "components": ["avatar", "name", "faction / identity label"],
      "shape": "{argument name=\"card shape\" default=\"rounded square\"}"
    }
  },
  "composition": {
    "structure": "{argument name=\"composition\" default=\"main character center + companions left and right + rivals at the far ends\"}",
    "hierarchy": "main character card largest, important supporting characters medium, minor characters smallest"
  },
  "relationships": {
    "types": [
      {"name": "blood relation", "color": "dark red", "line": "solid"},
      {"name": "friendship / companion", "color": "warm orange", "line": "solid"},
      {"name": "mentor-student", "color": "gold", "line": "double solid"},
      {"name": "rivalry", "color": "dark purple", "line": "zigzag"},
      {"name": "secret crush", "color": "pink", "line": "dashed"},
      {"name": "alliance", "color": "green", "line": "thick solid"}
    ],
    "annotation_rule": "brief relationship text labeled at the midpoint of each line"
  },
  "title_block": {
    "main_title": "{argument name=\"main title\" default=\"Demon Slayer · Character Relationship Diagram\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"One-Image Beginner Guide\"}",
    "position": "top"
  },
  "legend": {
    "enabled": "{argument name=\"legend enabled\" default=\"true\"}",
    "position": "{argument name=\"legend position\" default=\"bottom right corner\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"character avatars faithful to original work style + modern poster layout\"}",
    "color_palette": "{argument name=\"color palette\" default=\"reference original work main colors\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "main character visually largest",
      "relationship lines not crossing chaotically",
      "each character name clearly readable",
      "legend strictly corresponding to relationship types"
    ],
    "avoid": [
      "information overload (>15 characters)",
      "line types > 6",
      "colors exceeding 8",
      "cheap flowchart feel"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, character count
- Can default: relationship types, layout, legend, style
- Can randomize: background texture

### Auto-Complete Strategy

- When user provides a theme: auto-select representative characters + auto-determine relationship types
- Default main character center composition
- Default 6 relationship types, simplified as needed

## Variant 1: Organization / Team Structure Diagram

📝 Prompt

```json
{
  "type": "Organization / Team Structure Diagram",
  "ip": {
    "name": "{argument name=\"organization\" default=\"An AI Startup\"}",
    "tone": "modern corporate poster"
  },
  "composition": {
    "structure": "pyramid: CEO at top + executives in middle + regular employees at bottom"
  },
  "relationships": {
    "types": [
      {"name": "reporting", "color": "gray", "line": "solid"},
      {"name": "collaboration", "color": "blue", "line": "dashed"}
    ]
  },
  "constraints": {
    "must_feel": "professional + publishable"
  }
}
```

## Variant 2: Historical Event Participant Diagram

📝 Prompt

```json
{
  "type": "Historical Event Participant Relationship Diagram",
  "ip": {
    "name": "{argument name=\"event\" default=\"Battle of Red Cliffs, Three Kingdoms\"}",
    "tone": "historical illustration + poster design"
  },
  "composition": {
    "structure": "three factions opposing: Cao Cao / Sun Quan / Liu Bei"
  },
  "constraints": {
    "must_feel": "both textbook and poster quality"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Character Relationship Diagram Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides a theme (work / organization / event), auto-select characters + relationships + style + legend",
  "constraints": {
    "must_feel": "one-image beginner guide quality"
  }
}
```

## Things to Avoid

- Do not exceed 15 characters
- Do not exceed 6 line types
- Do not let all lines cross into a tangled web (must have clear reading order)
- Do not simply copy official poster layout
- Do not make label font size smaller than character names
- Do not omit the legend