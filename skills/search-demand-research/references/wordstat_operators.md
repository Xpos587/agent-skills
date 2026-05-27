# Wordstat Operators for Research

Quick reference for Yandex Wordstat search operators. Use for precise research queries, not general collection.

## Operators

| Operator | Syntax | Effect | Research use |
|---|---|---|---|
| None | `фигурное катание` | All word forms and tails | Default — landscape discovery |
| Quotation | `"фигурное катание"` | Only these words in any order | Exact demand for specific phrase |
| Exclamation | `!купить` | Fixed word form | Check exact form frequency |
| Plus | `+сталь` | Includes stop-word in query | When stop-words matter |
| Brackets | `[красный мяч]` | Fixed word order | Precise intent matching |
| Minus | `обувь -детская` | Excludes word | Filter noise from results |
| Grouping | `(купить|заказать) X` | OR logic | Cover synonyms in one query |

## Research Patterns

| Goal | Operator pattern | Example |
|---|---|---|
| Pain demand | `"как улучшить" X` | `"как улучшить" прыжок` |
| Exact product search | `"X инструмент"` | `"анализ видео" инструмент` |
| Commercial intent | `(купить\|заказать\|цена) X` | `(купить\|цена) тренажер` |
| Exclude DIY/info | `X -своими -бесплатно -скачать` | `ремонт -своими -бесплатно` |
| Competitor check | `"X vs Y"` | `"kinovea" фигурное` |
| Parent segment | `X ребёнок\|детский` | `фигурное катание ребёнок` |

## Rules

- Use operators deliberately for targeted research, not randomly during general collection
- Operator queries return smaller result sets — interpret carefully
- Quotation marks restrict results significantly; use for validation of specific phrases, not discovery
- Minus operators help separate signal from noise in high-volume root masks