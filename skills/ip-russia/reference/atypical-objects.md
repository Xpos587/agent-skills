# Atypical Objects (Нетипичные объекты ИС)

Objects that don't fit neatly into copyright, patent, or individualization categories.

## Object Types

| Object | Legal basis | Registration | Term | Key criterion |
|---|---|---|---|---|
| Know-how (ноу-хау / секрет производства) | Art. 1465–1467 | Not required | Perpetual (while secret) | Commercial value + secrecy |
| Selection achievement (селекционное достижение) | Art. 1414–1415 | Mandatory (Минсельхоз) | 30–35 years | Distinctness + uniformity + stability |
| IC layout (топология ИМС) | Art. 1448–1451 | Optional (Rospatent) | 10 years | Originality |

**Verify**: ConsultantPlus → Art. 1401–1467 ГК РФ.

## Know-How (Trade Secret)

### What qualifies
- **Commercial value** because it is secret
- **Not generally known** or easily accessible
- Holder takes **reasonable measures** to maintain secrecy (NDA, access control, marking)

### Rights
- No exclusive right to prohibit independent discovery
- Can license (requires NDA from licensee)
- Protection = contract-based + unfair competition law

### vs Patent strategy

| Factor | Patent | Know-how |
|---|---|---|
| Reverse engineering | Protected | Lost if reverse-engineered |
| Disclosure | Published | Kept secret |
| Term | Fixed (20 years) | Perpetual (while secret) |
| Independent creation | Infringement | Not infringement |
| Cost | High | Low |

**Rule of thumb**: If reverse engineering reveals the solution → patent. If it remains hidden (Coca-Cola formula, algorithms) → know-how.

**Key**: Once secret is out → protection ends. No restoration.

## Selection Achievements

- Plant/animal breeds developed through breeding
- Must be distinct, uniform, stable
- Registered with Ministry of Agriculture (Минсельхоз) via State Commission
- **Farmers' privilege**: can save seed for own use (limited)

## IC Layouts

- Three-dimensional design of integrated circuits
- Protection for original (creatively created) layouts
- Registration optional but provides evidence
- Reverse engineering for compatibility = not infringement

## Common Mistakes

- Relying solely on know-how for reverse-engineerable tech → patent instead
- Not implementing actual secrecy measures → know-how protection fails
- Know-how cannot be "registered" → registration defeats the purpose
- Independent discovery of know-how is NOT infringement

## See Also

- [patent-law.md](patent-law.md) — patent vs know-how decision
- [copyright.md](copyright.md) — trade secret overlaps with copyright
- [contract.md](contract.md) — NDAs and know-how licensing

## Live Verification

```bash
# IC topology search
rospatent.py search "<topology keywords>" -d topologies

# СИП litigation
sip.py search -p "<company>" --cookie "..."

# FIPS topology document
fips.py get <number> -d vz --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Art. 1401–1467
**Selection achievements**: FIPS (fips.ru) — separate register