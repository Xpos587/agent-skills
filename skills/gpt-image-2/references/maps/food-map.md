# Hand-Drawn City Food Map Template

This file is used to generate "a foodie map of a city / area" visual, common uses:

- Travel / food guide main visual
- Self-media traffic-driving image
- Restaurant brand campaign main visual
- Education / cultural infographic
- City IP merchandise image

Key features:

- Hand-drawn watercolor / vintage illustration style
- Numbered points + text labels
- Legend and compass rose
- Central IP (panda / city mascot / food mascot)
- Corner decorations

## Scope

- City food map
- Neighborhood food route map
- Holiday / themed event food map
- Single cuisine / single category food map (hotpot / tea / baking)

## When to Use

- User mentions "food map / foodie map / city food / restaurant exploration map"
- User wants a strong hand-drawn feel, suitable for social sharing
- User wants the sense that "one image can tell you where to eat"

Do NOT use:

- User wants a "generic city map" (use `illustrated-city-map.md`)
- User wants a "route navigation map" (use `travel-route-map.md`)
- User wants a "store distribution map" (use `store-distribution-map.md`)

## Missing Information Priority Questions

1. City / area name
2. Theme: food / trending shops / street snacks / beverages
3. Food entries: user-specified or I'll list them for you
4. Whether landmarks are needed (within 10)
5. Style: vintage parchment / modern watercolor / chibi illustration
6. Whether a central mascot is needed (panda, chili pepper, city symbol)
7. Language: Chinese / bilingual

## Main Template: Vintage Hand-Drawn City Food Map

📖 Description

Overall, a vintage-textured parchment or beige background with abstract roads, rivers, and parks drawn on it; landmarks and food items distributed as numbered mini-illustrations across the map, with a legend in the bottom-right, a mascot in the center, and plant decorations in the corners.

📝 Prompt

```json
{
  "type": "Hand-drawn map infographic",
  "goal": "Generate a high-completion city food map, usable as a travel guide / self-media hero image / city culture main visual",
  "style": "{argument name=\"art style\" default=\"Watercolor ink hand-drawn illustration on vintage parchment\"}",
  "title_section": {
    "city": "{argument name=\"city name\" default=\"Chengdu\"}",
    "title_text": "{argument name=\"map title\" default=\"Foodie Rampage Map\"}",
    "mascot": "{argument name=\"title mascot\" default=\"Cartoon red chili pepper wearing sunglasses and giving a thumbs up\"}"
  },
  "border": "{argument name=\"border decoration\" default=\"Green leaves and red chili pepper vines\"}",
  "layout": {
    "background": "{argument name=\"background description\" default=\"Textured beige parchment with yellow roads, blue rivers, and green park areas\"}",
    "sections": [
      {
        "title": "Landmarks",
        "count": "{argument name=\"landmark count\" default=\"6\"}",
        "illustrations": "{argument name=\"landmark illustrations\" default=\"Traditional pavilion, traditional temple, modern skyscraper with climbing panda, TV tower, traditional archway, industrial building\"}",
        "labels": "{argument name=\"landmark labels\" default=\"People's Park, Wenshu Monastery, IFS, 339 TV Tower, Kuanzhai Alley, Eastern Suburb Memory\"}"
      },
      {
        "title": "Food Locations",
        "count": "{argument name=\"food count\" default=\"12\"}",
        "illustrations": "{argument name=\"food illustrations\" default=\"Mapo Tofu, Red oil dumplings, Cold pot skewers, San Da Pao, Egg cake, Nine-grid hotpot, Intestine noodles, Bobo chicken, Mao cai, Covered bowl tea, Ice jelly, Rabbit head\"}",
        "labels": "{argument name=\"food labels\" default=\"1 Chen Mapo Tofu, 2 Zhong Dumplings, 3 Chunxi Road, 4 Kuanzhai Alley San Da Pao, 5 Jianshe Road Ye Popo Egg Cake, 6 Yulin Road Xiao Long Kan Hotpot, 7 Xiangxiang Alley Intestine Noodles, 8 Wuhou Shrine Street Bobo Chicken, 9 Eastern Suburb Memory Maojiao Huola, 10 People's Park Heming Teahouse, 11 Jinli Ancient Street Ice Jelly, 12 Shuangliu Old Mom Rabbit Head\"}"
      },
      {
        "title": "Legend",
        "position": "Bottom right",
        "items": ["Red dot: Food location", "Green building: Landmark attraction", "Green tree: Park/green space", "Blue line: River/lake", "Yellow double line: Main road"]
      }
    ],
    "centerpiece": "{argument name=\"centerpiece\" default=\"Giant panda sitting and eating bamboo\"}",
    "extras": [
      "{argument name=\"compass\" default=\"Vintage compass rose with N/S/E/W\"}",
      "{argument name=\"disclaimer\" default=\"Disclaimer with chili pepper icon: Friendly reminder — approach spicy food with caution, protect your stomach~\"}"
    ]
  },
  "constraints": {
    "must_keep": [
      "Food entry count must match the numbering",
      "Label text clearly readable",
      "Central mascot eye-catching but not competing with the legend position",
      "Overall maintains hand-drawn watercolor style"
    ],
    "avoid": [
      "Appearing like a real map scale (this is an illustrated map)",
      "Too many food entries causing crowding",
      "Multiple label font styles mixed together",
      "Legend missing or not corresponding to points"
    ]
  }
}
```

### Parameter Strategy

- Required: city name, theme, food list (or allow me to list), style
- Defaultable: background texture, legend, compass
- Random: specific landmark names (reasonable within the city)

### Auto-fill Strategy

- When user only provides a city name: pick 8-12 well-known foods + 6 classic landmarks for that city
- Style defaults to "vintage watercolor + beige parchment"
- Central mascot by city: Chengdu panda, Chongqing panda with hotpot, Guangzhou roast goose, Beijing dragon, Changsha stinky tofu
- Slogan no more than 12 characters

## Variant 1: Single-Category Food Map (Hotpot / Tea / Desserts)

📝 Prompt

```json
{
  "type": "Single-category food map",
  "city": "{argument name=\"city\" default=\"Chongqing\"}",
  "category": "{argument name=\"category\" default=\"Hotpot\"}",
  "title_text": "{argument name=\"title\" default=\"Hotpot Map\"}",
  "mascot": "{argument name=\"mascot\" default=\"Cartoon panda holding a red soup ladle\"}",
  "sections": [
    {
      "title": "Recommended Shops",
      "count": "{argument name=\"store count\" default=\"10\"}"
    },
    {
      "title": "Legend",
      "items": ["Red dot: Shop", "Chili count: Spice level", "Gold label: Must-eat"]
    }
  ],
  "constraints": {
    "must_feel": "Clear shop theme, do not mix in other categories"
  }
}
```

## Variant 2: Modern Flat-Style Food Map

📝 Prompt

```json
{
  "type": "Flat illustration-style food map",
  "city": "{argument name=\"city\" default=\"Shanghai\"}",
  "style": "Flat vector illustration, soft pink + beige + gray-blue",
  "title_text": "{argument name=\"title\" default=\"Weekend Shop Exploration Map\"}",
  "centerpiece": "Cartoon girl holding a map",
  "constraints": {
    "must_feel": "Suitable for Xiaohongshu / WeChat Moments sharing, clean and not vintage"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Food map auto-fill template",
  "mode": "auto-fill",
  "rule": "User only provides city, auto-determine landmarks, food list, style, and mascot",
  "constraints": {
    "must_feel": "Complete, shareable, user doesn't need to fill in any more information"
  }
}
```

## Things to Avoid

- Do NOT draw the food map to real geographic scale
- Do NOT have more than 15 food entries, too many will squeeze labels against each other
- Do NOT let the legend position overlap with landmarks
- Do NOT mix "food + routes + store distribution" three functions in one map (split into different templates)
- Do NOT make the mascot more prominent than the title (mascot is supplementary)