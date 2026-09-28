# FMCG Demand Forecasting & Promotion Intelligence

A Python project scaffold for developing demand forecasting and promotion analysis tools for fast-moving consumer goods (FMCG). The intended goal is to help teams understand demand patterns, assess promotional activity, and produce useful forecasts from retail sales data.

> **Project status:** Early scaffold. Forecasting, promotion analysis, data ingestion, and evaluation workflows are not implemented yet. This README describes the project direction and current repository layout, not available production features.

## Project Goals

The project is intended to grow toward workflows for:

- Preparing and validating historical sales and promotion data.
- Exploring demand patterns across products, stores, and time.
- Building and comparing demand forecasting approaches.
- Measuring forecast quality and the effect of promotions.
- Producing clear reports to support planning decisions.

These are planned capabilities; none are currently exposed as runnable commands or APIs.

## Repository Layout

```text
.
├── configs/                    # Configuration files (to be added)
├── data/                       # Local datasets (not tracked yet)
├── notebooks/                  # Exploratory analysis (to be added)
├── reports/                    # Generated findings and outputs (to be added)
├── scripts/                    # Command-line workflows (to be added)
├── src/
│   └── fmcg_intelligence/
│       ├── data/                # Data utilities; implementation pending
│       ├── evaluation/          # Forecast evaluation (planned)
│       ├── features/            # Feature engineering (planned)
│       ├── forecasting/         # Forecasting methods (planned)
│       ├── promotion/           # Promotion analysis (planned)
│       └── utils/               # Shared utilities (planned)
└── tests/                      # Tests (to be added)
```

## Getting Started

### Prerequisites

- Python 3.10 or later
- Git

The project dependencies are listed in `requirements.txt`.

### Create a virtual environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Once the environment is active, run the current data download script with:

```bash
python src/fmcg_intelligence/data/download.py
```

The download uses KaggleHub. Your Kaggle account must be authorized to access the Favorita Grocery Sales Forecasting competition, and any applicable competition rules must be accepted. Kaggle authentication may be required before the download succeeds.

## Data

The `data/` directory is reserved for local input data and generated datasets. No dataset, schema, or ingestion workflow is included yet. Avoid committing private, licensed, or otherwise sensitive business data; document the source and permitted use of any dataset added to the project.

## Development

Implementation lives under `src/fmcg_intelligence/`. Tests belong under `tests/`. A test suite and test configuration have not been added yet.

## Roadmap

1. Define supported input data and validation rules.
2. Implement reusable data loading and preparation.
3. Add a baseline forecast and evaluation metrics.
4. Add promotion features and analysis methods.
5. Provide reproducible scripts, configuration, and reports.

## License

No license has been specified yet. Until one is added, the repository's reuse and redistribution terms are not defined.
