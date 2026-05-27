# 18+ Module Mascot Full-Process Brand Design Document Template

This file is used to generate "a super-large canvas that flattens the entire design document from DNA analysis to landing applications for a mascot into one image" visuals.

Typical uses:

- Design agency brand book / IP guideline proposal image for clients
- Designer portfolio cover (one image showcasing the complete design process)
- IP pre-launch "design rationale" board
- Teaching example: "a mascot from concept to landing" full process
- Bidding / competitive proposal capability showcase image

Characteristics (differences from existing `mascot-brand-kit.md`):

| Dimension | `mascot-brand-kit.md` (existing) | This template (new) |
|---|---|---|
| Module count | 4-6 sections | **18-24 modules** |
| Perspective | Hero image + three-view + expressions + applications | **DNA analysis → moodboard → exploration sketches → line art → 3D → colors → materials → design system → digital applications → physical applications → final render** |
| Use case | IP introduction page / merchandise catalog | **Complete brand book / design proposal / bid document** |
| Render density | Medium | Extremely high (approaching brand book PDF page collage) |

## Scope

- 18+ module mascot full-process design document
- Complete brand book / IP guideline one-image overview
- Design agency bid / proposal hero image
- "Design process visualization" teaching board

## When to use

- User mentions "complete brand design process / brand guideline / IP design book"
- User wants to produce "including design derivation process" not just results
- Client needs one image covering "DNA → sketches → line art → 3D → applications" all stages

Do NOT use for:

- Only need IP character collection → use `branding-and-packaging/mascot-brand-kit.md`
- Only need general brand identity (logo / colors / fonts / applications) → use `branding-and-packaging/brand-identity-board.md`
- Single character three-view / expressions → use `portraits-and-characters/character-sheet.md`
- IP merchandise images → use `branding-and-packaging/character-merch-board.md`

## Missing Information Priority Question Order

1. Brand / IP name + industry (tea shop / education / tech / creative goods...)
2. Mascot main form (animal / humanoid / anthropomorphic / food / abstract)
3. Primary + secondary colors (if not specified, default by industry)
4. Render style (**3D Pixar realistic cartoon / flat 2D / chibi Q-version / anthropomorphic**)
5. Module density (18 / 24 / custom list)
6. Required application scenarios (plush toy / packaging / app icon / storefront / etc.)

## Main Template: 18-Module Mascot Full-Process Brand Design Document

Description

3 columns x 6 rows = 18 equal-size modules, each module forms its own design process stage. The overall image looks like an 18-page brand book PDF with each page shrunk to a cell and assembled into one large image.

Prompt

```json
{
  "type": "18-panel brand identity and character design document",
  "goal": "Generate a complete design document large image recording the full process from DNA analysis to landing applications for a mascot, usable as a brand book one-image overview or design proposal hero image",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"Muyang MUYANG TEA\"}",
    "industry": "{argument name=\"industry\" default=\"tea shop\"}",
    "tagline": "{argument name=\"tagline\" default=\"warm cup, drink slowly with you\"}",
    "colors": [
      "{argument name=\"primary color\" default=\"yellow\"}",
      "{argument name=\"secondary color\" default=\"green\"}",
      "white",
      "brown",
      "dark green"
    ]
  },
  "character": {
    "description": "{argument name=\"character description\" default=\"3D rendered cute Shiba Inu mascot wearing a green apron, big sparkly eyes, plush soft body, friendly smile\"}",
    "rendering_style": "{argument name=\"render style\" default=\"Pixar-quality 3D, soft subsurface scattering, glossy plush texture\"}"
  },
  "layout": {
    "grid": "3 columns by 6 rows",
    "panel_count": 18,
    "panel_borders": "thin light-gray dividers, generous white margin between cells",
    "global_typography": "section titles in bilingual Chinese + English, small body text, panel numbers 01-18 prominently labeled",
    "background": "{argument name=\"page background\" default=\"clean off-white paper\"}"
  },
  "sections": [
    {
      "id": "01",
      "title": "01 Brand DNA Analysis / BRAND DNA ANALYSIS",
      "elements": ["small logo lockup", "5 color swatches with HEX codes", "6 brand keyword icons", "small target audience donut chart"]
    },
    {
      "id": "02",
      "title": "02 Concept Ideation / CONCEPT MOODBOARD",
      "elements": ["5 inspiration photo references", "4 mood / vibe icons", "1 design equation diagram (e.g. tea + dog + warmth = MUYANG)"]
    },
    {
      "id": "03",
      "title": "03 Form Study / FORM STUDY",
      "elements": ["4 logo anatomy icons", "4 evolution steps from primitive shape to refined silhouette", "4 final silhouette variants"]
    },
    {
      "id": "04",
      "title": "04 Concept Exploration / CONCEPT EXPLORATION",
      "elements": ["12 quick line-art character sketches with subtle pose / expression variation"]
    },
    {
      "id": "05",
      "title": "05 Refined Line Art / REFINED LINE ART",
      "elements": ["3 rows showing front and side line-art with proportion guides, head-body ratio markers, and grid alignment"]
    },
    {
      "id": "06",
      "title": "06 Detail Refinement / DETAIL REFINEMENT",
      "elements": ["2 large full-body 3D renders with annotation labels", "4 circular close-up callouts (eyes, paw, apron stitch, tail)"]
    },
    {
      "id": "07",
      "title": "07 Expression Sheet / EXPRESSION SHEET",
      "elements": ["11 3D rendered head expressions: happy, sad, surprised, sleepy, angry, shy, proud, worried, laughing, wink, neutral"]
    },
    {
      "id": "08",
      "title": "08 Pose Library / POSE LIBRARY",
      "elements": ["9 full-body 3D rendered poses: waving, bowing, holding tea, jumping, sitting, sleeping, presenting, running, hugging cup"]
    },
    {
      "id": "09",
      "title": "09 Turnaround View / TURNAROUND VIEW",
      "elements": ["5 full-body 3D renders at 0°/45°/90°/135°/180°", "5 matching line-art turnaround views below"]
    },
    {
      "id": "10",
      "title": "10 Color Development / COLOR DEVELOPMENT",
      "elements": ["5 rows of 5-color palettes (primary, accent, monochrome, seasonal, dark mode)", "short color psychology paragraph"]
    },
    {
      "id": "11",
      "title": "11 Material Specification / MATERIAL SPECIFICATION",
      "elements": ["5 texture swatches (plush, vinyl, ceramic, fabric, plastic)", "property sliders (softness / glossiness / transparency)", "4 manufacturing process icons"]
    },
    {
      "id": "12",
      "title": "12 Color Application / COLOR APPLICATION",
      "elements": ["4 mascot color variant renders", "2 light-mode and dark-mode renders", "4 contrast rating circles (AAA / AA / A / fail)"]
    },
    {
      "id": "13",
      "title": "13 Construction Guide / CONSTRUCTION GUIDE",
      "elements": ["1 line-art geometry construction diagram (with circles / triangles / proportion lines)", "1 grid alignment diagram"]
    },
    {
      "id": "14",
      "title": "14 Design System Rules / DESIGN SYSTEM RULES",
      "elements": ["minimum size icons (16px / 24px / 48px)", "clear-space diagram with X-height markers", "4 do/don't usage examples"]
    },
    {
      "id": "15",
      "title": "15 Asset Variants / ASSET VARIANTS",
      "elements": ["3 size variants (S / M / L)", "3 line-art variants", "3 simplified flat icon-style heads"]
    },
    {
      "id": "16",
      "title": "16 Digital Applications / DIGITAL APPLICATIONS",
      "elements": ["1 app icon mockup", "2 social avatar mockups", "small UI element row (button / loader / badge)", "3-step animation cycle thumbnails"]
    },
    {
      "id": "17",
      "title": "17 Physical Applications / PHYSICAL APPLICATIONS",
      "elements": ["1 plush toy mockup", "1 product packaging mockup", "1 merchandise (tote / mug) mockup", "1 storefront / signage mockup"]
    },
    {
      "id": "18",
      "title": "18 Final Rendering / FINAL RENDERING",
      "elements": ["1 large hero-size 3D render of mascot in signature pose holding brand product", "logo lockup", "file format / deliverable list"]
    }
  ],
  "global_style": {
    "rendering": "premium design agency presentation board, mixing 3D character renders, line art, photo mockups, charts, and infographic typography",
    "color_tone": "calm, professional, off-white background with brand colors as accents",
    "panel_density": "each panel completely filled but not cluttered; consistent label position (top-left) and small body text",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait poster (e.g. A2 print)\"}"
  },
  "constraints": {
    "must_keep": [
      "18 module numbers clearly visible, bilingual titles",
      "Mascot design completely consistent across all 3D modules",
      "Overall reads like a brand book page collage, not 18 independent posters",
      "Sub-element count per module exact (11 expressions / 9 poses / 5 turnarounds / etc.)"
    ],
    "avoid": [
      "Style drift between modules (one module 3D realistic, another suddenly hand-drawn)",
      "Omitting numbers or bilingual titles",
      "Drawing expressions / poses / turnarounds as the same pose copied",
      "Application mockups not looking like real objects (e.g. plush looking like a screenshot)"
    ]
  }
}
```

### Parameter Strategy

- **Must ask**: brand name + industry, character description, render style, primary/secondary colors
- **Can default**: tagline, page background, aspect ratio
- **Can randomize**: specific 11 / 9 items in expression / pose libraries (auto based on IP personality)

### Auto-Fill Strategy

- User only says "mascot" + industry → auto-generate character by industry semantics (tea shop → Shiba Inu / rabbit; tech → robot / pixel creature; maternal/baby → cute beast / cloud figure)
- If specific 11 expressions / 9 poses not specified → use standard set from template
- If materials / application scenarios not specified → default by industry (food & beverage emphasizes packaging / plush toys; tech emphasizes app icon / UI)

## Variant 1: 24-Module Complete IP Guideline (for Major Client Proposals)

Add 6 more modules on top of the 18 modules above, covering deeper dimensions of IP commercialization.

Prompt

```json
{
  "type": "24-panel mascot IP commercialization guideline",
  "extra_sections_after_18": [
    {
      "id": "19",
      "title": "19 Co-Branding Scenarios / CO-BRANDING SCENARIOS",
      "elements": ["4 co-branding mockups (cross-industry brand collaborations)"]
    },
    {
      "id": "20",
      "title": "20 Seasonal Variations / SEASONAL VARIATIONS",
      "elements": ["4 seasonal variants (Spring Festival / Mid-Autumn / Christmas / Halloween)"]
    },
    {
      "id": "21",
      "title": "21 Sticker Pack / STICKER PACK",
      "elements": ["16 chibi expression sticker grid"]
    },
    {
      "id": "22",
      "title": "22 Merch Matrix / MERCH MATRIX",
      "elements": ["6 merchandise categories (figures / stationery / apparel / home / digital / food)"]
    },
    {
      "id": "23",
      "title": "23 Social Content Kit / SOCIAL CONTENT KIT",
      "elements": ["1 public account header + 1 video cover + 1 Moments 9-grid + 1 livestream background"]
    },
    {
      "id": "24",
      "title": "24 Commercialization Roadmap / COMMERCIALIZATION ROADMAP",
      "elements": ["timeline with 4 phases: launch / merchandise / co-branding / IP licensing"]
    }
  ]
}
```

### When to choose this variant

- Major client IP competitive bid
- Proposal needs to show "not only design capability, but also commercialization understanding"
- Want one image showcasing complete IP commercial blueprint

## Variant 2: Minimal 9-Module Quick Brand Kit

Suitable for small-to-medium client budgets, no need for full process, but richer than a single image.

Prompt

```json
{
  "type": "9-panel quick mascot brand kit",
  "layout": { "grid": "3 columns by 3 rows", "panel_count": 9 },
  "sections": [
    "01 LOGO + COLOR",
    "02 Hero 3D Character",
    "03 6 Expressions",
    "04 4 Poses",
    "05 Three-View",
    "06 Color Palette",
    "07 Typography Specs",
    "08 Application mockup (packaging + app icon)",
    "09 Final Hero Render"
  ]
}
```

### When to choose this variant

- Client budget limited / time tight
- One image = one mini design document (Moments-level readability)
- Trial stage: produce this version first, confirm direction, then upgrade to 18 / 24 modules

## Variant 3: Pure Design Derivation Edition (No 3D, All Sketches + Line Art)

Suitable for academic / creative goods / handmade brands, emphasizing "design thinking process."

Prompt

```json
{
  "type": "18-panel mascot design rationale (sketch-first edition)",
  "rendering_override": "ALL panels in pencil sketch + ink line + watercolor wash; NO 3D renders even in 06/08/09; final panel 18 may upgrade to ink-color illustration",
  "vibe": "designer's working notebook scanned and laid out as a document",
  "extra_visual_elements": ["coffee stain", "tape strips", "handwritten margin notes"]
}
```

### When to choose this variant

- Creative / publishing / handmade / academic brands
- Want to emphasize "hand-designed, with warmth"
- Aligning with independent designer / illustrator portfolios

## Things to Avoid

- Module numbers missing or out of order (18 module numbers are the soul of the template)
- Letting mascot design drift across modules (must strictly maintain the same form)
- Expression / pose / turnaround counts imprecise (11 / 9 / 5 are validated visual densities)
- Drawing the mockup area as sticker collages rather than realistic material renders
- All 18 modules sharing one font size → hierarchy collapses; section titles must be >= 1.6x larger than body
- Overall looking like 18 independent poster collages → should have shared background + consistent margins + consistent title style
- Forcing 24 modules when image quality is limited → per-cell detail will collapse, 18 modules recommended as maximum