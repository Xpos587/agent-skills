# Protect Command

Step-by-step checklist for protecting an IP object: registration, documentation, deadlines, enforcement.

## Workflow

```
User identifies object to protect
│
├─ Step 1: Classify the object
│   └─ Use classify workflow if unclear
│
├─ Step 2: Load matching reference
│   ├─ Copyright → reference/copyright.md
│   ├─ Patent → reference/patent-law.md
│   ├─ Trademark → reference/individualization.md
│   └─ etc.
│
├─ Step 3: Generate protection checklist
│
└─ Step 4: Recommend enforcement strategy
```

## Protection Checklists by Type

### Copyright / Computer Program
- Fix work in tangible medium (write, save, publish)
- Document authorship (git commits, dated drafts)
- Add copyright notice (© Year Author) — optional but helpful
- Consider notary deposit (for evidence of creation date)
- Register computer program with Rospatent (optional, for evidence)
- Keep creation records
- If commissioned → check work-for-hire rules (Art. 1296)
- If employee-created → check service work rules (Art. 1295)
- License/assign rights in writing

### Patent
- **Do NOT publicly disclose before filing** — destroys novelty
- Conduct prior art search (FIPS, Espacenet, Google Patents)
- Draft application (description, claims, drawings, abstract)
- File with Rospatent — get priority date
- Request substantive examination within 3 years (inventions)
- Pay filing fees
- Pay annual maintenance fees (year 3+ for inventions, year 1+ for utility models)
- Monitor for infringement
- Consider international filing (PCT, Hague) within 12 months

### Trademark
- Conduct trademark search (FIPS, TMview) before adoption
- Ensure distinctiveness
- File application with Rospatent (name, image, classes)
- Respond to office actions
- Publish for opposition
- Receive registration certificate
- Use commercially (3-year non-use = cancellation risk)
- Renew every 10 years
- Monitor for confusingly similar marks
- Consider Madrid system for international protection

### Know-How
- Identify what constitutes the secret
- Implement physical security (access control, restricted areas)
- Implement digital security (access logs, encryption, watermarks)
- Mark documents "confidential" / "commercial secret"
- NDAs with specific clauses for all employees
- Limit access on need-to-know basis
- Document measures taken (evidence of "reasonable measures")
- Include know-how clauses in contracts
- Train employees on secrecy obligations
- Departure procedures (exit interviews, reminder of obligations)

### Database
- Document investment in obtaining/verifying/presenting data
- Implement access controls (API keys, rate limits, ToS)
- Monitor for unauthorized scraping
- Keep records of database structure development
- Check if creative arrangement → also copyrightable

## Enforcement Strategy

| Stage | Action | Timing |
|---|---|---|
| Pre-litigation | Cease-and-desist letter (досудебная претензия) | Immediately |
| Litigation | File claim (general jurisdiction or arbitration) | Within 3 years of knowledge |
| Urgent | Request preliminary injunction (обеспечительные меры) | Before or with claim |
| After judgment | Enforcement via bailiffs (ФССП) | After judgment enters force |

## Key Deadlines

Verify current deadlines: ConsultantPlus → relevant ГК РФ articles.

| Action | Deadline | Missing = |
|---|---|---|
| Patent examination request | 3 years from filing | Application withdrawn |
| Patent annual fees | Year 3+ (inventions), year 1+ (utility models) | Patent lapses |
| Trademark renewal | Every 10 years | Registration cancelled |
| Infringement claim | 3 years from knowledge | Time-barred |
| Convention priority (patent) | 12 months from first filing | Priority lost |
| Convention priority (trademark) | 6 months from first filing | Priority lost |

## Live Verification

```bash
# Search prior art before filing
rospatent.py search "ключевые слова" -d patents_ru

# Check if similar mark already registered
rospatent.py search "название бренда" -d patents_ru

# Check for existing litigation
sip.py search -p "ваша компания" --cookie "..."
```

**Filing**: Rospatent (fips.ru) | **Collective rights**: RAO (rao.ru), VOIS (vois.ru)