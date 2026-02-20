# ETL Pipeline with CI/CD using GitHub Actions

## Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline using Python and Pandas, integrated with PostgreSQL and fully automated using GitHub Actions for CI/CD.

The pipeline:

- Extracts raw data from a CSV file
- Cleans and transforms the dataset
- Loads processed data into PostgreSQL
- Executes analytical SQL queries
- Runs automated unit tests
- Executes entirely inside GitHub Actions

The workflow triggers automatically on every push to the `main` branch.

---

## Project Structure

```
ETLWorkflow/
│
├── .github/
│ └── workflows/
│ └── runetl.yml
│
└── etl_project/
├── ETL_job.py
├── data.csv
├── queries.sql
├── requirements.txt
├── tests/
│ └── test_etl.py
```

---

## ETL Process

### 1. Extract

- Reads input data from `data.csv`
- Uses `pandas.read_csv()`
- Handles extraction errors using try/except

```python
df = pd.read_csv("data.csv")
```

---

### 2. Transform

The transformation step performs:

- Convert `order_date` to datetime
- Remove invalid dates
- Remove rows with missing `quantity`
- Remove duplicate records
- Standardize `country` to uppercase
- Format `customer_name` using title case
- Create new column:

```
total_price = quantity * unit_price
```

---

### 3. Load

- Saves the cleaned dataset to Posgresql DB:

```
raw_orders
```

```python
df.to_sql("raw_orders", engine, if_exists="replace", index=False)
```

---

## Automated Testing

Unit testing is implemented using pytest.

The test validates:

- Invalid date removal
- Null value handling
- Duplicate removal
- Correct calculation of `total_price`
- Proper formatting of `country`
- Proper formatting of `customer_name`

To run tests locally:

```bash
pytest
```

---

## CI/CD with GitHub Actions

The workflow performs the following steps:

1. Checkout repository
2. Setup Python environment
3. Install dependencies
4. Run ETL script
5. Load data into database
6. Execute SQL queries
7. Run unit tests


The workflow triggers automatically on push to `main`.

---

## Downloading the Output File

After a successful workflow run:

1. Navigate to GitHub → Actions
2. Open the latest workflow run
3. Scroll to Artifacts
4. Download `etl-output`
5. Extract `output.csv`

The output file is generated during the CI run and is not committed to the repository.

---

## Technologies Used

- Python 3.10
- Pandas
- Pytest
- GitHub Actions
- YAML
- SQLAlchemy
- PostgreSQL 
- Psycopg2
---

## Running Locally

1. Clone the repository:

```bash
git clone <repository-url>
cd ETLWorkflow/etl_project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the ETL pipeline:

```bash
python ETL_job.py
```

4. Run tests:

```bash
pytest
```
