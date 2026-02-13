# House Prices in Grand Tunis - Data Mining Project

A comprehensive data mining project analyzing real estate prices in Grand Tunis using machine learning and statistical analysis techniques.

> **🌐 Live App**: [house-prices-in-grand-tunis-ml.streamlit.app](https://house-prices-in-grand-tunis-ml.streamlit.app/)

## Quick Start

1. **Read the Documentation**: Visit [`docs/`](docs/) for complete project documentation
2. **Setup Environment**: Install dependencies from `requirements.txt`  
3. **Explore Data**: Start with the merged dataset in `data/processed/merged.csv`
4. **Run Analysis**: Execute notebooks by source or use the complete [`Merge.ipynb`](notebooks/Merge.ipynb)
5. **View Results**: Check individual notebook outputs for generated visualizations

## Documentation

All project documentation is organized in the [`docs/`](docs/) directory:

| Section | Status | Description |
|---------|--------|-------------|
| [Index](docs/index.md) | - | Main navigation |
| [Source 1](docs/source_1/) | Complete | Tunisia Property Prices dataset |
| [Source 2](docs/source_2/) | Complete | Additional apartment dataset |
| [Aggregation](docs/aggregation/) | Complete | Data integration with inflation adjustment |
| [Model](docs/model/) | Complete | Predictive modeling (Voting Ensemble, R²=0.8833) |

## Project Structure

```
House-Prices-in-Grand-Tunis-Data-Mining/
├── README.md
├── requirements.txt             
├── data/
│   ├── raw/
│   │   ├── source_1/            # Tunisia property prices
│   │   └── source_2/            # Additional dataset
│   └── processed/
│       ├── source_1/            # Cleaned data
│       ├── source_2/            # Cleaned data
│       └── merged.csv           # Unified dataset with inflation adjustment
├── notebooks/
│   ├── source_1/                # Source 1 analysis (5 notebooks)
│   ├── source_2/                # Source 2 analysis (6 notebooks)
│   └── Merge.ipynb              # Data aggregation and inflation adjustment
├── docs/
│   ├── index.md                 # Main navigation
│   ├── source_1/                # Source 1 docs
│   ├── source_2/                # Source 2 docs
│   ├── aggregation/             # Aggregation docs
│   └── model/                   # Model docs
└── reports/
    └── figures/                 # Generated visualizations
```

## Key Features

- **Multi-source Data Integration** - Successfully merged two real estate datasets
- **Inflation Adjustment** - Applied 25% adjustment based on Tunisia INS statistics  
- **Comprehensive Cleaning Pipeline** - Robust data preprocessing and validation  
- **Modular Analysis Workflow** - Specialized Jupyter notebooks for each data source
- **Geographic Focus** - Grand Tunis region analysis (6 cities, 95 regions)
- **Statistical Analysis** - Price correlations and distributions
- **Duplicate Detection** - Intelligent deduplication across data sources
- **ML Prediction Pipeline** - 5-step inference: KNN region imputation → KMeans clustering → tier lookup → feature engineering → ensemble prediction (R² = 0.8833)
- **Streamlit Web App** - Interactive price prediction UI with visualizations and prediction history
- **XGBoost-Powered Ensemble** - Champion Voting Ensemble combining XGBoost, Gradient Boosting, and SVR

## Project Pipeline

```
┌─────────────┐     ┌─────────────┐
│  Source 1   │     │  Source 2   │
│             │     │             │
│ (2020 data) │     │ (2024 data) │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 ▼
        ┌─────────────────┐
        │   Aggregation   │
        │                 │
        │ +25% Inflation  │
        │  1,513 records  │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │  ML Pipeline    │
        │                 │
        │ KNN Imputation  │
        │ KMeans Clusters │
        │ Tier Lookup     │
        │ Voting Ensemble │
        │ R² = 0.8833     │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │  Streamlit App  │
        │                 │
        │ Price Predictor │
        └─────────────────┘
```

## Results

- **Merged Dataset**: 1,513 property listings with inflation adjustment
- **Coverage**: Grand Tunis region (6 cities, 95 regions)
- **Property Type**: Apartments for sale  
- **Price Range**: $47 - $1,920 (inflation-adjusted 2020→2024)
- **Data Quality**: Complete dataset with no missing values
- **Inflation Adjustment**: 25% applied to Source 1 based on [Tunisia INS data](https://ins.tn/publication/indice-des-prix-de-limmobilier-premier-trimestre-2024)
- **Export**: [`merged.csv`](data/processed/merged.csv) ready for machine learning models

## Technology Stack

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **scikit-learn** - ML algorithms, pipelines, and preprocessing
- **XGBoost** - Gradient boosting (used in champion ensemble)
- **Streamlit** - Interactive web application
- **Plotly** - Interactive charts and visualizations
- **Matplotlib & Seaborn** - Data visualization
- **NumPy** - Numerical computations
- **Jupyter** - Interactive analysis environment
- **joblib** - Model serialization and deployment

## Support

Need help? Check the documentation first:

1. **[Start Here](docs/index.md)** - Documentation index
2. **Browse** the [`docs/`](docs/) directory structure  
3. **Read** inline comments in notebooks
4. **Refer** to the original notebook for reference

## Authors

- **Mohamed Achref Hemissi**
- **Mohamed Dhia Medini**
- **Mohamed Aziz Dhoubi**
- **Khalil Ghimeji**
- **Rayen Chemlali**

---

**Get Started Now**: Visit [`docs/index.md`](docs/index.md) for the complete documentation!
