# Store Distribution Map Template

This file is used to generate "brand / restaurant / retail store distribution within an area" visualizations:

- Chain brand store distribution
- Franchise recruitment map
- City / business district store coverage
- Holiday event reachable store markers
- Bank / charging station / shared facility distribution

## Scope

- Nationwide / provincial / city-level store distribution
- Single business district store distribution
- Franchise recruitment showcase
- Regional service coverage map

## When to Use

- User mentions "store distribution / branch network / coverage map / store map / franchise recruitment"
- User wants one image to clearly show "where stores are located"
- User wants to highlight store density and brand coverage

Do NOT use:

- Food exploration map (use `food-map.md`)
- Route map (use `travel-route-map.md`)
- Cityscape map (use `illustrated-city-map.md`)

## Missing Information Priority Questions

1. Area: nationwide / provincial / city / business district
2. Brand name + logo description
3. Store type: flagship / standard / pop-up / franchise
4. Store count and specific names (or allow me to list)
5. Whether legend distinguishing store types is needed
6. Style: brand color modern flat / realistic map / infographic style

## Main Template: Modern Flat Brand Store Distribution Map

📖 Description

Base map is a simplified regional outline, stores marked with brand-colored pins / icons, paired with brand info card + legend.

📝 Prompt

```json
{
  "type": "Brand store distribution map",
  "goal": "Generate a store distribution visualization map that can be directly used for brand website / franchise brochure / holiday event",
  "brand": {
    "name": "{argument name=\"brand name\" default=\"AURA Coffee\"}",
    "logo_description": "{argument name=\"brand logo\" default=\"Gold coffee bean + brand wordmark\"}",
    "brand_color": "{argument name=\"brand color\" default=\"Warm brown + cream white\"}"
  },
  "scope": {
    "region": "{argument name=\"region scope\" default=\"Nationwide\"}",
    "base_map_style": "{argument name=\"base map style\" default=\"Simplified province outlines + light color fill\"}"
  },
  "stores": {
    "total_count": "{argument name=\"total stores\" default=\"168\"}",
    "by_type": [
      "{argument name=\"flagship\" default=\"8 Flagship stores\"}",
      "{argument name=\"standard\" default=\"120 Standard stores\"}",
      "{argument name=\"pop_up\" default=\"12 Pop-up stores\"}",
      "{argument name=\"franchise\" default=\"28 Franchise stores\"}"
    ],
    "highlight_cities": "{argument name=\"highlight cities\" default=\"Beijing, Shanghai, Guangzhou, Shenzhen, Chengdu, Hangzhou\"}"
  },
  "marker_design": {
    "shapes": "Round brand-colored pins + different sizes representing different types",
    "rule": "Size ranking: Flagship > Standard > Pop-up > Franchise"
  },
  "info_panel": {
    "enabled": "{argument name=\"info panel enabled\" default=\"true\"}",
    "position": "{argument name=\"info panel position\" default=\"Right side\"}",
    "content": [
      "Total store count",
      "Cities covered",
      "New openings in the past year",
      "Top 5 key cities"
    ]
  },
  "legend": {
    "items": [
      "Large dot: Flagship",
      "Medium dot: Standard",
      "Triangle: Pop-up",
      "Square: Franchise"
    ]
  },
  "extras": ["Brand logo corner badge", "Franchise contact area"],
  "constraints": {
    "must_keep": [
      "Store density realistic and reasonable (not dense dots everywhere nationally)",
      "Brand color strictly unified",
      "Legend matches store types",
      "Key cities clearly readable"
    ],
    "avoid": [
      "Base map details overwhelming the stores",
      "Non-brand colors appearing",
      "Markers too dense to read",
      "Missing legend"
    ]
  }
}
```

### Parameter Strategy

- Required: brand, area, store count, brand color
- Defaultable: legend style, info panel content
- Random: city ranking, minor decorations

### Auto-fill Strategy

- When user only provides brand name: auto-set 100-200 store level, key cities select Top 5-10
- If brand color not specified, use industry-common color (coffee brown, milk tea pink, retail blue, medical green)
- Legend minimum 2 items, maximum 5 items

## Variant 1: Single Business District Density Map

📝 Prompt

```json
{
  "type": "Business district store density map",
  "scope": {
    "region": "{argument name=\"district\" default=\"Shanghai · Jing'an Temple District\"}"
  },
  "stores": {
    "total_count": "{argument name=\"store count\" default=\"24\"}",
    "highlight_cities": "Store specific names + numbering"
  },
  "constraints": {
    "must_feel": "Localized, density feel, neighborhood level"
  }
}
```

## Variant 2: Service Coverage Map (Charging Stations / Branches / Service Points)

📝 Prompt

```json
{
  "type": "Service coverage distribution map",
  "service": {
    "name": "{argument name=\"service name\" default=\"NEX Charging Network\"}",
    "color": "{argument name=\"service color\" default=\"Tech blue + highlight yellow\"}"
  },
  "stations_count": "{argument name=\"station count\" default=\"800+\"}",
  "marker_design": {
    "shapes": "Lightning icon + different colors representing charging speed levels"
  },
  "legend": {
    "items": ["Yellow: Supercharger", "Blue: Fast charge", "Gray: Slow charge"]
  },
  "constraints": {
    "must_feel": "Tech, professional, reliable"
  }
}
```

## Variant 3: Auto-fill Mode

📝 Prompt

```json
{
  "type": "Store distribution map auto-fill template",
  "mode": "auto-fill",
  "rule": "User provides brand + industry, auto-estimate store scale, brand color, legend",
  "constraints": {
    "must_feel": "Franchise brochure grade"
  }
}
```

## Things to Avoid

- Do NOT make point density unrealistic (small brands should not look nationwide full of dots)
- Do NOT let the brand logo get drowned in map details
- Do NOT mix multiple different industry brands on one map
- Do NOT let the info panel take up more than 1/3 of the frame
- Do NOT use real map screenshot style (this is a brand map, not a GIS screenshot)