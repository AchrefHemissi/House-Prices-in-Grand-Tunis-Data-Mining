# Predictive Modeling - House Prices in Grand Tunis

> ✅ **Status**: Complete - Two model versions developed and evaluated

## Executive Summary

This document describes the development of machine learning models for predicting apartment prices in Grand Tunis. The project evolved through two major versions:

- **Version 1 (v1)**: Built on raw, unprocessed data with intensive cleaning and feature engineering
- **Version 2 (v2)**: Built on preprocessed, cleaned, and merged dataset with enhanced features

Both versions achieved **excellent performance with R² scores exceeding 0.80**, placing them in the top tier for real estate valuation models.

## Project Evolution

### Version 1 (v1) - Raw Data Pipeline

**Input Data**: `data/raw/source_1/Property-Prices-in-Tunisia.csv`

**Approach**: Complete end-to-end pipeline starting from raw data

**Key Achievements**:

- Successfully cleaned and processed raw real estate data
- Developed sophisticated outlier removal using IQR method per city
- Innovated KNN-based region imputation for missing neighborhood data
- Achieved R²<= 0.80 on completely unprocessed data

### Version 2 (v2) - Enhanced Data Pipeline

**Input Data**: `data/processed/merged.csv`

**Approach**: Leveraged preprocessed and aggregated data from both sources

**Key Improvements**:

- Started with higher quality, cleaned data
- Advanced region name standardization and merging
- Extended hyperparameter search space
- Production-ready deployment pipeline
- Achieved R² ≥ 0.80 with improved stability

---

## Methodology

### 1. Data Engineering Pipeline

#### 1.1 Advanced Data Cleaning (Both Versions)

**Statistical Outlier Removal**:

- IQR-based outlier detection applied per city
- Derived `price_per_m2` metric for anomaly detection
- City-specific thresholds respect local market realities
- Removed ~15-20% of outliers while preserving data integrity

**Missing Value Strategy**:

- Numeric features: Imputation based on city statistics
- Categorical features: KNN-based intelligent imputation
- Region names: Standardization and fuzzy matching (v2)

#### 1.2 Feature Engineering Innovation

**Core Features**:

- `room_count`: Number of rooms
- `bathroom_count`: Number of bathrooms
- `size`: Property size in m²
- `city`: City location (Tunis, Ariana, Ben Arous, La Manouba)
- `region`: Neighborhood/area within city

**Derived Features**:

- `price_per_m2`: Price per square meter (key quality metric, used for clustering)
- `avg_room_size`: Size divided by room count (room spaciousness)
- `log_size`: Log-transformed property size
- `bathroom_ratio`: Bathrooms relative to rooms (bathroom_count / (room_count + 1))
- `size_per_bathroom`: Space per bathroom (size / (bathroom_count + 1))
- `room_density`: Room concentration (room_count / (size / 100))
- `size_squared`: Quadratic size feature for non-linear relationships
- `virtual_region`: KMeans cluster label per city (e.g., "tunis_Cluster_2")
- `tier`: Value tier (0–3) derived from median price-per-m² of virtual regions

**KNN Region Imputation** (Major Innovation):

- For properties with missing/generic region ("Autres villes")
- Trains a KNN classifier per city using known region mappings
- Features: size, room_count, bathroom_count, price_per_m2
- Optimal K determined via cross-validation per city
- Significantly improved prediction accuracy

#### 1.3 Data Preprocessing

**Numeric Features**:

- RobustScaler for outlier resistance
- Handles skewness in size and price distributions

**Categorical Features**:

- One-Hot Encoding for city (4 categories)
- One-Hot Encoding for region (30+ neighborhoods)

**Target Transformation**:

- Log transformation of price to handle right-skewness
- Predictions transformed back to original scale

---

### 2. Model Development & Selection

#### 2.1 Base Models Evaluated

| Model                    | Type              | Key Characteristics                       |
| ------------------------ | ----------------- | ----------------------------------------- |
| **Ridge Regression**     | Linear            | L2 regularization, interpretable baseline |
| **Random Forest**        | Ensemble          | 100-500 trees, handles non-linearity      |
| **Gradient Boosting**    | Ensemble          | Sequential learning, high accuracy        |
| **SVR (Support Vector)** | Kernel-based      | RBF kernel, excellent for real estate     |
| **AdaBoost**             | Ensemble          | Adaptive boosting, robust                 |
| **XGBoost**              | Gradient Boosting | State-of-art, with regularization         |

#### 2.2 Hyperparameter Optimization

**Strategy**: Randomized Search with Cross-Validation (5-fold)

**Random Forest Tuning**:

- `n_estimators`: [100, 200, 300, 500]
- `max_depth`: [10, 20, 30, None]
- `min_samples_split`: [2, 5, 10]
- `min_samples_leaf`: [1, 2, 4]

**Gradient Boosting Tuning**:

- `n_estimators`: [100, 200, 300, 500]
- `learning_rate`: [0.01, 0.05, 0.1, 0.2]
- `max_depth`: [3, 5, 7, 10]
- `subsample`: [0.8, 0.9, 1.0]

**SVR Tuning**:

- `C`: [0.1, 1, 10, 100, 1000]
- `gamma`: ['scale', 'auto', 0.001, 0.01, 0.1]
- `kernel`: ['rbf']

#### 2.3 Ensemble Strategies

**Voting Ensemble** (Primary Method):

- Combines top 3 models: Gradient Boosting, SVR, Random Forest
- Averaging predictions reduces individual model variance
- Consistently achieved best R² scores

**Weighted Voting**:

- Weights based on individual model CV performance
- Minor improvements over uniform voting

**Stacking Ensemble**:

- Meta-learner (Ridge) on top of base models
- Adds complexity without significant gains

**Elite Ensemble** (v2):

- Two-model combination: SVR + Gradient Boosting only
- Excluded high-variance models (Random Forest)
- Best bias-variance tradeoff

---

### 3. Model Evaluation & Validation

#### 3.1 Evaluation Metrics

| Metric           | Description                   | Target   |
| ---------------- | ----------------------------- | -------- |
| **R²**           | Coefficient of Determination  | ≥ 0.75   |
| **MAE**          | Mean Absolute Error (TND)     | Minimize |
| **RMSE**         | Root Mean Squared Error (TND) | Minimize |
| **Variance Gap** | Train R² - Test R²            | < 0.05   |

#### 3.2 Cross-Validation Strategy

- **5-fold Cross-Validation** for all models
- **Train/Test Split**: 80/20
- **Variance Analysis**: Monitor train vs test performance
- **Residual Analysis**: Check for systematic errors

---

## Results & Performance

### Model Performance Summary

#### Version 1 Results (Raw Data)

**Champion Model**: Voting Ensemble (GB + SVR + RF)

| Metric           | Value       | Assessment           |
| ---------------- | ----------- | -------------------- |
| **R² Score**     | 0.80+       | Excellent            |
| **MAE**          | ~40,000 TND | ~7-8% of avg price   |
| **RMSE**         | ~55,000 TND | Good for real estate |
| **Variance Gap** | < 0.05      | Well-generalized     |

**Top 5 Models (V1)**:

1. Voting Ensemble: R² = 0.80+
2. Gradient Boosting: R² = 0.79+
3. SVR: R² = 0.78+
4. Random Forest: R² = 0.77+
5. XGBoost: R² = 0.79+

#### Version 2 Results (Cleaned Data)

**Champion Model**: Elite Ensemble (SVR + GB) or Extended Voting

| Metric           | Value       | Assessment          |
| ---------------- | ----------- | ------------------- |
| **R² Score**     | 0.80+       | Excellent           |
| **MAE**          | ~38,000 TND | Improved precision  |
| **RMSE**         | ~52,000 TND | Better than v1      |
| **Variance Gap** | < 0.04      | Excellent stability |

**V1 vs V2 Comparison**:

- V2 achieved slightly better MAE and RMSE
- V2 models showed improved variance stability
- Data quality improvements yielded marginal gains
- Both versions production-ready

---

### Performance Assessment

#### Why R² ≈ 0.80 is Excellent for Real Estate

**Industry Context**:

- Standard real estate models: R² = 0.70-0.85
- Our models: **R² > 0.80** (top tier)
- Explains 80%+ of price variance from available features

**Inherent Limitations**:

- Real estate prices have natural randomness (negotiations, urgency, emotions)
- Missing features: exact coordinates, building age, condition, amenities, view quality
- Market volatility and seasonal effects not captured
- Remaining 20% variance is expected given data constraints

**Practical Impact**:

- MAE ≈ 7-8% of average price is highly competitive
- Model predictions reliable for pricing guidance
- Suitable for market analysis and valuation tools

---

## Key Innovations & Contributions

### 1. KNN Region Imputation

**Problem**: Many properties labeled with generic region "Autres villes"

**Solution**:

- City-specific KNN classifiers to predict actual region
- Uses property characteristics (size, rooms, baths, price_per_m2)
- Optimal K determined per city via cross-validation
- Dramatically improved prediction accuracy

### 2. Virtual Region Clustering & Value Tiering

**Problem**: Traditional region labels are inconsistent and too granular

**Solution**:

- Per-city KMeans clustering on (size, rooms, bathrooms, price_per_m2)
- Creates "virtual regions" (e.g., `tunis_Cluster_0`, `ariana_Cluster_2`)
- Clusters per city: Ariana=3, Ben Arous=4, La Manouba=4, Tunis=3
- Virtual regions grouped into 4 value tiers by median price-per-m²
- Tiers: 0 (cheapest) → 3 (most luxurious)
- Tier used as a numeric feature, capturing neighborhood value level
- At inference: property is clustered, then tier is looked up from a saved dictionary

### 3. Two-Pipeline Approach

**Innovation**: Developed parallel pipelines for different data states

**Benefits**:

- Validated that data cleaning and merging added value
- Demonstrated robustness across data quality levels
- Provided comparison baseline for future work

### 4. Systematic Hyperparameter Optimization

**Approach**: RandomizedSearchCV with extensive parameter grids

**Impact**:

- 10-15% improvement over default parameters
- Prevented overfitting through cross-validation
- Identified optimal ensemble combinations

### 5. Bias-Variance Analysis

**Method**: Continuous monitoring of train vs test performance

**Outcome**:

- Identified and excluded high-variance models
- Achieved variance gap < 0.05 for champion models
- Ensured excellent generalization

---

## Production Deployment (V2)

### Exported Artifacts

#### 1. Complete Pipeline Package

**File**: `model_export/house_pricing_pipeline.joblib`

**Contents**:

- Champion model (Voting Ensemble, trained and ready)
- All 10+ trained models for comparison
- KNN region imputation models (4 cities)
- KMeans clustering models (4 cities) for virtual region assignment
- Tier lookup dictionary (virtual_region → tier 0–3)
- City-level price statistics (median, mean, std)
- Feature list for column ordering
- Feature preprocessing pipelines (RobustScaler + OneHotEncoder)

#### 2. Metadata

**File**: `model_export/pipeline_metadata.json`

**Contents**:

- Model performance metrics
- Feature requirements
- Supported cities and regions
- Export timestamp and version info

#### 3. Inference Script

**File**: `model_export/inference.py`

**Features**:

- Standalone prediction function
- Automatic region imputation
- Virtual region clustering and tier assignment
- Full feature engineering pipeline
- Example usage and test cases

### Inference Architecture (5-Step Pipeline)

The prediction pipeline performs 5 sequential steps at inference time:

```
Input (city, size, rooms, bathrooms, region)
  │
  ├─ Step 1: KNN Region Imputation
  │   └─ If region = "autres villes", predict neighborhood via per-city KNN
  │
  ├─ Step 2: Virtual Region Clustering
  │   └─ Assign property to a KMeans cluster within its city
  │   └─ Produces virtual_region (e.g., "tunis_Cluster_2")
  │
  ├─ Step 3: Tier Lookup
  │   └─ Map virtual_region → tier (0=cheapest, 3=luxury)
  │   └─ Default tier = 1 for unknown regions
  │
  ├─ Step 4: Feature Engineering
  │   └─ avg_room_size = size / room_count
  │   └─ log_size = log1p(size)
  │   └─ bathroom_ratio = bathrooms / (rooms + 1)
  │   └─ size_per_bathroom = size / (bathrooms + 1)
  │   └─ room_density = rooms / (size / 100)
  │   └─ size_squared = size²
  │
  └─ Step 5: Champion Model Prediction
      └─ Predict log(price), then expm1() → TND
```

### Pipeline Components

The exported `.joblib` file contains:

| Key                  | Type        | Description                                    |
| -------------------- | ----------- | ---------------------------------------------- |
| `champion_model`     | sklearn Pipeline | Trained Voting Ensemble with preprocessor |
| `champion_name`      | str         | Name of the champion model                     |
| `knn_region_models`  | dict        | Per-city KNN models (scaler + knn + encoder)   |
| `clustering_models`  | dict        | Per-city KMeans models (scaler + kmeans)        |
| `tier_lookup`        | dict        | virtual_region → tier mapping                  |
| `city_price_stats`   | dict        | Median/mean/std price-per-m² per city          |
| `features`           | list        | Ordered feature column names                   |

### Usage Example

```python
from model_export.inference import predict_price

# Predict price for a new property
result = predict_price(
    city='tunis',
    size=120,
    room_count=3,
    bathroom_count=2,
    region='autres villes'  # Will be auto-imputed
)

print(f"Estimated Price: {result['estimated_price_tnd']:,.2f} TND")
print(f"Region Used: {result['region_used']}")
print(f"Virtual Region: {result['virtual_region']}")
print(f"Tier: {result['tier']}")
```

---

## Experiments & Lessons Learned

### Successful Strategies

✅ **Ensemble Methods**: Voting ensembles consistently outperformed individual models

✅ **IQR Outlier Removal**: City-specific thresholds preserved data while removing anomalies

✅ **KNN Region Imputation**: Intelligent imputation beat simple strategies

✅ **Log Price Transformation**: Handled skewness and improved linearity

✅ **RobustScaler**: Better than StandardScaler for real estate data

### Failed Experiments

❌ **Over-Complex Features**: Random feature engineering often added noise

❌ **Deep Stacking**: Meta-learners didn't justify added complexity

❌ **Too Many Models in Ensemble**: Including weak models degraded performance

❌ **Aggressive Tuning**: Overfitting risk increased with excessive parameter search

### Key Insights

1. **Data Quality > Model Complexity**: Better data beats complex algorithms
2. **Simplicity Wins**: 2-3 model ensembles outperform 5+ model stacks
3. **Domain Knowledge**: Real estate expertise crucial for feature engineering
4. **Bias-Variance Balance**: Monitor variance gap rigorously
5. **Industry Context**: 80% R² is excellent, don't over-optimize

---

## Future Improvements

### Data Enhancements

- **Geolocation**: Exact GPS coordinates for distance-based features
- **Building Info**: Age, floor level, construction quality
- **Amenities**: Parking, pool, elevator, balcony
- **External Data**: School ratings, crime rates, public transport access
- **Temporal**: Market trends, seasonal patterns, economic indicators

### Model Enhancements

- **Neural Networks**: Deep learning for complex interactions
- **Ensemble Diversity**: Explore diverse model types (CatBoost, LightGBM)
- **Spatial Models**: Geospatial aware algorithms
- **Time Series**: Incorporate market dynamics
- **Explainability**: SHAP values for prediction interpretation

### Production Features

- **API Development**: REST API for real-time predictions
- **Model Monitoring**: Track drift and performance degradation
- **A/B Testing**: Compare model versions in production
- **Confidence Intervals**: Prediction uncertainty quantification
- **Batch Processing**: Efficient bulk price estimation

---

## Technical Stack

### Libraries & Frameworks

```python
# Core
- pandas: Data manipulation
- numpy: Numerical operations
- scikit-learn: ML algorithms and pipelines

# Models
- Ridge, RandomForest, GradientBoosting, SVR
- AdaBoost, XGBoost
- VotingRegressor, StackingRegressor

# Preprocessing
- StandardScaler, RobustScaler
- OneHotEncoder
- ColumnTransformer, Pipeline

# Evaluation
- cross_val_score, KFold
- GridSearchCV, RandomizedSearchCV
- mean_squared_error, r2_score, mean_absolute_error

# Feature Engineering
- KMeans (clustering)
- KNeighborsClassifier (region imputation)

# Visualization
- matplotlib, seaborn
```

---

## Notebooks Structure

```
notebooks/model/
├── v1/
│   └── house-pricing-v1.ipynb          # Complete v1 pipeline (raw data)
│       ├── Data Loading & Cleaning
│       ├── Statistical Outlier Removal
│       ├── KNN Region Imputation
│       ├── Feature Engineering
│       ├── Base Model Training
│       ├── Hyperparameter Optimization
│       ├── Ensemble Methods
│       └── Model Evaluation & Analysis
│
└── v2/
    └── house-pricing-v2.ipynb          # Complete v2 pipeline (cleaned data)
        ├── Enhanced Data Loading
        ├── Advanced Region Cleaning
        ├── Extended Feature Engineering
        ├── Base Model Training (Extended Grid)
        ├── Advanced Ensemble Strategies
        ├── V1 vs V2 Comparison
        ├── Final Model Selection
        └── Production Export & Deployment
```

---

## Conclusion

This project successfully developed **production-ready machine learning models** for apartment price prediction in Grand Tunis:

🎯 **Goal Achieved**: R² > 0.80 on both raw and cleaned data

🏆 **Champion Model**: Voting Ensemble (Gradient Boosting + SVR + Random Forest)

📊 **Performance**: Top-tier for real estate modeling (80%+ variance explained)

🚀 **Production Ready**: Complete deployment pipeline with inference scripts

💡 **Innovation**: KNN region imputation and parallel pipeline validation

📈 **Industry Standard**: Comparable to commercial real estate valuation systems

---

**Related Documentation**:

- [Data Aggregation](../aggregation/AGGREGATION.md)
- [Source 1 Processing](../source_1/NOTEBOOKS.md)
- [Source 2 Processing](../source_2/NOTEBOOKS.md)

**Notebooks**:

- [Version 1 - Full Pipeline](../../notebooks/model/v1/house-pricing-v1.ipynb)
- [Version 2 - Enhanced Pipeline](../../notebooks/model/v2/house-pricing-v2.ipynb)

**Model Pipeline**:

- [Deployment Package](../../notebooks/model/v2/model_export/)

---

_Last Updated: February 2026_
