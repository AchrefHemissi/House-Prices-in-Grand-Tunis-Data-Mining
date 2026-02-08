# Source 1: Property Prices in Tunisia

## Basic Information

| Property | Value |
|----------|-------|
| **Source Name** | Property Prices in Tunisia |
| **File** | `Property-Prices-in-Tunisia.csv` |
| **Location** | `data/raw/source_1/` |
| **Size** | 1.05 MB |
| **Records** | 12,749 |
| **Author** | Ghassen Chaabouni |

## Data Collection

| Property | Value |
|----------|-------|
| **Collection Period** | January 22, 2020 - February 26, 2020 |
| **Collection Method** | Web Scraping |
| **Source Platform** | [Kaggle Dataset](https://www.kaggle.com/datasets/ghassen1302/property-prices-in-tunisia) |
| **Geographic Coverage** | Tunisia (nationwide) |

## Dataset Schema

### Original Columns

| Column | Type | Description |
|--------|------|-------------|
| `room_count` | Numeric | Number of rooms in the property |
| `bathroom_count` | Numeric | Number of bathrooms |
| `size` | Numeric | Property size in square meters (m²) |
| `price` | Numeric | Sale price in Tunisian Dinars (TND) |
| `city` | Categorical | City where property is located |
| `region` | Categorical | Specific neighborhood/area within city |
| `category` | Categorical | Property type (Appartements, Villas, etc.) |
| `type` | Categorical | Listing type (À Vendre, À Louer) |
| `log_price` | Numeric | Log-transformed price |

### Filtered Dataset (After Processing)

| Column | Type | Description |
|--------|------|-------------|
| `room_count` | Numeric | Number of rooms |
| `bathroom_count` | Numeric | Number of bathrooms |
| `size` | Numeric | Size in m² |
| `price` | Numeric | Price in **kTND** (thousands) |
| `city` | Categorical | Grand Tunis cities only |
| `region` | Categorical | Neighborhoods in Grand Tunis |

## Data Scope After Filtering

### Geographic Focus: Grand Tunis Region
- **Tunis** (capital)
- **Ariana**
- **Ben Arous**
- **La Manouba**

### Property Type Focus
- **Category**: Appartements (Apartments) only
- **Listing Type**: À Vendre (For Sale) only

## Output

| Property | Value |
|----------|-------|
| **Output File** | `apartments_cleaned.csv` |
| **Location** | `data/processed/source_1/` |
| **Format** | CSV |

---

**Related Documentation**: [Notebook Workflow](NOTEBOOKS.md)