# Means of Individualization (Средства индивидуализации)

Art. 1473–1515 Civil Code. Protect identifiers of businesses and goods. **Consumer-centric** — will the buyer be confused?

## Object Types

| Type | What it identifies | Registration | Term |
|---|---|---|---|
| Trademark / service mark | Goods and services | Mandatory (Rospatent) | 10 years + unlimited renewal |
| Trade name (фирменное наименование) | Legal entity | Automatic (upon incorporation) | While entity exists |
| Commercial name (коммерческое обозначение) | Enterprise/business | Not required (use-based) | While in use |
| Geographical indication (ГУ) | Region-based product quality | Mandatory | 10 years + renewal |
| Appellation of origin (НМПТ) | Strict region + quality link | Mandatory | While conditions met |

**Verify terms**: ConsultantPlus → Art. 1473–1515 ГК РФ.

## Trademark — Core Rules

### Distinctiveness Required
Must be capable of distinguishing goods/services of one entity from another.

### What CANNOT Be a Trademark
Generic/descriptive designations, deceptive marks, state symbols, marks contrary to public order, identical/confusingly similar to earlier marks.
Verify: Art. 1483 ГК РФ.

### Types
Word, device (image), composite, sound, 3D, color marks (rare, must acquire distinctiveness).

### Well-Known Trademarks
Recognized by Rospatent upon court request. Extended protection to ALL goods/classes. Examples: Sber, Coca-Cola.

### Dominant vs Weak Elements
When comparing marks: dominant elements carry primary consumer impression (e.g., "Sber" in "SberPay"), weak elements are common/functional (e.g., "QR" abbreviation).

## Consumer Focus — The Key Principle

Unlike copyright (creator-centered), individualization is evaluated from the **consumer's perspective**:
- Likelihood of confusion — risk consumer will mix up goods?
- No actual confusion required — selling fake Chanel at 1000₽ is infringement even if buyer knows it's fake
- Visual/aural/conceptual similarity — three-way test

## Permissible Uses of Others' Trademarks

| Use | Permissible? | Conditions |
|---|---|---|
| Comparative advertising | Generally yes | No confusion, no denigration, verifiable facts |
| Nominative use | Yes | Necessary to identify product, no endorsement suggestion |
| Descriptive use | Yes | Term used in ordinary meaning |
| Parody | Debatable | Russian courts less receptive than US/EU |
| Keyword advertising | Debatable | No binding СИП precedent; lower courts split |

**Key limitation**: No permissible use may create likelihood of confusion about source/sponsorship.

## Trade Name vs Trademark vs Commercial Name

| Feature | Trade name | Trademark | Commercial name |
|---|---|---|---|
| Object | Legal entity | Goods/services | Enterprise |
| Arises | Upon incorporation | Upon registration | Upon use |
| Registration | EGRUL (automatic) | Rospatent (mandatory) | Not required |
| Territory | Russia-wide | Registered classes | Location of enterprise |

## Geographical Indications vs Appellations of Origin

| Feature | ГУ | НМПТ |
|---|---|---|
| Quality link to region | At least partly (reputation, quality) | Strictly determined by region |
| Raw materials | May come from outside | Must come from region |

## Key Cases

- **Sber vs SberPay** — dominant "Sber", weak "QR". 1.5B₽ reversed by СИП.
- **Moscow Metro** — 19.7M₽ for using "M" on flower pots, clothing.
- **Namfleg vs Sunlight** — jewelry design copying.

See [cases.md](cases.md) for details.

## Common Mistakes

- Choosing descriptive/generic mark → cannot be registered
- Not checking existing marks before adopting → infringement risk
- Confusing trade name with trademark → different regimes
- Ignoring Madrid system → limited territorial protection

## See Also

- [copyright.md](copyright.md) — logo/design also has copyright
- [contract.md](contract.md) — licensing trademarks, franchise

## Live Verification

```bash
# Search trademarks
rospatent.py search "<trademark>" -d patents_ru       # In patent DB
rospatent.py search "<design>" -d designs_ru           # Industrial designs

# FIPS document by registration number
fips.py get <number> -d rutm --cookie "..."

# СИП litigation
sip.py search -p "<brand owner>" --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Art. 1473–1515
**International marks**: TMview (tmview.europa.eu), Madrid System (wipo.int/madrid)