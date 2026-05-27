# Healing Scene Illustration Template

This file is used to generate "soft light, warm, healing" scene illustrations:

- Healing everyday scenes
- Seasonal atmosphere illustrations
- Card / merchandise cover images
- Social media / Xiaohongshu cover images
- Brand gentle main images

Features:

- Soft color palette
- Natural light feel
- Restrained use of white space
- Character + scene + small props composition
- Does not emphasize dramatic conflict

## Scope

- Healing everyday scenes
- Seasonal atmosphere images
- Social media cover images
- Merchandise cards

## When to Use

- User mentions "healing / gentle / soft light / everyday / Studio Ghibli style"
- User wants visuals that make people want to pause and look

Do NOT use for:

- Concept / epic scenes (use `concept-scene.md`)
- Picture book illustrations (use `picture-book-scene.md`)
- Minimalist white space mood (use `minimalist-mood-scene.md`)

## Missing Information Priority Question Order

1. Scene (cafe / room / window side / seaside / street corner)
2. Season / time
3. Whether to include a character
4. Props (book / cat / tea / plant)
5. Style: hand-drawn anime / watercolor / digital illustration
6. Color tone base

## Main Template: Healing Everyday Scene

📖 Description

Overall a soft light scene illustration, subject is an everyday environment, optionally with one character or one animal, warm and natural color palette.

📝 Prompt

```json
{
  "type": "Healing Everyday Scene Illustration",
  "goal": "Generate a healing everyday scene illustration that makes people want to pause and look",
  "scene": {
    "location": "{argument name=\"location\" default=\"small desk by the window\"}",
    "season": "{argument name=\"season\" default=\"early summer\"}",
    "time_of_day": "{argument name=\"time of day\" default=\"morning\"}",
    "weather_or_mood": "{argument name=\"mood\" default=\"sunny, gentle breeze, just-woke-up feeling\"}"
  },
  "subject": {
    "human_or_animal": "{argument name=\"main subject\" default=\"short-haired girl from behind, chin in hand looking out the window\"}",
    "scale": "{argument name=\"subject scale\" default=\"occupies 1/3 of frame\"}"
  },
  "props": {
    "items": [
      "{argument name=\"prop 1\" default=\"open book + half cup of hot tea\"}",
      "{argument name=\"prop 2\" default=\"small potted plant on the windowsill\"}",
      "{argument name=\"prop 3\" default=\"folded beige blanket\"}"
    ]
  },
  "lighting": {
    "type": "{argument name=\"light type\" default=\"natural light\"}",
    "direction": "{argument name=\"light direction\" default=\"side light, streaming in from the window\"}",
    "intensity": "{argument name=\"light intensity\" default=\"soft\"}",
    "color_temp": "{argument name=\"color temp\" default=\"warm golden\"}"
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"hand-drawn anime + watercolor soft light\"}",
    "rendering": "grain + soft light + low saturation",
    "color_palette": "{argument name=\"color palette\" default=\"cream white + warm orange + green\"}"
  },
  "constraints": {
    "must_keep": [
      "overall atmosphere warm and healing",
      "light direction consistent",
      "color tone restrained, not flashy",
      "props and scene share the same atmosphere"
    ],
    "avoid": [
      "dramatic emotions appearing",
      "overly saturated colors",
      "overly dense scene elements",
      "brand advertisements appearing"
    ]
  }
}
```

### Parameter Strategy

- Must ask: scene, season, subject
- Can default: style, lighting, color scheme
- Can randomize: specific prop shapes

### Auto-Complete Strategy

- Season auto-determines color scheme (spring = cherry pink / summer = blue-white / autumn = warm brown / winter = snow white)
- Default subject is back view or partial, avoiding face stealing focus
- Default style is hand-drawn anime + watercolor

## Variant 1: Pet Healing Scene

📝 Prompt

```json
{
  "type": "Pet Healing Scene Illustration",
  "subject": {
    "human_or_animal": "{argument name=\"animal\" default=\"orange cat curled up in a blanket\"}"
  },
  "constraints": {
    "must_feel": "fluffy, cozy, want to pet"
  }
}
```

## Variant 2: Outdoor Healing Scene

📝 Prompt

```json
{
  "type": "Outdoor Healing Scene Illustration",
  "scene": {
    "location": "{argument name=\"outdoor\" default=\"wooden boardwalk by the lake\"}",
    "weather_or_mood": "dusk + gentle breeze"
  },
  "subject": {
    "human_or_animal": "two figures from behind, walking side by side"
  },
  "constraints": {
    "must_feel": "cinematic, white space, slow pace"
  }
}
```

## Variant 3: Auto-Complete Mode

📝 Prompt

```json
{
  "type": "Healing Scene Auto-Complete Template",
  "mode": "auto-fill",
  "rule": "User provides season / time / a mood sentence, auto-decide scene, subject, props, color scheme",
  "constraints": {
    "must_feel": "can serve as social media / Xiaohongshu cover image"
  }
}
```

## Things to Avoid

- Do not let the character's full face steal focus
- Do not let light source directions be inconsistent
- Do not let colors become saturated to "cloying"
- Do not cram too many props
- Do not include identifiable logos