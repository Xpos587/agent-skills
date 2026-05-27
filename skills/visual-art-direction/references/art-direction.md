# Art Direction Reference

Responsive image strategy per viewport and channel for any UI/UX surface.

## Viewport Breakpoints

| Name | Min Width | Typical Use | Aspect Ratio |
|---|---|---|---|
| Desktop | 1024px | Full-width hero, feature sections | 16:9 or 21:9 |
| Tablet | 768px | Compact hero, split layouts | 4:3 or 3:2 |
| Mobile | 0px | CTA-first, image-secondary | 4:5 or 1:1 |

## Channel Variants

| Channel | Aspect Ratio | Use Case | Key Consideration |
|---|---|---|---|
| Web hero | 16:9 or 21:9 | Homepage, landing | Text overlay space reserved |
| Mobile hero | 4:5 or 1:1 | App, mobile web | CTA visible, focal point centered |
| Social square | 1:1 | Instagram feed, LinkedIn | Brand mark visible |
| Social vertical | 9:16 | Stories, Reels, TikTok | Top/bottom safe zones |
| Social portrait | 4:5 | Instagram portrait, Pinterest | Product/subject prominent |
| Email banner | 3:1 typical | Email header | Simple, no fine detail |
| Display ad | 300×250, 728×90 | Paid media | Bold, readable at small size |

## Art Direction Decisions

### What changes per viewport/variant

1. **Crop**: Desktop shows full scene; mobile crops tight on focal subject
2. **Subject placement**: Desktop uses rule-of-thirds; mobile centers key element
3. **Text overlay space**: Desktop reserves left/right zone; mobile reserves bottom third
4. **Background detail**: Desktop shows environment; mobile simplifies to avoid clutter
5. **People**: Desktop can show full body; mobile crops waist-up or face-only
6. **Safe zones**: Social vertical needs top/bottom clear (UI overlays); email needs centered content

### What stays constant

- Color palette and grading
- Key subject identity (same product/person)
- Brand identity (logo position, font)
- Emotional tone

## Prompt Construction Per Variant

### Desktop Hero (landscape_16_9)

```
[WIDE ESTABLISHING SHOT]. [Full scene context]. [Subject in environment].
[Rule-of-thirds composition]. [Lighting]. [Atmosphere].
[Left 30% reserved for text overlay]. [No text on image itself].
```

### Tablet Hero (landscape_4_3)

```
[MEDIUM SHOT]. [Tighter crop on subject]. [Key environment elements visible].
[Center-weighted composition]. [Simplified background].
[Bottom 25% reserved for text overlay].
```

### Mobile Hero (portrait_4_5)

```
[CLOSE-UP on focal subject]. [Vertical composition]. [Subject fills frame].
[Clean/simple background]. [Strong focal point].
[Bottom third reserved for CTA text].
```

### Social Square (square / 1:1)

```
[CENTERED SUBJECT]. [Square composition]. [Subject and key element visible].
[Brand mark or product centered]. [No text overlay needed — text goes in caption].
[Background clean or branded pattern].
```

### Social Vertical (portrait_9_16 / 9:16)

```
[VERTICAL FULL-FRAME]. [Subject dominates frame]. [Top 15% clear for UI overlay].
[Bottom 20% clear for CTA/sticker area]. [Strong vertical composition].
[Bold, eye-catching at small thumbnail size].
```

### Email Banner (landscape_3_1)

```
[WIDE STRIP]. [Horizontal band composition]. [Single focal element].
[Simple, no fine detail — email clients may resize]. [Text-safe center zone].
[Left 40% for headline text overlay].
```

## HTML Implementation

### Art-directed `<picture>` (different crops per viewport)

See [picture-element.md](picture-element.md) for full details.

```html
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.webp" type="image/webp">
  <source media="(min-width: 768px)" srcset="hero-tablet.webp" type="image/webp">
  <img src="hero-mobile.webp" alt="DESCRIPTION" loading="eager"
       width="800" height="1000"
       style="max-width:100%;height:auto;">
</picture>
```

### Resolution-switching `srcset` (same crop, different resolutions)

Use when same crop, different resolutions (NOT art direction):

```html
<img srcset="hero-400.webp 400w, hero-800.webp 800w, hero-1200.webp 1200w"
     sizes="(max-width: 768px) 100vw, 60vw"
     src="hero-800.webp" alt="DESCRIPTION"
     width="800" height="600"
     loading="lazy">
```

See [srcset-sizes.md](srcset-sizes.md) for width descriptor patterns and [modern-formats.md](modern-formats.md) for AVIF/WebP fallback chains.

### CSS Aspect Ratio

```css
.hero { aspect-ratio: 16 / 9; }
.hero--mobile { aspect-ratio: 4 / 5; }
.hero--square { aspect-ratio: 1 / 1; }
.hero--vertical { aspect-ratio: 9 / 16; }
```

See [aspect-ratio.md](aspect-ratio.md) for CLS prevention patterns.

## Niche-Specific Guidance

### SaaS

- Desktop: Dashboard/product screenshot in environment, soft glow
- Tablet: Dashboard crop with key metric highlighted
- Mobile: Single metric or icon, clean gradient background
- Social: Dashboard close-up or abstract data viz

### E-Commerce

- Desktop: Product with lifestyle context, wide shot
- Tablet: Product centered, minimal context
- Mobile: Product on clean background, CTA visible
- Social: Product detail or lifestyle shot

### Fintech

- Desktop: Abstract data visualization, trust indicators
- Tablet: Simplified chart + person
- Mobile: App screen mockup or abstract pattern
- Social: Abstract trust/growth imagery

### Health/Fitness

- Desktop: Active lifestyle full scene
- Tablet: Person mid-activity, environment visible
- Mobile: Close-up on determination/action
- Social: Action shot or transformation

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Same prompt for all variants | Adjust crop/focus/background per variant |
| Text rendered ON generated image | Reserve space for HTML text overlay instead |
| No safe zone for CTA | Specify reserved zones in prompt |
| Mobile image too busy | Simplify background, reduce elements |
| CLS from missing dimensions | Always set `width`/`height` attributes |
| Social vertical without safe zones | UI overlays cover top/bottom — keep clear |
| Email banner with fine detail | Email clients resize aggressively — keep simple |
| Missing social variants | Plan all distribution channels upfront |
