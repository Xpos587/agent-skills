# Biomimetic / Industrial Design Concept Poster Template

This file is used to generate "natural prototype → abstraction → industrial product" concept design posters, combining biological forms, evolution derivation, final product hero render, multi-view technical drawings, and brand copy into a single concept board.

Typical uses:

- Biomimetic industrial design concepts (aircraft / car / robot / appliance / footwear)
- Designer / student portfolio cover
- Startup demo day "how we went from inspiration to product" showcase
- Academic industrial design course deliverable
- Speed / efficiency brand visual manifesto poster
- Quick sketch → blueprint → render full-process demonstration

Characteristics (compared to existing poster templates):

| Template | Use Case |
|---|---|
| `brand-poster.md` (existing) | Brand main poster (product / person / text claim) |
| `campaign-kv.md` (existing) | Campaign KV + derivative layout system |
| `banner-hero.md` (existing) | Web hero / landing page horizontal composition + CTA |
| `editorial-cover.md` (existing) | Magazine / journal cover |
| **This template** (new) | **Industrial design concept poster: prototype → evolution → hero → multi-view technical drawings** |

## Scope

- Biomimetic industrial design (manta / shark / falcon / leaf / honeycomb inspired)
- Concept product introduction poster
- Student / designer portfolio cover
- "Inspiration → Product" visual narrative
- High-end manufacturing / aerospace / automotive / outdoor categories

## When to Use

- User mentions "biomimetic / concept design / industrial design / evolution derivation / inspiration source"
- Wants to create a "from biological prototype to final product" visual story
- Needs hero render + multi-view technical drawings + design derivation all in one image

Do NOT use:

- Pure product advertising poster → use `brand-poster.md` or `product-visuals/premium-studio-product.md`
- Academic paper figure → use `academic-figures/method-pipeline-overview.md`
- User research / needs analysis poster → use `slides-and-visual-docs/visual-report-page.md`

## Missing Information Priority Questions

1. Product type + name (aircraft SKYRAY / shoe SHARK SOLE / chair LEAF CHAIR)
2. Biomimetic prototype (stingray / shark / leaf / honeycomb / lobster ...)
3. Style tone (**black + cyan high-tech / off-white + black iron line art / warm wood + natural / vintage blueprint**)
4. Whether evolution strip is needed (5-stage inspiration → product)
5. Whether technical multi-view is needed (top / side / front / rear / underside / detail)
6. Tagline / footer body text
7. Aspect ratio (default portrait 3:4)

## Main Template: Biomimetic Concept Product Poster

📖 Description

Portrait poster / landscape board, divided into 5 zones: header (emblem + name + tagline) + evolution strip (5-stage derivation) + hero render (center 3D) + technical views grid (6 views) + footer body text.

📝 Prompt

```json
{
  "type": "biomimetic concept design poster",
  "goal": "Generate a \"natural prototype → derivation → hero → multi-view\" concept product board, usable as design proposal / portfolio cover / demo day poster",
  "subject": {
    "vehicle_or_product": "{argument name=\"product type\" default=\"futuristic aircraft concept\"}",
    "name": "{argument name=\"product name\" default=\"SKYRAY\"}",
    "inspiration": "{argument name=\"animal inspiration\" default=\"stingray\"}",
    "design": "{argument name=\"design description\" default=\"blended-wing-body aircraft shaped like a manta ray, wide triangular planform, smooth organic curves, sharp pointed nose, slightly raised central spine, tapered wing tips curling subtly upward, dark graphite-black metallic skin with fine panel lines and faint blue illuminated accents along edges and seams\"}"
  },
  "style": {
    "mood": "{argument name=\"mood\" default=\"premium futuristic industrial design presentation\"}",
    "rendering": "{argument name=\"rendering\" default=\"hyper-detailed cinematic 3D concept art mixed with blueprint visualization\"}",
    "color_palette": "{argument name=\"color palette\" default=\"black, charcoal, gunmetal, silver, deep ocean blue, electric cyan highlights\"}",
    "lighting": "{argument name=\"lighting\" default=\"low-key dramatic studio lighting with glossy reflections, cool rim light, subtle underwater ambience in the top inspiration strip\"}"
  },
  "layout": {
    "background": "{argument name=\"background\" default=\"full black poster with faint technical grid lines and soft vignetting\"}",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait poster\"}",
    "sections": [
      {
        "title": "header",
        "position": "top",
        "count": 3,
        "labels": ["emblem mark", "{argument name=\"product name\" default=\"SKYRAY\"}", "{argument name=\"tagline\" default=\"INSPIRED BY THE SEA. ENGINEERED FOR THE SKY.\"}"]
      },
      {
        "title": "evolution strip",
        "position": "upper middle",
        "count": 5,
        "labels": [
          "{argument name=\"evo 1\" default=\"realistic stingray underwater at far left\"}",
          "{argument name=\"evo 2\" default=\"top-view biological stingray study\"}",
          "{argument name=\"evo 3\" default=\"abstract aerodynamic line sketch\"}",
          "{argument name=\"evo 4\" default=\"faceted aircraft blueprint transition drawing\"}",
          "{argument name=\"evo 5\" default=\"final sleek aircraft concept at far right\"}"
        ]
      },
      {
        "title": "hero render",
        "position": "center",
        "count": 1,
        "labels": ["large three-quarter view of the {argument name=\"product type\" default=\"aircraft\"}"]
      },
      {
        "title": "technical views grid",
        "position": "lower middle",
        "count": 6,
        "labels": ["TOP", "SIDE", "FRONT", "REAR", "UNDERSIDE", "DETAIL"]
      },
      {
        "title": "footer text",
        "position": "bottom",
        "count": 1,
        "labels": [
          "{argument name=\"body text\" default=\"A biomimetic high-speed aircraft concept shaped by the hydrodynamic elegance of the stingray. Its blended wing body, low-drag silhouette, and fluid control surfaces translate ocean-born efficiency into atmospheric performance.\"}"
        ]
      }
    ],
    "technical_views": {
      "TOP": "top orthographic view with measurement ticks",
      "SIDE": "thin side profile with long smooth belly curve",
      "FRONT": "front orthographic view emphasizing broad wingspan and central cockpit hump",
      "REAR": "rear orthographic view showing narrow tail end and wing sweep",
      "UNDERSIDE": "underside three-quarter view",
      "DETAIL": "close-up crop of metallic skin, seam lines, and glowing blue edge strip"
    }
  },
  "graphics": {
    "logo": "{argument name=\"logo description\" default=\"minimal four-point symmetrical emblem above title, resembling a stylized ray silhouette\"}",
    "arrows": "4 thin cyan arrows connecting the 5 stages in the evolution strip",
    "typography": "widely spaced modern sans-serif uppercase text, clean luxury-tech branding"
  },
  "camera": {
    "hero_render": "slightly elevated front-left three-quarter angle",
    "technical_views": "orthographic",
    "inspiration_image": "{argument name=\"inspiration camera\" default=\"underwater side angle with light rays from above\"}"
  },
  "quality": "ultra-clean, polished, high contrast, sharp, poster-ready, concept design board for {argument name=\"industry\" default=\"aerospace\"} branding or speculative industrial design",
  "constraints": {
    "must_keep": [
      "5-stage evolution strip has clear left-to-right logic (biological → abstract → product)",
      "Hero render occupies the visual center ≥ 35% of height",
      "6 technical view angles complete and product form consistent",
      "Header / footer layout aligned to hero center axis",
      "Overall color scheme no more than 4 main colors + 1 accent"
    ],
    "avoid": [
      "Evolution strip drawn as 5 photos of the same pose (should show progressive abstraction from realistic to abstract)",
      "Technical views proportionally distorted (top / front / rear must be orthographically accurate)",
      "Product form drifting between hero and technical views",
      "Footer body text too long → should be limited to 2-3 sentences",
      "Emblem / logo placed as a large image → should be a small badge",
      "Too many neon colors destroying the industrial feel"
    ]
  }
}
```

### Parameter Strategy

- **Required**: product type + name, animal/biological inspiration, industry
- **Defaultable**: tagline, background, color palette
- **Random**: evolution 5-stage specific descriptions, technical views detail crop

### Auto-fill Strategy

- User provides "product + inspiration" → auto-generate 5-step derivation following "biology → anatomy → abstraction → industrial → final product"
- Industry not specified → auto-categorize by product type (aircraft = aerospace; shoe = footwear; chair = furniture)
- Colors not specified → recommend by industry (aerospace = black+cyan; footwear = white+orange; furniture = warm wood+cream)

## Variant 1: Vintage Blueprint Edition (cream paper + ink)

📝 Prompt

```json
{
  "type": "biomimetic concept poster vintage blueprint edition",
  "style_override": {
    "background": "aged cream blueprint paper with subtle stains and grid",
    "color_palette": "navy ink, dark sepia, faded brown, no neon",
    "rendering": "fine ink linework + stippled engraving + vintage drafting style",
    "mood": "Leonardo da Vinci notebook meets industrial blueprint"
  },
  "extra_elements": ["handwritten margin notes", "small wax seal stamp", "ruler tick marks along edges"]
}
```

### When to choose this variant

- Emphasizing "design philosophy / Renaissance feel"
- Education / publishing / cultural brand
- Contrast point: presenting a futuristic product with a vintage tactile feel

## Variant 2: Natural Tones (warm wood + off-white, suitable for home / shoes / chairs)

📝 Prompt

```json
{
  "type": "biomimetic concept poster organic warm edition",
  "style_override": {
    "background": "warm off-white textured paper with subtle plant shadows",
    "color_palette": "cream, beige, warm wood, sage green, soft black",
    "rendering": "soft 3D render + photograph composite",
    "mood": "biophilic design, sustainability, calm premium"
  }
}
```

### When to choose this variant

- Home / chair / shoe / tableware categories
- Emphasizing sustainability / eco-friendly / nature affinity
- Does NOT want the cold "industrial feel"

## Variant 3: Horizontal Triptych (left inspiration / center product / right technical)

Suitable for widescreen display / agency proposal hero image.

📝 Prompt

```json
{
  "type": "biomimetic concept poster horizontal triptych",
  "layout_override": {
    "format": "horizontal poster, 16:9 or 21:9",
    "structure": "3 vertical panels: left = biological inspiration column, center = hero product render, right = technical views stack",
    "evolution_strip": "vertical thin strip on the far left edge, 5 stages stacked top-to-bottom"
  },
  "use_case": "Widescreen deck / agency proposal front page / Behance project cover"
}
```

### When to choose this variant

- Widescreen display channels
- Designer case study project cover
- Presentation / proposal front page

## Things to Avoid

- Evolution strip 5 stages all showing "the final product from different angles" → must have "biological → abstract → product" progression
- Product outline / proportions inconsistent between hero and technical views
- All 6 technical views are rendered images → at least 4 should be orthographic line drawings, 1 should be a material detail crop
- Footer text written as marketing copy → should be design philosophy / engineering description
- Using anime / cartoon style for industrial products (should use hyperreal 3D or blueprint)
- Emblem / logo placed as large text → should be ≤ 1/3 the headline size as a small badge
- More than 6 colors across the entire image (should be limited to 3-4 main colors + 1 accent)