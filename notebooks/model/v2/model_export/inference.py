"""
House Price Prediction - Standalone Inference Script
Production Version
"""
import joblib
import pandas as pd
import numpy as np

# Load pipeline
pipeline = joblib.load("model_export/house_pricing_pipeline.joblib")

champion_model = pipeline["champion_model"]
champion_name = pipeline["champion_name"]
knn_models = pipeline["knn_region_models"]
clustering_models = pipeline["clustering_models"]
tier_lookup = pipeline["tier_lookup"]
city_stats = pipeline["city_price_stats"]
features = pipeline["features"]

def predict_price(city, size, room_count, bathroom_count, region="autres villes"):

    city = city.lower()
    region = region.lower()

    # --------------------------
    # 1. Region Imputation (KNN)
    # --------------------------
    city_median_ppm2 = city_stats["median"].get(city, 3000)

    if region == "autres villes" and city in knn_models:
        models = knn_models[city]
        scaler = models["scaler"]
        knn = models["knn"]
        label_encoder = models["label_encoder"]

        X_knn = pd.DataFrame(
            [[size, room_count, bathroom_count, city_median_ppm2]],
            columns=["size", "room_count", "bathroom_count", "price_per_m2"]
        )

        X_scaled = scaler.transform(X_knn)
        encoded = knn.predict(X_scaled)[0]
        region = label_encoder.inverse_transform([encoded])[0]

    # --------------------------
    # 2. Virtual Region (Cluster)
    # --------------------------
    if city in clustering_models:
        models = clustering_models[city]
        scaler = models["scaler"]
        kmeans = models["kmeans"]

        X_cluster = pd.DataFrame(
            [[size, room_count, bathroom_count, city_median_ppm2]],
            columns=["size", "room_count", "bathroom_count", "price_per_m2"]
        )

        X_scaled = scaler.transform(X_cluster)
        cluster_id = kmeans.predict(X_scaled)[0]
        virtual_region = f"{city}_Cluster_{cluster_id}"
    else:
        virtual_region = None

    # --------------------------
    # 3. Tier
    # --------------------------
    tier = tier_lookup.get(virtual_region, 1)

    # --------------------------
    # 4. Feature Engineering
    # --------------------------
    avg_room_size = size / room_count if room_count > 0 else 0

    input_data = {
        "city": city,
        "region": region,
        "virtual_region": virtual_region,
        "tier": tier,
        "size": size,
        "room_count": room_count,
        "bathroom_count": bathroom_count,
        "avg_room_size": avg_room_size,
        "log_size": np.log1p(size),
        "bathroom_ratio": bathroom_count / (room_count + 1),
        "size_per_bathroom": size / (bathroom_count + 1),
        "room_density": room_count / (size / 100),
        "size_squared": size ** 2,
    }

    input_df = pd.DataFrame([input_data])

    # Ensure correct column order
    input_df = input_df.reindex(columns=features, fill_value=0)

    # --------------------------
    # 5. Predict
    # --------------------------
    log_price = champion_model.predict(input_df)[0]
    estimated_price = np.expm1(log_price)

    return {
        "city": city,
        "region_used": region,
        "virtual_region": virtual_region,
        "tier": tier,
        "model_used": champion_name,
        "estimated_price_tnd": round(float(estimated_price), 2)
    }

# Example usage
if __name__ == "__main__":
    print("House Price Prediction - Production Inference")
    print("=" * 50)

    test_cases = [
        ("tunis", 120, 3, 2),
        ("ariana", 80, 2, 1),
        ("ben arous", 150, 4, 2),
    ]

    for city, size, rooms, baths in test_cases:
        result = predict_price(city, size, rooms, baths)

        print(f"\n{city.title()} | {size}m² | {rooms} rooms | {baths} bath")
        print(f"  -> Region Used: {result['region_used']}")
        print(f"  -> Virtual Region: {result['virtual_region']}")
        print(f"  -> Tier: {result['tier']}")
        print(f"  -> Estimated Price: {result['estimated_price_tnd']:,.2f} TND")
