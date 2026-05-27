# Audit Command

Assess IP infringement risk: analyze situation → identify rights holders → evaluate liability → recommend actions.

## Workflow

```
User describes situation/action/product
│
├─ Step 1: Identify all IP objects involved
│   ├─ What is the user creating/using?
│   ├─ What existing IP might be affected?
│   └─ Use classify if object type unclear
│
├─ Step 2: Map rights holders
│   ├─ Who owns the relevant IP?
│   ├─ Are rights valid and in force?
│   └─ Any licenses/assignments recorded?
│
├─ Step 3: Assess infringement risk
│   ├─ Is the use within free use exceptions?
│   ├─ Likelihood of confusion (trademarks)?
│   ├─ Substantial similarity (copyright)?
│   └─ Does the use fall within patent claims?
│
├─ Step 4: Evaluate liability
│   ├─ Which compensation formula applies?
│   └─ See cases.md → Case 8 for calculation patterns
│
├─ Step 5: Recommend actions
│
└─ Step 6: Check registries
    ├─ rospatent.py search — patent/trademark validity
    └─ sip.py search — pending litigation
```

## Risk Assessment Matrix

| Risk Level | Description | Action |
|---|---|---|
| **Critical** | Clear infringement, no defense | Stop use, negotiate license |
| **High** | Likely infringement, defenses uncertain | Get legal opinion, consider license/redesign |
| **Medium** | Debatable — depends on court interpretation | Document position, monitor, prepare defense |
| **Low** | Unlikely infringement or strong defense | Document justification, proceed with caution |
| **None** | No IP conflict or free use applies | Proceed |

## Audit Card (output template)

```markdown
## IP Audit Report

### Situation
[Description]

### IP Objects Involved
| Object | Type | Rights holder | Risk |
|---|---|---|---|
| [object 1] | [type] | [owner] | [risk level] |

### Infringement Analysis
- **[Object 1]**: [analysis]

### Potential Liability
| Risk | Compensation range | Basis |
|---|---|---|
| [risk 1] | [amount] | [Art. XXXX] |

### Recommendations
1. [Immediate action]
2. [Medium-term action]
3. [Long-term strategy]

### Defenses Available
- [Free use exception, if applicable]
- [Invalidity challenge, if applicable]
```

## Key Defenses

| Defense | Applies to | Art. |
|---|---|---|
| Free use — citation | Copyright | 1274 |
| Free use — personal use | Copyright | 1273 |
| Independent creation | Copyright (NOT patent) | N/A |
| Prior use (до использования) | Patents, trademarks | 1361, 1487 |
| Exhaustion of rights | Copyright, trademark | 1227(2), 1487 |
| Non-use of trademark | Trademark (3 years) | 1486 |
| Invalidity of IP right | All registered rights | Various |

**Verify current defenses**: ConsultantPlus → Art. 1273–1280.1 ГК РФ.

## Live Verification

```bash
# Check patent/trademark ownership and validity
rospatent.py search "[trademark]" -d patents_ru

# Check pending СИП litigation by party name
sip.py search -p "[company name]" --cookie "..."

# FIPS — detailed patent/trademark register
fips.py get <number> -d rutm --cookie "..."
```

**Law text**: ConsultantPlus / ГАРАНТ → Part 4, Chapter 70 (copyright), 72 (patent), 76 (trademark)