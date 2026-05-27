# Founder / Media Feature Portrait Template

This file is used to generate "founder / executive / industry figure" level media feature portraits:

- Financial magazine interview feature images
- Startup media covers
- Founder main images (fundraising / IPO news)
- Industry figure close-ups
- Personal brand feature portraits

Features:

- Dramatic lighting
- Strong "character presence"
- High contrast / high narrative feel
- Usually vertical 3:4 / 4:5
- Space reserved for titles or quotes

## Scope

- Financial / startup magazine interviews
- Company website founder feature portraits
- Industry figure close-ups
- Personal brand main images

## When to Use

- User mentions "founder feature / magazine interview / executive portrait / media portrait / character presence portrait"
- User wants highly narrative visuals with a "the person IS the story" feel

Do NOT use for:

- Standard business headshots (use `professional-portrait.md`)
- VTuber characters (use `virtual-host.md`)
- Character designs (use `character-sheet.md`)

## Missing Information Priority Question Order

1. Person's identity / industry
2. Gender / age
3. Style: black-and-white literary / industrial / innovative / classical financial
4. Composition: environmental portrait / close-up / half-body
5. Color scheme / lighting tone
6. Whether title space needs to be reserved

## Main Template: Media Feature Founder Portrait

📖 Description

Overall vertical portrait, subject is half-body or environmental portrait, dramatic side lighting, strong narrative, title space reserved.

📝 Prompt

```json
{
  "type": "Media Feature Founder Portrait",
  "goal": "Generate a media feature portrait that can be directly used as a financial magazine / startup media interview feature / company website founder main image",
  "subject": {
    "identity": "{argument name=\"identity\" default=\"AI company founder CEO\"}",
    "gender": "{argument name=\"gender\" default=\"East Asian male\"}",
    "age_range": "{argument name=\"age range\" default=\"35-45 years old\"}",
    "appearance": "{argument name=\"appearance\" default=\"neatly groomed hair, composed demeanor\"}",
    "outfit": "{argument name=\"outfit\" default=\"dark turtleneck knit + long overcoat\"}"
  },
  "composition": {
    "shot": "{argument name=\"shot\" default=\"environmental portrait + half-body\"}",
    "framing": "{argument name=\"framing\" default=\"subject at 1/3 of frame, 2/3 left for environment\"}",
    "title_safe_area": "{argument name=\"title safe area\" default=\"upper right reserved for title\"}"
  },
  "environment": {
    "location": "{argument name=\"location\" default=\"modern office space, floor-to-ceiling windows + minimalist furniture\"}",
    "depth": "{argument name=\"depth\" default=\"shallow depth of field, background blurred\"}"
  },
  "lighting": {
    "style": "{argument name=\"lighting style\" default=\"dramatic side light\"}",
    "key_light": "{argument name=\"key light\" default=\"large natural window light\"}",
    "fill_light": "{argument name=\"fill light\" default=\"shadow detail preserved\"}",
    "color_temp": "{argument name=\"color temp\" default=\"slightly cool\"}"
  },
  "expression": {
    "mood": "{argument name=\"mood\" default=\"composed, contemplative\"}",
    "gaze": "{argument name=\"gaze\" default=\"slightly off-camera, looking into the distance\"}"
  },
  "style": {
    "rendering": "high-resolution portrait photography + magazine post-processing",
    "tone": "slightly dark + high contrast + slight grain",
    "color_palette": "{argument name=\"color palette\" default=\"cool gray + ink black + warm skin tone\"}"
  },
  "constraints": {
    "must_keep": [
      "character expression has narrative quality",
      "lighting direction consistent",
      "composition leaves title space",
      "overall restraint, not entertainment-style"
    ],
    "avoid": [
      "logos and brand elements appearing",
      "overly dramatic lighting",
      "saturated filters",
      "environment overpowering the subject"
    ]
  }
}
```

### Parameter Strategy

- Must ask: identity, gender, age, environment
- Can default: color tone, lighting, composition
- Can randomize: environmental furniture details

### Auto-Complete Strategy

- Industry auto-selects environment (finance = marble lobby; tech = minimalist office; manufacturing = factory floor; creative = studio)
- Default lighting is window light + dramatic side light
- Default title space is upper right

## Variant 1: Black-and-White Literary Founder Portrait

📝 Prompt

```json
{
  "type": "Black-and-White Literary Founder Portrait",
  "style": {
    "rendering": "high contrast black-and-white + grain",
    "color_palette": "pure black-and-white"
  },
  "lighting": {
    "style": "hard light + strong shadows"
  },
  "constraints": {
    "must_feel": "timeless, narrative, literary"
  }
}
```

## Variant 2: Industrial / Factory Background Founder

📝 Prompt

```json
{
  "type": "Industrial Background Founder Portrait",
  "environment": {
    "location": "{argument name=\"factory\" default=\"behind production line, robotic arms blurred\"}"
  },
  "lighting": {
    "style": "industrial cool light + localized warm light"
  },
  "constraints": {
    "must_feel": "hardcore, manufacturing feel, trustworthy"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Founder Feature Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides industry + person name / gender, auto-decide environment, style, lighting",
  "constraints": {
    "must_feel": "ready for financial magazine cover"
  }
}
```

## Things to Avoid

- Do not place the subject face-on dead center (media features dislike rigid compositions)
- Do not let real brand logos appear in the background
- Do not over-retouch (skin should retain texture)
- Do not make lighting so dramatic it feels "makeup-heavy"
- Do not ignore title space reservation