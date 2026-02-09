# Source 2: Notebook Documentation

## Notebook Pipeline

```
notebooks/source_2/
├── 01_Data_Loading_and_Setup.ipynb
├── 02_Data_Cleaning_and_Preprocessing.ipynb
├── 03_Feature_Distribution_Analysis.ipynb
├── 04_Price_Analysis.ipynb
├── 05_Model_Training_and_Evaluation.ipynb
├── 06_Data_Export.ipynb
└── full_code.ipynb (original combined notebook)
```

**Execution Order**: Run notebooks sequentially (01 → 02 → 03 → 04 → 05 → 06)

---

## 01_Data_Loading_and_Setup.ipynb

### Purpose

Initial setup and data loading for the apartment prices dataset.

### Operations

- Import essential libraries: `pandas`, `matplotlib`, `seaborn`, `numpy`
- Load dataset: `data_prices_cleaned.csv`
- Initial data inspection and overview

### Output

- DataFrame `df` loaded in memory for subsequent notebooks

---

## 02_Data_Cleaning_and_Preprocessing.ipynb

### Purpose

Data filtering, cleaning, and outlier removal.

### Operations

#### Numerical Column Cleaning

- Clean numerical columns: `superficie`, `chambres`, `salles_de_bains`, `price`
- Remove spaces and convert comma decimals to dots
- Handle non-numeric values and convert to NaN

#### Column Renaming

- `superficie` → `size`
- `chambres` → `room_count`
- `salles_de_bains` → `bathroom_count`

#### Geographic Filtering

- Limited data to Grand Tunis regions only:
  - `Tunis`, `Ariana`, `Ben Arous`, `La Manouba`

#### Property Type Filtering

- Focused exclusively on `Appartements` category
- Filtered for properties with `sale` transaction status

#### Price Transformation

- Converted prices from TND to **kTND** (thousands) by dividing by 1000

#### Outlier Removal

- Size filters: 24 m² ≤ size < 500 m²
- Price filters: price > 20 kTND
- Price-to-size ratio: excluded properties where price/size > 6
- Removed anomalies: large properties with low prices and small properties with very high prices
- Room count: 0 < rooms < 10
- Bathroom count: ≥ 0

#### Column Removal

- Dropped irrelevant columns: `contact`, `category`, `location`, `descriptions`, `currency`, `date`, `transaction`, `titles`, `shops`, `profiles`

#### Data Validation

- Removed rows with missing values in key columns: `price`, `size`, `room_count`, `bathroom_count`

### Output

- Cleaned DataFrame ready for analysis
- Summary statistics provided

---

## 03_Feature_Distribution_Analysis.ipynb

### Purpose

Comprehensive analysis of property feature distributions.

### Analyses

#### Size Distribution

- Descriptive statistics for property sizes
- Histogram with KDE for size distribution
- Count of properties > 250 m² and > 400 m²
- Identification of large outliers

#### Room Count Distribution

- Count plot showing distribution of properties by number of rooms
- Price statistics grouped by room count

#### Bathroom Count Distribution

- Descriptive statistics for bathroom counts
- Count plot showing distribution by bathroom count
- Price statistics grouped by bathroom count

#### Geographic Distribution

- Distribution of properties across Grand Tunis cities
- Distribution of properties by region/neighborhood

### Visualizations

- Histograms with KDE
- Count plots
- Box plots for distributions

---

## 04_Price_Analysis.ipynb

### Purpose

Detailed analysis of property prices and their relationships with features.

### Analyses

#### Basic Price Statistics

- Descriptive statistics for price column
- Identification of price outliers

#### Price vs Size Relationship

- Regression plot showing price-to-size relationship
- Log-transformed price for better visualization

#### Overall Price Distribution

- Box plot of overall price distribution (log-transformed)

#### Geographic Price Analysis

- Price distribution per region (log-transformed)
- Price distribution per city (log-transformed)

#### Price by Features

- Price distribution by bathroom count (log-transformed)
- Price distribution by room count (log-transformed)

#### Price per Square Meter

- Analysis of price-to-size ratios
- Identification of outliers with high price per m²

### Visualizations

- Regression plots
- Box plots (log-transformed for better readability)
- Comparative visualizations across different features

---

## 05_Model_Training_and_Evaluation.ipynb

### Purpose

Build and evaluate an XGBoost machine learning model for apartment price prediction.

### Operations

#### Data Preparation

- Feature selection: `room_count`, `bathroom_count`, `size`
- Target variable: `price` (in kTND)
- Check for missing values

#### Train-Test Split

- 80% training set
- 20% test set
- Random state: 42

#### Feature Scaling

- Applied `StandardScaler` to normalize features

#### Model Configuration

- **Algorithm**: XGBoost Regressor
- **Hyperparameters**:
  - n_estimators: 100
  - learning_rate: 0.1
  - max_depth: 5
  - min_child_weight: 1
  - subsample: 0.8
  - colsample_bytree: 0.8
  - objective: 'reg:squarederror'

#### Model Evaluation Metrics

- **Training Set**:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- **Test Set**:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R² Score
- **Cross-Validation**: 5-fold cross-validation with R² scoring

#### Feature Importance

- Ranking of features by importance
- Identification of most influential features for price prediction

### Visualizations

- Actual vs Predicted scatter plots (training and test sets)
- Feature importance bar chart
- Residual plots (training and test sets)
- Prediction error distribution histogram

---

## 06_Data_Export.ipynb

### Purpose

Prepare and export cleaned data for further use or sharing.

### Operations

#### Data Preparation

- Select relevant columns:
  - `room_count`
  - `bathroom_count`
  - `size`
  - `price` (in kTND)
  - `state` (renamed to `city`)
  - `city` (renamed to `region`)

#### Data Export

- Export to CSV file: `processed_apartment_data.csv`
- Index excluded from export
- Preview of exported data

### Output

| Property        | Value                                                             |
| --------------- | ----------------------------------------------------------------- |
| **Output File** | `processed_apartment_data.csv`                                    |
| **Columns**     | `room_count`, `bathroom_count`, `size`, `price`, `city`, `region` |
| **Format**      | CSV (comma-separated values)                                      |

---

## Summary

The Source 2 notebook pipeline provides a comprehensive workflow from raw data to a trained machine learning model:

1. **Loading**: Import and inspect raw data
2. **Cleaning**: Remove outliers, filter data, handle missing values
3. **Analysis**: Explore feature distributions and patterns
4. **Price Analysis**: Examine pricing relationships
5. **Modeling**: Build and evaluate XGBoost prediction model
6. **Export**: Save cleaned data for future use

This structured approach ensures reproducibility and makes it easy to understand each step of the data processing and modeling pipeline.
| **Location** | `data/processed/source_2/` |
| **Format** | CSV |

---

**Related Documentation**: [Data Source Information](DATA_SOURCE.md)
