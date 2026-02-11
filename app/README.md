# 🏠 Tunisia House Price Predictor - Streamlit App

A machine learning-powered web application for predicting real estate prices in Tunisia (Tunis, Ariana, Ben Arous, La Manouba).

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
pip install streamlit pandas numpy plotly joblib scikit-learn
```

3. **Ensure you have the model files**:
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

2. **Open your browser** to the URL shown (typically `http://localhost:8501`)

3. **Make predictions**:
   - Select a city from the dropdown
   - Enter property details (size, rooms, bathrooms)
   - Optionally specify a region (or leave as "autres villes" for auto-prediction)
   - Click "Predict Price"

4. **View history and insights**:
   - Check the "Prediction History" tab to see all your past predictions
   - Explore "Market Insights" for city comparisons and trends

## 📊 Model Information

- **Champion Model**: Stacking Ensemble
- **R² Score**: 0.8011 (80.11% accuracy)
- **Features Used**:
  - City (categorical)
  - Region (categorical, auto-imputed if unknown)
  - Size in m²
  - Number of rooms
  - Number of bathrooms
  - Average room size (derived)

## 🌍 Supported Cities

- Tunis
- Ariana
- Ben Arous
- La Manouba

## 📁 File Descriptions

- **app.py**: Main Streamlit application with UI and logic
- **config.py**: Configuration constants (cities, paths, colors, etc.)
- **utils.py**: Utility functions for prediction, visualization, and data processing
- **model_export/house_pricing_pipeline.joblib**: Trained ML pipeline (not included, must be generated)
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
