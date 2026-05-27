# Limitations of Search Data for CustDev

Search data is one signal, not the whole picture. These limitations determine when search data is useful and when it misleads.

## 1. People don't search for products that don't exist

"IMU tracker for figure skating" → 0 queries. This doesn't mean no demand — it means the category doesn't exist in search vocabulary.

**How to apply**: Search by pain/problem, not by solution name. If 0 queries on pain keywords too, that's a weaker signal but still not proof of no market. Combine with interviews.

## 2. Informational queries ≠ purchase intent

"How to improve jump technique" = informational. The searcher may want a free YouTube tutorial, not a paid product.

**How to apply**: Distinguish search intent when interpreting results. High volume on informational queries confirms awareness of the problem but doesn't validate WTP. Look for commercial-intent signals ("buy X", "X tool", "X software", "X service").

## 3. B2B barely searches

A club director doesn't google "analytics for sports school" — they ask colleagues at conferences.

**How to apply**: For B2B hypotheses, low search volume is expected and doesn't invalidate the hypothesis. Search data is less useful for B2B validation. Rely more on interviews and industry sources.

## 4. Narrow niche = noise

In niche markets, queries may be in tens per month, not thousands. Both Wordstat and Trends perform poorly at very low volumes.

**How to apply**:
- Wordstat: `totalCount` below ~100/month is unreliable
- Trends: interest score 0-5 is indistinguishable from noise
- Don't make strong conclusions from low-volume data either way

## 5. Google Trends = relative numbers

The 0-100 scale is relative to the peak interest for that specific query in that time range. 100 for "sourdough bread" and 100 for "quantum computing" are not comparable.

**How to apply**:
- Compare terms only within the same Trends query (up to 5 terms)
- Use TIMESERIES to compare relative interest between related terms
- Don't interpret absolute Trends scores as market size

## 6. Google ≠ whole market

Significant portions of target audiences use Yandex (Russia/CIS), native search in social platforms (YouTube, TikTok), or app stores.

**How to apply**:
- For Russian market: use Wordstat, not just Trends
- For developer tools: check GitHub/StackOverflow search, not just Google
- For consumer products: social media search signals may be stronger than web search

## 7. Seasonality can mislead

If you collect data during a seasonal trough, you may underestimate demand. If during a peak, you may overestimate.

**How to apply**: Always collect dynamics/timeseries data, not just current snapshots. Compare same month across years when possible.

## 8. Search volume ≠ market size

Even with absolute numbers (Wordstat), search volume is not market size. Many people with the problem never search. Many who search never buy.

**How to apply**:
- Use search volume as directional signal (exists/doesn't exist, growing/declining)
- Don't project revenue from search volume
- Combine with conversion rate assumptions from comparable markets if you must estimate

## Interpretation Rule

Search data is one validation source among many:
- Positive signal = **confirmation**, not proof
- Absent signal = **no data**, not disproof
- Strong positive across multiple signals = high confidence to proceed
- Mixed signals = proceed with targeted interviews to resolve ambiguity
- Negative signals (declining trend, 0 pain queries) = revise hypothesis before investing more