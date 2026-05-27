# Travel Route Map Template

This file is used to generate "a travel route / itinerary" visualization map, common uses:

- Self-drive / cycling / hiking route recommendation map
- Multi-day itinerary guide hero image
- Cross-city travel guide
- Self-media travel content cover
- Travel brand campaign visual

## Scope

- Multi-day itinerary map (D1-D7)
- Cross-city route map
- Single-day city walk route map
- Outdoor hiking / cycling route map
- Themed route (cherry blossoms, hot springs, anime pilgrimage spots, etc.)

## When to Use

- User mentions "route map / itinerary map / guide map / self-drive route"
- User wants to emphasize "sequence + time" rather than "point density"

Do NOT use:

- User wants a food map (use `food-map.md`)
- User wants a cityscape map (use `illustrated-city-map.md`)

## Missing Information Priority Questions

1. Starting point / destination / cities along the way
2. Number of days
3. Theme (food, nature, culture, family, art)
4. Transportation (self-drive / high-speed rail / flight / hiking / cycling)
5. Style: vintage hand-drawn / modern flat / chibi
6. Whether a daily highlights list is needed

## Main Template: Multi-Day Itinerary Travel Route Map

📖 Description

On the map, multiple cities or attractions connected by colored solid/dashed lines, labeled D1-Dn, each stop with a small illustration. Bottom or sidebar lists daily itinerary highlights.

📝 Prompt

```json
{
  "type": "Travel route map",
  "goal": "Generate a multi-day itinerary visualization route map, usable as a travel guide / holiday campaign hero image",
  "style": "{argument name=\"art style\" default=\"Vintage hand-drawn + watercolor + beige parchment base\"}",
  "title_section": {
    "title_text": "{argument name=\"title\" default=\"7-Day Kansai Japan Deep Dive\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"D1-D7 Food + Culture + Nature Route\"}"
  },
  "route": {
    "transport": "{argument name=\"transport\" default=\"High-speed rail + walking\"}",
    "stops": [
      "{argument name=\"stop 1\" default=\"D1 Osaka: Dotonbori Night View\"}",
      "{argument name=\"stop 2\" default=\"D2 Kyoto: Kiyomizu-dera + Gion\"}",
      "{argument name=\"stop 3\" default=\"D3 Kyoto: Arashiyama + Bamboo Grove\"}",
      "{argument name=\"stop 4\" default=\"D4 Nara: Todai-ji + Feeding Deer\"}",
      "{argument name=\"stop 5\" default=\"D5 Kobe: Kitano Ijinkan\"}",
      "{argument name=\"stop 6\" default=\"D6 Osaka: Universal Studios\"}",
      "{argument name=\"stop 7\" default=\"D7 Osaka: Return Shopping\"}"
    ],
    "line_style": "{argument name=\"route line style\" default=\"Red dashed line + dot connections\"}"
  },
  "stop_illustrations": "Each stop with a simple hand-drawn illustration, such as torii gate, temple, deer, hot spring, pagoda",
  "side_panel": {
    "enabled": "{argument name=\"side panel enabled\" default=\"true\"}",
    "position": "{argument name=\"side panel position\" default=\"Right side or bottom\"}",
    "content_type": "Daily highlights list, containing D1-Dn, 2-3 bullets per day"
  },
  "legend": {
    "items": [
      "Red dashed line: High-speed rail route",
      "Blue solid line: Walking route",
      "Gold star: Must-visit attraction",
      "Pink flower: Trending photo spot"
    ]
  },
  "extras": ["Vintage compass rose", "Short disclaimer", "Subtle patterned border"],
  "constraints": {
    "must_keep": [
      "Route order matches numbering",
      "Each stop has illustration + label",
      "Side panel daily highlights brief, no more than 3 lines each"
    ],
    "avoid": [
      "City positions showing obvious misplacement (should follow approximate geographic direction)",
      "Labels blocking the route",
      "Overly saturated colors",
      "More than 2 line types"
    ]
  }
}
```

### Parameter Strategy

- Required: starting point, destination, number of days, theme
- Defaultable: style, compass, legend
- Random: minor details in daily bullet points

### Auto-fill Strategy

- When user only provides a destination country: auto-select 5-8 classic cities
- Auto-select a matching mascot for the style
- Auto-arrange a logical route sequence (no backtracking)
- Default itinerary days to 5-7

## Variant 1: Single-Day City Walk Route

📝 Prompt

```json
{
  "type": "Single-day city walk route map",
  "city": "{argument name=\"city\" default=\"Shanghai\"}",
  "duration": "{argument name=\"duration\" default=\"Half day\"}",
  "title_text": "{argument name=\"title\" default=\"Shanghai Weekend City Walk · Wukang Road Area\"}",
  "stops": [
    "{argument name=\"stop 1\" default=\"Anfu Road\"}",
    "{argument name=\"stop 2\" default=\"Wukang Road\"}",
    "{argument name=\"stop 3\" default=\"Wuyuan Road\"}",
    "{argument name=\"stop 4\" default=\"Urumqi Middle Road\"}"
  ],
  "side_panel": {
    "enabled": true,
    "content_type": "Each point with 1 recommended reason + recommended time slot"
  },
  "constraints": {
    "must_feel": "Leisurely, photogenic, lifestyle feel"
  }
}
```

## Variant 2: Outdoor Route (Hiking / Cycling)

📝 Prompt

```json
{
  "type": "Outdoor hiking / cycling route map",
  "title_text": "{argument name=\"title\" default=\"Western Sichuan Grand Loop 7-Day Cycling\"}",
  "transport": "{argument name=\"transport\" default=\"Cycling\"}",
  "stops_count": "{argument name=\"stops count\" default=\"7\"}",
  "elevation_chart": {
    "enabled": "{argument name=\"elevation chart\" default=\"true\"}",
    "position": "Bottom"
  },
  "legend": {
    "items": [
      "Solid line: Main route",
      "Dashed line: Alternative route",
      "Triangle: Campsite",
      "Heart: Photo spot"
    ]
  },
  "constraints": {
    "must_feel": "Hardcore, outdoor, professional"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Travel route map auto-fill template",
  "mode": "auto-fill",
  "rule": "User only provides destination and number of days, auto-arrange classic route, style, and side panel highlights",
  "constraints": {
    "must_feel": "Publishable guide hero image"
  }
}
```

## Things to Avoid

- Do NOT make the route length exceed the image boundary, causing it to loop back and overlap
- Do NOT break stop numbering (must be D1 → Dn continuous)
- Do NOT make side panel text density exceed the map itself
- Do NOT mix more than 2 transportation line types (solid + dashed is enough, don't need 5)
- Do NOT draw it as a real precise scale map, the illustration style will collapse