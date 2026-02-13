# 🚀 Quick Start Guide

> **🌐 Try it online**: [house-prices-in-grand-tunis-ml.streamlit.app](https://house-prices-in-grand-tunis-ml.streamlit.app/) — no installation needed!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy plotly joblib scikit-learn xgboost
```

## Step 2: Prepare Model Files

Create a `model_export/` folder and place these files inside:

- `house_pricing_pipeline.joblib` (your trained model)
- `pipeline_metadata.json` (model metadata)

## Step 3: Run the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Step 4: Make Your First Prediction

1. Select a city (e.g., "Tunis")
2. Enter size in m² (e.g., 120)
3. Enter number of rooms (e.g., 3)
4. Enter number of bathrooms (e.g., 2)
5. Click "🔮 Predict Price"

## That's it! 🎉

Explore the other tabs to:

- View prediction history
- See market insights
- Compare prices across cities

---

## Need Help?

Check the full README.md for detailed information and troubleshooting tips.
