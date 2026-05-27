# Copyright (Авторское право)

Art. 1255–1302 Civil Code. Protects works of science, literature, and art — regardless of merit or purpose.

## Key Rules

**Protection of form, not content.** Copyright protects the expression, not the underlying idea or data.

**No formalities required.** Copyright arises automatically upon creation. No registration needed (Berne Convention).

**Presumption of creativity.** A result of intellectual labor is presumed creative until proven otherwise. Rebuttable.

**Independence from merit.** Both a masterpiece and a mediocre work get the same copyright protection.

## Rights

### Moral rights (личные неимущественные) — inalienable
- Right of authorship, right to name, right to inviolability, right of publication, right of withdrawal
- Verify current list: ConsultantPlus → Art. 1265–1269 ГК РФ

### Exclusive right — proprietary, alienable, licensable
- Author can use, authorize, prohibit. Transferable by contract or law.
- Term: life of author + 70 years (from Jan 1 of year following author's death)

### Other rights
- Right of access (visit museum to reproduce art), right of follow-up (% on resale), right to remuneration
- Verify: Art. 1292–1294 ГК РФ

## Computer Programs & Databases

- **Computer program** = set of instructions, protected as literary work (Art. 1261)
- **Database** = structured collection, protected if creative arrangement; sui generis if not (Art. 1262)
- Code theft proof: visual source comparison, file dates, sizes, checksums

## Free Uses (exceptions)

Free uses change — verify current list in Art. 1273–1280.1 ГК РФ. Key categories:

| Use | Key condition |
|---|---|
| Quotation | Scientific/polemic/critical, with attribution, proportionate |
| Personal use | Single copy, not commercial. **Excludes**: architecture, databases, programs, full books, pro video |
| Library/archive | Preservation, replacement (Art. 1275) |
| Educational | Brief excerpts, attribution |
| Public space works | Buildings/monuments permanently in public view (Art. 1276) |
| Parody | Free use for parody (Art. 1274) |
| Ceremonial | Music at official/religious ceremonies (Art. 1277) |
| Judicial | Legal proceedings (Art. 1278) |
| Orphan works | Unknown author, specific conditions (Art. 1280.1) |

## Common Mistakes

- Buying physical copy ≠ transferring copyright
- Registration not required (but can serve as evidence)
- No copyright notice ≠ no copyright
- Free use ≠ unlimited personal use

## See Also

- [patent-law.md](patent-law.md) — functional/technical aspects
- [related-rights.md](related-rights.md) — performers, phonograms, broadcasting
- [atypical-objects.md](atypical-objects.md) — know-how vs copyright
- [contract.md](contract.md) — licensing and assigning copyright
- [cases.md](cases.md) — Prosveshcheniye, Varlamov, VKontakte cases

## Live Verification

```bash
# Search registered programs/databases
rospatent.py search "<program name>" -d programs
rospatent.py search "<database name>" -d copyrights_db

# Check СИП litigation
sip.py search -p "<author/company>" --cookie "..."

# FIPS document lookup
fips.py get <number> -d evm --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Part 4, Art. 1255–1302
**Authorship evidence**: notarized deposit, registration with RAO (rao.ru)
