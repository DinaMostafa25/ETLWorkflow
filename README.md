# ETL Pipeline with CI/CD using GitHub Actions

## Overview

This project implements an automated ETL (Extract, Transform, Load) pipeline using Python and Pandas, integrated with GitHub Actions for CI/CD.

The pipeline:

- Extracts raw data from a CSV file
- Cleans and transforms the dataset
- Generates a processed output file
- Runs automated unit tests
- Uploads the output as a downloadable artifact

The workflow runs automatically on every push to the `main` branch.

---

## Project Structure

```
ETLWorkflow/
│
├── .github/workflows/
│   └── runetl.yml
│
└── etl_project/
    ├── ETL_job.py
    ├── data.csv
    ├── requirements.txt
    ├── output.csv
    └── tests/
        └── test_etl.py
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

- Saves the cleaned dataset to:

```
output.csv
```

```python
df.to_csv("output.csv", index=False)
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
5. Execute unit tests
6. Upload `output.csv` as an artifact

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
