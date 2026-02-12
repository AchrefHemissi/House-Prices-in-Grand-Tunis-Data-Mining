import joblib
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from config import *

# Global variable to store loaded pipeline
_pipeline = None


def load_pipeline():
    """Load the ML pipeline from disk (cached)"""
    global _pipeline
    if _pipeline is None:
        try:
            _pipeline = joblib.load(PIPELINE_PATH)
        except Exception as e:
            raise Exception(
                f"Error loading pipeline: {str(e)}. This might be a scikit-learn version mismatch. Try: pip install scikit-learn==1.3.0 or retrain your model with the current environment.")
    return _pipeline


def predict_price(city, size, room_count, bathroom_count, region='autres villes'):
    """
    Predict house price for a new property.

    Parameters:
    -----------
    city : str - City name (tunis, ariana, ben arous, la manouba)
    size : float - Property size in m²
    room_count : int - Number of rooms
    bathroom_count : int - Number of bathrooms
    region : str - Region name (use 'autres villes' if unknown)

    Returns:
    --------
    dict with prediction details
    """
    pipeline = load_pipeline()

    # Extract components
    champion_model = pipeline['champion_model']
    knn_models = pipeline['knn_region_models']
    clustering_models = pipeline['clustering_models']
    tier_lookup = pipeline['tier_lookup']
    city_stats = pipeline['city_price_stats']
    features = pipeline['features']

    city = city.lower()
    region = region.lower()

    # 1. Region Imputation (KNN)
    city_median_ppm2 = city_stats['median'].get(city, 3000)

    if region == 'autres villes' and city in knn_models:
        models = knn_models[city]
        scaler = models['scaler']
        knn = models['knn']
        label_encoder = models['label_encoder']

        X_features = pd.DataFrame([[size, room_count, bathroom_count, city_median_ppm2]],
                                  columns=['size', 'room_count', 'bathroom_count', 'price_per_m2'])
        X_scaled = scaler.transform(X_features)
        predicted_encoded = knn.predict(X_scaled)[0]
        imputed_region = label_encoder.inverse_transform([predicted_encoded])[0]
    else:
        imputed_region = region

    # 2. Virtual Region (Cluster assignment)
    if city in clustering_models:
        models = clustering_models[city]
        scaler = models['scaler']
        kmeans = models['kmeans']

        X_cluster = pd.DataFrame([[size, room_count, bathroom_count, city_median_ppm2]],
                                 columns=['size', 'room_count', 'bathroom_count', 'price_per_m2'])
        X_scaled = scaler.transform(X_cluster)
        cluster_id = kmeans.predict(X_scaled)[0]
        virtual_region = f"{city}_Cluster_{cluster_id}"
    else:
        virtual_region = None

    # 3. Tier lookup
    tier = tier_lookup.get(virtual_region, 1)

    # 4. Feature Engineering
    avg_room_size = size / room_count if room_count > 0 else 0

    input_data = {
        'city': city,
        'region': imputed_region,
        'virtual_region': virtual_region,
        'tier': tier,
        'size': size,
        'room_count': room_count,
        'bathroom_count': bathroom_count,
        'avg_room_size': avg_room_size,
        'log_size': np.log1p(size),
        'bathroom_ratio': bathroom_count / (room_count + 1),
        'size_per_bathroom': size / (bathroom_count + 1),
        'room_density': room_count / (size / 100) if size > 0 else 0,
        'size_squared': size ** 2,
    }

    input_df = pd.DataFrame([input_data])
    input_df = input_df.reindex(columns=features, fill_value=0)

    # 5. Predict
    log_price = champion_model.predict(input_df)[0]
    estimated_price = np.expm1(log_price)
    price_per_m2 = estimated_price / size if size > 0 else 0

    return {
        'city': city.title(),
        'size': size,
        'room_count': room_count,
        'bathroom_count': bathroom_count,
        'original_region': region,
        'imputed_region': imputed_region,
        'estimated_price_tnd': round(estimated_price, 2),
        'price_per_m2': round(price_per_m2, 2),
        'avg_room_size': round(avg_room_size, 2)
    }


def get_city_statistics():
    """Get price statistics by city from the pipeline"""
    try:
        pipeline = load_pipeline()
        city_stats = pipeline['city_price_stats']

        stats_df = pd.DataFrame({
            'City': [city.title() for city in city_stats['median'].keys()],
            'Median Price/m²': [round(price, 2) for price in city_stats['median'].values()],
            'Mean Price/m²': [round(price, 2) for price in city_stats['mean'].values()],
            'Std Dev': [round(std, 2) for std in city_stats['std'].values()]
        })

        return stats_df
    except Exception as e:
        # Fallback: return hardcoded statistics from metadata
        return pd.DataFrame({
            'City': ['Tunis', 'Ariana', 'Ben Arous', 'La Manouba'],
            'Median Price/m²': [3000, 2800, 2600, 2500],
            'Mean Price/m²': [3200, 2900, 2700, 2600],
            'Std Dev': [500, 450, 400, 350]
        })


def create_city_comparison_chart(stats_df):
    """Create a bar chart comparing median prices across cities"""
    fig = px.bar(
        stats_df,
        x='City',
        y='Median Price/m²',
        title='Median House Price per m² by City',
        labels={'Median Price/m²': f'Price ({CURRENCY}/m²)'},
        color='Median Price/m²',
        color_continuous_scale='Blues'
    )

    fig.update_layout(
        showlegend=False,
        height=400,
        xaxis_title="City",
        yaxis_title=f"Median Price ({CURRENCY}/m²)"
    )

    return fig


def create_prediction_gauge(predicted_price, city_median):
    """Create a gauge chart showing prediction vs city median"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=predicted_price,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"Predicted Price ({CURRENCY})", 'font': {'size': 20}},
        delta={'reference': city_median, 'valueformat': '.0f'},
        gauge={
            'axis': {'range': [None, max(predicted_price * 1.5, city_median * 1.5)], 'tickformat': '.0f'},
            'bar': {'color': CHART_COLORS['primary']},
            'steps': [
                {'range': [0, city_median * 0.8], 'color': 'lightgray'},
                {'range': [city_median * 0.8, city_median * 1.2], 'color': 'gray'}
            ],
            'threshold': {
                'line': {'color': CHART_COLORS['danger'], 'width': 4},
                'thickness': 0.75,
                'value': city_median
            }
        }
    ))

    fig.update_layout(height=300)
    return fig


def create_history_chart(history_df):
    """Create a scatter plot of prediction history"""
    if history_df.empty:
        return None

    fig = px.scatter(
        history_df,
        x='size',
        y='estimated_price_tnd',
        color='city',
        size='room_count',
        hover_data=['bathroom_count', 'price_per_m2', 'imputed_region'],
        title='Prediction History',
        labels={
            'size': 'Size (m²)',
            'estimated_price_tnd': f'Predicted Price ({CURRENCY})',
            'city': 'City',
            'room_count': 'Rooms'
        }
    )

    fig.update_layout(height=500)
    return fig


def format_currency(amount):
    """Format number as currency"""
    return f"{amount:,.2f} {CURRENCY}"


def get_model_info():
    """Get model metadata information"""
    try:
        import json
        with open('model_export/pipeline_metadata.json', 'r') as f:
            metadata = json.load(f)
        return metadata
    except:
        return None


def get_available_regions(city=None):
    """Get list of available regions, optionally filtered by city"""
    try:
        pipeline = load_pipeline()

        # Get regions from KNN models (they have the label encoders with CLEANED regions)
        all_regions = set()

        if city and city.lower() in pipeline['knn_region_models']:
            # Get regions for specific city (these are the CLEANED regions the model was trained on)
            label_encoder = pipeline['knn_region_models'][city.lower()]['label_encoder']
            regions = label_encoder.classes_.tolist()
            all_regions.update(regions)
        else:
            # Get all unique regions from all cities
            for city_name, models in pipeline['knn_region_models'].items():
                label_encoder = models['label_encoder']
                regions = label_encoder.classes_.tolist()
                all_regions.update(regions)

        # Sort alphabetically (excluding "autres villes")
        regions_list = sorted([r for r in all_regions if r.lower() != 'autres villes'])

        # Add "autres villes" at the top if it exists
        if 'autres villes' in [r.lower() for r in all_regions]:
            regions_list.insert(0, next(r for r in all_regions if r.lower() == 'autres villes'))
        else:
            regions_list.insert(0, 'autres villes')

        # Capitalize first letter of each word for display
        return [r.title() if r.lower() != 'autres villes' else 'Autres Villes' for r in regions_list]

    except Exception as e:
        print(f"Error loading regions: {e}")
        # Fallback to common cleaned regions
        return ['Autres Villes', 'Centre Ville', 'Lac 1', 'Lac 2', 'Ennasr', 'Menzah', 'Manar',
                'Ariana Ville', 'Sokra', 'Mnihla', 'Ben Arous Ville', 'Rades', 'Megrine']