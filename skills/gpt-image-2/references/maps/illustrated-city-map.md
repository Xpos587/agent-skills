# Hand-Drawn Cityscape Map Template

This file is used to generate "an overall cityscape map of a city", not focusing on food / routes / stores, but on the city itself:

- City tourism promotion image
- City culture main visual
- City IP image
- Holiday event main visual
- Education / public outreach image

Features:

- City-level coverage
- Multiple iconic landmarks distributed
- Stylized illustrations
- Center may feature a city symbol / river / mountain range

## Scope

- Overall cityscape map
- City culture main visual
- City IP identity image
- District / neighborhood-level landscape map

## When to Use

- User mentions "city map / city illustrated map / cityscape map / city main visual map"
- User wants to highlight city culture and landmarks, not food / routes

Do NOT use:

- Food theme (use `food-map.md`)
- Route theme (use `travel-route-map.md`)
- Store distribution theme (use `store-distribution-map.md`)

## Missing Information Priority Questions

1. City / area name
2. Style: vintage watercolor / modern flat / chibi / isometric 3D / Chinese heritage
3. Which landmarks to highlight (5-12)
4. Whether to include river / lake / mountain
5. Whether to include a central mascot
6. Language: Chinese / bilingual

## Main Template: Vintage Watercolor Cityscape Map

📖 Description

Overall bird's-eye-view hand-drawn city illustration, with iconic buildings distributed across the image, geographic elements (rivers, mountains, bridges) as visual backbone, and cultural elements decorating the corners.

📝 Prompt

```json
{
  "type": "Cityscape illustrated map",
  "goal": "Generate an illustrated map representing the entire city's character, usable as city culture main visual, tourism hero image, or city IP main visual",
  "style": "{argument name=\"art style\" default=\"Vintage watercolor + beige parchment\"}",
  "title_section": {
    "city": "{argument name=\"city\" default=\"Hangzhou\"}",
    "title_text": "{argument name=\"title\" default=\"Millennium Hangzhou Cityscape\"}",
    "subtitle": "{argument name=\"subtitle\" default=\"Jiangnan poetry · Between mountains and water\"}"
  },
  "geography_skeleton": {
    "rivers_or_lakes": "{argument name=\"water elements\" default=\"West Lake, Qiantang River\"}",
    "mountains": "{argument name=\"mountains\" default=\"Baoshi Mountain, Leifeng Mountain\"}",
    "main_streets": "{argument name=\"streets\" default=\"Nanshan Road, Hubin Road\"}"
  },
  "landmarks": {
    "count": "{argument name=\"landmark count\" default=\"10\"}",
    "items": "{argument name=\"landmarks\" default=\"Leifeng Pagoda, Broken Bridge, Su Causeway, Lingyin Temple, Chenghuang Pavilion, Qinghefang, Longjing Village, Hefang Street, Beijing-Hangzhou Grand Canal, Xixi Wetland\"}"
  },
  "centerpiece": "{argument name=\"centerpiece\" default=\"Center of the image reserved for West Lake and Leifeng Pagoda as the visual core\"}",
  "edge_decorations": [
    "{argument name=\"deco 1\" default=\"Jiangnan eaves silhouette\"}",
    "{argument name=\"deco 2\" default=\"Floating osmanthus blossoms\"}",
    "{argument name=\"deco 3\" default=\"Poetic calligraphy seal\"}"
  ],
  "extras": ["Vintage compass rose", "Thin line border", "City culture short phrase"],
  "constraints": {
    "must_keep": [
      "Iconic landmarks must be recognizable",
      "Relative positions of rivers / lakes / mountains cannot be seriously wrong",
      "Overall maintains hand-drawn watercolor feel"
    ],
    "avoid": [
      "Modern cars / highways / skyscrapers stealing the show",
      "Multiple label font styles",
      "Overly saturated colors"
    ]
  }
}
```

### Parameter Strategy

- Required: city name, style, landmark list (or allow me to list)
- Defaultable: corner decorations, compass, subtitle
- Random: small calligraphy seal, decorative floral elements

### Auto-fill Strategy

- When user only provides a city name: auto-select 8-12 classic landmarks + the city's most recognizable geography
- Style defaults to watercolor
- Calligraphy seal defaults to a phrase related to the city's culture

## Variant 1: Modern Flat Isometric View

📝 Prompt

```json
{
  "type": "Modern flat isometric city illustrated map",
  "city": "{argument name=\"city\" default=\"Shenzhen\"}",
  "style": "Flat vector + isometric 3D + bright blue-green tones",
  "highlights": [
    "{argument name=\"highlight 1\" default=\"Shenzhen Bay\"}",
    "{argument name=\"highlight 2\" default=\"Ping An Finance Centre\"}",
    "{argument name=\"highlight 3\" default=\"OCT Creative Park\"}"
  ],
  "constraints": {
    "must_feel": "Modern, tech, young"
  }
}
```

## Variant 2: Chinese Heritage Chibi City Map

📝 Prompt

```json
{
  "type": "Chibi Chinese heritage city illustrated map",
  "city": "{argument name=\"city\" default=\"Chengdu\"}",
  "style": "Chibi Chinese heritage + warm orange + beige, all elements anthropomorphized",
  "centerpiece": "{argument name=\"centerpiece\" default=\"Cartoon panda sitting in the center of the map\"}",
  "constraints": {
    "must_feel": "Cute, young, suitable for cultural merchandise"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Cityscape map auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides city name only, auto-determine style, landmarks, and decorations",
  "constraints": {
    "must_feel": "Can be directly used as a tourism / cultural merchandise main visual"
  }
}
```

## Things to Avoid

- Do NOT compress the city map to real precise proportions
- Do NOT draw all the city's tall buildings (visually it will collapse)
- Do NOT show obvious direction errors for rivers
- Do NOT let border decorations overpower the main image
- Do NOT cram more than 15 landmarks