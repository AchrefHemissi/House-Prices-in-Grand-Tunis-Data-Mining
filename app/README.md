# 🏠 Tunisia House Price Predictor - Streamlit App

A machine learning-powered web application for predicting real estate prices in Tunisia (Tunis, Ariana, Ben Arous, La Manouba).

> **🌐 Live App**: [house-prices-in-grand-tunis-ml.streamlit.app](https://house-prices-in-grand-tunis-ml.streamlit.app/)

## 📋 Features

- **Real-time Price Prediction**: Predict house prices based on location, size, rooms, and bathrooms
- **Smart Region Imputation**: Automatically predicts the region using KNN when not specified
- **Interactive Visualizations**:
  - Price comparison gauges
  - City-wise market insights
  - Prediction history charts
- **Prediction History**: Track all predictions with filtering and export capabilities
- **Market Insights**: Compare median prices across different cities

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone or download this project**

2. **Install required packages**:

```bash
pip install streamlit pandas numpy plotly joblib scikit-learn xgboost
```

1. **Ensure you have the model files**:
   - Place `house_pricing_pipeline.joblib` in a folder named `model_export/`
   - Place `pipeline_metadata.json` in the same `model_export/` folder

Your directory structure should look like:

```
project/
├── app.py
├── config.py
├── utils.py
├── model_export/
│   ├── house_pricing_pipeline.joblib
│   └── pipeline_metadata.json
└── README.md
```

## 🎮 Usage

1. **Run the application**:

```bash
streamlit run app.py
```

1. **Open your browser** to the URL shown (typically `http://localhost:8501`)

2. **Make predictions**:
   - Select a city from the dropdown
   - Enter property details (size, rooms, bathrooms)
   - Optionally specify a region (or leave as "autres villes" for auto-prediction)
   - Click "Predict Price"

3. **View history and insights**:
   - Check the "Prediction History" tab to see all your past predictions
   - Explore "Market Insights" for city comparisons and trends

## 📊 Model Information

- **Champion Model**: Voting Ensemble (XGBoost + Gradient Boosting + SVR)
- **R² Score**: 0.8833 (88.33% accuracy)
- **Inference Pipeline** (5 steps):
  1. **KNN Region Imputation** — predicts the neighborhood when region is unknown
  2. **Virtual Region Clustering** — assigns the property to a KMeans cluster per city
  3. **Tier Lookup** — maps the cluster to a value tier (0=cheapest → 3=luxury)
  4. **Feature Engineering** — computes derived features from raw inputs
  5. **Price Prediction** — champion model predicts log-price, converted back to TND

- **Features Used**:
  - `city` (categorical, one-hot encoded)
  - `region` (categorical, auto-imputed via KNN if unknown)
  - `tier` (integer 0–3, derived from KMeans clustering)
  - `size` (m²)
  - `room_count`
  - `bathroom_count`
  - `avg_room_size` (size / room_count)
  - `log_size` (log-transformed size)
  - `bathroom_ratio` (bathroom_count / (room_count + 1))
  - `size_per_bathroom` (size / (bathroom_count + 1))
  - `room_density` (room_count / (size / 100))
  - `size_squared` (size²)

## 🌍 Supported Cities

- Tunis
- Ariana
- Ben Arous
- La Manouba

## 📁 File Descriptions

- **app.py**: Main Streamlit application with UI and logic
- **config.py**: Configuration constants (cities, paths, colors, etc.)
- **utils.py**: Utility functions — full 5-step inference pipeline, visualization, and data processing
- **model_export/house_pricing_pipeline.joblib**: Trained ML pipeline containing:
  - Champion model (Voting Ensemble)
  - KNN region imputation models (per city)
  - KMeans clustering models (per city)
  - Tier lookup dictionary
  - City-level price statistics
  - Feature list for column ordering
- **model_export/pipeline_metadata.json**: Model metadata and performance metrics

## 🔧 Configuration

You can modify settings in `config.py`:

- `PIPELINE_PATH`: Path to the ML pipeline file
- `CITIES`: List of supported cities
- `MAX_HISTORY_SIZE`: Maximum number of predictions to keep
- `CHART_COLORS`: Color scheme for visualizations
- `DEFAULT_*`: Default values for input fields

## 🎨 Features in Detail

### Price Prediction

- Input property details through an intuitive form
- Get instant price predictions in Tunisian Dinar (TND)
- See price per m² and average room size
- Compare against city median prices

### Prediction History

- Automatic storage of all predictions
- Filter by city and price range
- Visual scatter plot of prediction patterns
- Export to CSV for further analysis
- Clear history option

### Market Insights

- City-by-city price comparison charts
- Detailed statistics (median, mean, standard deviation)
- Example price ranges for standard properties
- Identify most expensive and affordable cities

## 🐛 Troubleshooting

**Error: "No module named 'streamlit'"**

- Solution: Install streamlit with `pip install streamlit`

**Error: "No module named 'xgboost'"**

- Solution: Install xgboost with `pip install xgboost`

**Error: "columns are missing: {'tier'}"**

- Solution: Ensure `utils.py` includes the full 5-step inference pipeline (clustering + tier lookup). See the latest version.

**Error: "Unable to load pipeline"**

- Solution: Ensure `house_pricing_pipeline.joblib` is in the `model_export/` folder

**Error: "FileNotFoundError"**

- Solution: Check that all files are in the correct directory structure

## 📝 License

This project is for educational/demonstration purposes.

## 👥 Credits

Developed as part of a machine learning real estate prediction project for the Tunisian market.

---

**Note**: This application requires the trained ML pipeline file (`house_pricing_pipeline.joblib`) which should be generated separately using the training notebook.
