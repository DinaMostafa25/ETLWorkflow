import pandas as pd
from datetime import datetime
import sys
from sqlalchemy import create_engine


# Create engine (for GitHub Actions service)
engine = create_engine(
    "postgresql://admin:secret@localhost:5432/etl_db"
)



# Extract step

def extract(f_path):
    print("Start Extract...")
    try:
        df = pd.read_csv(f_path)
        print("DONE Extract")
        return df
    except Exception as e:
        print("Extract error!")
        print(e)
        sys.exit(1)


# Transform step 

def transform(df):
    print("Start Transform...")
    try:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df = df.dropna(subset=["order_date"])
        df = df.dropna(subset=["quantity"])
        df = df.drop_duplicates()

        df["country"] = df["country"].str.upper()
        df["customer_name"] = df["customer_name"].str.title()

        df["total_price"] = df["quantity"] * df["unit_price"]

        print("DONE Transform")
        return df

    except Exception as e:
        print("Transform error!")
        print(e)
        sys.exit(1)



# Load to PostgreSQL

def load(df):
    print("Start Load to PostgreSQL...")
    try:
        df.to_sql("raw_orders", engine, if_exists="replace", index=False)
        print("DONE Load to PostgreSQL")
    except Exception as e:
        print("Load error!")
        print(e)
        sys.exit(1)



# Main

if __name__ == "__main__":

    start_time = datetime.now()
    print("START pipeline")

    data = extract("data.csv")
    output = transform(data)
    load(output)

    end_time = datetime.now()

    print("ETL pipeline completed successfully")
    print("Time:", end_time - start_time)
