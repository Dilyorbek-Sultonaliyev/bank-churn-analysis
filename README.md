# Bank Customer Churn Analysis

A data science project analyzing and predicting customer churn for a bank, covering the full workflow from synthetic data generation to a working machine learning model.

## About the project

I built this project to understand which factors drive bank customers to leave, and to practice the kind of end-to-end analysis I'd want to do as a data analyst. It goes from raw data generation, through SQL analysis and Python-based exploration, to a trained ML model and a Power BI dashboard.

## Tech stack

- **Python** — data generation and analysis (Pandas, NumPy, Faker)
- **PostgreSQL** — database
- **SQL** — analytical queries
- **Matplotlib** — visualization
- **scikit-learn** — machine learning
- **Power BI** — interactive dashboard

## Workflow

1. **Data generation** — created a synthetic dataset of 50,000 bank customers (`generate_data.py`)
2. **Database** — loaded the data into PostgreSQL
3. **SQL analysis** — ran 7 queries to explore which factors correlate with churn
4. **Python analysis** — further exploration and charts with Pandas/Matplotlib
5. **Machine learning** — trained and compared Logistic Regression and Random Forest models
6. **Dashboard** — built an interactive Power BI dashboard to present the findings

## Key results

- **Random Forest accuracy:** 86.46%
- **Logistic Regression accuracy:** 82%
- **Overall churn rate:** 26.5%

### Feature importance

| Feature | Importance |
|---|---|
| Active membership | 30.0% |
| Tenure (months) | 20.4% |
| Balance | 11.9% |
| Salary | 11.5% |

### Main finding

Inactive customers churn at a rate of **55.6%**, compared to just **7.1%** for active customers — nearly an 8x difference. This suggests that keeping customers engaged is one of the highest-leverage retention levers a bank has.

## Project structure

    bank_churn_project/
    ├── generate_data.py      # Synthetic data generation
    ├── analyze_data.py       # SQL, Pandas & ML analysis (local only, not on GitHub)
    ├── requirements.txt      # Dependencies
    ├── README.md              
    └── data/                 # Data and chart outputs (local only)

## Running it locally

    pip install -r requirements.txt
    python generate_data.py

## About me

**Dilyorbek Sultonaliyev**
Management student at Tashkent University of Economics, currently building out my data analytics skills through self-directed projects like this one.
