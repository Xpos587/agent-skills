# Specifications Validation Rules

Use these rules to verify that claimed product specifications are realistic and consistent.

## Computers & Laptops

### CPU Validation

| Spec Pattern | Valid | Suspicious | Notes |
|-------------|-------|-----------|-------|
| `Intel Core i5-13400` | ✅ | | Full model number |
| `Intel i7` (no model) | | ⚠️ | Could be ancient i7-2600K |
| `Intel Core i7-14700K` | ✅ | | Current gen |
| `Intel Core i9-14900HX` | ✅ | | Laptop variant |
| `AMD Ryzen 5 7530U` | ✅ | | |
| `AMD Ryzen 7` (no model) | | ⚠️ | Could be Ryzen 7 1700 (2017) |
| `Процессор: Современный 8-ядерный` | | 🔴 | No model = hiding weak CPU |
| `MTK / MediaTek` (laptops) | | ⚠️ | Uncommon, verify carefully |

**Key rules:**
- Must have full model number (brand + series + generation + SKU)
- Intel 12th gen+ or AMD Ryzen 5000+ are "current" (2023-2025)
- Intel 10th gen or older = suspicious if price is premium
- Server CPUs (Xeon, EPYC) in consumer laptops = red flag

### GPU Validation

| Spec Pattern | Valid | Suspicious | Notes |
|-------------|-------|-----------|-------|
| `NVIDIA RTX 4060` | ✅ | | |
| `NVIDIA RTX 4060 Laptop` | ✅ | | Laptop variant is slower |
| `NVIDIA GeForce RTX` (no model) | | 🔴 | Hiding the actual GPU |
| `Intel UHD Graphics` | ✅ | | Integrated — not for gaming |
| `RTX 4090` in 40,000₽ laptop | | 🔴 | Price doesn't match |
| `GTX 1650` in 2025 premium laptop | | ⚠️ | Outdated GPU |

**Price benchmarks (approximate, 2024-2025):**
- Laptop with RTX 4050: 55,000-80,000 ₽
- Laptop with RTX 4060: 70,000-110,000 ₽
- Laptop with RTX 4070: 90,000-150,000 ₽
- Laptop with RTX 4080+: 150,000+ ₽

### RAM Validation

| Spec Pattern | Valid | Suspicious | Notes |
|-------------|-------|-----------|-------|
| `16 ГБ DDR5` | ✅ | | |
| `До 32 ГБ` | | ⚠️ | "Up to" — actual RAM may be less |
| `8 ГБ (расширяемая до 64)` | ✅ | | Clear about base + max |
| `Оперативная память: Есть` | | 🔴 | No specifics |
| `4 ГБ` in 2025 laptop | | ⚠️ | Very low for modern use |

### Storage Validation

| Spec Pattern | Valid | Suspicious | Notes |
|-------------|-------|-----------|-------|
| `512 ГБ SSD NVMe` | ✅ | | |
| `1 ТБ SSD` (no brand) | | ⚠️ | Could be low-quality drive |
| `eMMC 64 ГБ` | ✅ | | Common in budget laptops |
| `SSD + HDD: 256 ГБ + 1 ТБ` | ✅ | | Dual storage |
| `1 ТБ SSD` for 15,000₽ laptop | | 🔴 | Doesn't match price |

### Screen Validation

| Spec Pattern | Valid | Suspicious | Notes |
|-------------|-------|-----------|-------|
| `15.6" IPS 1920x1080` | ✅ | | |
| `Full HD` (no size/resolution) | | ⚠️ | Verify actual specs |
| `13.3" 4K OLED` | ✅ | | Premium but possible |
| `17.3" TN 1366x768` | ✅ | | Budget panel |
| `120Hz` in budget laptop | | ⚠️ | Verify — may be interpolated |

## Phones

| Spec | Valid Range | Suspicious |
|------|------------|-----------|
| Battery | 3000-6000 mAh | >6500 mAh (may be fake) |
| Screen | 5.5"-7.2" | |
| RAM | 4-16 GB | <4 GB in 2025 |
| Storage | 64-512 GB | >1TB in mid-range phone |

## Price-to-Spec Consistency Matrix

Use this to check if the price makes sense for the specs:

### Laptops
```
Price Range        | Expected Specs
-------------------|-----------------------------------------
< 20,000 ₽        | Celeron/Pentium, 4-8GB, 128-256GB, TN screen
20,000-35,000 ₽    | i3/Ryzen3, 8GB, 256GB SSD, IPS
35,000-55,000 ₽    | i5/Ryzen5, 8-16GB, 256-512GB SSD, IPS
55,000-80,000 ₽    | i5/i7/Ryzen5/7, 16GB, 512GB SSD, IPS good
80,000-120,000 ₽   | i7/Ryzen7, 16-32GB, 512-1TB, premium build
> 120,000 ₽        | High-end, dedicated GPU, premium everything
```

### Phones
```
Price Range        | Expected Specs
-------------------|-----------------------------------------
< 10,000 ₽        | Budget SoC, 4GB RAM, 64GB, basic camera
10,000-25,000 ₽    | Mid-range SoC, 6-8GB, 128GB, decent camera
25,000-50,000 ₽    | Upper mid-range, 8GB, 128-256GB, good camera
50,000-80,000 ₽    | Flagship SoC, 8-12GB, 256GB, great camera
> 80,000 ₽         | Flagship, premium everything
```

## How to Validate

1. Extract claimed specs from the product listing
2. For each spec, check against the tables above
3. Verify the spec combination is physically possible
4. Check price-to-spec consistency
5. If specs don't match the price, flag as 🔴

**Example validation:**
```
Listing: "Ноутбук ASUS, i7, 32GB RAM, 1TB SSD, RTX 4070" — 35,000 ₽
Check:
  - i7 (no model) → ⚠️
  - 32GB RAM → possible but premium
  - 1TB SSD → possible but premium
  - RTX 4070 → 90,000+ ₽ expected
  - Price 35,000₽ for these specs → 🔴 IMPOSSIBLE
Verdict: SCAM — price doesn't match specs by factor of 3x
```
