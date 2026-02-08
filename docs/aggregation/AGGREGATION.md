# Data Aggregation

> ⚠️ **Status**: Planned - Awaiting Source 2 integration

## Purpose

Combine cleaned datasets from Source 1 and Source 2 into a unified dataset for predictive modeling.

## Prerequisites

| Requirement | Status |
|-------------|--------|
| Source 1 cleaned data | ✅ Complete |
| Source 2 cleaned data | 🔲 Pending |

## Input Files

| Source | File | Location |
|--------|------|----------|
| Source 1 | `apartments_cleaned.csv` | `data/processed/source_1/` |
| Source 2 | *To be defined* | `data/processed/source_2/` |

## Aggregation Strategy

### 1. Schema Alignment

Ensure both datasets have compatible columns:

| Column | Type | Requirement |
|--------|------|-------------|
| `room_count` | Numeric | Required |
| `bathroom_count` | Numeric | Required |
| `size` | Numeric | Required (m²) |
| `price` | Numeric | Required (kTND) |
| `city` | Categorical | Required |
| `region` | Categorical | Required |
| `source` | Categorical | Added during merge |

### 2. Unit Normalization

- **Price**: Standardize to kTND (thousands of Tunisian Dinars)
- **Size**: Standardize to square meters (m²)

### 3. Geographic Standardization

- Normalize city names (case, spelling)
- Normalize region names
- Handle regional variations between sources

### 4. Merge Strategy

```python
# Planned approach
df_combined = pd.concat([df_source1, df_source2], ignore_index=True)
df_combined['source'] = ['source_1'] * len(df_source1) + ['source_2'] * len(df_source2)
```

### 5. Post-Merge Quality Checks

- Duplicate detection across sources
- Outlier detection on combined data
- Distribution analysis by source
- Feature correlation validation

## Output

| Property | Value |
|----------|-------|
| **Output File** | `apartments_aggregated.csv` |
| **Location** | `data/processed/` |
| **Format** | CSV |

## Planned Notebook

```
notebooks/
└── aggregation/
    └── 01_Data_Aggregation.ipynb
```

---

**Related Documentation**:
- [Source 1 Data](../source_1/DATA_SOURCE.md)
- [Source 2 Data](../source_2/DATA_SOURCE.md)
- [Model Documentation](../model/MODEL.md)