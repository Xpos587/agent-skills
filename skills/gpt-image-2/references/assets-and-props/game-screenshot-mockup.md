# In-Game Screenshot Mockup Template

This file is used for "faking an in-game screenshot" visuals:

- Open world game screenshots
- RPG battle screenshots
- Pixel / voxel game screenshots
- Visual novel screenshots
- Game UI mockups

Characteristics:

- Overall looks "like a real in-game screen"
- Includes game UI (HUD / quest panel / health bar / minimap)
- Has camera language (first-person / third-person / top-down / isometric)
- Emphasizes game feel rather than pure illustration
- Usually with text bubbles / quest prompts

## Scope

- In-game screenshot mockups
- Game promotional images (fake screenshots)
- Game project demo visuals
- Livestream thumbnails (fake game screens)

## When to use

- User mentions "game screenshot / game screenshot / mockup / HUD / UI"
- User wants it to "look like a game screen" rather than illustration

Do NOT use for:

- Anime KV → use `storyboards-and-sequences/anime-key-visual.md`
- Game project pitch → use `grids-and-collages/anime-pitch-board.md`
- Character design → use `portraits-and-characters/character-sheet.md`

## Missing Information Priority Question Order

1. Game type (open world / RPG / pixel / visual novel / simulation)
2. Camera (first-person / third-person / top-down / isometric)
3. Scene (outdoor / indoor / city / battle)
4. Main character description (if any)
5. UI elements (HUD / health bar / quest / minimap)
6. Aspect ratio

## Main Template: Open World Game Screenshot

Description

One image simulating a real in-game screenshot, including HUD UI.

Prompt

```json
{
  "type": "open world game screenshot",
  "goal": "Generate a visual that looks like a real in-game screenshot",
  "game_meta": {
    "game_name": "{argument name=\"game name\" default=\"FROZEN FANTASIA\"}",
    "engine_feel": "{argument name=\"engine feel\" default=\"modern AAA engine (close to Unreal 5 rendering)\"}",
    "perspective": "{argument name=\"perspective\" default=\"third-person over-shoulder\"}"
  },
  "scene": {
    "environment": "{argument name=\"environment\" default=\"snowfield + distant castle + aurora\"}",
    "time_of_day": "{argument name=\"time\" default=\"dusk\"}",
    "weather": "{argument name=\"weather\" default=\"light snow\"}",
    "lighting": "{argument name=\"lighting\" default=\"cool blue key light + warm gold rim light\"}"
  },
  "character": {
    "description": "{argument name=\"character\" default=\"female protagonist, silver-white long hair, back facing, drawing sword\"}",
    "position": "lower third of frame, back facing the distance"
  },
  "ui_elements": {
    "hud": {
      "enabled": "{argument name=\"hud enabled\" default=\"true\"}",
      "items": [
        "{argument name=\"hud item 1\" default=\"lower left: health bar + mana bar + character portrait\"}",
        "{argument name=\"hud item 2\" default=\"lower right: 4 skill slots + item bar\"}",
        "{argument name=\"hud item 3\" default=\"upper left: minimap (circular) + current coordinates\"}",
        "{argument name=\"hud item 4\" default=\"upper right: quest tracker - 'Find the Source of Spring'\"}"
      ]
    },
    "subtitle": {
      "enabled": "{argument name=\"subtitle enabled\" default=\"true\"}",
      "speaker": "{argument name=\"speaker\" default=\"fox companion\"}",
      "text": "{argument name=\"subtitle text\" default=\"Ahead is the Frozen Gorge, be careful\"}"
    },
    "interaction_prompt": {
      "enabled": "{argument name=\"prompt enabled\" default=\"true\"}",
      "text": "{argument name=\"prompt\" default=\"Press [E] to investigate\"}"
    }
  },
  "style": {
    "rendering": "{argument name=\"rendering\" default=\"PBR rendering + high dynamic range + subtle film grain\"}",
    "color_palette": "{argument name=\"color palette\" default=\"ice blue + moon white + warm gold\"}"
  },
  "aspect_ratio": "{argument name=\"aspect ratio\" default=\"16:9\"}",
  "constraints": {
    "must_keep": [
      "Looks like an in-game screenshot (with real HUD)",
      "HUD and scene colors do not conflict",
      "Subtitle font and HUD font unified",
      "Character and scene proportions correct"
    ],
    "avoid": [
      "Looks like a static illustration (no HUD)",
      "HUD elements > 8",
      "Mixed UI styles (pixel + modern in same frame)",
      "Subtitles too long / typos"
    ]
  }
}
```

### Parameter Strategy

- Must ask: game type, camera, scene
- Can default: UI elements, subtitles, color palette
- Can randomize: environment details

### Auto-Fill Strategy

- User gives game concept → auto-decide camera / HUD / subtitles
- Default 16:9
- Default modern AAA rendering

## Variant 1: Pixel Game Screenshot

Prompt

```json
{
  "type": "pixel game screenshot",
  "game_meta": {
    "engine_feel": "16-bit JRPG style (like Secret of Mana 3)",
    "perspective": "top-down / isometric"
  },
  "style": {
    "rendering": "pixel art + 16-color palette",
    "color_palette": "16-color retro RPG palette"
  },
  "ui_elements": {
    "hud": {
      "items": ["bottom dialog box + character portrait"]
    }
  },
  "constraints": {
    "must_feel": "FC / SNES JRPG"
  }
}
```

## Variant 2: Visual Novel Screenshot

Prompt

```json
{
  "type": "visual novel screenshot",
  "game_meta": {
    "engine_feel": "Galgame / Visual Novel",
    "perspective": "first-person (looking at character)"
  },
  "ui_elements": {
    "hud": null,
    "subtitle": {
      "enabled": true,
      "speaker": "{argument name=\"speaker\" default=\"heroine\"}",
      "text": "..."
    }
  },
  "style": {
    "rendering": "anime semi-thick painting + soft light"
  },
  "constraints": {
    "must_feel": "VN standard dialogue scene"
  }
}
```

## Variant 3: Auto-Fill Mode

Prompt

```json
{
  "type": "game screenshot auto-fill",
  "mode": "auto-fill",
  "rule": "User gives one-sentence game concept, auto-decide camera / scene / HUD / main character",
  "constraints": {
    "must_feel": "usable as Steam store screenshot"
  }
}
```

## Things to Avoid

- Do not let HUD elements exceed 8
- Do not let UI style disconnect from game type (pixel games should not have modern frosted glass HUD)
- Do not let subtitles exceed 2 lines
- Do not let the main character take up too much of the frame, overwhelming the HUD
- Do not let the "screenshot" look like a static illustration (HUD is the key identifier)
- Do not let the quest panel have obvious typos / garbled text
