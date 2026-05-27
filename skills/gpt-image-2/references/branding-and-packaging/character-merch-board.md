# Character IP x Merchandise Board Template

This file is used to generate "a composite visual board centered on a single anime / VTuber / 2D character, overlaid with brand logo + packaging + merchandise + SNS profile + promotional banner."

Typical uses:

- VTuber debut / anniversary / new project introduction image
- Doujin / personal IP launch promotional image
- Anime brand (candy / bakery / cafe / general store) store collaboration image
- Character merchandise one-image collection
- IP room lifestyle goods catalog
- Social media promotional image (one image covering character intro + product preview + SNS handle)

Characteristics (differences from other mascot / brand templates):

| Template | Main subject | Focus |
|---|---|---|
| `mascot-brand-kit.md` (existing) | Cartoon mascot | Three-view + expressions + applications |
| `full-mascot-brand-doc.md` (new) | Cartoon mascot | 18-module full-process design document |
| `brand-identity-board.md` (existing) | Abstract brand | logo + colors + fonts + application mockups |
| **This template** (new) | **Anime character / VTuber / personal IP** | **Character image + packaging + merchandise + SNS + lifestyle goods** |

## Scope

- VTuber merchandise introduction board
- Personal IP / VUP debut promotional image
- Anime brand x physical product collaboration image
- Character lifestyle / room goods collection
- Doujin convention exhibition promotional image

## When to use

- User mentions "character merchandise / VTuber debut / IP merch board / personal project image"
- Character is anime / 2D / moe style, not corporate-level mascot
- Need "one image showcasing complete IP commercial ecosystem" (character + products + SNS + packaging)

Do NOT use for:

- Corporate / restaurant brand mascot complete design document → use `full-mascot-brand-doc.md`
- Character three-view / expressions only → use `portraits-and-characters/character-sheet.md`
- Single character single poster → use `portraits-and-characters/virtual-host.md`
- Pure packaging design → use `branding-and-packaging/cosmetic-packaging.md`

## Missing Information Priority Question Order

1. Character name + one-line personality description (must ask, the soul of the image)
2. Theme color + motif (cherry blossoms / ocean / starry sky / candy / rabbit...)
3. Style base (**soft pink moe / gothic dark / cyber / Japanese traditional / fairytale**)
4. Required product categories (packaged food / stationery / apparel / home / digital accessories)
5. SNS handle (optional, adds realism to the project)
6. Whether to include store / event info (e.g. "4.26 NEW OPEN")

## Main Template 1: Anime Character Brand Identity + Merchandise Board (Case 112 Style)

Description

One large image containing header banner + packaging mockup + promotional poster + web banner + SNS profile + merchandise collection, all centered on the same character.

Prompt

```json
{
  "type": "brand identity and merchandise design board",
  "goal": "Generate a complete brand launch board centered on a single anime character, usable as character debut, anniversary project, or IP launch promotional image",
  "theme": {
    "color_palette": "{argument name=\"theme color\" default=\"pastel pink\"} and white",
    "motif": "{argument name=\"motif\" default=\"cherry blossoms\"} and pink hearts",
    "vibe": "{argument name=\"vibe\" default=\"sweet, soft, dreamy, idol-debut energy\"}"
  },
  "character": {
    "name": "{argument name=\"character name\" default=\"Yuon Chi\"}",
    "subname": "{argument name=\"character subtext\" default=\"yuonchii\"}",
    "description": "{argument name=\"character description\" default=\"anime girl with short brown bob hair, pink eyes, wearing a white hoodie, gentle smile\"}",
    "personality": "{argument name=\"personality\" default=\"healing type, gentle, loves sweets\"}"
  },
  "branding": {
    "main_logo": "{argument name=\"main logo text\" default=\"Yuon Chi\"}",
    "sub_logo": "{argument name=\"sub logo text\" default=\"yuonchii\"}",
    "social_handle": "{argument name=\"social handle\" default=\"@yuonchii\"}"
  },
  "layout": {
    "format": "single large composite board, vertical poster orientation",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait\"}",
    "background": "{argument name=\"background\" default=\"clean white with soft pink gradient corners and tiny doodles\"}",
    "sections": [
      {
        "type": "header banner",
        "position": "top",
        "elements": ["large main logo", "small sub logo beneath", "cherry blossom decorative graphics", "character portrait on the right"]
      },
      {
        "type": "product packaging",
        "position": "middle left",
        "elements": [
          "1 square box with heart-shaped transparent window showing {argument name=\"packaging filling\" default=\"pink heart candies\"} inside",
          "character illustration printed on the box front",
          "2 individual candy / product wrappers placed beside the box",
          "5 scattered {argument name=\"scattered item\" default=\"heart candies\"} around the packaging"
        ]
      },
      {
        "type": "promotional poster",
        "position": "middle right",
        "elements": [
          "character portrait centered",
          "{argument name=\"poster prop\" default=\"heart-shaped candy bowl\"}",
          "main logo at the top",
          "{argument name=\"event tag\" default=\"4.26 NEW OPEN\"} text",
          "social handle text"
        ]
      },
      {
        "type": "horizontal web banner",
        "position": "lower middle",
        "elements": ["main logo on the left", "{argument name=\"motif\" default=\"cherry blossoms\"} graphics filling the middle", "character portrait on the right", "thin tagline below"]
      },
      {
        "type": "social media profile mockup",
        "position": "bottom left",
        "elements": [
          "header / cover image with logo and motif",
          "1 circular profile picture (character close-up)",
          "handle text '{argument name=\"social handle\" default=\"@yuonchii\"}'",
          "1 follow button (filled accent color)",
          "mock bio: 2-3 lines of character introduction"
        ]
      },
      {
        "type": "merchandise collection",
        "position": "bottom right",
        "count": 9,
        "items": [
          "{argument name=\"merch 1\" default=\"1 white t-shirt with logo\"}",
          "{argument name=\"merch 2\" default=\"1 white mug with character\"}",
          "{argument name=\"merch 3\" default=\"4 round pin badges\"}",
          "{argument name=\"merch 4\" default=\"1 acrylic keychain\"}",
          "{argument name=\"merch 5\" default=\"2 candy packets\"}"
        ]
      }
    ]
  },
  "global_style": {
    "rendering": "polished anime-illustration style for the character + photorealistic product mockups for packaging / merchandise + clean editorial layout for SNS / banner",
    "typography": "main logo in cute display font; SNS / body in clean sans-serif; small handwritten accents",
    "consistency": "the same character appearance used in EVERY section without drift",
    "panel_density": "moderate; each section breathes with consistent margin"
  },
  "constraints": {
    "must_keep": [
      "Character appearance completely consistent across all sections (hairstyle / color palette / expression base)",
      "Logo / SNS handle spelling unified",
      "Each section has clear boundaries, no spillover into each other",
      "Packaging / merchandise looks like real objects, not sticker collages"
    ],
    "avoid": [
      "Changing character hair color / clothing base color in different sections",
      "Merchandise items looking like the same object copied (should have material differences: ceramic / cotton / acrylic / paper)",
      "SNS profile section not looking like a real social platform UI",
      "Header logo font size squeezed by surrounding decoration to be hard to read"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: character name, character description, theme color, motif
- **Can default**: merch 1-5 (auto-recommend merchandise categories based on vibe), aspect ratio
- **Can randomize**: scattered item / poster prop (auto based on motif), bio copy

### Auto-Fill Strategy

- User only says "VTuber debut promotional image" + character image → auto-pair pink cherry blossom / blue ocean / purple starry sky motif
- User doesn't specify merchandise → default 9-item set (T-shirt / mug / 4 badges / keychain / 2 packages)
- User doesn't mention store info → SNS profile section emphasizes "PROFILE" instead of "NEW OPEN"

## Main Template 2: Character Room Goods Lifestyle Merchandise Collection (Case 167 Style)

Description

Not emphasizing debut / brand launch, but "what kind of room life does this character like," combining 6 home lifestyle items + character + concept explanation into one image.

Prompt

```json
{
  "type": "pastel lifestyle poster / character room-goods feature sheet",
  "goal": "Generate a magazine-style catalog image with the character as spokesperson, showcasing their favorite room lifestyle items, suitable for SNS sharing / product preview / personal project",
  "theme": "{argument name=\"theme\" default=\"soft dreamy lavender jellyfish aesthetic\"}",
  "style": "{argument name=\"style\" default=\"Japanese cute editorial graphic, airy white background, pastel lilac palette, delicate handwritten notes, sparkles and tiny doodles, soft product photography mixed with magazine layout\"}",
  "subject": {
    "character": {
      "name": "{argument name=\"character name\" default=\"Kurage-chan\"}",
      "appearance": "{argument name=\"character appearance\" default=\"young woman with a short platinum-blonde bob haircut, wearing a fluffy pale-lavender zip hoodie over a white inner top, shown from chest up on the lower right, face intentionally obscured with a plain beige rectangle\"}"
    }
  },
  "layout": {
    "orientation": "vertical poster",
    "background": "clean white with faint pastel doodles of stars, bubbles, tiny jellyfish, and musical notes",
    "sections": [
      { "title": "header", "position": "top", "elements": ["speech bubble intro", "main title", "small subtitle GOODS", "horizontal lavender ribbon tagline", "round badge on the top right"] },
      { "title": "featured goods grid", "position": "upper and middle left", "count": 6, "labels": ["{argument name=\"goods 1\" default=\"Swaying Jellyfish Lamp\"}", "{argument name=\"goods 2\" default=\"Dream with Jellyfish Bed Linen\"}", "{argument name=\"goods 3\" default=\"Jellyfish Shell Mirror\"}", "{argument name=\"goods 4\" default=\"Jellyfish Gradient Mug\"}", "{argument name=\"goods 5\" default=\"Jellyfish Heartbeat Storage Box\"}", "{argument name=\"goods 6\" default=\"Jellyfish Fluffy Mat\"}"] },
      { "title": "side handwritten note", "position": "upper right", "labels": ["{argument name=\"side note\" default=\"Let's all chill together in Kurage-chan's Room\"}"] },
      { "title": "room concept box", "position": "lower left", "labels": ["{argument name=\"concept title\" default=\"Kurage-chan's Room Design Philosophy\"}"] },
      { "title": "pick up circle", "position": "lower center-left", "labels": ["Pick up!"] }
    ]
  },
  "product_images": {
    "count": 6,
    "items": [
      { "name": "{argument name=\"goods 1\" default=\"Swaying Jellyfish Lamp\"}", "description": "small translucent jellyfish-shaped lamp on a white base, glowing softly in pale blue-lavender" },
      { "name": "{argument name=\"goods 2\" default=\"Dream with Jellyfish Bed Linen\"}", "description": "plush pastel-lavender bed with fluffy comforter and pillows, dreamy cozy bedroom styling" },
      { "name": "{argument name=\"goods 3\" default=\"Jellyfish Shell Mirror\"}", "description": "small tabletop mirror with a puffy shell-like pastel-lilac frame and rounded base" },
      { "name": "{argument name=\"goods 4\" default=\"Jellyfish Gradient Mug\"}", "description": "ceramic mug with lavender-to-pink gradient and a simple jellyfish illustration" },
      { "name": "{argument name=\"goods 5\" default=\"Jellyfish Heartbeat Storage Box\"}", "description": "pastel storage box holding cosmetics and small bottles, decorated with a jellyfish emblem" },
      { "name": "{argument name=\"goods 6\" default=\"Jellyfish Fluffy Mat\"}", "description": "small fluffy cloud-like or jellyfish-like mat in pale lavender and white" }
    ]
  },
  "text_elements": {
    "main_title": "{argument name=\"headline text\" default=\"Kurage-chan's Room Items\"}",
    "tagline": "{argument name=\"tagline\" default=\"Welcome to my fluffy, sweet, slightly dreamy room\"}",
    "concept_points": {
      "count": 3,
      "items": [
        "{argument name=\"concept 1\" default=\"Colors unified in white and lavender!\"}",
        "{argument name=\"concept 2\" default=\"A soft space where light gathers\"}",
        "{argument name=\"concept 3\" default=\"Treasuring a space where you can be yourself, surrounded by items with friends\"}"
      ]
    },
    "product_blurbs": "each product has a short handwritten Japanese description in a cute casual font beside or below the image"
  },
  "composition": "the poster is left-heavy with product cards and text, while the character portrait occupies the lower right third, slightly overlapping the layout",
  "color_palette": ["white", "pastel lavender", "soft lilac", "pale gray-violet", "touches of pastel blue-pink gradient"],
  "constraints": {
    "must_keep": [
      "6 products with unified style (same color family + same material tendency)",
      "Character appears in a fixed position without stealing focus from main content",
      "Overall feels like a refined SNS-shareable catalog"
    ],
    "avoid": [
      "Products stacked messily without grid",
      "Too many font types (recommend Japanese handwritten + one main title font)",
      "Character drawn too large, becoming the main focus instead of supporting"
    ]
  }
}
```

### When to choose this variant

- User is making a "what's in my room" / "IP same-style goods" type project
- Emphasizes atmosphere / lifestyle over commercial / debut
- Suitable for SNS sharing, no need for logo system / packaging mockups

## Main Template 3: Minimal Version (Character + 4-6 Merch Items + Logo)

Suitable for limited resources, just wanting a single IP launch announcement scenario.

Prompt

```json
{
  "type": "minimal character merch announcement",
  "sections": [
    "top: large main logo + character close-up",
    "middle: 4-6 merchandise items in a grid",
    "bottom: SNS handle + release date + 1 line tagline"
  ],
  "vibe": "{argument name=\"vibe\" default=\"clean, premium, focus on products\"}",
  "merch_count": 6,
  "must_keep": ["unified product photography feel", "logo and SNS handle spelling consistent"]
}
```

### When to choose this variant

- No time for 6-8 sections
- Only want to emphasize "character + merchandise + launch time"
- Want "clean minimalist" style rather than "information explosion" style

## Things to Avoid

- Changing character's hairstyle / color palette / clothing base across different sections → visual immediately no longer reads as "same IP"
- Drawing 6 products as the same object copied → must have material / shape / purpose differences
- Logo font inconsistent between header and web banner
- SNS profile section follow button conflicting with character IP main color
- Merchandise mockups with perspective errors (e.g. mug ellipse flattened, T-shirt wrinkles unnatural)
- Packaging mockup "transparent window" rendered as pure sticker rather than realistic refraction
- Overall color palette ≥ 5 main tones → loses IP consistency, should be controlled to 2-3 main colors + 1-2 accents