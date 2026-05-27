# Moodboard Guide

Reference gathering workflow for landing page visual direction.

## Search Strategy

### Primary Search Terms

For each project, search across 3-4 term categories:

| Category | Purpose | Example |
|---|---|---|
| Mood/tone | Atmosphere + emotion | "serene workspace morning light" |
| Color palette | Brand color direction | "navy gold corporate" |
| Layout ref | Composition ideas | "SaaS hero left text right image" |
| Typography cue | Font style direction | "minimal sans serif hero" |

### Provider Rotation

| Provider | Best For | Rate Limit |
|---|---|---|
| Pexels | Lifestyle, workspace, nature | 200/hr |
| Unsplash | Artistic, atmospheric, diverse | 50/hr |
| Pixabay | Varied, high volume | 5000/hr |

Run all configured providers in parallel per search.

## Moodboard Presentation Format

```
## Moodboard: [Project Name]

### Direction: [1-2 sentence summary]

| # | Image | Source | Key Takeaway |
|---|---|---|---|
| 1 | [Description] | Pexels / Author | Warm tones, morning light |
| 2 | [Description] | Unsplash / Author | Clean geometry, minimal |
| ... |

### Color Palette (extracted)
- Primary: #HEX
- Secondary: #HEX
- Accent: #HEX
- Background: #HEX

### Confirmed Direction
[Summary of chosen direction before generation]
```

## Niche Reference Libraries

Common niches and their typical reference needs:

| Niche | Hero Style | Color Direction | Typical Mood |
|---|---|---|---|
| SaaS | Dashboard in context | Blue/indigo/white | Trust, clarity, efficiency |
| E-Commerce | Product lifestyle | Brand-dependent | Desire, simplicity, speed |
| Fintech | Abstract data/money | Dark blue/gold/green | Trust, growth, security |
| Health/Fitness | Active people | Green/blue/white | Energy, vitality, freshness |
| Education | Learning environment | Blue/orange/yellow | Growth, curiosity, approachability |
| Creative Agency | Bold visuals | Vibrant, varied | Innovation, boldness, artistry |

## Stock Search Tips

1. **Orientation**: Search `landscape` for desktop refs, `portrait` for mobile refs
2. **Color**: Use Pexels `color` parameter to match brand palette
3. **Locale**: Use Pexels `locale` for localized content (e.g., `ja` for Japan)
4. **Attribution**: Always include — `Photo by [Author](url) on [Provider]`

## From References to Prompts

After confirming moodboard direction, translate visual direction into generation prompts:

1. Extract 3-5 keywords from reference takeaways
2. Map color palette to prompt color terms
3. Identify composition pattern (split hero / centered / asymmetric)
4. Note lighting style (soft studio / natural / dramatic / neon)
5. Specify negative constraints (no text, no watermarks, no people if needed)
6. Build per-breakpoint prompt using [[art-direction]]