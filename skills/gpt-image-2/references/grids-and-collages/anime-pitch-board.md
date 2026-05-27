# Anime Project Pitch Board Template

This file is used for "presenting poster + characters + settings + copy in a single image" project-level document visuals:

- Anime / game project pitch
- IP full setting document
- Film project pitch deck single page
- Publisher new work proposal
- Animation studio in-house proposal

Characteristics:

- One large image divided into multiple sections
- Main section: poster / KV
- Secondary sections: character cards / settings / worldview
- Copy section: title + tagline + log line
- Looks like a "professional project document" rather than a single image

## Scope

- Anime / game project pitch
- Film proposal
- IP full proposal

## When to use

- User mentions "project pitch / pitch / proposal / full settings / one image tells the whole work"
- User wants "project document-level" visuals

Do NOT use for:

- Single KV image → use `storyboards-and-sequences/anime-key-visual.md`
- Character design sheet → use `portraits-and-characters/character-sheet.md`
- Relationship diagram → use `storyboards-and-sequences/character-relationship-diagram.md`
- General marketing poster → use `poster-and-campaigns/brand-poster.md`

## Missing Information Priority Question Order

1. Work title + one-line tagline
2. Genre + type (sci-fi / school / post-apocalyptic / ...)
3. Main character count + character descriptions
4. Worldview / era
5. Style base
6. Whether Japanese / English / Chinese titles needed

## Main Template: Anime Project Pitch Board

Description

One large image, divided into KV main section + character card section + worldview section + copy section.

Prompt

```json
{
  "type": "Anime Project Pitch Board",
  "goal": "Generate a single-page full visual document that can serve as an anime / game project pitch",
  "ip": {
    "title": "{argument name=\"title\" default=\"Frost White Fantasia\"}",
    "title_localized": "{argument name=\"title localized\" default=\"FROZEN FANTASIA\"}",
    "tagline": "{argument name=\"tagline\" default=\"This snow has fallen for a thousand years\"}",
    "logline": "{argument name=\"logline\" default=\"In a kingdom of eternal winter, a girl who forgot her name meets a fox that can understand the snow, and together they set out to find the source of spring\"}",
    "genre": "{argument name=\"genre\" default=\"Fantasy / Healing / Adventure\"}"
  },
  "regions": {
    "main_kv": {
      "position": "{argument name=\"kv position\" default=\"upper 60%\"}",
      "content": "{argument name=\"kv content\" default=\"Female protagonist standing in the snowfield, frozen castle in background, fox at her feet\"}",
      "style": "cinematic poster-grade anime thick painting"
    },
    "character_cards": {
      "position": "{argument name=\"character region\" default=\"lower left\"}",
      "count": "{argument name=\"character count\" default=\"3\"}",
      "items": [
        "{argument name=\"char 1\" default=\"Female protagonist · Frost white hair · Amnesia\"}",
        "{argument name=\"char 2\" default=\"Swordsman companion · Black hair · Guardian\"}",
        "{argument name=\"char 3\" default=\"Fox companion · Snow white · Spirit medium\"}"
      ],
      "card_design": "rounded square avatar + name + one-line intro"
    },
    "world_setting": {
      "position": "{argument name=\"world region\" default=\"lower right\"}",
      "content": "{argument name=\"world content\" default=\"A floating kingdom sealed by winter for a thousand years, the only living things are drifting snow and auroras\"}",
      "extras": ["map thumbnail (optional)", "3 key prop icons"]
    },
    "title_block": {
      "position": "{argument name=\"title position\" default=\"top center of image\"}",
      "components": ["main title (large)", "localized title", "tagline (small italic)"]
    },
    "footer_meta": {
      "position": "bottom",
      "content": "{argument name=\"footer\" default=\"PRESENTED BY · X STUDIO · 2026\"}"
    }
  },
  "style": {
    "art_style": "{argument name=\"art style\" default=\"modern anime + semi-realistic + thick painting background\"}",
    "color_palette": "{argument name=\"color palette\" default=\"ice blue + moon white + warm gold\"}",
    "typography": "title serif + body sans"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"3:4\"}",
  "constraints": {
    "must_keep": [
      "KV section is always the visual anchor",
      "Character cards have unified style",
      "Information sections are clear, not confused",
      "Color palette strictly unified"
    ],
    "avoid": [
      "Too much information squeezing the KV section",
      "Character card style drift",
      "Title font > 2 types",
      "Missing tagline / logline"
    ]
  }
}
```

### Parameter Strategy

- Must ask: work title, tagline, main characters
- Can default: layout, style, color palette, fonts
- Can randomize: background details

### Auto-Fill Strategy

- User gives one-sentence work concept → auto-expand title + tagline + logline + main characters + worldview
- Default KV occupies 60% + character cards + worldview sections
- Default portrait 3:4

## Variant 1: Game Project Pitch

Prompt

```json
{
  "type": "Game project pitch board",
  "regions": {
    "main_kv": {"content": "game key visual + core gameplay scene"},
    "character_cards": {"content": "playable characters + intro"},
    "world_setting": {"content": "core gameplay loop + key systems"}
  },
  "constraints": {
    "must_feel": "GDC pitch level"
  }
}
```

## Variant 2: Film/TV Project Pitch

Prompt

```json
{
  "type": "Film project pitch board",
  "regions": {
    "main_kv": {"content": "film key visual"},
    "character_cards": {"content": "main characters + actor candidates"},
    "world_setting": {"content": "era + art references"}
  },
  "constraints": {
    "must_feel": "presentable to investors"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "Pitch board auto-fill",
  "mode": "auto-fill",
  "rule": "User gives one-sentence work concept, auto-expand all sections",
  "constraints": {
    "must_feel": "presentable as formal pitch deck cover page"
  }
}
```

## Things to Avoid

- Do not let the KV section be squeezed below 50%
- Do not let character card styles drift
- Do not let information sections become confused
- Do not omit tagline / logline
- Do not let the color palette exceed 4 main colors
- Do not let title fonts exceed 2 types