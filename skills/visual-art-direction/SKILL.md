---
name: visual-art-direction
description: Use when gathering visual references, building moodboards, planning art-directed image variants across viewports and channels, or generating responsive hero/feature images for any UI/UX surface — landing pages, apps, dashboards, e-commerce, marketing campaigns
argument-hint: "[project or niche description]"
user-invocable: true
---

# Visual Art Direction

Moodboard + art direction + responsive image generation for any UI/UX surface. Combines stock reference search (Pexels/Unsplash/Pixabay) with GPT Image 2 generation/editing via fal.ai to produce art-directed variants per viewport and channel.

## When to Use

- Building moodboards or gathering style references for any digital product
- Planning image variants across viewports (desktop/tablet/mobile) or channels (web/social/email)
- Generating hero, feature, product, or marketing images adapted per breakpoint
- Editing existing images (background swap, style transfer, mask-based local edit)
- Art-directing responsive images for apps, dashboards, e-commerce, campaigns
- Writing art direction briefs or variant specifications

Do NOT activate for: icon design, logo creation, illustration-only requests, print media, video production.

## Workflow

```
1. Moodboard → 2. Art Direction → 3. Generate/Edit → 4. Export
```

### Phase 1: Moodboard (Reference Gathering)

Collect visual references to anchor direction. See [references/moodboard-guide.md](references/moodboard-guide.md).

1. Ask: product type + target audience + mood/tone (or infer from domain)
2. Search stock providers for 5-8 reference images covering:
   - Mood/atmosphere
   - Color palette inspiration
   - Layout/composition references
   - Typography-style cues
3. Present as numbered grid with attribution
4. Confirm direction with user before proceeding

**Stock search**: Use [[searching-stock-images]] skill. Run providers in parallel. Always include attribution.

**Moodboard presentation**:

```
## Moodboard: [Project Name]

### Direction: [1-2 sentence summary]

| # | Image | Source | Key Takeaway |
|---|-------|--------|-------------|
| 1 | [Description] | Pexels / Author | Warm tones, morning light |
| 2 | [Description] | Unsplash / Author | Clean geometry, minimal |

### Color Palette (extracted)
- Primary: #HEX | Secondary: #HEX | Accent: #HEX | Background: #HEX

### Confirmed Direction
[Summary of chosen direction]
```

### Phase 2: Art Direction (Variant Planning)

Define image treatment per viewport/channel. See [references/art-direction.md](references/art-direction.md).

**Core principle**: Art direction means different crops/compositions per context, not just scaling the same image.

#### Viewport Breakpoints

| Breakpoint | Width | Typical Use | Hero Treatment |
|---|---|---|---|
| Desktop | ≥1024px | Full scene with context | Wide landscape, rule-of-thirds |
| Tablet | 768-1023px | Compact hero | Tighter crop, subject centered |
| Mobile | <768px | CTA-first | Vertical close-up on focal point |

#### Channel Variants (beyond viewport)

| Channel | Aspect Ratio | Use Case | Key Consideration |
|---|---|---|---|
| Web hero | 16:9 or 21:9 | Homepage, landing | Text overlay space reserved |
| Mobile hero | 4:5 or 1:1 | App, mobile web | CTA visible, focal point centered |
| Social square | 1:1 | Instagram feed, LinkedIn | Brand mark visible |
| Social vertical | 9:16 | Stories, Reels, TikTok | Top/bottom safe zones |
| Social portrait | 4:5 | Instagram portrait, Pinterest | Product/subject prominent |
| Email banner | 3:1 typical | Email header | Simple, no fine detail |
| Display ad | 300×250, 728×90 | Paid media | Bold, readable at small size |

**For each image, specify:**
- Story: what this image communicates
- Composition: crop, subject placement, text overlay zones
- Which variants are required and how composition adapts per variant
- What to avoid (category cliches, forbidden treatments)

**Art direction brief template**: [references/creative-brief-template.md](references/creative-brief-template.md)

### Phase 3: Generate / Edit

**Script**: `scripts/hero.py` (Python, `uv run --script`, requires `FAL_KEY`)

#### Generate images per variant

```bash
scripts/hero.py generate \
  --prompt "SaaS dashboard hero, morning light, soft gradient" \
  --project my-saas \
  --quality high
```

**Size presets**:

| Variant | `image_size` | Notes |
|---|---|---|
| Desktop hero | `landscape_16_9` | Full scene |
| Tablet hero | `landscape_4_3` | Tighter composition |
| Mobile hero | `portrait_4_5` | Vertical focal close-up |
| Social square | `square` | 1:1 composition |
| Social vertical | `portrait_9_16` | Stories/Reels |
| Email banner | `landscape_3_1` | Wide strip |

Default: generates desktop/tablet/mobile. Use `--breakpoints desktop,mobile` to skip tablet. Use `--breakpoints desktop,mobile,social-square` for custom variant sets.

**Quality vs cost**:

| Quality | Use When | Relative Cost |
|---|---|---|
| `high` | Final production images | 1x (default) |
| `medium` | Iteration/draft passes | ~0.4x |
| `low` | Quick concept sketches | ~0.2x |
| `auto` | Let model decide | varies |

**Output format**: `webp` (default), `png` (transparency), `jpeg` (photos).

#### Edit existing image(s)

```bash
scripts/hero.py edit \
  --prompt "Replace background with coastal sunset, keep product centered" \
  --image-urls "https://example.com/hero-desktop.webp"
```

**Edit endpoint**: `https://fal.run/openai/gpt-image-2/edit`

| Parameter | Required | Description |
|---|---|---|
| `prompt` | yes | Edit instruction |
| `image_urls` | yes | 1+ source image URLs |
| `mask_url` | no | White = edit zone, black = preserve |
| `image_size` | no | `auto` (default) or preset |
| `quality` | no | `high` (default) |
| `output_format` | no | `webp` (default) |

**Edit use cases**:

| Task | How |
|---|---|
| Background swap | `edit` with prompt describing new background |
| Local edit (mask) | `edit` + `--mask-url` white/black mask |
| Style transfer | `edit` with "render in watercolor style" |
| Mobile crop from desktop | `edit` + `--image-size portrait_4_5` + crop prompt |
| Color grading fix | `edit` with "warmer tones, golden hour light" |
| Dark mode variant | `edit` with "dark background, light accents" |

#### Common options (both modes)

| Flag | Purpose |
|---|---|
| `--prompt-file <path>` | Read prompt from file (structured JSON templates) |
| `--project <slug>` | Output directory slug |
| `--output-dir <path>` | Override output directory |
| `--num-images <1-4>` | Generate multiple variants per run |
| `--json` | Structured JSON output (for scripting) |

### Phase 4: Export

Default output: `visual-assets/<project-slug>/`

```
visual-assets/<project-slug>/
  hero-desktop.webp
  hero-tablet.webp
  hero-mobile.webp
  social-square.webp       (if requested)
  prompt-<timestamp>.md
  responsive.html
```

#### Responsive HTML (auto-generated by `generate`)

**Art-directed `<picture>`** (different crops per viewport):

```html
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.webp" type="image/webp">
  <source media="(min-width: 768px)" srcset="hero-tablet.webp" type="image/webp">
  <img src="hero-mobile.webp" alt="DESCRIPTION" loading="eager"
       width="800" height="1000"
       style="max-width:100%;height:auto;">
</picture>
```

**Resolution-switching `srcset`** (same crop, different resolutions):

```html
<img srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
     sizes="(max-width: 768px) 100vw, 60vw"
     src="hero-800.webp" alt="DESCRIPTION"
     width="800" height="600"
     loading="lazy">
```

**Art direction + modern formats** (AVIF → WebP → JPEG per viewport):

```html
<picture>
  <source media="(min-width: 1024px)"
    srcset="hero-desktop-800.avif 800w, hero-desktop-1600.avif 1600w"
    sizes="100vw" type="image/avif">
  <source media="(min-width: 1024px)"
    srcset="hero-desktop-800.webp 800w, hero-desktop-1600.webp 1600w"
    sizes="100vw" type="image/webp">
  <source media="(min-width: 768px)"
    srcset="hero-tablet-600.avif 600w, hero-tablet-1200.avif 1200w"
    sizes="100vw" type="image/avif">
  <source media="(min-width: 768px)"
    srcset="hero-tablet-600.webp 600w, hero-tablet-1200.webp 1200w"
    sizes="100vw" type="image/webp">
  <img src="hero-mobile-800.jpg"
    srcset="hero-mobile-400.webp 400w, hero-mobile-800.webp 800w"
    sizes="100vw" alt="DESCRIPTION"
    width="800" height="1000"
    loading="eager" fetchpriority="high">
</picture>
```

#### Loading Strategy

| Image Position | loading | fetchpriority | Why |
|---|---|---|---|
| Hero/LCP | `eager` | `high` | Optimize LCP |
| Above fold (not LCP) | `eager` | omit | Normal load |
| Below fold | `lazy` | omit | Defer until near viewport |

#### CLS Prevention

Always set `width` + `height` on `<img>`. Use CSS `aspect-ratio` for containers.

## Quick Reference

| Task | Command |
|---|---|
| Moodboard only | Search stock refs → present grid → no generation |
| Full pipeline | Moodboard → art direction → `hero.py generate` → export |
| Custom variant set | `hero.py generate --breakpoints desktop,mobile,social-square` |
| Regenerate one variant | `hero.py generate --breakpoints desktop --prompt "..."` |
| Edit existing image | `hero.py edit --prompt "..." --image-urls URL` |
| Mask-based local edit | `hero.py edit --prompt "..." --image-urls URL --mask-url MASK` |
| Dark mode variant | `hero.py edit --prompt "dark background version" --image-urls URL` |
| Just HTML snippet | Provide image paths → generate `<picture>` markup |

## Failure Patterns

| Pattern | Fix |
|---|---|
| "Same image for all breakpoints" | Art-direct each: different crop/focus/composition per variant |
| Skip moodboard, generate blind | Always gather references first to anchor style |
| "Modern, clean, minimal" brief | Means nothing. Use specific references, named artists, hex codes |
| No variant planning upfront | Plan all variants before generation. Missing crops at delivery = reshoot |
| PNG for web photos | WebP — 50% smaller. AVIF — 70% smaller |
| No `alt` text | Always include descriptive alt |
| Missing `width`/`height` | CLS prevention. Always set intrinsic dimensions |
| Lazy load LCP hero | Hero = `loading="eager"` + `fetchpriority="high"` |
| Reference = competitor work | You'll get something that looks like the competitor. Never use |
| Text rendered ON generated image | Reserve space for HTML text overlay instead |
| Use `generate` for minor tweaks | `edit` is cheaper for background/style changes on existing images |
| No "what to avoid" in brief | Vendors/agents interpret broadly. Explicitly state what's out of bounds |

## Niche Direction Guide

| Niche | Hero Style | Color Direction | Typical Mood |
|---|---|---|---|
| SaaS | Dashboard in context | Blue/indigo/white | Trust, clarity, efficiency |
| E-Commerce | Product lifestyle | Brand-dependent | Desire, simplicity, speed |
| Fintech | Abstract data/money | Dark blue/gold/green | Trust, growth, security |
| Health/Fitness | Active people | Green/blue/white | Energy, vitality, freshness |
| Education | Learning environment | Blue/orange/yellow | Growth, curiosity, approachability |
| Creative Agency | Bold visuals | Vibrant, varied | Innovation, boldness, artistry |
| B2B Enterprise | Abstract/structural | Navy/grey/white | Authority, reliability, scale |

## Environment Setup

| Variable | Purpose | Required |
|---|---|---|
| `FAL_API_KEY` | fal.ai API key (preferred) | For Phase 3 |
| `FAL_KEY` | fal.ai API key (fallback) | For Phase 3 |
| `PEXELS_API_KEY` | Pexels stock search | For Phase 1 (optional) |
| `UNSPLASH_ACCESS_KEY` | Unsplash stock search | For Phase 1 (optional) |
| `PIXABAY_API_KEY` | Pixabay stock search | For Phase 1 (optional) |

## Red Flags — STOP and Correct

- "Just use one image for mobile and desktop" → Art direction requires per-variant compositions
- "Skip the moodboard" → No references = no style anchor. Always gather first
- "Use `urls.raw` for Unsplash download" → `links.download` only. TOS compliance
- "No attribution needed" → Attribution is TOS-required for all stock images
- "Generate at `low` quality for production" → `low` = concept only. Production = `high`
- "Generate from scratch for a minor bg change" → Use `edit` mode — cheaper, faster, preserves composition
- "Same prompt for all breakpoints" → Adjust crop/focus/background per variant
- NEVER display API keys or echo commands containing keys

## Prompt Template References

For complex compositions, use structured templates from [[gpt-image-2]] `references/`:

- Hero/banner: `references/poster-and-campaigns/banner-hero.md`
- Product visuals: `references/product-visuals/`
- Brand identity: `references/branding-and-packaging/brand-identity-board.md`
- Edit workflows: `references/editing-workflows/`
- Methodology: `references/prompt-writing.md`

Read only the specific template needed — never load entire `references/`.
