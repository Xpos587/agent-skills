# Patent Law (Патентное право)

Art. 1345–1392 Civil Code. Protects inventions, utility models, and industrial designs. Mandatory registration.

## Object Types

| Type | Criteria | Term | Art. |
|---|---|---|---|
| Invention (изобретение) | Novelty + inventive step + industrial applicability | 20 years (extendable for pharma/pesticides) | 1350 |
| Utility model (полезная модель) | Novelty + industrial applicability | 10 years (NOT extendable) | 1351 |
| Industrial design (промышленный образец) | Novelty + originality | 5+5+5+5 = up to 25 years | 1352 |

**Verify current terms**: ConsultantPlus → Art. 1350–1352 ГК РФ (terms can change).

## Criteria

- **Novelty**: Not in prior art (worldwide). Prior art = everything publicly available before priority date.
- **Inventive step**: Not obvious to person skilled in the art. Key differentiator from utility models.
- **Industrial applicability**: Can be used in industry/agriculture. Not purely theoretical.

## Software Patentability

Computer programs "as such" excluded (Art. 1350). Technical solution via software CAN be patented if **technical effect** in material world.

| Claim | Patentable? |
|---|---|
| "A sorting algorithm" | No — mathematical method |
| "A program that sorts data" | No — computer program as such |
| "Method of controlling industrial equipment using [algorithm]" | Maybe — technical effect |

**Strategy**: Copyright for code + know-how for algorithms. Patent only if clear technical effect beyond computing.

## What Cannot Be Patented

Discoveries, scientific theories, mathematical methods, game rules, computer programs as such, aesthetic solutions, plant/animal breeds, surgery/therapy methods (but products for these CAN be patented).

Verify: Art. 1350 §5 ГК РФ for full exclusion list.

## Key Differences: Invention vs Utility Model

| Aspect | Invention | Utility Model |
|---|---|---|
| Inventive step required | Yes | No |
| Examination | Substantive | Formal only |
| Term | 20 years | 10 years |
| Protection strength | Higher | Lower (easier to invalidate) |

## Common Mistakes

- Utility model ≠ invention with shorter term — different criteria, weaker protection
- Disclosing before filing destroys novelty
- Ignoring maintenance fees → patent lapses
- Patent = right to exclude, NOT right to use (may still need licenses from others)

## See Also

- [copyright.md](copyright.md) — software, artistic works
- [atypical-objects.md](atypical-objects.md) — know-how alternative
- [contract.md](contract.md) — licensing patents

## Live Verification

```bash
# Search prior art
rospatent.py search "<keywords>" -d patents_ru
rospatent.py search "<keywords>" -d patents_all     # International

# Industrial designs
rospatent.py search "<design>" -d designs_ru

# FIPS — patent document by number
fips.py get <number> -d rupat --cookie "..."
fips.py get <number> -d rupm --cookie "..."    # Utility model

# СИП litigation
sip.py search -p "<applicant>" --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Art. 1345–1392
**Additional**: Espacenet (epo.org), Google Patents (patents.google.com)