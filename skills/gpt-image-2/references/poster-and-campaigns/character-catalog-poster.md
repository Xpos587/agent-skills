# Character Catalog / Series Card Infographic Poster Template

This file is used to generate "infographic posters where one base character / base series object splits into N variants (zodiac / element / dynasty / personality / season), each variant with its own panel + personalized copy + decorative theme."

Typical uses:

- 12 zodiac series card poster (3 per image, 4 elemental posters total)
- MBTI 16 personality visual poster
- Dynasty / mythology / ethnic series portraits
- "Same model, different styling" series photo promotional image
- Solar term / month / season series poster
- Character multi-angle personality profile

Features:

- **Same base character** reused across all panels (appearance traits consistent)
- **N panels** share unified border / layout / typography system
- **Each panel** has independent theme color, decorative motif, 6-8 lines of copy
- Overall feels like "one page of a character / concept dictionary"

Comparison with other templates:

| Template | Focus |
|---|---|
| `portraits-and-characters/character-sheet.md` (existing) | Single character three-view + expressions + outfits |
| `avatars-and-profile/cultural-portrait-series.md` (existing) | Dynasty / ethnic / literary series portraits (focus on portrait itself) |
| `avatars-and-profile/character-grid-portrait.md` (existing) | n×n grid portraits (multiple professions / expressions / dynasties) |
| **This template** (new) | **Same character multi-version cards, each card with independent theme + 6-8 personality lines + decorative motif** |

## Scope

- 12 zodiac / 4 elements / MBTI / solar terms / dynasty / mythology series posters
- "Same model, different styling + personality profile" SNS share images
- IP character branch profiles
- Personality test / personality classification visual posters

## When to Use

- User mentions "zodiac / MBTI / solar terms / dynasty / personality classification poster"
- Same character needs to be split into N versions for display
- Each version needs independent copy + decorative theme
- Output should look like "one page of an illustrated guide" / "one chapter of a profile book"

Do NOT use:

- Single character multi-expression → use `portraits-and-characters/character-sheet.md`
- Dynasty / mythology portraits without personality profiles → use `avatars-and-profile/cultural-portrait-series.md`
- n×n grid portraits (without copy) → use `avatars-and-profile/character-grid-portrait.md`

## Missing Information Priority Questions

1. Series theme (12 zodiac / MBTI / dynasty / season / custom)
2. How many panels in this image (3 / 4 / 9 / 12 / 16)
3. Main character description (**realistic / anime / photorealistic / idol style**) + whether same person
4. Primary language (Chinese / English / Japanese / bilingual)
5. Overall aesthetic (**soft pastel kawaii / vintage archival / minimalist punk / classical Chinese painting / pastel editorial**)
6. Whether each panel needs independent theme color
7. Aspect ratio (default 3:4 portrait)

## Main Template: 3-Panel Same-Character Variant Card Poster (suitable for 12 zodiac by element / MBTI 4 dimensions)

📖 Description

Vertical poster with header (main title + subtitle) + 3 vertically stacked panels, each panel internally divided into left character / right copy, with independent theme color, symbol, constellation / motif.

📝 Prompt

```json
{
  "type": "{argument name=\"theme type\" default=\"Chinese zodiac-style character infographic poster\"}",
  "subject_overview": "{argument name=\"subject overview\" default=\"twelve zodiac character list, water signs edition\"}",
  "language": "{argument name=\"language\" default=\"Traditional Chinese\"}",
  "format": "vertical poster",
  "style": {
    "overall": "{argument name=\"style overall\" default=\"elegant anime-inspired character catalog with editorial infographic layout\"}",
    "rendering": "{argument name=\"rendering\" default=\"soft polished digital illustration, pastel gradients, delicate sparkles, ornamental border design\"}",
    "mood": "{argument name=\"mood\" default=\"dreamy, celestial, refined, feminine, aquatic\"}"
  },
  "canvas": {
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"2:3\"}",
    "background": "{argument name=\"background\" default=\"very light pearl white with pale blue-lavender tint, subtle texture, thin decorative frame with filigree corners and tiny stars\"}"
  },
  "header": {
    "title": "{argument name=\"headline text\" default=\"Twelve Zodiac Character List | Water Signs\"}",
    "subtitle": "{argument name=\"subtitle text\" default=\"Feeling · Intuition · Resonance\"}",
    "icons": ["small stars", "{argument name=\"top right motif\" default=\"water droplet emblem in top right\"}", "curled cloud-like line art in top left"]
  },
  "layout": {
    "sections_count": 3,
    "sections": [
      {
        "title": "{argument name=\"section 1 title\" default=\"Cancer\"}",
        "position": "top panel",
        "theme_color": "{argument name=\"section 1 color\" default=\"powder blue\"}",
        "symbol": "{argument name=\"section 1 symbol\" default=\"Cancer glyph inside circle at left\"}",
        "constellation": "{argument name=\"section 1 constellation\" default=\"Cancer constellation at upper right\"}",
        "count": 6,
        "labels": [
          "{argument name=\"section 1 line 1\" default=\"Element: Water\"}",
          "{argument name=\"section 1 line 2\" default=\"Concept: Emotional Guardian, Puts Others First\"}",
          "{argument name=\"section 1 line 3\" default=\"Personality: Gentle, Sensitive, Home-loving\"}",
          "{argument name=\"section 1 line 4\" default=\"Action Principle: Validate Feelings First, Then Protect Loved Ones\"}",
          "{argument name=\"section 1 line 5\" default=\"Love Tendency: Warms Up Slowly, Gets Clingier the Closer\"}",
          "{argument name=\"section 1 line 6\" default=\"Social Quirk: Says It's Fine, But Remembers Everything\"}"
        ],
        "character": {
          "identity": "{argument name=\"base character\" default=\"young woman model reimagined as zodiac character\"}",
          "pose": "{argument name=\"section 1 pose\" default=\"half-body portrait, facing forward, arms gently wrapped around a large seashell pillow\"}",
          "outfit": "{argument name=\"section 1 outfit\" default=\"light blue celestial slip dress with lace trim and sheer cardigan embroidered with stars and moons\"}",
          "background": "{argument name=\"section 1 bg\" default=\"soft blue night sky with crescent moon, seashell, sparkling stars, stylized ocean wave and tiny water droplets\"}"
        }
      },
      {
        "title": "{argument name=\"section 2 title\" default=\"Scorpio\"}",
        "position": "middle panel",
        "theme_color": "{argument name=\"section 2 color\" default=\"deep violet\"}",
        "symbol": "Scorpio glyph inside circle at left",
        "constellation": "Scorpio constellation at upper right",
        "count": 6,
        "labels": [
          "Element: Water",
          "{argument name=\"section 2 line 2\" default=\"Concept: Deep-Sea Reconnaissance, Emotion Has Depth\"}",
          "{argument name=\"section 2 line 3\" default=\"Personality: Focused, Mysterious, Strong-Willed\"}",
          "{argument name=\"section 2 line 4\" default=\"Action Principle: Observe First, Then Strike Precisely\"}",
          "{argument name=\"section 2 line 5\" default=\"Love Tendency: Loves Deeply, Values Loyalty and Exclusivity\"}",
          "{argument name=\"section 2 line 6\" default=\"Social Quirk: The More They Care, the Less They Say, Secretly Testing\"}"
        ],
        "character": {
          "identity": "{argument name=\"base character\" default=\"young woman model reimagined as zodiac character\"}",
          "pose": "half-body portrait, one hand near chin in a composed enigmatic gesture",
          "outfit": "black semi-sheer dress with gothic details and a dark plum off-shoulder shawl",
          "background": "dark purple celestial sea scene with crescent moon, bubbles, stars, and curling misty water shapes"
        }
      },
      {
        "title": "{argument name=\"section 3 title\" default=\"Pisces\"}",
        "position": "bottom panel",
        "theme_color": "{argument name=\"section 3 color\" default=\"lavender\"}",
        "symbol": "Pisces glyph inside circle at left",
        "constellation": "Pisces constellation at upper right",
        "count": 6,
        "labels": [
          "Element: Water",
          "{argument name=\"section 3 line 2\" default=\"Concept: Dream Empath, Navigates by Intuition\"}",
          "{argument name=\"section 3 line 3\" default=\"Personality: Romantic, Soft, Imaginative\"}",
          "{argument name=\"section 3 line 4\" default=\"Action Principle: Feel First, Then Go With the Flow for Answers\"}",
          "{argument name=\"section 3 line 5\" default=\"Love Tendency: Falls Easily, Craves Soul-Level Companionship\"}",
          "{argument name=\"section 3 line 6\" default=\"Social Quirk: Often Absorbs Other People's Emotions as Their Own\"}"
        ],
        "character": {
          "identity": "{argument name=\"base character\" default=\"young woman model reimagined as zodiac character\"}",
          "pose": "half-body portrait, one hand lifted as if balancing floating bubbles, other hand resting at chest",
          "outfit": "translucent lavender fantasy dress with soft draped sleeves and shimmering fabric",
          "background": "pale lilac underwater-celestial blend with bubbles, sparkles, and flowing translucent wave forms"
        }
      }
    ],
    "dividers": "three horizontal framed panels with thin ornamental borders"
  },
  "footer": {
    "center_icon": "{argument name=\"footer icon\" default=\"small blue seashell emblem\"}",
    "decorations": ["tiny stars", "fine scrollwork"]
  },
  "constraints": {
    "must_keep": [
      "3 panels must use the same base character (face / body type / hairstyle base consistent)",
      "Each panel differentiated by outfit / props / background motif",
      "Text content clear and aligned (6 personality lines per panel)",
      "Overall color theme unified (e.g., water signs all use blue-violet range)",
      "Panel divider border style consistent"
    ],
    "avoid": [
      "Drawing the base character as 3 completely different people",
      "Decorative motif style drifting between panels (one realistic, one cartoon)",
      "Personality text occupying more than half the panel area",
      "Including other 9 zodiac signs / content outside the theme",
      "Using too many fonts (recommend main title + personality list + English zodiac name, 3 fonts only)"
    ]
  }
}
```

### Parameter Strategy

- **Required**: theme type (series theme), 3 section titles, base character description
- **Defaultable**: language (recommended by theme), aspect ratio, decorative motif
- **Random**: 6 personality lines per character (auto-generated by character personality)

### Auto-fill Strategy

- User provides "water signs" → auto-fill Cancer / Scorpio / Pisces + blue-violet tones + ocean motif
- User provides "fire signs" → auto-fill Aries / Leo / Sagittarius + red-orange-gold tones + flame motif
- User provides "MBTI Analyst group" → auto-fill INTJ / INTP / ENTJ / ENTP + purple + geometric motif

## Variant 1: 4-Panel Horizontal Bento Grid (suitable for 16-panel set split into 4 images)

📝 Prompt

```json
{
  "type": "4-panel character catalog poster, horizontal bento layout",
  "format_override": "horizontal poster, 16:9 or 4:3",
  "layout_override": {
    "structure": "2x2 grid, 4 equal panels",
    "use_case": "MBTI 4 dimensions (NT / NF / SJ / SP), one representative character per dimension"
  },
  "section_count": 4,
  "must_keep": ["4 panels share the same base character", "diagonal/grid balance"]
}
```

### When to choose this variant

- Making MBTI 16 types split into 4 dimensions
- 12 zodiac split into 4 elements, 3 per image → or 1 image with 4 element representatives
- Horizontal sharing channels (Twitter / Moments)

## Variant 2: 12-Panel Full Set (not recommended for single image, but if necessary)

📝 Prompt

```json
{
  "type": "12-panel full series character catalog poster",
  "section_count": 12,
  "layout_override": {
    "format": "very tall vertical poster, 1:2 or longer",
    "structure": "3 columns x 4 rows OR 4 columns x 3 rows",
    "panel_internal_layout": "much smaller per-panel: 1 character thumb + 3 short labels (not 6)"
  },
  "warning": "More panels = less detail per cell; recommend splitting into 4 elemental posters instead of 1 image with 12 panels"
}
```

### When to choose this variant

- Must output 1 image = all 12 zodiac signs / 12 solar terms
- Client accepts sacrificing per-panel detail
- Used as series overview image (not a close-reading image)

## Variant 3: Dynasty / Mythology Series Portraits (no zodiac symbols, add cultural motifs)

📝 Prompt

```json
{
  "type": "dynastic / mythological character catalog poster",
  "section_count": 3,
  "section_examples": ["Tang / Song / Ming / Qing / Republic"],
  "style_override": {
    "overall": "elegant editorial portrait series with classical Chinese motifs",
    "palette": "warm beige, antique gold, ink black, vermilion red",
    "decoration_per_panel": "corresponding dynasty patterns / clothing / architecture / artifacts"
  },
  "labels_per_panel_count": 5,
  "labels_examples": ["era", "clothing characteristics", "representative artifact", "personality keyword", "seal / signature mark"]
}
```

### When to choose this variant

- Cultural / publishing / educational history category
- Want to create "same model in different dynasties" photo series
- Don't need modern classifications like zodiac / MBTI

## Things to Avoid

- Drawing the base character as multiple different people → fatal, immediately destroys the "same character, multiple versions" core concept
- Decorative motif style drifting between panels (one realistic, one chibi)
- Stuffing 12 zodiac signs into a 3-panel poster → unreadable
- Personality text covering the character's face / occupying > 50% of area
- Panel borders / typography inconsistent → looks like 3 different posters collaged together
- Inserting off-theme elements (e.g., fire appearing in a "water signs" poster)
- Color palette ≥ 5 main colors → loses series cohesion
- One panel with 6 lines of text, another with 8, another with 4 → must be equal