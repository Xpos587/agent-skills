# JSON Prompt Template Master Specification

This file is the master methodology document for the `gpt-image-2` skill's template system. All subsequent specific template files should follow the rules defined here.

It does not provide a complete template for any specific visual scenario; instead, it defines:

- How templates should be organized
- How fields should be designed
- How parameters are classified as "required / default / random"
- How to ask about missing information
- How to extract reusable structured JSON templates from reference cases

---

# 1. When to Use JSON Templates

Prefer JSON templates over writing a single block of natural language prompt when any of the following conditions are met:

1. The image has many elements
2. The image contains multiple functional areas
3. The image requires UI / product cards / comment sections / legends / annotations / headers and footers or similar structures
4. Multiple variants need to be supported
5. Three modes need to be supported: "user-specified / default / randomly generated"
6. The prompt is likely to be reused, expanded, or debugged later

Typical applicable scenarios:

- E-commerce livestream UI mockups
- Product exploded view posters
- Hand-drawn city maps
- Explanatory slides
- High information-density diagrams

Scenarios where JSON templates are NOT necessary:

- Very simple single-subject images
- No complex layout or multi-area structure
- The user just wants to quickly try a lightweight visual direction

---

# 2. references Directory Rules

The `references/` directory must follow this structure:

- Level 1: category directories
- Level 2: single-template Markdown files

For example:

```text
references/
  ui-mockups/
    live-commerce-ui.md
    social-interface-mockup.md
  product-visuals/
    exploded-view-poster.md
```

Do NOT use:

- One large file per broad category
- One file per source
- One flat file per case without categorization

Benefits of the directory tree structure:

- Precise reading
- Easy to extend
- Templates do not pollute each other
- Each template file can be written comprehensively

---

# 3. Standard Structure for a Single Template File

Each specific template file should follow this structure:

```markdown
# Template Name

## Scope

## When to Use

## Missing Information Priority Question Order

## Main Template

📖 Description

📝 Prompt
```json
{ ... }
```

### Parameter Strategy

### Auto-Completion Strategy

### Variant Methods

## Variant 1

## Variant 2

## Things to Avoid
```

Notes:

- The `Main Template` must come first
- Variant templates build upon the main template
- Parameter strategy, auto-completion strategy, and things to avoid must not be omitted

---

# 4. Recommended JSON Template Skeleton

Most templates should start from the following skeleton:

```json
{
  "type": "template type",
  "goal": "image purpose",
  "subject": {},
  "scene": {},
  "layout": {},
  "style": {},
  "details": {},
  "constraints": {}
}
```

## Field Responsibilities

### `type`

Template type name, for example:

- Livestream UI mockup
- Product exploded view poster
- Hand-drawn map infographic

### `goal`

Describes what the image is ultimately for, for example:

- E-commerce livestream screenshot mockup
- Brand hero visual poster
- Travel guide map
- High information-density explanatory diagram

### `subject`

Primary content, for example:

- Person
- Product
- City
- Character
- Illustration protagonist

### `scene`

Setting, background, environment, atmosphere.

### `layout`

Image area organization method, applicable to:

- Posters
- UI
- Maps
- slides
- Multi-area structural diagrams

### `style`

Style, rendering, material, color tendency, lighting.

### `details`

Used to hold local details, for example:

- Product selling points
- callout labels
- Comment content
- Legend elements
- Footer copy

### `constraints`

Used to specify:

- What must appear
- What must be avoided
- What the final result should resemble, and what it should not resemble

---

# 5. Scene-Specific Field Recommendations

Different categories can extend different structures.

## 5.1 UI Mockups

Recommended additional fields:

```json
{
  "ui_overlay": {
    "top_header": {},
    "chat_area": {},
    "gift_area": {},
    "product_card": {},
    "bottom_bar": {}
  }
}
```

## 5.2 Product Visuals

Recommended additional fields:

```json
{
  "header": {},
  "centerpiece": {},
  "callout_labels": {},
  "footer": {},
  "component_layers": []
}
```

## 5.3 Maps & Infographics

Recommended additional fields:

```json
{
  "title_section": {},
  "sections": [],
  "legend": {},
  "centerpiece": {},
  "extras": {}
}
```

## 5.4 Slides & Visual Docs

Recommended additional fields:

```json
{
  "page_type": "",
  "information_density": "",
  "headline_system": {},
  "visual_blocks": [],
  "annotation_style": {}
}
```

## 5.5 Storyboards & Sequences (Cinematic storyboards / TVC / Process boards / Comics)

Applicable to visuals that output multiple panels in an NxM grid for "the same narrative / the same process / the same set of actions." Subcategories differ significantly in fields, so field recommendations are given per subcategory:

### 5.5.1 Cinematic Storyboards for Film / Shorts (e.g., `cinematic-storyboard-grid.md`)

```json
{
  "subject": { "primary": "", "secondary": "", "mood": "", "style": "", "aspect_ratio_per_panel": "" },
  "vehicle_or_actor": { "design": "", "scale": "" },
  "layout": {
    "grid": { "rows": 0, "columns": 0, "count": 0 },
    "sheet_aspect_ratio": "",
    "panel_borders": "",
    "sections": [{ "position": "row x col y", "description": "" }],
    "continuity": "(required) explicitly state N panels are continuous narrative / same hero / same mood"
  },
  "lighting": { "primary": "", "secondary": "", "accents": "" },
  "environment": { "location": "", "weather": "", "threat": "" }
}
```

Field experience:

- `sections` must be an array, **strictly list each shot in row-major order** (do not let the model arrange freely)
- `continuity` is a key field for this subcategory, **required**
- Each shot description should include the three elements: "shot type + subject action + lighting/mood"
- Mix wide / medium / close-up / POV shots; do not use all close-ups or all wide shots

### 5.5.2 Commercial TVC Storyboards (e.g., `product-tvc-storyboard.md`)

```json
{
  "header": { "title": "", "subtitle_meta": "", "product_name_subtitle": "" },
  "layout": { "grid": { "rows": 0, "columns": 0, "panel_count": 0, "panel_aspect_ratio": "" } },
  "scenes": {
    "count": 0,
    "items": [{ "id": 1, "title_zh": "", "timestamp": "0-2s", "description": "" }]
  }
}
```

Field experience:

- Compared to cinematic storyboards, must have `header.product_name_subtitle` + per-shot `timestamp` (advertising hard constraint)
- Each shot's `title_zh` is a Chinese subtitle for the client (e.g., "Environment Setup," "Hero Close-up," "Person + Product Frame")
- `description` must **explicitly include the product**, and the product's appearance must be consistent across all shots

### 5.5.3 Live-Action / Character Cinematic Process Boards (e.g., `process-photo-board.md`)

```json
{
  "subject": {
    "character": { "gender": "", "age": "", "identity": "", "hair": "", "undersuit": "", "armor_or_outfit": "", "helmet_or_headpiece": "" },
    "environment": { "location": "", "background_elements": "" }
  },
  "layout": {
    "header": { "count": 2, "labels": ["title", "subtitle"], "design": "" },
    "sections": [{ "step_id": 1, "title": "", "position": "", "labels": [], "image": "" }],
    "footer": { "count": 1, "labels": ["slogan"], "design": "" },
    "grid": { "rows": 0, "columns": 0, "panel_count": 0, "panel_borders": "", "number_badges": "" }
  },
  "text_rendering": { "language": "", "font": "", "colors": "" }
}
```

Field experience:

- **Character consistency** relies on isolating all fixed attributes (gender / hair / undersuit) into the `subject.character` field
- **State progression** relies on each step's `image` field explicitly describing "what is currently worn / what is being done at this point"
- Must have a `number_badges` field (step numbers visually identifiable at a glance)
- Title language (Chinese / Japanese / English) is explicitly declared via `text_rendering.language`

## 5.6 Catalog / Lineup / Character-Variant Poster (Multi-card infographic posters)

Applicable to visuals where "the same base (character / product / concept) has multiple variants displayed side by side in a single poster." Subcategories:

### 5.6.1 Same Character, Multiple Versions Poster (e.g., `character-catalog-poster.md`)

```json
{
  "subject_overview": "(required) overall poster theme, e.g. 'Zodiac Women Catalog'",
  "language": "",
  "format": "vertical poster",
  "style": { "overall": "", "rendering": "", "mood": "" },
  "layout": {
    "sections_count": 0,
    "sections": [{
      "title": "",
      "position": "",
      "theme_color": "(required) this panel's theme color, must differ across panels",
      "symbol": "",
      "constellation": "",
      "labels": [],
      "character": { "pose": "", "outfit": "", "background": "" }
    }]
  }
}
```

Field experience:

- Each section must have its own `theme_color` + `symbol` + `motif`, otherwise the model will paint them as the same image
- The `character` subfield preserves the same base (face shape / body type / hair color), varying only outfit / pose / background
- `subject_overview` is the key prompt for the model to understand "why these panels should be placed together"

### 5.6.2 Product Lineup Comparison Poster (e.g., `lineup-comparison-poster.md`)

```json
{
  "subject": "(required) one-line description including 'lineup chart / catalog board / comparison poster'",
  "branding": { "headline": "", "signature": "", "seals": [] },
  "palette": { "background": "", "highlights": [] },
  "layout": {
    "header": { "elements": [{ "type": "legend", "title": "", "labels": [] }] },
    "sections": [{ "title": "row N tier name", "labels": [] }]
  },
  "content_grid": "explicitly state N SKUs per row + what each SKU card looks like",
  "visual_details": "material / reflection / print / accessories that differentiate SKUs"
}
```

Field experience:

- Must have `legend` type elements (tier key / icon key / style key), otherwise the poster's "comparison" meaning disappears
- The `content_grid` field must explicitly state "N SKUs per row + intra-row sort logic (by price / by color / by year)"
- SKU count is typically 12 - 36; too few doesn't look like a lineup, too many causes each to be painted poorly

## 5.7 Day-trip Itinerary Map (Left itinerary card + Right illustrated map split poster)

Applicable to "day-trip split posters" (e.g., `itinerary-day-trip-map.md`):

```json
{
  "destination": { "name": "", "duration": "1 day", "theme": "" },
  "headline": { "main": "", "tagline": "", "divider": "" },
  "style": { "overall": "", "left_panel_look": "", "right_panel_look": "", "color_palette": "", "atmosphere": "" },
  "layout": {
    "format": "vertical 2:3 poster, split into two equal vertical columns",
    "left_panel": { "type": "itinerary card", "header": [], "stop_count": 5, "stop_design": [], "border": "" },
    "right_panel": { "type": "painted map scene", "background": "", "path": "", "marker_design": "", "compass_rose": "", "stats_box": "" },
    "alignment_rule": "(required) left-right numbers / names / order must strictly align"
  },
  "stops": {
    "count": 5,
    "items": [{ "number": 1, "name": "", "time": "", "description": "", "left_vignette": "", "right_scene": "" }]
  },
  "footer_box": { "compass_rose": "", "stats_box": { "design": "", "stats": [] } }
}
```

Field experience:

- `alignment_rule` is **required**, otherwise the left and right columns can easily become misaligned
- Each stop provides both `left_vignette` (card small illustration) + `right_scene` (map large scene) dual visual
- `stops.count` is recommended at 5-7; too few doesn't feel like an itinerary, too many won't fit on the card
- `language` defaults to the destination's official language (Taiwan -> Traditional Chinese, Kyoto -> Japanese)

## 5.8 Multi-Grid Ad Banner Set (Multi-industry mixed ad banner grid)

Applicable to "one image simultaneously displaying N independent industry / theme banners" (e.g., `ad-banner-multi-grid.md`):

```json
{
  "language": "",
  "layout": {
    "structure": "2x2 / 3x3 grid of equal quadrants",
    "gutter": "",
    "overall_aspect_ratio": "",
    "panel_aspect_ratio": "",
    "quadrants": [{
      "position": "top-left",
      "theme": "(required) this quadrant's industry / theme, e.g. 'Travel' / 'Skincare'",
      "subject": "",
      "elements": [],
      "text_labels": [],
      "style": "(required) this quadrant's visual style, must differ from other quadrants"
    }]
  },
  "global_style": "unifying elements across all quadrants (e.g. consistent font / border)",
  "constraints": { "must_keep": ["each quadrant is independent, no narrative connection"] }
}
```

Field experience:

- The `quadrants` array is **required**; each cell must independently specify `theme` + `style`
- `global_style` is used for "visual unity" (e.g., unified font), but do NOT let all cells share the same subject
- Difference from `cinematic-storyboard-grid`: this template **emphasizes no narrative connection between panels**; each cell is an independent piece
- Difference from `banner-grid-2x2` (existing): this template is **multi-industry / multi-theme**, while the existing one is same-brand multiple creatives

## 5.9 Full Brand / Mascot Doc (18+ module large brand identity full-process document)

Applicable to "one image overview of the entire brand / mascot from DNA to execution" (e.g., `full-mascot-brand-doc.md`):

```json
{
  "brand": { "name": "", "industry": "", "primary_colors": [], "voice": "" },
  "character": { "description": "", "rendering_style": "" },
  "layout": {
    "grid": "3 columns by 6 rows",
    "panel_count": 18,
    "sections": [
      { "id": "01", "title": "01 BRAND DNA ANALYSIS", "elements": [] },
      { "id": "02", "title": "02 CONCEPT MOODBOARD", "elements": [] }
    ]
  }
}
```

Field experience:

- The `sections` array **explicitly lists 18 modules**, each with its own `id` + `title` + `elements`
- Module `id` uses double-digit numbering (01-18), making it easy to create a visual "table of contents" feel
- Each module's `elements` must explicitly list "what to draw in this cell" (sketch / 3D / color palette / application scenario)
- Difference from `mascot-brand-kit` (existing): this template is a **full-process document** (18-24 cells), while the existing one is a **simplified kit** (6-9 cells)

---

# 6. Parameter Design Rules

For each template field, determine which of the following categories it belongs to.

## 6.1 Core Parameters (Ask First)

When missing, these significantly affect the result; ask the user first.

Common examples:

- Who is the subject
- What is the product name
- What is the city name
- What is the theme
- Is it a real photo or a text description
- What is the platform style

## 6.2 Defaultable Parameters

When missing, a default value can be used without affecting the template's normal operation.

Common examples:

- Background color
- Secondary button copy
- General decorative elements
- General lighting terms
- Conventional color tendencies

## 6.3 Randomizable Parameters

Auto-completion is allowed, but must be reasonably generated within the style range.

Common examples:

- bystander nicknames
- secondary chat messages
- gift notifications
- small decorative elements
- secondary background content

---

# 7. Parameter Notation Convention

Variables uniformly use the following format:

```text
{argument name="host name" default="Elon Musk"}
```

Recommended rules:

- `name`: concise and clear
- `default`: provide a working default value
- If a field will frequently need randomization later, still provide a reasonable default value first

Do NOT use:

- Vague parameter names
- No default value but also not a required field

---

# 8. Missing Information Questioning Strategy

## 8.1 General Principle

Questions must be:

- Precise
- Few
- Focused on template key fields
- Not broadly or vaguely asked

## 8.2 General Priority

It is recommended to judge whether to ask in the following order:

1. What is the subject source
2. What is the image purpose
3. What is the core object / product / theme
4. Whether auto-completion of missing information is allowed
5. Whether there are elements that must be preserved or must be avoided

## 8.3 Livestream UI Example

Do NOT ask:

- "What feeling do you want to achieve?"

Ask first:

- Who is the livestreamer?
- Use a real photo, celebrity name, character description, or random generation?
- What is the product name?
- Is the product price specified?
- May I auto-complete comments and gift content?

## 8.4 Film / TVC Storyboard Example

Do NOT ask:

- "What story do you want?"

Ask first:

- One-sentence story: who + where + what happens + what is the ending?
- What is the genre? (sci-fi / disaster / combat / romance / thriller / film noir)
- Number of shots? (9 / 12 / 16) + grid (3x3 / 3x4 / 4x4)
- Emotional arc: rise -> escalation -> climax -> fall / consistently tense / calm then burst?
- Style: photoreal / oil painting / anime cinematic / black & white / vintage film?
- (TVC specific) What is the product? Brand name / selling point / duration / aspect ratio?

## 8.5 Process Board / Equipment Donning / Tutorial Board Example

Do NOT ask:

- "How many images do you want to make?"

Ask first:

- What is the process theme? (equipment / makeup / operation / training / maintenance)
- Who is the protagonist? (gender / age / key identifying features / whether face privacy protection is needed)
- Number of steps? (4 / 6 / 8 / 9) + grid
- For each step: "title + brief description + current equipment state / action at this point"
- Style: cinematic live-action / fashion editorial / tokusatsu special effects / workshop documentary?
- Text language (language used for titles / description fields)?

## 8.6 Character Multi-Version Catalog Poster Example (catalog character poster)

Do NOT ask:

- "What character do you want to draw?"

Ask first:

- What is the overall theme? (twelve zodiac / five elements / dynasties / personality types / solar terms)
- How many versions total? (3 / 5 / 6 / 12)
- For each version: "name + theme color + outfit / prop / background"
- Same character base (face shape / body type / hair color) — what stays constant?
- Style: anime / Chinese gongbi / chibi / realistic?

## 8.7 Product Lineup Comparison Poster Example

Do NOT ask:

- "What kind of poster do you want to make?"

Ask first:

- What is the brand / product line name?
- How many SKUs total? (recommended 12-36)
- Sorted by what dimension? (tier / series / year / price)
- Is a legend needed? (tier key / icon key / style key)
- Background tone: luxury dark / vintage kraft paper / industrial minimalist?

## 8.8 Day-trip Split Poster Example

Do NOT ask:

- "Where do you want to go?"

Ask first:

- Destination (scenic area / city / national park name)?
- Title copy + text language (Chinese / Japanese / English)?
- Number of stops (5-7) + per stop "name + time + one-sentence description + small illustration + large scene"?
- Overall route theme (nature / history / food / photography / pilgrimage)?
- Style: vintage illustration / national park poster / watercolor Japanese / Art Nouveau?
- Footer stats (total distance / steps / estimated time)?

---

# 9. Auto-Completion Strategy

When the user explicitly states:

- "Fill it in for me"
- "Generate it randomly"
- "Give me a demo first"

Then it is permitted to:

1. Ask only the 1-2 most critical questions
2. Use default values for the remaining fields
3. Or reasonably generate values for randomizable fields

Auto-completion must satisfy:

- Does not break subject consistency
- Does not conflict with user-specified information
- Does not create overly absurd secondary elements

---

# 10. Relationship Between Main Template and Variant Templates

Each template file must have at least:

1. One main template
2. Several variant templates (optional but recommended)

## Main Template

Should satisfy:

- Most general
- Most reusable
- Covers most use cases

## Variant Templates

Common variants:

- User provides reference photo version
- User provides celebrity name version
- User provides text description version
- Auto-completion version
- Platform style version
- Commercially enhanced version

Variants should not completely diverge from the main template; they should adjust a small number of fields on top of the main template structure.

---

# 11. Steps for Extracting Templates from Reference Cases

Reference case sources are currently mainly:

- `<skill-dir>/100+GPT-Image2-prompts.md`

When extracting templates in the future, strictly follow these steps:

## Step 1: Determine the Category First

Assign the case to the correct first-level directory (consistent with the `SKILL.md` template index):

- ui-mockups
- product-visuals
- maps (no longer called maps-and-infographics)
- slides-and-visual-docs
- poster-and-campaigns
- portraits-and-characters
- scenes-and-illustrations
- editing-workflows
- avatars-and-profile
- storyboards-and-sequences
- grids-and-collages
- branding-and-packaging
- typography-and-text-layout
- assets-and-props
- academic-figures
- infographics
- technical-diagrams

## Step 2: Determine Whether It Is a New Prototype or a Variant of an Existing Prototype

For example:

- VR headset exploded view -> new prototype
- Phone exploded view -> variant of existing prototype

## Step 3: Decompose Fields

Decompose the case into:

- Subject
- Scene
- Layout
- Style
- Copy
- Constraints

## Step 4: Mark Parameter Types

For each field, mark:

- Required
- Defaultable
- Randomizable

## Step 5: Write the Main Template First

Do not write 4 versions at the outset. Write the most general main template first.

## Step 6: Then Add Variants

For example:

- Reference photo version
- Celebrity name version
- Text description version
- Auto-completion version

## Step 7: Add Question Order

Describe which fields should be asked about first in a real conversation.

## Step 8: Add Things to Avoid

Summarize the most common failure points for this template.

---

# 12. Template File Naming Rules

Template file names should satisfy:

- Lowercase letters
- Numbers or hyphens
- Express the topic as precisely as possible
- Do not name by source
- Do not name by sequence number

Correct examples:

- `live-commerce-ui.md`
- `exploded-view-poster.md`
- `food-map.md`

Incorrect examples:

- `template-01.md`
- `youmind-case-1.md`
- `twitter-prompt-4.md`

---

# 13. Single-File Implementation Checklist (must be followed for every new template added)

Every time a new template file is added, follow this checklist:

1. Determine the first-level category directory
2. Verify the file name is precise enough
3. Determine whether it is a new prototype or a variant of an existing prototype
4. Write `Scope`
5. Write `When to Use`
6. Write `Missing Information Priority Question Order`
7. Write the main template JSON
8. Write the parameter strategy
9. Write the auto-completion strategy
10. Write the variant methods
11. Write the things to avoid
12. If this is a new template topic, also update the `SKILL.md` index
