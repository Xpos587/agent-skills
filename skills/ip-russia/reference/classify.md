# Classify Command

Classify an IP object → determine legal regime, rights, terms, criteria.

## Workflow

```
User describes object/idea/creation
│
├─ Step 1: Identify the object type
│   └─ Use the classification tree in SKILL.md
│
├─ Step 2: Determine legal regime
│   ├─ Copyright? → reference/copyright.md
│   ├─ Patent? → reference/patent-law.md
│   ├─ Related rights? → reference/related-rights.md
│   ├─ Individualization? → reference/individualization.md
│   ├─ Atypical? → reference/atypical-objects.md
│   └─ Not in Art. 1225? → No IP protection
│
├─ Step 3: Check criteria
│   ├─ Copyright: creative character? form vs content?
│   ├─ Patent: novelty? inventive step? industrial applicability?
│   ├─ Trademark: distinctiveness? not descriptive?
│   └─ Know-how: commercial value? secrecy maintained?
│
├─ Step 4: Output classification card
│
└─ Step 5: Check registries
    ├─ rospatent.py search — prior art, existing marks
    └─ sip.py search — related litigation
```

## Classification Card (output template)

```markdown
## Classification Result

| Field | Value |
|---|---|
| **Object** | [what user described] |
| **Legal regime** | [copyright / patent / related rights / individualization / atypical / none] |
| **Civil Code articles** | [specific articles] |
| **Criteria met** | [which criteria apply] |
| **Criteria at risk** | [which criteria might not be met] |
| **Registration required** | [yes/no] |
| **Protection term** | [duration] |
| **Rights arising** | [exclusive / moral / other] |
| **Next steps** | [what to do to secure protection] |
```

## Common Classification Scenarios

| User says | Classification |
|---|---|
| "I wrote an app" | Computer program → copyright (no registration needed) |
| "I have a new algorithm" | Idea → NOT protectable. Code → copyright. Technical solution → patent? |
| "I designed a logo" | Industrial design (3D) OR trademark (identifies business) OR copyright (artwork) |
| "My company name" | Trade name (automatic in EGRUL) + consider trademark registration |
| "I have a recipe" | Know-how (if secret) OR patent (if meets criteria) — not copyright |
| "I made a database" | Copyright (creative arrangement) + sui generis (substantial investment) |
| "A new plant breed" | Selection achievement → mandatory registration with Минсельхоз |
| "My teaching method" | NOT protectable — methods/ideas excluded from IP |

## Edge Cases

- **Software + hardware**: algorithm = not patentable, but technical effect from software-hardware interaction may be
- **Logo as both copyright and trademark**: dual protection possible
- **Database of facts**: facts not copyrightable, but creative arrangement + investment may be
- **Fashion design**: copyright (artistic) + industrial design (if registered)

## Live Verification

```bash
# Search existing patents/trademarks (prior art, conflicting marks)
rospatent.py search "название" -d patents_ru

# Check for related litigation in СИП
sip.py search -p "название" --cookie "..."
```