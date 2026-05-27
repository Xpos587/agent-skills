# Long-Page Landing Page / Case Study UI Mockup Template

This file is used to generate "an entire page of SaaS / marketing / case study landing page UI mockup" — assembling multiple sections (hero / strategy / performance / social proof / CTA) vertically into one super-long image.

Typical uses:

- SaaS product homepage mockup
- Marketing case study long page (post-investment report / KPI review)
- Growth / agency business intro page
- Y Combinator style demo day project page
- Client proposal / investor deck web-style presentation

Characteristics (compared to existing UI templates):

| Template | Visual Scope | Use Case |
|---|---|---|
| `chat-interface-scene.md` | Single-screen chat interface | iMessage / WeChat / group chat |
| `social-interface-mockup.md` | Single-screen social post detail | Twitter / Xiaohongshu / Weibo |
| `live-commerce-ui.md` | Single-screen live stream UI overlay | Douyin / Taobao Live |
| `product-card-overlay.md` | Single-screen hero / detail main image | E-commerce detail page hero |
| **This template** | **Full long page** (5-7 sections stacked vertically) | **SaaS / marketing long page / case study** |

## Scope

- SaaS landing page / product homepage
- Marketing case study long page
- Growth review report web version
- Investor / client proposal web mockup
- Agency business intro long page

## When to Use

- User mentions "landing page / case study / full page / long page / website mockup"
- User wants "top-to-bottom complete section structure" rather than a single-screen screenshot
- Client needs to see the full marketing narrative: "hero → data → timeline → social proof → CTA"

Do NOT use:

- Single-screen UI screenshot → use `chat-interface-scene` / `social-interface-mockup` / `live-commerce-ui`
- Hero section only → use `poster-and-campaigns/banner-hero.md`
- Real interactive HTML web page → should generate HTML code instead of an image

## Missing Information Priority Questions

1. Business type (SaaS / agency / course / case study / post-investment report)
2. Brand / main headline + one-line positioning
3. Whether it's a "marketing case study" (needs data + client logos) or "product homepage" (needs features + screenshots)
4. Color scheme (**dark + neon / pure white + strong accent / light beige business / glassmorphism**)
5. Core data that must appear (GMV / views / client count / growth rate)
6. Whether client logo wall / testimonials / CTA form is needed
7. Aspect ratio (**3:4 / 9:16 long screenshot / full desktop screenshot**)

## Main Template: Marketing Case Study Long Page Mockup

📖 Description

One super-long screenshot, 6-7 independent sections from top to bottom, unified dark + neon accent throughout, each section looks like a module that would appear on a real landing page.

📝 Prompt

```json
{
  "type": "UI/UX landing page mockup",
  "goal": "Generate a highly realistic marketing case study long page screenshot that can serve as a proposal, post-investment report, or portfolio cover",
  "theme": "{argument name=\"theme\" default=\"dark mode, sleek modern aesthetic, glassmorphism, neon purple and blue glowing accents\"}",
  "viewport": {
    "width": "{argument name=\"viewport width\" default=\"desktop 1440px width\"}",
    "scroll_capture": "{argument name=\"capture style\" default=\"full-page screenshot, vertical scroll captured into one tall image\"}",
    "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4 portrait long page\"}"
  },
  "header": {
    "logo": "{argument name=\"brand name\" default=\"goViralX\"}",
    "nav_items": ["Home", "Case Studies", "Pricing", "Contact"],
    "top_right_cta": "{argument name=\"top cta\" default=\"Login\"}",
    "top_right_tag": "{argument name=\"top right tag\" default=\"VIRAL CAMPAIGN CASE STUDY\"}"
  },
  "layout": {
    "section_count": 6,
    "section_separation": "subtle horizontal divider, 80-120px vertical breathing room",
    "sections": [
      {
        "name": "Hero",
        "position": "top",
        "headline": "{argument name=\"hero headline\" default=\"How We Created 10M+ Viral Impact\"}",
        "subheadline": "{argument name=\"hero subhead\" default=\"3 days to viral explosion, helping the brand achieve exponential growth\"}",
        "stats_row": {
          "count": 4,
          "labels": ["{argument name=\"stat label 1\" default=\"Total Views\"}", "{argument name=\"stat label 2\" default=\"Engagement Rate\"}", "{argument name=\"stat label 3\" default=\"Conversions\"}", "{argument name=\"stat label 4\" default=\"Execution Period\"}"],
          "values": ["{argument name=\"stat value 1\" default=\"10,240,000+\"}", "{argument name=\"stat value 2\" default=\"18.7%\"}", "{argument name=\"stat value 3\" default=\"3,200+\"}", "{argument name=\"stat value 4\" default=\"72 hours\"}"]
        },
        "visual": "{argument name=\"hero visual\" default=\"cinematic shot of a person in a hoodie looking at glowing digital screens and graphs, large play button overlay\"}"
      },
      {
        "name": "Strategy",
        "title": "{argument name=\"strategy title\" default=\"Our 3-Day Execution Strategy\"}",
        "layout_type": "vertical timeline",
        "steps_count": 3,
        "elements_per_step": ["timeline node circle", "step title", "3 bullet points", "video thumbnail with play button", "description box"],
        "step_titles": ["Day 1: Asset Production", "Day 2: Multi-Platform Launch", "Day 3: Amplification & PR"]
      },
      {
        "name": "Performance",
        "title": "{argument name=\"perf title\" default=\"Data-Driven Performance\"}",
        "left_column": {
          "stat_cards_count": 4,
          "values": ["10M+", "43%", "28,000+", "3,200+"],
          "labels": ["Total Views", "Engagement", "New Followers", "Leads"]
        },
        "right_column": {
          "charts_count": 2,
          "chart_1": "line graph showing 7-day growth peaking at Day 3, x-axis days 1-7, y-axis views, glowing line",
          "chart_2": "horizontal segmented bar chart showing platform distribution (TikTok 52%, Instagram 24%, X 15%, YouTube 9%)"
        }
      },
      {
        "name": "Keys to Success",
        "title": "{argument name=\"keys title\" default=\"The 3 Keys to Viral Success\"}",
        "cards_count": 3,
        "card_elements": ["glowing icon (fire / target / antenna)", "card title", "2-line description", "VIEW DETAIL link with arrow"]
      },
      {
        "name": "Social Proof",
        "title": "{argument name=\"sp title\" default=\"TRUSTED BY CREATORS & BRANDS\"}",
        "left_column": {
          "logos_count": 8,
          "grid": "2x4",
          "brands": ["{argument name=\"logo 1\" default=\"SHEIN\"}", "SHOPLINE", "Blueglass", "instacart", "lemon8", "mi", "CIDER", "bellroy"]
        },
        "right_column": {
          "testimonial_cards_count": 2,
          "elements": ["large quotation mark", "italic quote text", "author avatar circle", "author name + title (e.g. SaaS Founder, Growth Manager)"]
        }
      },
      {
        "name": "Call to Action",
        "title": "{argument name=\"cta title\" default=\"READY TO GO VIRAL?\"}",
        "interactive_elements": [
          "text input field with placeholder '{argument name=\"input placeholder\" default=\"Your work email\"}'",
          "glowing button with text '{argument name=\"call to action text\" default=\"Get Your Growth Plan ->\"}'"
        ],
        "visual": "{argument name=\"cta visual\" default=\"3D render of a rocket ship taking off with purple and blue flames\"}"
      }
    ]
  },
  "footer": {
    "logo": "{argument name=\"brand name\" default=\"goViralX\"}",
    "columns": ["Product", "Company", "Resources", "Legal"],
    "social_icons": ["X", "LinkedIn", "YouTube", "Instagram"],
    "copyright": "© 2026 {argument name=\"brand name\" default=\"goViralX\"}. All rights reserved."
  },
  "global_style": {
    "rendering": "production-quality web UI mockup, sharp pixel-perfect typography, realistic component spacing, modern web design",
    "typography": "modern sans-serif (Inter / Space Grotesk feel), strong size hierarchy across sections",
    "color_tone": "{argument name=\"color tone\" default=\"dark navy / charcoal background, neon purple + electric blue accents, white-90% body text\"}",
    "components": "rounded corners 12-16px, soft glassmorphism cards, subtle shadows, accent gradient buttons",
    "browser_chrome": "{argument name=\"chrome\" default=\"none, just the page itself\"}"
  },
  "constraints": {
    "must_keep": [
      "6 sections in clear top-to-bottom order, each independently identifiable",
      "Each section's internal components follow standard web design (cards / grids / timelines / charts)",
      "Data readable, fonts clear, sufficient contrast",
      "Overall looks like a real scrollable web page screenshot, not a PPT collage"
    ],
    "avoid": [
      "No visual separation between sections (easy to blend together)",
      "Drawing charts as illustrations rather than real data visualizations",
      "Brand names in the logo wall becoming unreadable",
      "CTA button color conflicting with the page-wide color scheme",
      "Hero taking up 80%+ of height (crushes the sections below)"
    ]
  }
}
```

### Parameter Strategy

- **Required**: brand name + business positioning, core data values, color scheme
- **Defaultable**: nav items, footer columns, stat labels (recommended by business type)
- **Random**: specific brands in client logo wall (match real existing brand names by industry), testimonial quote content

### Auto-fill Strategy

- User only says "marketing case study landing page" → default to dark + neon scheme + 6-section standard structure
- User provides core data (e.g., "3 days 10M views") → auto-derive stat labels / charts / strategy timeline
- User doesn't mention client logos → generate 8 real brand names by industry (don't fabricate fake names)

## Variant 1: SaaS Product Homepage (feature-driven)

📝 Prompt

```json
{
  "type": "SaaS product homepage mockup",
  "section_count": 7,
  "sections": [
    "Hero (headline + subhead + CTA + dashboard screenshot)",
    "Logo Strip (8 customer logos)",
    "Feature Grid (3x2 = 6 features with icon + title + description)",
    "How It Works (3-step process)",
    "Product Screenshot Showcase (1 large dashboard image)",
    "Pricing (3 tiers comparison table)",
    "Testimonials + CTA"
  ],
  "theme": "{argument name=\"theme\" default=\"clean white + accent blue, modern startup\"}",
  "must_have": "1 prominent product UI screenshot embedded in Hero, 1 dashboard image in showcase section"
}
```

### When to choose this variant

- User is building a SaaS product homepage, not a case study
- Needs to show "what the product looks like" (screenshot-within-screenshot)
- Needs a pricing table

## Variant 2: Investor / Client Deck Web Version

📝 Prompt

```json
{
  "type": "investor / client pitch deck rendered as one long landing page",
  "section_count": 8,
  "sections": [
    "Hero (problem statement)",
    "Solution Overview",
    "Market Size (chart)",
    "Product Demo (screenshots)",
    "Traction (key metrics + growth chart)",
    "Team (4 avatars + roles)",
    "Roadmap (4 phases timeline)",
    "Ask + Contact"
  ],
  "theme": "professional, premium, slightly editorial, soft shadow + light grid background",
  "tone": "credible, ambitious, data-backed"
}
```

### When to choose this variant

- Startup needs a demo day pitch deck web version
- Converting a Keynote deck into a shareable web mockup
- Needs all elements of a "traditional deck" (market / team / ask)

## Variant 3: Glassmorphism + Gradient (trending 2026 style)

📝 Prompt

```json
{
  "type": "glassmorphism landing page",
  "theme_override": {
    "background": "deep purple-to-pink gradient with floating blur orbs",
    "cards": "frosted glass effect (backdrop-blur 20px), 1px white border at 20% opacity",
    "accents": "neon green and hot pink glow",
    "typography": "ultra-bold sans-serif headlines, very thin weight body"
  },
  "section_count": 5,
  "sections": ["Hero", "Feature Cards 3x", "Stats", "Testimonials", "CTA"],
  "vibe": "Y2K x Apple Vision Pro x Linear.app"
}
```

### When to choose this variant

- Design-driven brand / AI tools / creative products
- Needs to trigger designer reshares on social media
- Client wants "visually stunning" rather than "corporate stable"

## Things to Avoid

- Sections without clear separation → must have 80-120px whitespace + subtle color/background difference
- Drawing charts as pure decoration (must look like real data curves)
- Fabricating brand names in the logo wall (use real well-known brands or clearly mark as "example")
- CTA button color conflicting with brand color → should be an accent version of the brand color
- Hero area too large, crushing subsequent sections (hero ≤ 35% total height)
- Using only one font size on the entire page → must have ≥ 4 levels of hierarchy (H1 / H2 / Body / Caption)
- Leaving placeholder text like "VIEW DETAIL" as-is → should replace with real copy based on the business
- Choosing the wrong output aspect ratio (e.g., 1:1 can't fit a full long page; recommended 3:4 / 9:16)