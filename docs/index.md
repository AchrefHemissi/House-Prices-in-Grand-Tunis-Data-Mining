# House Prices in Grand Tunis - Documentation

## Project Overview

A data mining project analyzing apartment prices in Grand Tunis region using multiple data sources, data aggregation, and predictive modeling.

## Documentation Structure

```
docs/
├── index.md                    # ← You are here
├── source_1/                   # Dataset 1: Property Prices in Tunisia
│   ├── DATA_SOURCE.md         # Dataset information
│   └── NOTEBOOKS.md           # Analysis workflow documentation
├── source_2/                   # Dataset 2: Additional Apartment Data
│   ├── DATA_SOURCE.md         # Dataset information
│   └── NOTEBOOKS.md           # Analysis workflow documentation
├── aggregation/                # Data Integration
│   └── AGGREGATION.md         # Integration methodology
└── model/                      # Predictive Modeling 
    └── MODEL.md               # Model documentation
```

## Project Pipeline

```
┌─────────────┐     ┌─────────────┐
│  Source 1   │     │  Source 2   │
│  Dataset    │     │  Dataset    │
└──────┬──────┘     └──────┬──────┘
       │                   │
       ▼                   ▼
┌─────────────┐     ┌─────────────┐
│  Cleaning   │     │  Cleaning   │
│  & EDA      │     │  & EDA      │
└──────┬──────┘     └──────┬──────┘
       │                   │
       └─────────┬─────────┘
                 ▼
        ┌─────────────────┐
        │   Aggregation   │
        │                 │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │  Predictive     │
        │  Model          │
        │                 │
        └─────────────────┘
```

## Quick Navigation

| Section | Status | Description |
|---------|--------|-------------|
| [Source 1](source_1/) | Complete | Property Prices in Tunisia dataset |
| [Source 2](source_2/) | Complete | Additional dataset |
| [Aggregation](aggregation/) | Complete | Data integration from both sources |
| [Model](model/) | Planned | Predictive modeling |

---

**Project**: House-Prices-in-Grand-Tunis-Data-Mining  
**Author**: AchrefHemissi  
**Last Updated**: February 8, 2026