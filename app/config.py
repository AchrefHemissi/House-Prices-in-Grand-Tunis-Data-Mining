# House Price Prediction Configuration
import os

# Model Configuration
# Use relative path that works both locally and on Streamlit Cloud
PIPELINE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "notebooks", "model", "v2", "model_export", "house_pricing_pipeline.joblib")


# Supported Cities
CITIES = ["Tunis", "Ariana", "Ben Arous", "La Manouba"]

# App Configuration
APP_TITLE = " Tunisia House Price Predictor"
APP_ICON = ""
MAX_HISTORY_SIZE = 100  # Maximum number of predictions to keep in history

# Visualization Colors
CHART_COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "danger": "#d62728",
    "info": "#17becf"
}

# Currency
CURRENCY = "K TND"
CURRENCY_SYMBOL = "د.ت"

# Default Values
DEFAULT_CITY = "Tunis"
DEFAULT_REGION = "Autres Villes"  # Capitalized for display
DEFAULT_SIZE = 100
DEFAULT_ROOMS = 3
DEFAULT_BATHROOMS = 2