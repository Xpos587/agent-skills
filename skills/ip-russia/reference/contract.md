# IP Contracts (Договоры по ИС)

Art. 1233–1244 Civil Code. Ways to transfer/license IP rights.

## Contract Types

| Contract | What transfers | Art. | Key feature |
|---|---|---|---|
| Assignment (отчуждение) | Full exclusive right | 1234 | Permanent, irrevocable |
| License (лицензионный договор) | Permission to use within scope | 1235 | Territorial/temporal limits |
| Commercial concession (коммерческая концессия) | Complex of IP rights for business | 1027 | Franchise model |
| Pledge (залог) | Exclusive right as collateral | 1232 | Security interest |

**Verify**: ConsultantPlus → Art. 1233–1244 ГК РФ.

## License Agreement — Most Common

### Required elements
- **Subject**: which IP object(s), which rights
- **Territory**: where the license applies (default: entire RF)
- **Term**: duration (default: 5 years if unspecified)
- **Scope**: exclusive vs non-exclusive
- **Remuneration**: **mandatory** — without it → contract void

### Exclusive vs Non-Exclusive

| Feature | Exclusive (исключительная) | Non-exclusive (неисключительная) |
|---|---|---|
| Licensor can use | No (if grant covers it) | Yes |
| Licensor can license to others | No | Yes |
| Licensee can sublicense | Only if expressly permitted | Only if expressly permitted |
| Registration required | Yes (for registered IP) | Yes (for registered IP) |

## Assignment Agreement

- Transfers **entire** exclusive right (not a license)
- **Cannot transfer moral rights** — they stay with author forever
- Must be in writing; registration required for registered IP
- Author can terminate if assignee fails to use the work (limited cases)

## Commercial Concession (Franchise)

- Transfer of complex of IP rights (trademark, trade name, know-how, etc.)
- For use in business; must be registered with Rospatent
- Franchisor controls quality standards

## Registration Requirements

| IP Object | Assignment | License |
|---|---|---|
| Copyright/computer program | Not required | Not required |
| Patent | Rospatent registration | Rospatent registration |
| Trademark | Rospatent registration | Rospatent registration |
| Know-how | Not required | NDA sufficient |

## Common Mistakes

- License without remuneration → **void**
- Forgetting to register patent/trademark license → ineffective against third parties
- Assigning "copyright" but meaning "license" → words matter
- Not specifying territory/scope → defaults apply (may not be what you want)

## See Also

- [copyright.md](copyright.md) — moral rights (inalienable even in assignment)
- [patent-law.md](patent-law.md) — patent licensing specifics
- [individualization.md](individualization.md) — trademark licensing, franchise

## Live Verification

```bash
# Check if trademark/patent is registered before licensing
rospatent.py search "название" -d patents_ru

# Check for disputes on IP rights being transferred
sip.py search -p "правообладатель" --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Art. 1233–1244
**Register assignment/license**: Rospatent (fips.ru)