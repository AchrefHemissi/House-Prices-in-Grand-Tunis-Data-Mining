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
├── source_2/                   # Dataset 2: (To be added)
│   ├── DATA_SOURCE.md         # Dataset information
│   └── NOTEBOOKS.md           # Analysis workflow documentation
├── aggregation/                # Data Integration (Planned)
│   └── AGGREGATION.md         # Integration methodology
└── model/                      # Predictive Modeling (Planned)
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
        │   (Planned)     │
        └────────┬────────┘
                 ▼
        ┌─────────────────┐
        │  Predictive     │
        │  Model          │
        │  (Planned)      │
        └─────────────────┘
```

## Quick Navigation

| Section | Status | Description |
|---------|--------|-------------|
| [Source 1](source_1/) | ✅ Complete | Property Prices in Tunisia dataset |
| [Source 2](source_2/) | ✅ Complete | Additional dataset |
| [Aggregation](aggregation/) | 🔲 Planned | Data integration from both sources |
| [Model](model/) | 🔲 Planned | Predictive modeling |

## Current Progress

- ✅ **Source 1**: Data loaded, cleaned, analyzed, and exported
- 🔲 **Source 2**: Awaiting dataset integration
- 🔲 **Aggregation**: Will combine both sources
- 🔲 **Model**: Price prediction model development

---

**Project**: House-Prices-in-Grand-Tunis-Data-Mining  
**Author**: AchrefHemissi  
**Last Updated**: February 8, 2026