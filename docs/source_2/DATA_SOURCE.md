# Source 2: Tunisian Real Estate Dataset


## Basic Information

| Property | Value |
|----------|-------|
| **Source Name** | Tunisian Real Estate Dataset |
| **File** | `data_prices_cleaned.csv` |
| **Location** | `data/raw/source_2/` |
| **Size** | 5.48 MB |
| **Records** | 8,336 total records |
| **Author** | Debbichi Raaki |


## Data Collection

| Property | Value |
|----------|-------|
| **Collection Period** | February 14, 2024 - April 12, 2024 |
| **Collection Method** | Web scraping from Tayara platform |
| **Source URL** | [Kaggle Dataset](https://www.kaggle.com/datasets/debbichiraaki/tunisian-real-estate/data) |
| **Geographic Coverage** | Tunisia (all regions) |
| **Update Frequency** | One-time collection |

## Dataset Description

This dataset addresses the scarcity of real estate data for Tunisia by scraping comprehensive property listings from Tayara, Tunisia's popular online marketplace. The dataset provides valuable insights into the Tunisian real estate market dynamics, including property characteristics, pricing, and geographic distribution.

## Raw Dataset Schema

The raw dataset (`data/raw/source_2/data_prices_cleaned.csv`) contains **17 columns**:

| Column | Description | Type |
|--------|-------------|------|
| `location` | Full location string | Text |
| `price` | Property price | Numeric |
| `currency` | Currency (DT - Tunisian Dinar) | Text |
| `category` | Property category (Appartements, Maisons, etc.) | Text |
| `chambres` | Number of bedrooms/rooms | Numeric |
| `salles_de_bains` | Number of bathrooms | Numeric |
| `superficie` | Property size in m² | Numeric |
| `date` | Listing date | DateTime |
| `transaction` | Transaction type (sale/rent) | Text |
| `titles` | Property listing title | Text |
| `descriptions` | Detailed property description | Text |
| `contact` | Contact information | Text |
| `shops` | Shop/store information | Text |
| `profiles` | Profile information | Text |
| `state` | State/Governorate | Text |
| `city` | City/District | Text |

## Processed Dataset Schema

After cleaning and filtering, the processed dataset (`data/processed/source_2/processed_apartment_data.csv`) contains **6 columns**:

| Column | Description | Type | Notes |
|--------|-------------|------|-------|
| `room_count` | Number of rooms | Integer | Filtered: 0 < rooms < 10 |
| `bathroom_count` | Number of bathrooms | Integer | Filtered: ≥ 0 |
| `size` | Property size in m² | Float | Filtered: 24 ≤ size < 500 |
| `price` | Price in kTND (thousands) | Float | Filtered: > 20 kTND |
| `city` | Grand Tunis governorate | Text | Tunis, Ariana, Ben Arous, La Manouba |
| `region` | Specific city/neighborhood | Text | Various districts within Grand Tunis |

### Processing Statistics

| Metric | Value |
|--------|-------|
| **Original Records** | 8,336 |
| **Processed Records** | 566 |
| **Data Retention** | 6.8% |
| **Processed File Size** | 21.07 KB |
| **Geographic Focus** | Tunis (capital), Ariana, Ben Arous, La Manouba |
| **Property Type** | Apartments for sale only |

## Output

| Property | Value |
|----------|-------|
| **Output File** | `processed_apartments_data.csv` |
| **Location** | `data/processed/source_2/` |
| **Format** | CSV |

---

**Related Documentation**: 
- [Notebook Workflow](NOTEBOOKS.md)
- [Aggregation Strategy](../aggregation/AGGREGATION.md)