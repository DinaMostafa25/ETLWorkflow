import pandas as pd
from datetime import datetime
import sys
from sqlalchemy import create_engine


engine = create_engine(
    "postgresql://admin:secret@localhost:5432/etl_db"
)

df.to_sql("raw_orders", engine, if_exists="replace", index=False)


# Extract step
def extract(f_path):

    print("Start Extact.................")

    try :
        df = pd.read_csv(f_path)
        print("DONE Extract......................")
        return df
    except Exception as e:
        print("Extract error!!!!!!!!!!!!!")
        print(e)
        sys.exit(1)


# transform step 
def transform(df):
    print("Start Transform.................")

    try:
      
        
        # Convert order_date to datetime and drop invalid ones
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df = df.dropna(subset=["order_date"])

        # Drop rows where quantity is null
        df = df.dropna(subset=["quantity"])

        # Remove duplicates
        df = df.drop_duplicates()

        # Clean country
        df["country"] = df["country"].str.upper()

        # Clean customer name (title case)
        df["customer_name"] = df["customer_name"].str.title()

        # Create total_price column
        df["total_price"] = df["quantity"] * df["unit_price"]

        print("DONE Transform")

        return df


    except Exception as e:
        print("Transform error!!!!!!!!!!!!!")
        print(e)
        sys.exit(1)

# LOAD step 

def load(df):
    print("START Load..............................")
    df.to_csv("output.csv", index=False)
    print("DONE Load to outputcsv.........")
# main

if __name__ == "__main__":

    start_time = datetime.now()
    print("START pipeline.........")
    data =  extract("data.csv")
    output = transform(data)
    load(output)
    end_time = datetime.now()

    print("ETL pipeline completed successfully")
    print("Time : ",  end_time - start_time)
