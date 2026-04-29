import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("POSTGRES_USER", "postgres"),
    password=os.getenv("POSTGRES_PASSWORD", "25Fondy93?"),
    host=os.getenv("POSTGRES_HOST", "localhost"),
    port=int(os.getenv("POSTGRES_PORT", "5433")),
    database=os.getenv("POSTGRES_DB", "retail_db"),
)

engine = create_engine(url)

fact_df = pd.read_csv("data/processed/fact_sales.csv")
customer_df = pd.read_csv("data/processed/customers.csv")

fact_df.to_sql("factsales", engine, if_exists="replace", index=False)
customer_df.to_sql("dimcustomer", engine, if_exists="replace", index=False)

print("Data successfully loaded into PostgreSQL!")