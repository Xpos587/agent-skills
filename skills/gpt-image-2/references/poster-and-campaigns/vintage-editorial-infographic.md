# Vintage Archival / Editorial Infographic Poster Template

This file is used to generate "vintage infographic posters themed around historical figures / scientific concepts / classic theories, presented in 1940s Bell Labs archival / old newspaper / blueprint / museum publication style."

Typical uses:

- Scientist / thinker tribute poster (Shannon / Turing / Curie / Lu Xun...)
- Classic theory visualization (information theory / quantum mechanics / evolution)
- Course / publication / museum educational poster
- Knowledge popularization SNS / social media share image
- Vintage-style cultural / creative merchandise and peripherals

Features (comparison with existing poster / infographic templates):

| Template | Style |
|---|---|
| `editorial-cover.md` (existing) | Modern magazine cover |
| `infographics/legend-heavy-infographic.md` (existing) | High-density educational infographic (modern or natural) |
| `infographics/bento-grid-infographic.md` (existing) | Bento-grid modular (modern) |
| **This template** (new) | **Vintage archival / blueprint / old newspaper / museum educational poster** |

**Keywords**: 1940s style, aged paper, ink linework, engraved portrait, navy + charcoal, measurement ticks, formula, archival stamp.

## Scope

- Historical figure + thought / theory tribute poster
- Vintage blueprint / old newspaper / museum publication style educational image
- Scientific concept visualization (with formulas / charts / timelines)
- Cultural / creative merchandise / educational publishing / academic tribute

## When to Use

- User mentions "vintage infographic / tribute poster / old newspaper style / blueprint style / museum poster"
- Poster theme is a historical figure / classic theory
- Want "high text density + vintage texture"

Do NOT use:

- Modern flat infographic → use `infographics/legend-heavy-infographic.md`
- Modern bento grid → use `infographics/bento-grid-infographic.md`
- Pure magazine cover → use `editorial-cover.md`
- Taoist / mystical diagrams → use classical Chinese painting style (recommend natural language prompting, do not force this template)

## Missing Information Priority Questions

1. Theme figure / concept (Claude Shannon / Turing / Lu Xun...)
2. Core theory / formula / model (determines central diagram)
3. Historical period and archival style (**1940s Bell Labs / 1900s old newspaper / vintage blueprint / museum publication / academic manuscript**)
4. Whether a timeline is needed (historical context of the theory)
5. Whether a portrait is needed (if real faces not allowed → use face censor block / engraved silhouette)
6. Aspect ratio (**16:9 landscape exhibition board / 3:4 portrait poster**)
7. Primary language (English / Chinese / bilingual)

## Main Template: Vintage Archival Infographic Poster (Figure + Model + Formula + Timeline)

📖 Description

Wide-format poster with left archival sidebar + center hero model + right formula box + mid-lower theory sections + bottom timeline, including portrait + multiple charts + vintage paper texture.

📝 Prompt

```json
{
  "type": "vintage editorial infographic poster",
  "goal": "Generate a vintage archival / 1940s publication style educational poster, densely combining figure / theory / formula / application timeline into one image",
  "subject": "{argument name=\"subject\" default=\"Claude Shannon and information theory\"}",
  "style": {
    "era": "{argument name=\"era\" default=\"1940s Bell Labs archival poster\"}",
    "look": "{argument name=\"paper look\" default=\"aged cream paper, blueprint drafting grid, thin ink linework, muted navy and charcoal printing, subtle stains and paper wear, technical illustration mixed with newspaper editorial design\"}",
    "rendering": "high-detail diagrammatic collage with engraved portrait, scientific charts, labeled panels, and hand-drawn signal graphics"
  },
  "poster": {
    "headline": "{argument name=\"headline\" default=\"Claude Shannon — The Architecture of Information\"}",
    "subheadline": "{argument name=\"subheadline\" default=\"How uncertainty became measurable, and communication became engineering.\"}",
    "topRightMeta": {
      "note": "{argument name=\"meta note\" default=\"NOTE TOSELF No. 6713–2\"}",
      "date": "{argument name=\"meta date\" default=\"MAY 1948\"}",
      "subject": "{argument name=\"meta subject\" default=\"A Mathematical Theory of Communication\"}"
    }
  },
  "layout": {
    "sections": [
      {
        "title": "left archival sidebar",
        "position": "far left vertical column",
        "count": 5,
        "labels": [
          "{argument name=\"sidebar 1\" default=\"BELL LABORATORIES MURRAY HILL, N.J.\"}",
          "{argument name=\"sidebar 2\" default=\"ENGINEERING THE INTANGIBLE\"}",
          "{argument name=\"sidebar 3\" default=\"CLAUDE E. SHANNON 1916–2001\"}",
          "{argument name=\"sidebar 4\" default=\"TOOLS OF THE INFORMATION AGE\"}",
          "{argument name=\"sidebar 5\" default=\"quote panel with hand-set type\"}"
        ]
      },
      {
        "title": "{argument name=\"model title\" default=\"THE COMMUNICATION MODEL\"}",
        "position": "upper middle wide panel",
        "count": 5,
        "labels": ["1 INFORMATION SOURCE", "2 ENCODER", "3 CHANNEL", "4 DECODER", "5 DESTINATION"]
      },
      {
        "title": "{argument name=\"formula title\" default=\"ENTROPY: THE MEASURE OF UNCERTAINTY\"}",
        "position": "upper right box",
        "count": 4,
        "labels": [
          "{argument name=\"formula\" default=\"H(X) = −Σ p(x) log2 p(x)\"}",
          "PROBABILITY DISTRIBUTION p(x)",
          "MORE EVEN → MORE MAXED UNCERTAINTY",
          "MORE LOPSIDED → LESS UNCERTAINTY"
        ]
      },
      {
        "title": "lower theory panels",
        "position": "middle to lower band",
        "count": 3,
        "labels": [
          "{argument name=\"theory A\" default=\"A ENTROPY — uncertainty before a message is known\"}",
          "{argument name=\"theory B\" default=\"B NOISE — randomness that corrupts transmission\"}",
          "{argument name=\"theory C\" default=\"C Redundancy & Error Correction — structure added so signals can survive failure\"}"
        ]
      },
      {
        "title": "{argument name=\"timeline title\" default=\"THEORY THAT TRANSFORMED CIVILIZATION\"}",
        "position": "bottom horizontal timeline",
        "count": 8,
        "labels": [
          "{argument name=\"era 1\" default=\"1840s TELEGRAPHY\"}",
          "{argument name=\"era 2\" default=\"1876+ TELEPHONE NETWORKS\"}",
          "{argument name=\"era 3\" default=\"1930s–40s DIGITAL COMPUTERS\"}",
          "{argument name=\"era 4\" default=\"1950s–60s SATELLITE COMMUNICATION\"}",
          "{argument name=\"era 5\" default=\"1970s INTERNET PROTOCOLS\"}",
          "{argument name=\"era 6\" default=\"1980s–90s DATA COMPRESSION\"}",
          "{argument name=\"era 7\" default=\"1990s–2000s CRYPTOGRAPHY\"}",
          "{argument name=\"era 8\" default=\"2010s+ AI & INFORMATION SYSTEMS\"}"
        ]
      }
    ],
    "centerpiece": "{argument name=\"centerpiece description\" default=\"a large abstract cloud of blue and gray signal noise, dots, lines, and waveforms behind the communication model, with arrows moving left to right through the five stages\"}"
  },
  "visualElements": {
    "portrait": {
      "subject": "{argument name=\"portrait subject\" default=\"Claude Shannon\"}",
      "placement": "left-center",
      "style": "{argument name=\"portrait style\" default=\"black-and-white archival seated portrait at a desk with the face intentionally obscured by a pale square censor block, wearing suit and tie, writing on paper\"}"
    },
    "objectsLeft": [
      "{argument name=\"object 1\" default=\"rotary telephone on desk\"}",
      "{argument name=\"object 2\" default=\"open notebook or papers\"}",
      "{argument name=\"object 3\" default=\"technical console with CRT screen and knobs behind portrait\"}",
      "{argument name=\"object 4\" default=\"small icon row of 4 tools: oscilloscope, signal meter, relay, punched tape\"}"
    ],
    "centerModel": [
      "book and symbols under source",
      "binary digits under encoder",
      "large noisy channel cloud with wave overlays",
      "binary digits and interpretation under decoder",
      "light bulb icon under destination"
    ],
    "chartsAndDiagrams": [
      "bar chart for entropy probabilities",
      "two low vs high entropy mini bar charts",
      "tree diagram and entropy notation",
      "signal distortion sketches labeled thermal noise / cross talk / distortion",
      "error-correction binary pipeline from original message to recovered message"
    ],
    "bottomDecor": ["small waveform legend with sine wave, digital signal, and noise", "archival stamp or footer on lower right"]
  },
  "color": {
    "background": "{argument name=\"paper color\" default=\"warm ivory paper\"}",
    "primaryInk": "{argument name=\"primary ink\" default=\"dark navy\"}",
    "secondaryInk": "{argument name=\"secondary ink\" default=\"charcoal gray\"}",
    "accent": "{argument name=\"accent ink\" default=\"faded steel blue\"}"
  },
  "composition": "symmetrical wide poster with dense boxed annotations, fine border lines, and a museum-quality educational infographic feel",
  "textDensity": "very high, with many small labels, formulas, captions, and historical notes in a carefully organized grid",
  "aspectRatio": "{argument name=\"aspect ratio\" default=\"16:9 landscape\"}",
  "constraints": {
    "must_keep": [
      "Vintage 1940s printing texture (aged paper / grid / pen lines / ink tones)",
      "Formula / model / timeline / portrait all 4 elements present and clearly readable",
      "Overall color strictly limited to ivory + 1 primary ink + 1 secondary ink + 1 accent",
      "If using real person, face treated with censor block / engraved silhouette / blur"
    ],
    "avoid": [
      "Using modern flat icons / gradients → immediately destroys vintage texture",
      "Formula written incorrectly or missing (LaTeX characters must be clearly described in prompt)",
      "Timeline exceeding 8 nodes causing each node to be unreadable",
      "Portrait area too large crushing information density (should be ≤ 25% total area)",
      "Using neon / fluorescent colors"
    ]
  }
}
```

### Parameter Strategy

- **Required**: subject, headline, formula / model / timeline specific content
- **Defaultable**: era, paper look, portrait style, centerpiece description
- **Random**: sidebar 5 small text lines, bottom decor

### Auto-fill Strategy

- User provides subject figure → auto-infer core model / formula / timeline
- Portrait treatment not specified → default censor block face obscuration (avoid real face generation failure)
- Paper / ink color not specified → use template default ivory + navy + charcoal + steel blue

## Variant 1: Chinese Scholar / Literati Tribute Edition (Lu Xun / Qian Xuesen / Shen Kuo...)

📝 Prompt

```json
{
  "type": "vintage editorial infographic poster, Chinese scholar tribute edition",
  "subject": "{argument name=\"chinese subject\" default=\"Lu Xun and the Modern Vernacular Movement\"}",
  "style_override": {
    "era": "1920s Chinese New Culture Movement period publications",
    "look": "aged rice-yellow xuan paper with woodblock printing effect, red seal stamps, vertical traditional or simplified Chinese mixed with English annotation notes",
    "ink": "Ink black + vermilion red + gray-green"
  },
  "language_override": "Chinese primary + English small annotations",
  "extra_elements": ["traditional seal stamps", "vertical titles", "brush signature", "thread-bound book border decoration"]
}
```

### When to choose this variant

- Chinese scholars / literati / historical figures
- Education / publishing / cultural tribute
- Want "Eastern literati style" rather than "Western archival style"

## Variant 2: 3:4 Portrait Fine Print Poster (suitable for print / cultural merchandise)

📝 Prompt

```json
{
  "type": "vintage editorial infographic poster, vertical print edition",
  "aspectRatio_override": "3:4 portrait poster",
  "layout_override": {
    "structure": "top hero portrait + middle theory section + bottom timeline; sidebar moved to bottom strip",
    "headline_position": "very top, large serif"
  },
  "use_case": "Can be used as limited edition print poster / cultural merchandise product"
}
```

### When to choose this variant

- Cultural merchandise for sale (A2 / A3 print poster)
- Educational institution classroom display
- Want a "wall-mountable" finished product

## Variant 3: Museum Exhibition Panel Edition (bilingual, more educational)

📝 Prompt

```json
{
  "type": "museum exhibition panel infographic",
  "language": "bilingual (English + primary language)",
  "extra_sections": ["Acknowledgments / Thanks", "Further Reading / Extended Reading", "QR code square (museum app)"],
  "must_keep": ["All annotations bilingual side-by-side", "Bottom acknowledgments / source credits must appear"]
}
```

### When to choose this variant

- Real museum / exhibition publications
- Educational institution course display panels
- Academic tribute scenarios

## Things to Avoid

- Using gradients / neon / modern flat icons → immediately destroys vintage feel
- Drawing the figure too large, occupying 50%+ area → model / formula / timeline should dominate, portrait is supplementary
- Formula written incorrectly or missing (core theory must be readable)
- Timeline nodes > 10 → unreadable, keep to 6-8
- Letting GPT generate real faces → prioritize censor block / engraving / blur
- Using only one font size → vintage posters must have 4-5 levels of hierarchy
- Using modern web fonts (should describe as serif / hand-set / engraved type)
- Misspelling the subject figure's name (names appearing multiple times must be explicitly spelled out in the prompt)
