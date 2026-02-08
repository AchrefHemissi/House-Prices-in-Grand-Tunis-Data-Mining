# House Prices in Grand Tunis - Data Mining Project

A comprehensive data mining project analyzing real estate prices in Grand Tunis using machine learning and statistical analysis techniques.

## Quick Start

1. **Read the Documentation**: Visit [`docs/`](docs/) for complete project documentation
2. **Setup Environment**: Install dependencies from `requirements.txt`  
3. **Run Analysis**: Execute notebooks in sequence (01 → 02 → 03 → 04 → 05)
4. **View Results**: Check `reports/figures/` for generated visualizations

## Documentation

All project documentation is organized in the [`docs/`](docs/) directory:

| Section | Status | Description |
|---------|--------|-------------|
| [Index](docs/index.md) | - | Main navigation |
| [Source 1](docs/source_1/) | Complete | Tunisia Property Prices dataset |
| [Source 2](docs/source_2/) | Pending | Additional dataset |
| [Aggregation](docs/aggregation/) | Planned | Data integration |
| [Model](docs/model/) | Planned | Predictive modeling |

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
│       └── source_2/            # Cleaned data
├── notebooks/
│   ├── source_1/                # Source 1 analysis (5 notebooks)
│   └── source_2/                # Source 2 analysis (pending)
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

- **Multi-source Data Integration** - Combines multiple real estate datasets
- **Comprehensive Cleaning Pipeline** - Robust data preprocessing and validation  
- **Modular Analysis Workflow** - 5 specialized Jupyter notebooks
- **Geographic Focus** - Targeted analysis of Grand Tunis region
- **Statistical Analysis** - Price correlations and distributions
- **Visualization Ready** - Automated chart and plot generation

## Project Pipeline

```
┌─────────────┐     ┌─────────────┐
│  Source 1   │     │  Source 2   │
│  Done       │     │  Pending    │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 ▼
        ┌─────────────────┐
        │   Aggregation   │
        │   Planned       │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │  Predictive     │
        │  Model          │
        │  Planned        │
        └─────────────────┘
```

## Results

- **Dataset**: 12,749+ property listings → Cleaned dataset ready for ML
- **Coverage**: Grand Tunis (Tunis, Ariana, Ben Arous, La Manouba)  
- **Property Type**: Apartments for sale
- **Price Range**: Comprehensive analysis from budget to luxury properties
- **Export**: Clean CSV ready for machine learning models

## Technology Stack

- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib & Seaborn** - Data visualization
- **NumPy** - Numerical computations
- **Jupyter** - Interactive analysis environment

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