# Recipe / Process Step Diagram Template

This file is used for "step-by-step visual display of a process":

- Recipe / cooking step diagrams
- Product usage step diagrams
- DIY tutorial step diagrams
- Handcraft / makeup step diagrams
- Industrial process flowcharts

Features:

- Clear steps (numbered + description + illustration)
- Obvious flow direction (→ or numbered order)
- Emphasis on "one image you can follow along"
- Usually includes ingredient / tool list
- Clear visuals, moderate information density

## Scope

- Recipe / baking step diagrams
- Product usage / installation tutorial diagrams
- Handcraft / DIY tutorial diagrams
- Makeup / skincare step diagrams

## When to Use

- User mentions "step diagram / flowchart / recipe diagram / tutorial diagram / how-to"
- User wants "follow along just by looking at the image"

Do NOT use for:

- Educational diagrams (use `slides-and-visual-docs/educational-diagram-slide.md`)
- High-density infographics (use `infographics/legend-heavy-infographic.md`)
- Character relationship diagrams (use `character-relationship-diagram.md`)

## Missing Information Priority Question Order

1. Theme (what recipe / what tutorial)
2. Step count (4-8 steps)
3. Whether ingredient / tool list is needed
4. Style: hand-drawn watercolor / skeuomorphic 3D / flat cartoon / real photography
5. Whether bilingual / includes English
6. Aspect ratio

## Main Template: Recipe Step Diagram

📖 Description

Overall a single image, top has dish name + ingredient list, main body has 4-6 numbered step illustrations, bottom has the final dish image.

📝 Prompt

```json
{
  "type": "Recipe Step Diagram",
  "goal": "Generate a recipe step diagram usable as social media / Xiaohongshu / recipe book page",
  "recipe": {
    "name": "{argument name=\"recipe name\" default=\"Tomato Scrambled Eggs\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"5-minute home-style version\"}",
    "servings": "{argument name=\"servings\" default=\"2 servings\"}",
    "time": "{argument name=\"time\" default=\"5 minutes\"}"
  },
  "ingredients": {
    "enabled": "{argument name=\"ingredients enabled\" default=\"true\"}",
    "position": "{argument name=\"ingredients position\" default=\"top right\"}",
    "items": [
      "{argument name=\"ing 1\" default=\"2 tomatoes\"}",
      "{argument name=\"ing 2\" default=\"3 eggs\"}",
      "{argument name=\"ing 3\" default=\"scallions to taste\"}",
      "{argument name=\"ing 4\" default=\"salt / sugar / oil to taste\"}"
    ],
    "design": "each item with a small icon"
  },
  "steps": {
    "count": "{argument name=\"step count\" default=\"5\"}",
    "items": [
      {"id": 1, "scene": "{argument name=\"step 1\" default=\"Cut tomatoes into pieces, beat eggs\"}"},
      {"id": 2, "scene": "{argument name=\"step 2\" default=\"Heat oil, add eggs, scramble until half-cooked, set aside\"}"},
      {"id": 3, "scene": "{argument name=\"step 3\" default=\"Add oil, add tomatoes, cook until juices release\"}"},
      {"id": 4, "scene": "{argument name=\"step 4\" default=\"Return eggs to pan, add salt and a little sugar\"}"},
      {"id": 5, "scene": "{argument name=\"step 5\" default=\"Stir-fry evenly, sprinkle scallions, serve\"}"}
    ],
    "step_block_style": "number + illustration + 1 sentence description"
  },
  "final_dish": {
    "enabled": "{argument name=\"final dish enabled\" default=\"true\"}",
    "position": "{argument name=\"final dish position\" default=\"bottom center large image\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"hand-drawn watercolor + cream paper texture\"}",
    "color_palette": "{argument name=\"color palette\" default=\"tomato red + egg yolk yellow + cream white\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "step numbering continuous and clear",
      "each step illustration matches its description",
      "ingredient list corresponds to steps",
      "final dish image visually striking"
    ],
    "avoid": [
      "step descriptions exceeding 15 characters",
      "illustrations disconnected from text",
      "non-food natural colors in palette",
      "multiple font types"
    ]
  }
}
```

### Parameter Strategy

- Must ask: dish name, step count
- Can default: style, color scheme, ingredient presentation
- Can randomize: background texture

### Auto-Complete Strategy

- When user only provides dish name: auto-list ingredients + auto-expand 4-6 steps
- Default hand-drawn watercolor
- Step descriptions ≤ 15 characters per step

## Variant 1: Product Usage / Installation Tutorial Diagram

📝 Prompt

```json
{
  "type": "Product Usage / Installation Tutorial Diagram",
  "recipe": {
    "name": "{argument name=\"product\" default=\"AURORA Pro Earbuds Pairing\"}"
  },
  "ingredients": { "enabled": false },
  "steps": {
    "count": 4,
    "items": [
      {"id": 1, "scene": "Open the charging case"},
      {"id": 2, "scene": "Turn on phone Bluetooth"},
      {"id": 3, "scene": "Select 'AURORA Pro'"},
      {"id": 4, "scene": "Hear the confirmation tone, pairing successful"}
    ]
  },
  "final_dish": { "enabled": false },
  "style": {
    "art_style": "flat vector + brand colors"
  },
  "constraints": {
    "must_feel": "manual-level clarity"
  }
}
```

## Variant 2: Makeup / Skincare Step Diagram

📝 Prompt

```json
{
  "type": "Makeup / Skincare Step Diagram",
  "recipe": {
    "name": "{argument name=\"routine\" default=\"Morning Skincare 5 Steps\"}"
  },
  "steps": {
    "count": 5,
    "items": [
      {"id": 1, "scene": "Cleanser"},
      {"id": 2, "scene": "Toner"},
      {"id": 3, "scene": "Serum"},
      {"id": 4, "scene": "Moisturizer"},
      {"id": 5, "scene": "Sunscreen"}
    ]
  },
  "style": {
    "art_style": "minimalist illustration + soft pink"
  },
  "constraints": {
    "must_feel": "clean, feminine, shareable"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Process Flowchart Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides theme, auto-decide step count, ingredients / tools, style, color scheme",
  "constraints": {
    "must_feel": "ready to post on social media / Xiaohongshu"
  }
}
```

## Things to Avoid

- Do not exceed 8 steps (attention will break)
- Do not let single step descriptions exceed 15 characters
- Do not let illustrations be inconsistent with their descriptions
- Do not let the color palette disconnect from the theme (food images should not have neon blue)
- Do not miss numbering / skip steps
- Do not let the ingredient list overpower the image