# Case Patterns (Судебные кейсы)

Precedent-style patterns from Russian IP litigation. Use for `cases [situation]` command.

## Case Index

| Pattern | Key case | Core issue | Reference |
|---|---|---|---|
| Trademark dominant elements | Sber vs SberPay | Strong vs weak mark elements | [Case 1](#case-1-sber-vs-sberpay) |
| Well-known mark scope | Moscow Metro | Protection across classes | [Case 2](#case-2-moscow-metro) |
| Unlawful adaptation | Prosveshcheniye vs Ekzamen | Copying visual style/composition | [Case 3](#case-3-prosveshcheniye-vs-ekzamen) |
| Photograph citation | Varlamov vs Archi.ru | Can photos be "cited"? | [Case 4](#case-4-varlamov-vs-archiru) |
| Jewelry design overlap | Namfleg vs Sunlight | Industrial design vs copyright | [Case 5](#case-5-namfleg-vs-sunlight) |
| Database sui generis | VKontakte | Who owns user-generated data? | [Case 6](#case-6-vkontakte-database) |
| Code theft detection | Various | Proving code copying | [Case 7](#case-7-software-code-theft) |
| Compensation calculation | Prosveshcheniye, Metro | 2× license vs 2× counterfeit vs statutory | [Case 8](#case-8-compensation-calculation) |

---

## Case 1: Sber vs SberPay

**Key issue**: Dominant vs weak trademark elements.
**Analysis**: "Sber" = dominant (positioned first, logical stress, references brand series). "QR" = weak (generic abbreviation).
**Outcome**: СИП reversed. Sber did not infringe. Lower court judges lost status.
**Apply when**: Assessing trademark similarity, evaluating strength of mark elements.

## Case 2: Moscow Metro

**Key issue**: Scope of protection for well-known state-affiliated marks.
**Facts**: 19.7M₽ for using similar "M" letter and transport sign on flower pots, clothing, delivery.
**Apply when**: Well-known mark protection, non-competing goods.

## Case 3: Prosveshcheniye vs Ekzamen

**Key issue**: Unlawful adaptation (переработка) of visual work.
**Facts**: 63.4M₽ for copying textbook cover designs — color scheme, characters, composition to create association with official series.
**Compensation**: 2× counterfeit value (most aggressive formula).
**Apply when**: Visual design copying, "look and feel" disputes.

## Case 4: Varlamov vs Archi.ru

**Key issue**: Can photographs be "cited" like text?
**Outcome**: Court of first instance held citation permissible. Refused Varlamov's claim.
**Pattern**: Citation exception is evolving. Proportionality test is critical.
**Apply when**: Image citation disputes, fair use/free use defenses.

## Case 5: Namfleg vs Sunlight

**Key issue**: Overlap between industrial design and copyright for decorative objects.
**Pattern**: Dual protection possible. Copyright arises automatically; industrial design requires registration. Choosing the right basis for a claim matters.
**Apply when**: Design object infringement, dual protection strategy, jewelry/fashion IP.

## Case 6: VKontakte Database

**Key issue**: Does a social network have database rights when users create content?
**Outcome**: Court recognized VK's investment in structuring/verifying/maintaining the database. Investment, not authorship, creates the sui generis right.
**Apply when**: Database scraping, user-generated content platforms, data ownership.

## Case 7: Software Code Theft

**Key issue**: How to prove code copying in court?
**Evidence**: Visual comparison of source, matching file creation dates, identical file sizes in bytes, matching checksums.
**Pattern**: Russian courts typically do NOT perform deep technical analysis. Formal/visual comparison often sufficient.
**Apply when**: Software infringement, code copying claims.

## Case 8: Compensation Calculation

Three statutory formulas (Art. 1301, 1515):

| Formula | Description | When used |
|---|---|---|
| 10K₽–5M₽ | Statutory compensation (per work/right) | Default, simpler to prove |
| 2× license value | Twice lawful license cost | When license value is provable |
| 2× counterfeit value | Twice value of infringing copies | Most aggressive (Prosveshcheniye) |

**Pattern**: Rightsholder chooses the formula. No need to prove actual damages.

## How to Use

When user describes a situation:
1. Match to closest case pattern(s)
2. Explain the legal principle from the case
3. Note differences from user's situation
4. Suggest how the principle would likely apply
5. Reference specific Civil Code articles

## Live Verification

```bash
# Search СИП cases by party name
sip.py search -p "Сбербанк" --cookie "..."

# By judge
sip.py search --judge "Пашкова" --cookie "..."

# Full JSON output for analysis
sip.py search -p "Ровио" -f full --cookie "..."
```

**Case database**: kad.arbitr.ru (СИП), sudact.ru — broader judicial practice