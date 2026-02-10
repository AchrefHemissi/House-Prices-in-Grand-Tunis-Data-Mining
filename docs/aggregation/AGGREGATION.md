# Data Aggregation

> ✅ **Status**: Complete - Data successfully merged with inflation adjustment

## Purpose

Combine cleaned datasets from Source 1 and Source 2 into a unified dataset for predictive modeling, accounting for temporal differences through inflation adjustment.

## Prerequisites

| Requirement | Status |
|-------------|---------|
| Source 1 cleaned data | ✅ Complete |
| Source 2 cleaned data | ✅ Complete |

## Input Files

| Source | File | Location |
|--------|------|----------|
| Source 1 | `apartments_cleaned.csv` | `data/processed/source_1/` |
| Source 2 | `processed_apartment_data.csv` | `data/processed/source_2/` |

## Output Files

| File | Location | Description |
|------|----------|-------------|
| `merged.csv` | `data/processed/` | Unified dataset (1,513 records) |
| `Merge.ipynb` | `notebooks/` | Aggregation process documentation |

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

## Implementation

### 1. Inflation Adjustment

**Source 1 Price Adjustment**: Applied 25% inflation adjustment to Source 1 data (2020 prices) to bring them to 2024 equivalent:

```python
df['price'] = df['price'] * 1.25
```

**Rationale**: Based on [Institut National de la Statistique (INS) data](https://ins.tn/publication/indice-des-prix-de-limmobilier-premier-trimestre-2024), apartment prices in Tunisia increased by 25% from 2020 to 2024.

### 2. Schema Alignment

Both datasets had compatible schemas:

| Column | Type | Source 1 | Source 2 |
|--------|------|----------|----------|
| `room_count` | Numeric | ✅ | ✅ |
| `bathroom_count` | Numeric | ✅ | ✅ |
| `size` | Numeric | ✅ | ✅ |
| `price` | Numeric | ✅ (adjusted) | ✅ |
| `city` | Categorical | ✅ | ✅ |
| `region` | Categorical | ✅ | ✅ |

### 3. Duplicate Removal

- Identified common columns (excluding 'region' for regional variations)
- Detected and removed duplicate entries between sources
- Preserved unique records from both datasets

### 4. Merge Process

```python
# Remove duplicates based on common columns
common_cols = [col for col in df.columns if col in df2.columns and col != 'region']
duplicates_df = pd.merge(df, df2, on=common_cols, how='inner')
df_filtered = df[~df.set_index(common_cols).index.isin(duplicates_df.set_index(common_cols).index)]

# Concatenate filtered datasets
df_merged = pd.concat([df_filtered, df2], ignore_index=True)
```

## Results

| Property | Value |
|----------|-------|
| **Output File** | `merged.csv` |
| **Location** | `data/processed/` |
| **Total Records** | 1,513 |

### Data Quality

- **Coverage**: 6 unique cities, 95 unique regions
- **Price Range**: $47 k - $1,875 k
- **Size Range**: 30-500 m²
- **Room Range**: 1-8 rooms
- **No Missing Values**: Complete dataset

## Implementation Notebook

The aggregation process is fully documented in:

```
notebooks/
└── Merge.ipynb
```

This notebook includes:
- Inflation adjustment implementation
- Duplicate detection and removal
- Data exploration and visualization
- Quality validation and summary statistics

---

**Related Documentation**:
- [Source 1 Data](../source_1/DATA_SOURCE.md)
- [Source 2 Data](../source_2/DATA_SOURCE.md)
- [Model Documentation](../model/MODEL.md)