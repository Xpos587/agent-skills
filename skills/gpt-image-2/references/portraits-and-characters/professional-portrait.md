# Professional Portrait Template

This file is used to generate "professional-grade / business-grade / LinkedIn-grade" portrait visuals:

- Professional headshots
- LinkedIn profile photos
- Company website team pages
- Media interview feature images
- Personal brand main images

Features:

- Clean background
- Professional lighting
- Natural expression
- Emphasis on credibility
- Sophistication comes from "restraint" not "embellishment"

## Scope

- Business headshots
- Company website team photos
- LinkedIn / public speaking photos
- Media interview feature images

## When to Use

- User mentions "professional headshot / LinkedIn / business photo / company website photo"
- User wants visuals that look credible, professional, restrained

Do NOT use for:

- Founder media feature portraits (use `founder-portrait.md`)
- VTuber characters (use `virtual-host.md`)
- Character design sheets (use `character-sheet.md`)

## Missing Information Priority Question Order

1. Gender / age range / ethnicity
2. Industry / profession (affects attire and background)
3. Style: classic business / modern casual / creative industry
4. Composition: bust / half-body
5. Background: solid color / office environment / natural light
6. Expression: smile / natural / serious

## Main Template: Modern Business Professional Portrait

📖 Description

Overall a professional portrait, subject is a bust shot, clean background, natural light or soft studio light, natural expression, can be directly used as a LinkedIn profile photo.

📝 Prompt

```json
{
  "type": "Modern Business Professional Portrait",
  "goal": "Generate a professional portrait that can be directly used as a LinkedIn profile photo / company website team page / media interview feature image",
  "subject": {
    "gender": "{argument name=\"gender\" default=\"East Asian male\"}",
    "age_range": "{argument name=\"age range\" default=\"30-40 years old\"}",
    "appearance": "{argument name=\"appearance\" default=\"short neat hair, thin-frame glasses\"}",
    "outfit": "{argument name=\"outfit\" default=\"dark navy blazer + light gray shirt, no tie\"}"
  },
  "expression": {
    "mood": "{argument name=\"mood\" default=\"natural smile, steady gaze\"}",
    "gaze": "{argument name=\"gaze\" default=\"looking at camera\"}"
  },
  "composition": {
    "shot": "{argument name=\"shot\" default=\"bust\"}",
    "framing": "{argument name=\"framing\" default=\"subject centered slightly left, 1/3 left for background\"}"
  },
  "background": {
    "type": "{argument name=\"background\" default=\"light gray gradient + slightly blurred office environment\"}",
    "depth_of_field": "{argument name=\"dof\" default=\"shallow depth of field\"}"
  },
  "lighting": {
    "key_light": "{argument name=\"key light\" default=\"45-degree soft light\"}",
    "fill_light": "{argument name=\"fill light\" default=\"weak fill light from right\"}",
    "rim_light": "{argument name=\"rim light\" default=\"no obvious rim light\"}",
    "color_temp": "{argument name=\"color temp\" default=\"naturally warm\"}"
  },
  "style": {
    "rendering": "high-resolution portrait photography + natural skin texture",
    "post_processing": "restrained skin retouching, preserving pores and natural texture"
  },
  "constraints": {
    "must_keep": [
      "subject natural not stiff",
      "gaze focused",
      "skin texture real, not over-retouched",
      "attire matches industry"
    ],
    "avoid": [
      "exaggerated effects lighting",
      "fake-looking filter skin",
      "brand logos appearing",
      "background elements overpowering subject"
    ]
  }
}
```

### Parameter Strategy

- Must ask: gender, age, industry, composition
- Can default: background, lighting, post-processing
- Can randomize: glasses style, accessories

### Auto-Complete Strategy

- Industry auto-determines attire (finance = suit; tech = casual shirt; creative = black tee + jacket)
- Default expression is "natural smile"
- Default background is "light gray gradient + blurred environment"

## Variant 1: Outdoor Natural Light Portrait

📝 Prompt

```json
{
  "type": "Outdoor Natural Light Professional Portrait",
  "background": {
    "type": "{argument name=\"outdoor scene\" default=\"green park blurred background\"}"
  },
  "lighting": {
    "key_light": "natural front light",
    "color_temp": "golden hour warm"
  },
  "constraints": {
    "must_feel": "natural, approachable, lifestyle feel"
  }
}
```

## Variant 2: Solid Background Studio Shot

📝 Prompt

```json
{
  "type": "Studio Professional Portrait",
  "background": {
    "type": "{argument name=\"backdrop\" default=\"neutral gray backdrop paper\"}",
    "depth_of_field": "none"
  },
  "lighting": {
    "key_light": "butterfly lighting",
    "fill_light": "symmetric soft light"
  },
  "constraints": {
    "must_feel": "magazine feature quality"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Professional Portrait Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides industry + gender + age, auto-decide attire / lighting / background",
  "constraints": {
    "must_feel": "ready to swap into LinkedIn profile"
  }
}
```

## Things to Avoid

- Do not over-retouch skin, preserve skin texture
- Do not use over-saturated filters
- Do not let identifiable third-party logos appear in the background
- Do not let subject's attire obviously mismatch the industry
- Do not use exaggerated dramatic lighting (unless user explicitly requests it)