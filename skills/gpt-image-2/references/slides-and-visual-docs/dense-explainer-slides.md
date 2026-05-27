# High-Density Explainer Slides Template

This file is used to generate "one page that can explain a topic clearly" high-density Slides visuals, inspired by:

- Japanese Kasumigaseki-style government Slides
- Irasutoya simple warm illustrations
- Business consulting firm one-page summaries
- Academic poster one-page layouts

Features:

- Extremely high information density
- Has title area + multiple sections + multiple diagram blocks
- Restrained color palette (≤ 3 colors)
- Text + icons + small illustrations mixed

## Scope

- Single-page explainer Slides
- Public class / training / presentation single-page handout
- Self-media long image cover page
- Company one-page plan overview

## When to Use

- User mentions "explainer Slides / high-density page / explain in one page / policy style / Irasutoya style"
- User wants a lot of text and illustrations coexisting
- User wants an image that can disseminate information on its own

Do NOT use:

- User wants a policy announcement style (use `policy-style-slide.md`)
- User wants a business report (use `visual-report-page.md`)
- User wants a teaching diagram (use `educational-diagram-slide.md`)

## Missing Information Priority Questions

1. Topic
2. Style preference: warm illustration / government rigorous / academic / consulting
3. Information density (medium / high / very high)
4. Number of sections (3-6)
5. Whether English / Japanese / bilingual is needed
6. Whether a central main image is needed

## Main Template: Irasutoya x Kasumigaseki Blended Slides

📖 Description

Overall one Slides page, containing main title + subtitle + multiple sections + clean illustrations + necessary diagrams.

📝 Prompt

```json
{
  "type": "High-density explainer Slide",
  "goal": "Generate a high-density Slide usable as an explainer course / WeChat long image cover / training single-page handout",
  "style": {
    "format": "{argument name=\"format\" default=\"ponchi-e diagram\"}",
    "blend": "Irasutoya soft warm illustrations + Kasumigaseki style Slides high information density",
    "color_palette": "{argument name=\"color palette\" default=\"Off-white background + vermillion red + dark gray\"}"
  },
  "title_section": {
    "main_title": "{argument name=\"main title\" default=\"Momotaro Story Complete Diagram\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Understand this story with one image\"}",
    "language": "{argument name=\"language\" default=\"Japanese\"}"
  },
  "centerpiece": {
    "enabled": "{argument name=\"centerpiece enabled\" default=\"true\"}",
    "description": "{argument name=\"centerpiece description\" default=\"Upper center of the image, Momotaro standing on a peach, with dog, monkey, and pheasant surrounding him\"}"
  },
  "sections": {
    "count": "{argument name=\"section count\" default=\"5\"}",
    "items": [
      "{argument name=\"section 1\" default=\"Birth: Born from a peach\"}",
      "{argument name=\"section 2\" default=\"Growth: A brave and kind boy\"}",
      "{argument name=\"section 3\" default=\"Departure: Heading to Onigashima\"}",
      "{argument name=\"section 4\" default=\"Companions: Dog / Monkey / Pheasant\"}",
      "{argument name=\"section 5\" default=\"Victory: Defeating the demons and returning home\"}"
    ],
    "section_block_style": "Each section consists of a small illustration + title + 2-3 sentence explanation"
  },
  "annotations": {
    "style": "Thin leader lines + small labels",
    "rule": "Annotation lines must not cross the central subject"
  },
  "footer": {
    "summary": "{argument name=\"summary\" default=\"Kindness + Courage + Companions — the core of this story\"}"
  },
  "constraints": {
    "must_keep": [
      "High information density, but with clear reading order",
      "Central subject as visual anchor",
      "Illustration style consistent with text style",
      "Color palette strictly ≤ 3 colors"
    ],
    "avoid": [
      "Section text sizes inconsistent",
      "Overly refined illustrations breaking visual unity",
      "Text filling to edges with no whitespace",
      "Strange mixed English appearing"
    ]
  }
}
```

### Parameter Strategy

- Required: topic, number of sections
- Defaultable: color palette, subtitle, bottom summary sentence
- Random: specific illustration shapes for each section

### Auto-fill Strategy

- When user provides a topic: auto-decide section splitting (recommend 4-6 sections)
- Style defaults to Irasutoya x Kasumigaseki blend
- Central subject auto-selected based on the topic

## Variant 1: Business Consulting Firm One-Pager

📝 Prompt

```json
{
  "type": "Business consulting one-pager Slide",
  "style": {
    "color_palette": "Deep blue + gray + white",
    "blend": "Modern consulting firm style + minimalist icons"
  },
  "title_section": {
    "main_title": "{argument name=\"main title\" default=\"Product Strategy in the AI Era\"}",
    "subtitle": "One page explaining the strategic thinking"
  },
  "sections": {
    "count": 4,
    "items": [
      "Current Situation Diagnosis",
      "Core Opportunities",
      "Strategic Path",
      "Key Milestones"
    ]
  },
  "constraints": {
    "must_feel": "Rational, restrained, trustworthy"
  }
}
```

## Variant 2: Academic Poster One-Pager

📝 Prompt

```json
{
  "type": "Academic poster one-pager Slide",
  "style": {
    "color_palette": "Academic blue + beige + black",
    "blend": "Academic poster + paper-style layout"
  },
  "title_section": {
    "main_title": "{argument name=\"paper title\" default=\"Image Quality Assessment Method Based on Multimodal Signals\"}",
    "subtitle": "One-page abstract figure"
  },
  "sections": {
    "items": ["Research Question", "Method Overview", "Experimental Results", "Conclusion & Future Work"]
  },
  "constraints": {
    "must_feel": "Academic, rigorous, submittable quality"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "High-density explainer Slide auto-fill template",
  "mode": "auto-fill",
  "rule": "User only provides topic, auto-select style, sections, color palette, and central subject",
  "constraints": {
    "must_feel": "Publication quality"
  }
}
```

## Things to Avoid

- Do NOT make body text size larger than the title
- Do NOT have more than 6 sections on a single page
- Do NOT make the central subject so large it overshadows other sections
- Do NOT mix illustration sources with different styles from the main style
- Do NOT have Chinese + English + Japanese all appear on the same page