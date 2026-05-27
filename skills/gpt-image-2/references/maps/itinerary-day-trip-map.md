# Day Trip / Single-Day Itinerary Map Template (Left Stops + Right Scene Map)

This file is used to generate "a portrait 2:3 day trip guide poster, left half is itinerary cards (5 numbered stops + time + description), right half is a fantasy-realism landscape map (same 5 markers matching)".

Typical uses:

- Scenic area / national park / ancient town day trip recommendation poster
- Tourism bureau / cultural tourism campaign main visual
- WeChat Official / Xiaohongshu long-form content cover
- Travel brand / B&B / OTA day itinerary asset
- Holiday check-in route sharing image
- Travel journal cover / trip souvenir poster

Characteristics (compared to existing maps templates):

| Template | Nature |
|---|---|
| `travel-route-map.md` (existing) | **Multi-day itinerary** (D1-D7) cross-city route, emphasis on sequence + time |
| `food-map.md` (existing) | **Food map** (high shop density) |
| `illustrated-city-map.md` (existing) | **Cityscape map** (landmark illustrations) |
| `store-distribution-map.md` (existing) | **Store distribution map** |
| **This template** (new) | **Single-day split poster**: left itinerary card + right fantasy-realism map, 5-7 stops strictly aligned |

**Core distinction**: This template is a "single-day itinerary + vintage travel poster aesthetics + dual-column strict alignment" visual paradigm, best suited for scenic area day trips, national park itineraries, and city walk single-day plans.

## Scope

- Single-day itinerary (5-7 stops)
- Scenic area / national park / mountain / ancient town day trip
- City walk single-day plan
- Tourism bureau / travel brand campaign
- Vintage illustration style / national park poster aesthetics

## When to Use

- User explicitly says "day trip / one-day itinerary / single-day itinerary / one-day check-in"
- Wants vintage illustration + parchment + dual-column split design
- Moderate number of stops (recommended 5-7)
- Needs time + description + icon per stop

Do NOT use:

- Multi-day itinerary (D1-D7) → use `travel-route-map.md`
- Food map (high density, no strong sequence) → use `food-map.md`
- City landmark illustrations (not emphasizing routes) → use `illustrated-city-map.md`
- Store distribution (commercial) → use `store-distribution-map.md`

## Missing Information Priority Questions

1. Destination (scenic area / city / national park name)
2. Title copy (Chinese / Japanese / English ...)
3. Number of stops (recommended 5; max 7)
4. Each stop "name + time + one-sentence Chinese description + small illustration subject"
5. Overall route theme (nature / history / food / pilgrimage / photography)
6. Style tone (vintage illustration / national park poster / watercolor / Art Nouveau / parchment)
7. Color scheme (warm sepia + gold / emerald + gold / blue-white snow mountain)
8. Bottom stats (total distance / steps / elevation / estimated time)
9. Whether compass rose / decorative border / vintage seal is needed

## Main Template: 5-Stop Vertical Split Day Trip Poster

📖 Description

Portrait 2:3 poster, left half is parchment itinerary card (title + 5 numbered stations, each with circular numbered badge + small illustration + name + time in parentheses + Chinese description), right half is fantasy-realism landscape scene (golden winding path connecting 5 markers, each marker strictly matching the left column's number + name). Bottom-right corner with compass rose + stats info box. Overall sepia + gold + jade vintage travel poster aesthetics.

📝 Prompt

```json
{
  "type": "vintage illustrated travel itinerary poster, vertical split layout",
  "goal": "Generate a day trip guide poster with left itinerary card / right fantasy-realism map, 5 stops with strict number alignment, usable as scenic area / national park / city day trip main visual",
  "language": "{argument name=\"language\" default=\"Traditional Chinese\"}",
  "destination": {
    "name": "{argument name=\"destination name\" default=\"Alishan National Scenic Area\"}",
    "duration": "{argument name=\"duration\" default=\"1 day\"}",
    "theme": "{argument name=\"trip theme\" default=\"mountain forest railway and sunset cloud sea\"}"
  },
  "headline": {
    "main": "{argument name=\"headline text\" default=\"Alishan National Scenic Area Day Trip\"}",
    "tagline": "{argument name=\"tagline\" default=\"One mountain, five classic sights. An unforgettable fantasy journey.\"}",
    "divider": "small decorative mountain divider beneath the tagline"
  },
  "style": {
    "overall": "{argument name=\"art style\" default=\"premium tourism poster, painterly digital illustration, nostalgic national-park brochure aesthetic\"}",
    "left_panel_look": "{argument name=\"left look\" default=\"parchment-textured itinerary card in warm beige with ornate gold Art Nouveau borders and dark brown typography\"}",
    "right_panel_look": "{argument name=\"right look\" default=\"dramatic painted fantasy-realism map scene of a mountain journey at sunrise and sunset tones\"}",
    "color_palette": "{argument name=\"color palette\" default=\"warm sepia, gold, jade green, deep brown, cream, soft sunset orange\"}",
    "atmosphere": "layered mountain ranges, mist-filled valleys, evergreen forests, golden-hour light, luminous cloud seas, romantic painterly atmosphere"
  },
  "layout": {
    "format": "vertical 2:3 poster, split into two equal vertical columns",
    "left_panel": {
      "type": "itinerary card",
      "header": ["headline title centered top", "tagline beneath", "decorative mountain divider"],
      "stop_count": 5,
      "stop_design": [
        "circular black-and-gold number badge",
        "small vignette illustration",
        "bold location name in headline font",
        "time in parentheses beside name",
        "1-2 sentence Chinese description"
      ],
      "border": "ornate gold Art Nouveau frame with corner flourishes"
    },
    "right_panel": {
      "type": "painted map scene",
      "background": "continuous mountain landscape at sunrise to sunset gradient",
      "path": "glowing golden winding path connecting all numbered markers in order",
      "marker_design": "black-and-gold marker plaques with number + same location name as left panel",
      "compass_rose": "decorative compass rose labeled N E S W at bottom-right",
      "stats_box": "dark green and gold information box at bottom-right corner"
    },
    "alignment_rule": "the 5 numbered stops on the left must match the 5 numbered markers on the right exactly in order, label, and visual identity"
  },
  "stops": {
    "count": 5,
    "items": [
      {
        "number": 1,
        "name": "{argument name=\"stop 1 name\" default=\"Alishan Station\"}",
        "time": "{argument name=\"stop 1 time\" default=\"8:00 AM\"}",
        "description": "{argument name=\"stop 1 desc\" default=\"Begin the journey to explore ancient trees and forests.\"}",
        "left_vignette": "{argument name=\"stop 1 left vignette\" default=\"wooden mountain railway station\"}",
        "right_scene": "{argument name=\"stop 1 right scene\" default=\"a rustic alpine wooden station perched on a cliff among pine forests\"}"
      },
      {
        "number": 2,
        "name": "{argument name=\"stop 2 name\" default=\"Alishan Forest Railway\"}",
        "time": "{argument name=\"stop 2 time\" default=\"9:30 AM\"}",
        "description": "{argument name=\"stop 2 desc\" default=\"Journey through the forest, experience a century-old railway.\"}",
        "left_vignette": "{argument name=\"stop 2 left vignette\" default=\"red-and-black steam train\"}",
        "right_scene": "{argument name=\"stop 2 right scene\" default=\"a small steam locomotive traveling on a curved mountain railway with smoke drifting upward\"}"
      },
      {
        "number": 3,
        "name": "{argument name=\"stop 3 name\" default=\"Sacred Tree Area Boardwalk\"}",
        "time": "{argument name=\"stop 3 time\" default=\"11:30 AM\"}",
        "description": "{argument name=\"stop 3 desc\" default=\"Stroll beneath millennium-old giant trees, feel the forest spirit.\"}",
        "left_vignette": "{argument name=\"stop 3 left vignette\" default=\"giant cedar trees and elevated wooden boardwalk\"}",
        "right_scene": "{argument name=\"stop 3 right scene\" default=\"towering ancient red cypress trees with a spiral and zigzag wooden walkway around the trunks\"}"
      },
      {
        "number": 4,
        "name": "{argument name=\"stop 4 name\" default=\"Sister Lakes\"}",
        "time": "{argument name=\"stop 4 time\" default=\"1:30 PM\"}",
        "description": "{argument name=\"stop 4 desc\" default=\"Enjoy the serene lake scenery, listen to nature's symphony.\"}",
        "left_vignette": "{argument name=\"stop 4 left vignette\" default=\"tranquil forest lake and pavilion\"}",
        "right_scene": "{argument name=\"stop 4 right scene\" default=\"an emerald lake surrounded by dense forest with a small pavilion and arched bridge\"}"
      },
      {
        "number": 5,
        "name": "{argument name=\"stop 5 name\" default=\"Xiaoliyuan Mountain Lookout\"}",
        "time": "{argument name=\"stop 5 time\" default=\"4:00 PM\"}",
        "description": "{argument name=\"stop 5 desc\" default=\"Take in the magnificent mountain views and cloud sea, watch the sunset.\"}",
        "left_vignette": "{argument name=\"stop 5 left vignette\" default=\"wooden observation deck above clouds at sunset\"}",
        "right_scene": "{argument name=\"stop 5 right scene\" default=\"a lookout deck on a peak above a sea of clouds, facing a glowing sunset\"}"
      }
    ]
  },
  "footer_box": {
    "compass_rose": "decorative compass labeled N / E / S / W at bottom-right of map panel",
    "stats_box": {
      "design": "dark green and gold information box",
      "stats": [
        "{argument name=\"stat 1\" default=\"Total distance ~9 km / 5.6 miles\"}",
        "{argument name=\"stat 2\" default=\"Estimated time Full day - 14,500 steps\"}"
      ]
    }
  },
  "constraints": {
    "must_keep": [
      "5 stops strictly aligned: left numbering / name / sequence = right marker",
      "Portrait 2:3 split layout, left and right equal width",
      "Left parchment + gold Art Nouveau border + numbered badges",
      "Right winding golden path connecting all markers (in numbered order)",
      "Bottom-right corner with compass + stats box",
      "Overall vintage travel poster aesthetics (sepia + gold)",
      "Title language, font, and color scheme remain consistent",
      "Each stop name identical across left and right columns"
    ],
    "avoid": [
      "Left and right numbering misaligned / name drift",
      "Right-side path not connecting all markers",
      "Marker count not matching left-side stop count",
      "Breaking the 2:3 split layout (left/right unequal width / misaligned)",
      "Using modern minimalist style on the parchment card (breaks vintage tone)",
      "Making the itinerary map just a simple map (must have complete landscape realism scene)",
      "Missing time / description text",
      "Squeezing a multi-day itinerary into one image (use travel-route-map.md instead)"
    ]
  }
}
```

### Parameter Strategy

- **Required**: destination name, headline, 5 stops (name + time + desc + left vignette + right scene)
- **Defaultable**: style overall, left/right look, color palette, stats, tagline, language
- **Random**: tagline text, stats numbers (unless user provides actual data)

### Auto-fill Strategy

- User says "I want a XX day trip" → infer 5 stops from popular attractions (morning → evening time chain)
- User doesn't provide times → auto-progress at 8:00 / 9:30 / 11:30 / 1:30 PM / 4:00 PM
- No language specified → default to the official language of the destination (Taiwan → Traditional Chinese, Kyoto → Japanese, Paris → French, New York → English)
- No stats specified → give reasonable estimates (5km-15km / 8000-15000 steps)

## Variant 1: 7-Stop City Walk Edition (Walking + Food / Culture)

📝 Prompt

```json
{
  "type": "city walk one-day itinerary poster, vertical split layout",
  "stops_count": 7,
  "transport": "walking only",
  "stop_design": ["each stop adds estimated walking minutes between previous and current"],
  "right_scene_override": "vintage illustrated city map with streets, buildings, parks, and golden walking path threading through 7 markers",
  "use_case": "Kyoto city walk / Paris Left Bank / Tokyo shitamachi one-day stroll route"
}
```

### When to choose this variant

- Urban walking route
- More stops (6-7)
- Emphasis on streets / alleys / food / cafe culture

## Variant 2: Horizontal 16:9 Dual-Column (suitable for website banner / PPT hero)

📝 Prompt

```json
{
  "type": "horizontal split itinerary banner, 16:9",
  "layout_override": {
    "format": "horizontal 16:9 wide",
    "split": "left 40% itinerary card, right 60% map scene",
    "stops_arrangement": "left card lists 5 stops in 1 vertical column"
  },
  "use_case": "Scenic area website hero / PPT presentation / video opening image"
}
```

### When to choose this variant

- Horizontal format (website banner / presentation opening)
- No need for portrait social sharing

## Variant 3: Watercolor Japanese Style (Cherry Blossom / Onsen / Shrine)

📝 Prompt

```json
{
  "type": "Japanese watercolor one-day itinerary poster",
  "style_override": {
    "art_style": "delicate Japanese watercolor with soft sumi-e ink lines, sakura pastel palette",
    "color_palette": "soft pink, mint, indigo, cream, gold accents",
    "left_panel_look": "washi paper card with cherry blossom decorations and elegant kanji typography",
    "right_panel_look": "hazy mountain shrine and onsen valley painted in watercolor with cherry blossom drifting"
  },
  "use_case": "Kyoto cherry blossom day trip / Hakone onsen day trip / Kamakura temple pilgrimage"
}
```

### When to choose this variant

- Japanese theme / cherry blossom / onsen / shrine
- Wants softer watercolor Japanese aesthetics
- Does NOT want vintage Western Art Nouveau tone

## Things to Avoid

- Left and right numbering misaligned / name drift
- Right-side path not connecting all markers (must be a golden path connecting them in order)
- Breaking the 2:3 split layout (left and right must be equal width)
- Squeezing a multi-day itinerary into one image (**use `travel-route-map.md`**)
- Squeezing a food map into this template (**use `food-map.md`**)
- Missing time / description / stats
- Using modern minimalist style on the parchment card
- Drawing the right side as a simple line map (must be a complete landscape realism scene painting)
- Letting the model freely generate stops (must explicitly list each stop's name + time + desc + left vignette + right scene)
- More than 7 stops (visual density too high)