# Source 1: Notebook Documentation

## Notebook Pipeline

```
notebooks/source_1/
├── 01_Data_Loading_and_Setup.ipynb
├── 02_Data_Cleaning_and_Preprocessing.ipynb
├── 03_Feature_Distribution_Analysis.ipynb
├── 04_Price_Analysis.ipynb
├── 05_Correlation_Analysis_and_Export.ipynb
└── full_code.ipynb (original combined notebook)
```

**Execution Order**: Run notebooks sequentially (01 → 02 → 03 → 04 → 05)

---

## 01_Data_Loading_and_Setup.ipynb

### Purpose
Initial setup and data loading for the Tunisia property prices dataset.

### Operations
- Import essential libraries: `pandas`, `matplotlib`, `seaborn`, `numpy`
- Load dataset: `Property Prices in Tunisia.csv`
- Initial data inspection and overview

### Output
- DataFrame `df` loaded in memory for subsequent notebooks

---

## 02_Data_Cleaning_and_Preprocessing.ipynb

### Purpose
Data filtering, cleaning, and outlier removal.

### Operations

#### Geographic Filtering
- Limited data to Grand Tunis regions only:
  - `Tunis`, `Ariana`, `Ben Arous`, `La Manouba`

#### Property Type Filtering
- Focused exclusively on `Appartements` category
- Filtered for properties with `À Vendre` (For Sale) status

#### Price Transformation
- Converted prices from TND to **kTND** (thousands) by dividing by 1000

#### Column Cleanup
- Removed unnecessary columns: `category`, `type`, `log_price`

#### Outlier Removal
Applied multiple filters to remove unrealistic listings:

| Filter | Condition | Rationale |
|--------|-----------|-----------|
| High price cap | price > 3,000 kTND | Removes luxury outliers |
| Underpriced large | price ≤ 70 kTND AND size ≥ 70m² | Unrealistic cheap large apartments |
| Overpriced small | price ≥ 1,000 kTND AND size ≤ 90m² | Unrealistic expensive small apartments |
| Impossible config | rooms ≥ 2 AND size ≤ 25m² | Physically impossible configurations |

#### Duplicate Detection & Removal
- **Exact Duplicates**: Removed completely identical rows
- **Partial Duplicates**: Identified based on key features (`room_count`, `bathroom_count`, `size`, `city`, `region`) excluding price variations

#### Feature Engineering
- **Created**: `price_per_sqm` (price per square meter in TND)
- **Filtered**: Removed properties with price/m² > 6,000 TND
- **Dropped**: Temporary `price_per_sqm` column after analysis

### Output
- Cleaned DataFrame ready for analysis

---

## 03_Feature_Distribution_Analysis.ipynb

### Purpose
Exploratory Data Analysis (EDA) of individual features.

### Statistical Analysis
- Descriptive statistics for `size`, `bathroom_count`, and `price`
- Price distribution analysis by room count

### Visualizations

| Visualization | Type | Description |
|---------------|------|-------------|
| Size Distribution | Histogram + KDE | Property size distribution |
| Room Count Distribution | Count plot | Frequency of different room counts |
| Bathroom Count Distribution | Count plot | Bathroom count frequencies |
| City Distribution | Bar chart | Property counts per city |
| Region Distribution | Horizontal bar chart | Properties per region |

### Output
- Feature understanding and distribution insights

---

## 04_Price_Analysis.ipynb

### Purpose
Comprehensive price analysis and relationships with property features.

### Visualizations

| Visualization | Type | Description |
|---------------|------|-------------|
| Price per m² Distribution | Histogram + KDE | Price/m² with median line |
| Overall Price Distribution | Box plot | Log-transformed price distribution |
| Price by Region | Box plot | Price comparison across regions (log) |
| Price by City | Box plot | Price comparison across cities (log) |
| Price by Bathroom Count | Box plot | Price variation by bathrooms (log) |
| Price by Room Count | Box plot | Price variation by rooms (log) |
| Price vs Size | Regression plot | Size vs log price relationship |

### Specific Insights Generated
- Analysis of budget apartments (below 80 kTND / 80,000 TND)
- Analysis of luxury apartments (above 1 MTND / 1,000,000 TND)

### Output
- Price relationship insights and visualizations

---

## 05_Correlation_Analysis_and_Export.ipynb

### Purpose
Final correlation analysis and cleaned data export.

### Operations
- Calculate correlation matrix for all numeric features
- Generate correlation heatmap visualization

### Correlation Matrix
Analyzes relationships between:
- `room_count`
- `bathroom_count`
- `size`
- `price`

### Final Output
- **File**: `apartments_cleaned.csv`
- **Location**: `data/processed/source_1/`

---

## Key Transformations Summary

| Aspect | Original | After Processing |
|--------|----------|------------------|
| **Geographic Scope** | All Tunisia | Grand Tunis only |
| **Property Types** | All categories | Apartments for sale only |
| **Price Unit** | TND | kTND (thousands) |
| **Price Visualizations** | Raw values | Log-transformed |
| **Quality Control** | Raw data | Exact & partial duplicates removed |

---

**Related Documentation**: [Data Source Information](DATA_SOURCE.md)