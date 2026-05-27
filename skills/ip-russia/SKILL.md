---
name: ip-russia
description: "Use when the user asks about intellectual property in Russian legal context — what to protect, how to register, whether a use is infringing, or which IP regime applies. Triggers on: 'нарушение авторских прав', 'запатентовать', 'товарный знак', 'лицензионный договор', 'ноу-хау', 'программа для ЭВМ', 'компенсация за нарушение', 'СИП', 'Роспатент', 'исключительное право', IP, copyright, patent, trademark, trade secret, infringement, register, protect."
user-invocable: true
argument-hint: "[command] [target]"
---

Russian intellectual property law: classification, protection, audit, contracts, case law. Based on Civil Code Part 4 + international treaties + Court for Intellectual Property (СИП) practice.

## When NOT to Use

- Criminal IP liability (Art. 146, 147 УК РФ) — this skill covers civil law only
- Tax implications of IP transactions
- Detailed procedural law (specific court filings, deadlines for appeals)
- Non-Russian jurisdictions beyond brief treaty references
- Antitrust/competition law (though it intersects with IP)

## Setup

Before any IP analysis, verify context:

| Gate | Check | If fail |
|---|---|---|
| Jurisdiction | User specified Russia or context implies Russian law | Clarify jurisdiction before proceeding |
| Object type | Object of IP is identified or can be inferred | Run `classify` first |
| Register | Matching reference loaded for command | Load before continuing |

## Core Principles (apply to every analysis)

5 principles that thread through all Russian IP law:

1. **Immateriality** — IP object ≠ material carrier. Buying a book ≠ becoming the author. Rights to an idea ≠ rights to a thing.
2. **Triad of rights** — exclusive right (proprietary, alienable) + moral rights (inalienable: authorship, name, integrity) + other rights (right of follow-up, access, remuneration).
3. **Exclusive right = monopoly** — rightsholder may permit AND prohibit. Absence of prohibition ≠ consent. Silence ≠ license.
4. **Closed list** — Art. 1225 Civil Code. Only enumerated objects. Not on the list → no IP protection.
5. **Creative vs commercial objects** — copyright/patent: creator figure, creativity criterion. Means of individualization: consumer-focus — will the buyer be confused?

## Object Classification (Art. 1225 Civil Code)

```
What do you have?
│
├─ Creative result?
│   ├─ Work of science/literature/art → copyright [reference/copyright.md]
│   ├─ Computer program / database → copyright (special regime) [reference/copyright.md]
│   ├─ Performance / phonogram / broadcasting → related rights [reference/related-rights.md]
│   ├─ Invention / utility model / industrial design → patent law [reference/patent-law.md]
│   ├─ Selection achievement → atypical objects [reference/atypical-objects.md]
│   └─ Integrated circuit layout → atypical objects [reference/atypical-objects.md]
│
├─ Commercial designation?
│   ├─ Trademark / service mark → means of individualization [reference/individualization.md]
│   ├─ Trade name → means of individualization [reference/individualization.md]
│   ├─ Geographical indication / appellation of origin → means of individualization [reference/individualization.md]
│   └─ Commercial name → means of individualization [reference/individualization.md]
│
├─ Production secret? → know-how (ноу-хау) [reference/atypical-objects.md]
│
└─ Not in Art. 1225? → IP protection does NOT apply
```

## Commands

| Command | Category | Description | Reference |
|---|---|---|---|
| `classify [object]` | Analyze | Classify: type of rights, protection regime, terms, criteria | [reference/classify.md](reference/classify.md) |
| `audit [situation]` | Analyze | Risk audit: infringement? whose rights? remedies? | [reference/audit.md](reference/audit.md) |
| `protect [object]` | Build | Checklist: registration, protection, documents, deadlines | [reference/protect.md](reference/protect.md) |
| `contract [type]` | Build | Contract: license, assignment, commercial concession | [reference/contract.md](reference/contract.md) |
| `cases [situation]` | Evaluate | Similar court cases with analysis | [reference/cases.md](reference/cases.md) |
| `checklist` | Evaluate | Full IP checklist across all object types | [reference/checklist.md](reference/checklist.md) |

### Routing rules

1. **No argument**: render command table. Ask what they need.
2. **First word matches command**: load its reference, follow instructions. Everything after command = target.
3. **First word doesn't match**: general invocation. Run `classify` implicitly, then apply matching reference.

## International Framework

Russia is party to key treaties:

| Treaty | Objects | Key norms |
|---|---|---|
| Berne Convention (1886) | Copyright | National treatment, protection without formalities |
| WIPO Convention (1967) | All objects | Definition of IP, structure |
| TRIPS (1994) | All + trade aspects | Minimum standards, enforcement |
| Paris Convention (1883) | Patents, trademarks | Convention priority, national treatment |
| Madrid Agreement (1891) | Trademarks | International registration |

**National treatment principle**: foreign rightsholders get the same rights as Russian citizens.

## Live Verification

Don't memorize law — verify live. Three registries with API access.

```bash
# Rospatent Search Platform (no auth)
python3 <skill-dir>/scripts/rospatent.py search "нейронная сеть" -d patents_ru     # Patents
python3 <skill-dir>/scripts/rospatent.py search "антивирус" -d programs              # Computer programs
python3 <skill-dir>/scripts/rospatent.py sources                                     # All datasets
python3 <skill-dir>/scripts/rospatent.py suggest "нейро"                             # Autocomplete

# kad.arbitr.ru / СИП (DDoS-Guard — use --cdp or --cookie)
python3 <skill-dir>/scripts/sip.py search -p "Сбербанк" --cdp                  # Auto-extract cookies from Chromium
python3 <skill-dir>/scripts/sip.py search --judge "Пашкова" --cookie "..."     # Manual cookies

# FIPS register (get works without auth; search experimental)
python3 <skill-dir>/scripts/fips.py get 106651 -d rude          # Industrial design (no auth)
python3 <skill-dir>/scripts/fips.py get 2761234 -d rupat --cdp # Invention patent (auto-extract)
python3 <skill-dir>/scripts/fips.py search number 106651 -d rude --cookie "..."
python3 <skill-dir>/scripts/fips.py dbs                          # List all databases
```

| Registry | Auth | Method |
|---|---|---|
| Rospatent Search Platform | None | `rospatent.py` direct |
| kad.arbitr.ru (СИП) | DDoS-Guard | `--cdp` (auto) or `--cookie` (manual) |
| fips.ru | DDoS-Guard (partial) | `get` no auth / `--cdp` or `--cookie` for `search` |

Full API reference: [reference/registry-api.md](reference/registry-api.md). Scripts: [scripts/rospatent.py](scripts/rospatent.py), [scripts/sip.py](scripts/sip.py), [scripts/fips.py](scripts/fips.py).

## Quick Reference: Key Numbers

Verify current terms live — law changes. These are baseline values as of 2025:

| Object | Term (baseline) | Registration | Verify live |
|---|---|---|---|
| Copyright | Life + 70 yrs | No | ConsultantPlus / ГАРАНТ |
| Related rights | 50 yrs | No | ConsultantPlus / ГАРАНТ |
| Invention | 20 yrs | Yes | `rospatent.py search` / fips.ru |
| Utility model | 10 yrs | Yes | fips.ru |
| Industrial design | up to 25 yrs | Yes | fips.ru |
| Trademark | 10 yrs + renewal | Yes | fips.ru / TMview |
| Know-how | Perpetual (while secret) | No | N/A — contract-based |
