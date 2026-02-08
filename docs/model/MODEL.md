# Predictive Modeling

> ⚠️ **Status**: Planned - Awaiting data aggregation

## Purpose

Develop machine learning models to predict apartment prices in Grand Tunis based on property characteristics.

## Prerequisites

| Requirement | Status |
|-------------|--------|
| Source 1 cleaned data | ✅ Complete |
| Source 2 cleaned data | 🔲 Pending |
| Aggregated dataset | 🔲 Pending |

## Input Data

| Property | Value |
|----------|-------|
| **Input File** | `apartments_aggregated.csv` |
| **Location** | `data/processed/` |

## Target Variable

- **`price`** (in kTND) - Apartment sale price

## Feature Variables

| Feature | Type | Description |
|---------|------|-------------|
| `room_count` | Numeric | Number of rooms |
| `bathroom_count` | Numeric | Number of bathrooms |
| `size` | Numeric | Property size in m² |
| `city` | Categorical | City location |
| `region` | Categorical | Neighborhood/area |

## Planned Model Pipeline

### 1. Data Preparation
- Train/Test split (80/20 or 70/30)
- Feature scaling (StandardScaler / MinMaxScaler)
- Categorical encoding (One-Hot / Label Encoding)

### 2. Baseline Models

| Model | Type | Purpose |
|-------|------|---------|
| Linear Regression | Regression | Baseline performance |
| Decision Tree | Regression | Feature importance |
| Random Forest | Ensemble | Improved accuracy |

### 3. Advanced Models

| Model | Type | Purpose |
|-------|------|---------|
| Gradient Boosting | Ensemble | Higher accuracy |
| XGBoost | Ensemble | State-of-the-art performance |
| Neural Network | Deep Learning | Complex patterns |

### 4. Evaluation Metrics

| Metric | Description |
|--------|-------------|
| **MAE** | Mean Absolute Error |
| **RMSE** | Root Mean Squared Error |
| **R²** | Coefficient of Determination |
| **MAPE** | Mean Absolute Percentage Error |

### 5. Model Selection
- Cross-validation (5-fold or 10-fold)
- Hyperparameter tuning (GridSearch / RandomSearch)
- Model comparison and selection

## Planned Notebooks

```
notebooks/
└── model/
    ├── 01_Data_Preparation.ipynb
    ├── 02_Baseline_Models.ipynb
    ├── 03_Advanced_Models.ipynb
    └── 04_Model_Evaluation.ipynb
```

## Expected Outputs

| Output | Location | Description |
|--------|----------|-------------|
| Trained model | `models/` | Serialized model file |
| Predictions | `data/predictions/` | Price predictions |
| Metrics report | `reports/` | Model performance report |
| Feature importance | `reports/figures/` | Visualization |

---

**Related Documentation**:
- [Aggregation Strategy](../aggregation/AGGREGATION.md)
- [Source 1 Data](../source_1/DATA_SOURCE.md)
- [Source 2 Data](../source_2/DATA_SOURCE.md)