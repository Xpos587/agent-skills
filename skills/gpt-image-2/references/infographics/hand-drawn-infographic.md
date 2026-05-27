# Hand-Drawn Style Infographic Template

This file is used for generating "hand-drawn / notebook / doodle / warm macaron / morandi misty" texture infographics:

- Study notes / knowledge cards / concept diagrams
- WeChat / Xiaohongshu "hand-drawn recommendation" posts
- Teaching handouts / classroom doodles
- Travel journals / food journals / reading notes
- Event notices / warm-style event posters

Characteristics:

- All lines have slight wobble / irregularity (hand-drawn wobble)
- Color palette low-saturation, warm, like watercolor or colored pencils
- Lots of "whitespace + doodle decoration" between elements
- Fonts have a handwritten feel (not computer fonts)
- Color fills "leave edges", like hand-coloring

> Design judgment: Hand-drawn style is a "style language" with extremely high freedom; specific elements differ greatly across different topics (study / food / travel / mood). **Forcing JSON would constrain compositional freedom**, so this template uses a **"structured natural language prompt + parameter table + element list" hybrid format**, which is more natural than pure JSON.

## Scope

- Study notes / concept explanations / knowledge cards
- Step-by-step tutorials / how-to / operation process "hand-drawn edition"
- List / checklist / ranking "hand-drawn edition"
- Warm-style content (mood / healing / food / travel)
- WeChat / Xiaohongshu / social platform "journal style" illustrations

## When to use

- User mentions "hand-drawn / journal / sketch notes / doodle / notes / class notes / macaron / morandi / warm tones / healing"
- User wants the visual "approachable, easy to read, not like PPT"
- User wants "readers feel a real person drew it by hand"

Do NOT use for:

- User wants high-density science popularization causal chain / anatomy diagram → use `infographics/legend-heavy-infographic.md`
- User wants modular bento grid → use `infographics/bento-grid-infographic.md`
- User wants engineering-precision flowcharts / architecture diagrams → use `technical-diagrams/`
- User wants publication-grade charts → use `academic-figures/publication-chart.md`
- User wants genuine healing scene illustrations → use `scenes-and-illustrations/healing-scene.md`

## Missing Information Priority Question Order

1. Topic (what to talk about? e.g. "5 ways to brew coffee", "Pomodoro Technique", "Shanghai City Walk Top 10")
2. Number of information items (recommend 3-7 items)
3. Color palette (macaron warm cream / morandi misty / kraft brown paper / chalkboard)
4. Whether to include a character / mascot (a cat / stick figure person / no character)
5. Aspect ratio (Xiaohongshu 3:4 portrait / WeChat 16:9 landscape / 1:1 square)
6. Whether to use colored "item zones" or "free-form layout"

## Main Template: Hand-Drawn Style Infographic

Description

The entire image is an infographic "like someone drew it in their notebook": warm background + hand-lettered large title + 3-7 hand-drawn cards / circles / bubbles + stick-figure icons + doodle decorations + hand-drawn arrow connections.

Prompt (Structured Natural Language Template)

```
A hand-drawn educational infographic in the style of a high-quality bullet journal page.

Topic: {argument name="topic" default="5 Core Steps of the Pomodoro Technique"}.

Aspect ratio: {argument name="aspect_ratio" default="3:4 portrait"}.

Background:
- Warm {argument name="background_color" default="cream / off-white"} paper texture with subtle grain.
- Optional washi-tape strips in the corners (diagonal stripes, muted tones).
- DO NOT use pure white or pure black background.

Color palette:
- {argument name="palette" default="macaron"} — describe colors:
  - macaron: warm cream #F5F0E8 background, muted blue #A8D8EA, lavender #D5C6E0, mint #B5E5CF, peach #F8D5C4, coral red #E8655A accent
  - morandi: dusty sage, terracotta, mustard, taupe, soft brick
  - kraft: kraft paper background, dark brown ink, tomato red accent, muted navy
  - chalkboard: dark slate background, white chalk, yellow / coral / mint chalk highlights
- Limit to 4-5 colors total. Use the accent color sparingly for emphasis.

Title:
- "{argument name="title" default="Pomodoro Technique in 5 Steps"}" in large hand-lettered calligraphy at the top.
- Title sits inside a hand-drawn frame: irregular oval, scalloped rectangle, or wavy banner.
- Optional subtitle below in smaller handwritten print.

Body:
- {argument name="item_count" default="5"} information items.
- Each item is presented as a hand-drawn card / rounded rectangle / cloud bubble / circle, with:
  - A number badge (1, 2, 3 ... in a circle, drawn by hand)
  - Item title in bold handwritten text
  - 1-2 lines of body text in neat handwritten print
  - A simple doodle icon (1-2 strokes, NOT realistic) representing the item
- Items can be arranged: vertical list / 2-column grid / circular wheel / winding path.

Doodle decorations (sprinkle naturally, not symmetrically):
- Tiny stars, sparkles, hearts, arrows-curvy, dotted lines, exclamation marks
- Hand-drawn underlines and circle-marks for emphasis on key words
- Smiley / frowny faces as quality indicators where relevant
- Optional: a single mascot character (a cat / a stick-figure person / a coffee cup with face) as the "narrator"

Style enforcement:
- ALL lines have visible hand-drawn wobble — never perfectly straight
- ALL color fills leave a tiny gap before the outline (hand-painted feel)
- All text is hand-lettered — NO computer fonts, NO Helvetica, NO Arial
- Slight imperfection is intentional — it should NOT look digitally precise
- The whole image feels like a single page from someone's notebook

Composition:
- Generous whitespace (~30-40% of the canvas)
- Information hierarchy: title > item titles > body > doodle decorations
- Items are large enough to be readable; do not cram

Language: {argument name="language" default="Chinese (hand-lettered feel)"}; technical / proper nouns can stay in English.
```

### Parameter Strategy

- **Must ask**: `topic`, `item_count`, `aspect_ratio`
- **Can default**: `palette` (default macaron), `background_color` (follows palette), `language` (default Chinese)
- **Can randomize**: whether mascot appears / what mascot, doodle decoration specific shapes, card shapes (rounded rectangle / cloud / circle)

### Auto-Fill Strategy

- User only provides `topic`:
  - Auto-decide 5 key points (unless the topic is clearly a list type, e.g. "7 habits" then use 7 items)
  - Auto-use macaron color palette
  - Auto-use 3:4 portrait (Xiaohongshu-friendly)
  - No mascot (unless topic suits it, e.g. "5 steps for cat care" naturally includes a cat)
- User says "I want Xiaohongshu style" → palette auto-selects macaron or morandi, aspect 3:4
- User says "teaching / classroom" → palette auto-selects chalkboard or macaron
- User says "warm / food / healing" → palette auto-selects morandi or kraft

## Variant 1: Chalkboard Chalk-Style Hand-Drawn Infographic

Swap the palette in the above prompt to `chalkboard`:

```
Background: dark slate / chalkboard green (#2F4F4F) with faint chalk dust texture.
Lines and text: white chalk with visible pressure variation.
Highlights: yellow chalk for important keywords, coral / mint chalk for accents.
Decorations: hand-erased smudges in the background, chalk arrows, chalk underlines.
```

Suitable for: teaching handouts, classroom culture walls, knowledge popularization "classroom" feel.

## Variant 2: Kraft Paper / Kraft Warm-Style Hand-Drawn Infographic

Swap the background to `kraft paper`:

```
Background: warm kraft paper #C9A876 with visible paper fibers.
Lines and text: dark espresso brown #3E2723 with hand-drawn wobble.
Accents: tomato red #E63946, muted teal #457B9D.
Decorations: stamp marks, dotted borders, thread / yarn doodles, postal style elements.
```

Suitable for: vintage journals, coffee / baking / slow living, creative merchandise.

## Variant 3: Monochrome Pencil / Minimalist Hand-Drawn Infographic

```
Background: pure cream #FAF7F2.
Lines: single dark color (charcoal #2B2B2B or sepia #6B4423) only.
NO multi-color fills. Use varying line weight and cross-hatching for shading.
Decorations: minimal — just dotted lines and small symbols.
```

Suitable for: restrained / literary / serious content that still wants hand-drawn feel (philosophy, reading notes).

## Things to Avoid

- Any element having perfect geometric shapes / straight lines → loses hand-drawn soul
- Using Helvetica / Arial / Source Han Sans and other computer fonts → immediately feels plastic
- Color fills reaching all the way to the edge with no gap → looks like electronic stickers, not hand-drawn
- Gradients / shadows / glass textures / metallic textures → completely off-track
- >= 6 main colors on one image → loses journal's restrained feel
- Text line spacing too tight / identical font sizes → loses hierarchy
- Too many decorations to the point of overwhelming → information becomes unreadable
- All information cards having identical shapes (identical rounded rectangles x5) → loses hand-drawn organic feel