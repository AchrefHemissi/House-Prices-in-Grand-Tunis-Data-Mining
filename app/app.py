import streamlit as st
import pandas as pd
from datetime import datetime
from config import *
from utils import *

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f8ff;
        padding: 2rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .price-display {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2ca02c;
        text-align: center;
    }
    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #1557a0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for history
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []

# Header
st.markdown(f'<div class="main-header"> Tunisian House Price Predictor</div>', unsafe_allow_html=True)
st.markdown("### Predict real estate prices across Tunis, Ariana, Ben Arous, and La Manouba")

# Sidebar
with st.sidebar:
    st.header("About This App")
    st.markdown("""
    This application uses machine learning to predict house prices in Grand Tunis in Tunisia based on:
    - **Location** (City & Region)
    - **Property Size** (m²)
    - **Number of Rooms**
    - **Number of Bathrooms**

    The model was trained on real estate data and achieves **80% accuracy** (R² = 0.80).
    """)

    st.divider()

    # Model Information
    model_info = get_model_info()
    if model_info:
        st.subheader("🤖 Model Details")
        st.metric("Champion Model", model_info.get('champion_model_name', 'N/A'))
        st.metric("R² Score", f"{model_info.get('champion_r2', 0):.2%}")
        st.metric("Export Date", model_info.get('export_date', 'N/A')[:10])

    st.divider()

    # City Statistics
    st.subheader(" Market Overview")
    try:
        city_stats = get_city_statistics()
        st.dataframe(
            city_stats[['City', 'Median Price/m²']],
            hide_index=True,
            use_container_width=True
        )
    except:
        st.info("City statistics unavailable")

# Main content tabs
tab1, tab2, tab3 = st.tabs([" Price Prediction", " Prediction History", " Market Insights"])

# TAB 1: PRICE PREDICTION
with tab1:
    st.header("Enter Property Details")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Location")

        # City selection
        city = st.selectbox(
            "City",
            options=CITIES,
            index=CITIES.index(DEFAULT_CITY),
            help="Select the city where the property is located",
            key="city_select"
        )

        # Get available regions for selected city (dynamically filtered)
        available_regions = get_available_regions(city)

        # Region selection
        region = st.selectbox(
            "Region",
            options=available_regions,
            index=0,  # Default to "Autres Villes"
            help="Select the region - 'Autres Villes' will auto-predict the region based on property features",
            key="region_select"
        )

        # Show number of available regions for this city
        st.caption(f" {len(available_regions) - 1} regions available in {city} (+ Auto-predict option)")

    with col2:
        st.subheader("Property Features")
        size = st.number_input(
            "Size (m²)",
            min_value=10,
            max_value=1000,
            value=DEFAULT_SIZE,
            step=10,
            help="Total property size in square meters"
        )

        room_count = st.number_input(
            "Number of Rooms",
            min_value=1,
            max_value=20,
            value=DEFAULT_ROOMS,
            step=1,
            help="Total number of rooms"
        )

        bathroom_count = st.number_input(
            "Number of Bathrooms",
            min_value=1,
            max_value=10,
            value=DEFAULT_BATHROOMS,
            step=1,
            help="Total number of bathrooms"
        )

    st.divider()

    # Predict button
    col_predict, col_clear = st.columns([3, 1])

    with col_predict:
        predict_button = st.button(" Predict Price", type="primary", use_container_width=True)

    with col_clear:
        if st.button("🗑️ Clear", use_container_width=True):
            st.rerun()

    # Prediction
    if predict_button:
        with st.spinner("Analyzing property data..."):
            try:
                # Convert region back to lowercase for the model
                region_lower = region.lower()

                result = predict_price(city, size, room_count, bathroom_count, region_lower)

                # Store in history
                result['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                st.session_state.prediction_history.insert(0, result)

                # Keep only recent predictions
                if len(st.session_state.prediction_history) > MAX_HISTORY_SIZE:
                    st.session_state.prediction_history = st.session_state.prediction_history[:MAX_HISTORY_SIZE]

                # Display result
                st.success("✅ Prediction Complete!")

                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)

                # Main price display
                st.markdown(
                    f'<div class="price-display">{format_currency(result["estimated_price_tnd"])}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("---")

                # Details in columns
                detail_col1, detail_col2, detail_col3 = st.columns(3)

                with detail_col1:
                    st.metric("City", result['city'])
                    st.metric("Region", result['imputed_region'].title())

                with detail_col2:
                    st.metric("Size", f"{result['size']} m²")
                    st.metric("Price per m²", format_currency(result['price_per_m2']))

                with detail_col3:
                    st.metric("Rooms", result['room_count'])
                    st.metric("Avg Room Size", f"{result['avg_room_size']} m²")

                st.markdown('</div>', unsafe_allow_html=True)

                # Comparison gauge
                st.subheader("Price Comparison")
                try:
                    city_stats = get_city_statistics()
                    city_median_per_m2 = city_stats[city_stats['City'] == result['city']]['Median Price/m²'].values[0]
                    city_median_total = city_median_per_m2 * result['size']

                    gauge_fig = create_prediction_gauge(result['estimated_price_tnd'], city_median_total)
                    st.plotly_chart(gauge_fig, use_container_width=True)

                    # Comparison text
                    diff_pct = ((result['estimated_price_tnd'] - city_median_total) / city_median_total) * 100
                    if diff_pct > 0:
                        st.info(
                            f"💡 This property is **{abs(diff_pct):.1f}% above** the median price for {result['city']}")
                    else:
                        st.info(
                            f"💡 This property is **{abs(diff_pct):.1f}% below** the median price for {result['city']}")
                except:
                    pass

                # Region info
                if result['original_region'] == 'autres villes':
                    st.info(f"ℹ️ Region was automatically predicted as: **{result['imputed_region'].title()}**")

            except Exception as e:
                st.error(f"❌ Error making prediction: {str(e)}")
                st.exception(e)

# TAB 2: PREDICTION HISTORY
with tab2:
    st.header("Prediction History")

    if not st.session_state.prediction_history:
        st.info("No predictions yet. Make your first prediction in the 'Price Prediction' tab!")
    else:
        # Convert to DataFrame
        history_df = pd.DataFrame(st.session_state.prediction_history)

        # Filters
        filter_col1, filter_col2, filter_col3 = st.columns(3)

        with filter_col1:
            city_filter = st.multiselect(
                "Filter by City",
                options=sorted(history_df['city'].unique()),
                default=sorted(history_df['city'].unique())
            )

        with filter_col2:
            min_price = st.number_input(
                "Min Price (TND)",
                min_value=0,
                value=0,
                step=10000
            )

        with filter_col3:
            max_price = st.number_input(
                "Max Price (TND)",
                min_value=0,
                value=int(history_df['estimated_price_tnd'].max()) + 100000,
                step=10000
            )

        # Apply filters
        filtered_df = history_df[
            (history_df['city'].isin(city_filter)) &
            (history_df['estimated_price_tnd'] >= min_price) &
            (history_df['estimated_price_tnd'] <= max_price)
            ]

        # Display statistics
        st.subheader("Summary Statistics")
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

        with stat_col1:
            st.metric("Total Predictions", len(filtered_df))
        with stat_col2:
            st.metric("Avg Price", format_currency(filtered_df['estimated_price_tnd'].mean()))
        with stat_col3:
            st.metric("Min Price", format_currency(filtered_df['estimated_price_tnd'].min()))
        with stat_col4:
            st.metric("Max Price", format_currency(filtered_df['estimated_price_tnd'].max()))

        st.divider()

        # History chart
        st.subheader("Visual History")
        history_chart = create_history_chart(filtered_df)
        if history_chart:
            st.plotly_chart(history_chart, use_container_width=True)

        st.divider()

        # Data table
        st.subheader("Detailed History")

        # Format for display
        display_df = filtered_df.copy()
        display_df['estimated_price_tnd'] = display_df['estimated_price_tnd'].apply(lambda x: f"{x:,.2f} {CURRENCY}")
        display_df['price_per_m2'] = display_df['price_per_m2'].apply(lambda x: f"{x:,.2f} {CURRENCY}")

        # Rename columns
        display_df = display_df.rename(columns={
            'timestamp': 'Date/Time',
            'city': 'City',
            'size': 'Size (m²)',
            'room_count': 'Rooms',
            'bathroom_count': 'Bathrooms',
            'imputed_region': 'Region',
            'estimated_price_tnd': 'Predicted Price',
            'price_per_m2': 'Price/m²'
        })

        # Select columns to display
        columns_to_show = ['Date/Time', 'City', 'Region', 'Size (m²)', 'Rooms',
                           'Bathrooms', 'Predicted Price', 'Price/m²']

        st.dataframe(
            display_df[columns_to_show],
            hide_index=True,
            use_container_width=True
        )

        # Export options
        col_export1, col_export2 = st.columns([1, 4])

        with col_export1:
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="📥 Export to CSV",
                data=csv,
                file_name=f"house_predictions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
                use_container_width=True
            )

        with col_export2:
            if st.button("🗑️ Clear All History", type="secondary", use_container_width=True):
                st.session_state.prediction_history = []
                st.rerun()

# TAB 3: MARKET INSIGHTS
with tab3:
    st.header("Market Insights")

    try:
        city_stats = get_city_statistics()

        # City comparison chart
        st.subheader("City Price Comparison")
        city_chart = create_city_comparison_chart(city_stats)
        st.plotly_chart(city_chart, use_container_width=True)

        st.divider()

        # Detailed statistics table
        st.subheader("Detailed City Statistics")

        # Format the dataframe
        formatted_stats = city_stats.copy()
        for col in ['Median Price/m²', 'Mean Price/m²', 'Std Dev']:
            formatted_stats[col] = formatted_stats[col].apply(lambda x: f"{x:,.2f} {CURRENCY}")

        st.dataframe(
            formatted_stats,
            hide_index=True,
            use_container_width=True
        )

        st.divider()

        # Insights
        st.subheader(" Key Insights")

        highest_city = city_stats.loc[city_stats['Median Price/m²'].idxmax()]
        lowest_city = city_stats.loc[city_stats['Median Price/m²'].idxmin()]

        insight_col1, insight_col2 = st.columns(2)

        with insight_col1:
            st.success(f"""
            **Most Expensive City:** {highest_city['City']}
            - Median: {highest_city['Median Price/m²']:,.2f} {CURRENCY}/m²
            - Mean: {highest_city['Mean Price/m²']:,.2f} {CURRENCY}/m²
            """)

        with insight_col2:
            st.info(f"""
            **Most Affordable City:** {lowest_city['City']}
            - Median: {lowest_city['Median Price/m²']:,.2f} {CURRENCY}/m²
            - Mean: {lowest_city['Mean Price/m²']:,.2f} {CURRENCY}/m²
            """)

        # Price range analysis
        st.divider()
        st.subheader("📏 Example Price Ranges")

        st.markdown("**For a 100m² property with 3 rooms and 2 bathrooms:**")

        example_cols = st.columns(len(CITIES))
        for idx, city in enumerate(CITIES):
            with example_cols[idx]:
                try:
                    example_result = predict_price(city, 100, 3, 2)
                    st.metric(
                        city,
                        format_currency(example_result['estimated_price_tnd']),
                        delta=f"{example_result['price_per_m2']:.0f} {CURRENCY}/m²"
                    )
                except:
                    st.metric(city, "N/A")

    except Exception as e:
        st.error(f"Unable to load market insights: {str(e)}")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p><strong>Tunisia House Price Predictor</strong> | Powered by Machine Learning</p>
    <p style='font-size: 0.9rem;'>Model: Stacking Ensemble | R² Score: 80.11%</p>
</div>
""", unsafe_allow_html=True)