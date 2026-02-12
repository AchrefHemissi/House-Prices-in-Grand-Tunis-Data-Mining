"""
House Price Prediction - Standalone Inference Script
Generated from house-pricing-final.ipynb
"""
import joblib
import pandas as pd
import numpy as np

# Load the exported pipeline
pipeline = joblib.load('model_export/house_pricing_pipeline.joblib')

# Extract components
champion_model = pipeline['champion_model']
knn_models = pipeline['knn_region_models']
tier_lookup = pipeline['tier_lookup']
city_stats = pipeline['city_price_stats']
features = pipeline['features']

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
    city = city.lower()
    region = region.lower()
    
    # Impute region if 'autres villes'
    if region == 'autres villes' and city in knn_models:
        models = knn_models[city]
        scaler = models['scaler']
        knn = models['knn']
        label_encoder = models['label_encoder']
        
        city_median_ppm2 = city_stats['median'].get(city, 3000)
        X_features = pd.DataFrame([[size, room_count, bathroom_count, city_median_ppm2]], 
                                 columns=['size', 'room_count', 'bathroom_count', 'price_per_m2'])
        X_scaled = scaler.transform(X_features)
        predicted_encoded = knn.predict(X_scaled)[0]
        imputed_region = label_encoder.inverse_transform([predicted_encoded])[0]
    else:
        imputed_region = region
    
    # Prepare features
    avg_room_size = size / room_count if room_count > 0 else 0
    
    input_df = pd.DataFrame([{
        'city': city,
        'region': imputed_region,
        'size': size,
        'room_count': room_count,
        'bathroom_count': bathroom_count,
        'avg_room_size': avg_room_size
    }])
    
    # Predict
    log_price = champion_model.predict(input_df)[0]
    estimated_price = np.expm1(log_price)
    
    return {
        'city': city,
        'size': size,
        'room_count': room_count,
        'bathroom_count': bathroom_count,
        'original_region': region,
        'imputed_region': imputed_region,
        'estimated_price_tnd': round(estimated_price, 2)
    }

# Example usage
if __name__ == "__main__":
    print("House Price Prediction - Inference Example")
    print("="*50)
    
    # Test predictions
    test_cases = [
        ('tunis', 120, 3, 2),
        ('ariana', 80, 2, 1),
        ('ben arous', 150, 4, 2),
    ]
    
    for city, size, rooms, baths in test_cases:
        result = predict_price(city, size, rooms, baths)
        print(f"\n{city.title()} | {size}m², {rooms} rooms, {baths} bath")
        print(f"  → Imputed Region: {result['imputed_region']}")
        print(f"  → Estimated Price: {result['estimated_price_tnd']:,.2f} TND")
