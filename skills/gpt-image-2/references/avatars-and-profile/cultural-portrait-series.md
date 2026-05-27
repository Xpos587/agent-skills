# Cultural / Historical Figure Series Portrait Template

This file is used for "generating series portraits based on cultural / historical / mythological themes in bulk":

- Dynasty emperor series (Ming dynasty emperors / Qing dynasty emperors)
- Mythological character series (Greek mythology / Norse mythology)
- Historical figures series
- Classic literature character series
- Ethnic dress series

Features:

- Multiple characters, one per panel
- Each panel has name / title labels
- Unified style (same artist / same era style)
- Suitable for education / cultural creative / themed marketing

## Scope

- Dynasty emperors / famous figures series
- Mythological / literature character series
- Ethnic / cultural themed series

## When to Use

- User mentions "series / collection / dynasty / mythology / historical figures"
- User wants multiple characters + labels

Do NOT use for:

- Same person multi-version (use `character-grid-portrait.md`)
- Single image style transfer (use `style-transfer-selfie.md`)
- Character IP design sheets (use `portraits-and-characters/character-sheet.md`)

## Missing Information Priority Question Order

1. Theme (dynasty / mythology / literature / culture)
2. Character count (recommended 6-12)
3. Whether to include names / titles / brief descriptions
4. Style: ink wash realistic / oil painting / cartoon / semi-realistic
5. Whether referencing a particular style (user-provided reference image / classic artist style)
6. Aspect ratio

## Main Template: Dynasty Emperor Series Portraits

📖 Description

Overall a large image containing several emperor portraits, each with posthumous title + personal name below.

📝 Prompt

```json
{
  "type": "Dynasty Emperor Series Portraits",
  "goal": "Generate a series portrait image containing several emperors of a dynasty, usable as education / cultural creative / social media educational content",
  "theme": {
    "dynasty": "{argument name=\"dynasty\" default=\"Ming Dynasty\"}",
    "subject_count": "{argument name=\"subject count\" default=\"9\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"Chinese gongbi realistic portrait + slight ink wash feel\"}",
    "consistency": "all portraits must be painted in the same artist style",
    "color_palette": "{argument name=\"color palette\" default=\"low saturation gold + vermillion red + black\"}"
  },
  "layout": {
    "format": "{argument name=\"format\" default=\"3x3 grid\"}",
    "background": "{argument name=\"background\" default=\"cream silk fabric texture\"}",
    "panel_design": {
      "portrait_shape": "rounded square / oval",
      "label_position": "centered below portrait",
      "label_content": "posthumous title + personal name, e.g. 'Taizu Zhu Yuanzhang'"
    }
  },
  "subjects": {
    "auto_select": "{argument name=\"auto select\" default=\"true\"}",
    "rule": "if auto_select is true, select representative emperors by dynasty order; if user provides a list, follow the user list",
    "user_list": "{argument name=\"user list\" default=\"\"}"
  },
  "constraints": {
    "must_keep": [
      "all portraits in the same artist style",
      "clothing and accessories strictly matching the dynasty",
      "labels clearly readable and historically accurate",
      "portraits evenly distributed"
    ],
    "avoid": [
      "wrong dynasty clothing appearing",
      "portrait style drift (each looking like a different artist)",
      "label typos / misplacement",
      "overly decorated background"
    ]
  }
}
```

### Parameter Strategy

- Must ask: theme, count
- Can default: style, layout, color scheme, labels
- Can randomize: background texture details

### Auto-Complete Strategy

- When user provides a dynasty: auto-select 9 representative emperors
- Default style is Chinese gongbi
- Default label format is "posthumous title + personal name"

## Variant 1: Mythological Character Series

📝 Prompt

```json
{
  "type": "Mythological Character Series Portraits",
  "theme": {
    "mythology": "{argument name=\"mythology\" default=\"Greek Mythology\"}",
    "subject_count": 12
  },
  "style": {
    "art_style": "classical oil painting + impasto",
    "color_palette": "deep blue + gold + warm brown"
  },
  "layout": {
    "format": "4x3 grid",
    "panel_design": {
      "label_content": "deity name + domain"
    }
  },
  "subjects": {
    "user_list": "Zeus / Hera / Poseidon / Hades / Athena / Apollo / Artemis / Ares / Aphrodite / Hermes / Hephaestus / Dionysus"
  },
  "constraints": {
    "must_feel": "classical oil painting museum collection feel"
  }
}
```

## Variant 2: Classic Literature Character Series

📝 Prompt

```json
{
  "type": "Classic Literature Character Series",
  "theme": {
    "literature": "{argument name=\"literature\" default=\"Dream of the Red Chamber Twelve Beauties\"}",
    "subject_count": 12
  },
  "style": {
    "art_style": "gongbi heavy color + classical illustration",
    "color_palette": "rouge red + moon white + emerald green"
  },
  "constraints": {
    "must_feel": "classical literature album quality"
  }
}
```

## Variant 3: Ethnic Dress Series

📝 Prompt

```json
{
  "type": "Ethnic Dress Series Portraits",
  "theme": {
    "subject_count": 9,
    "category": "{argument name=\"category\" default=\"9 representative from China's 56 ethnic groups\"}"
  },
  "style": {
    "art_style": "high-resolution realistic portrait + studio photography",
    "color_palette": "preserve each ethnic group's original dress colors"
  },
  "constraints": {
    "must_feel": "culturally respectful, attire accurate"
  }
}
```

## Variant 4: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Cultural Figure Series Auto-Complete",
  "mode": "auto-fill",
  "rule": "User provides a cultural theme, auto-select character list, style, layout, labels",
  "constraints": {
    "must_feel": "textbook quality / publishable cultural creative"
  }
}
```

## Things to Avoid

- Do not mix up dynasty clothing (most common error)
- Do not let art style drift (a series must be unified)
- Do not use mocking expressions on culturally sensitive topics
- Do not paint deities in cosplay style
- Do not have label typos / missing words
- Do not exceed 12 characters per single image, otherwise visual fragmentation