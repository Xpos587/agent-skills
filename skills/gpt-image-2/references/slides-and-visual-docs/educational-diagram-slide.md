# Educational Diagram Slide Template

This file is used to generate "one page that clearly explains a concept / mechanism / process" educational-style visual pages:

- Course pages
- Textbook diagrams
- Online course screenshots
- Engineer teaching diagrams
- Training manual illustrations

Features:

- Central main image + step breakdown
- Restrained text
- Warm colors
- Emphasis on readability
- Suitable for repeated reading

## Scope

- Concept diagrams
- Mechanism / process flow diagrams
- Engineering principle diagrams
- Textbook page illustrations

## When to Use

- User mentions "teaching / course / textbook / concept diagram / mechanism diagram / principle diagram"
- User wants to clearly explain "how X works"
- User's audience is students / learners, not investors / government

Do NOT use:

- User wants an explainer course slide (use `dense-explainer-slides.md`)
- User wants a policy style (use `policy-style-slide.md`)
- User wants a business report (use `visual-report-page.md`)

## Missing Information Priority Questions

1. Concept / mechanism name
2. Teaching level (elementary / middle school / university / industry training)
3. Number of steps (3-7)
4. Whether a central main image is needed
5. Style: hand-drawn / cartoon / academic / engineering diagram
6. Color scheme

## Main Template: Step-Breakdown Educational Diagram

📖 Description

Overall one-page teaching diagram, top main title + central main image + numbered step breakdown around it + bottom summary sentence.

📝 Prompt

```json
{
  "type": "Educational diagram Slide",
  "goal": "Generate a teaching diagram that lets learners understand a concept / mechanism / process at a glance",
  "style": {
    "color_palette": "{argument name=\"color palette\" default=\"Warm beige + academic blue + light gray\"}",
    "rendering": "{argument name=\"rendering\" default=\"Clear vector illustration + clean typography\"}"
  },
  "header": {
    "main_title": "{argument name=\"main title\" default=\"How Photosynthesis Works\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"From light to sugar, understand in seven steps\"}",
    "audience": "{argument name=\"audience\" default=\"Middle school students\"}"
  },
  "centerpiece": {
    "enabled": "{argument name=\"centerpiece enabled\" default=\"true\"}",
    "description": "{argument name=\"centerpiece description\" default=\"A complete leaf cross-section with chloroplasts and stomata marked\"}"
  },
  "steps": {
    "count": "{argument name=\"step count\" default=\"6\"}",
    "items": [
      "{argument name=\"step 1\" default=\"01 Light enters the chloroplast\"}",
      "{argument name=\"step 2\" default=\"02 Water transported from roots\"}",
      "{argument name=\"step 3\" default=\"03 Carbon dioxide enters through stomata\"}",
      "{argument name=\"step 4\" default=\"04 Light reaction: Water splits into hydrogen and oxygen\"}",
      "{argument name=\"step 5\" default=\"05 Dark reaction: CO2 converted to sugar\"}",
      "{argument name=\"step 6\" default=\"06 Oxygen released, glucose produced\"}"
    ],
    "step_block_style": "Number + one sentence + small icon"
  },
  "annotations": {
    "style": "Thin leader lines + numbered small labels",
    "rule": "Annotation lines must not cross"
  },
  "summary_line": "{argument name=\"summary\" default=\"Photosynthesis = Light + Water + CO2 → Glucose + O2\"}",
  "constraints": {
    "must_keep": [
      "Central main image as visual anchor",
      "Step numbering continuous and clear",
      "Consistent typography",
      "Colors ≤ 3 main colors"
    ],
    "avoid": [
      "Too many steps to fit on one page",
      "Mixed illustration styles",
      "Leader lines crossing the main image",
      "Overuse of jargon without explanation in body text"
    ]
  }
}
```

### Parameter Strategy

- Required: concept, teaching level, number of steps
- Defaultable: style, color scheme, bottom formula sentence
- Random: specific icon shapes

### Auto-fill Strategy

- Lower teaching level → more cartoonish illustrations, shorter text
- Higher teaching level → more scientific diagrams, more precise text
- Recommended 4-7 steps; more than 7 steps should be split across multiple pages

## Variant 1: Engineering Principle Diagram

📝 Prompt

```json
{
  "type": "Engineering principle diagram Slide",
  "header": {
    "main_title": "{argument name=\"concept\" default=\"How the Four-Stroke Internal Combustion Engine Works\"}"
  },
  "centerpiece": {
    "description": "Cylinder cross-section + piston action"
  },
  "steps": {
    "count": 4,
    "items": ["Intake", "Compression", "Power", "Exhaust"]
  },
  "constraints": {
    "must_feel": "Engineering diagram feel, professional, credible"
  }
}
```

## Variant 2: Young Children's Educational Diagram

📝 Prompt

```json
{
  "type": "Young children's science educational Slide",
  "header": {
    "main_title": "{argument name=\"concept\" default=\"Why Does It Rain?\"}"
  },
  "style": {
    "color_palette": "Pink-orange + sky blue + off-white",
    "rendering": "Chibi cartoon illustration"
  },
  "steps": {
    "count": 4,
    "items": ["Sun heats water", "Water becomes clouds", "Clouds get heavy", "It rains"]
  },
  "constraints": {
    "must_feel": "Cute, easy to understand, warm"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Educational diagram auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides concept, auto-decide steps, style, color scheme, and main image",
  "constraints": {
    "must_feel": "Can be placed directly into a textbook / course slides"
  }
}
```

## Things to Avoid

- Do NOT make concepts so academic that elementary students can't understand them
- Do NOT have more than 7 steps
- Do NOT let illustration and explanation text styles conflict
- Do NOT include brand advertising in science diagrams
- Do NOT let annotation lines cross each other
- Do NOT use overly saturated colors that compromise reading comfort