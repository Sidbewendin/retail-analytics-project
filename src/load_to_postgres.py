import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:My_Password?@localhost:5433/retail_db"
)

fact_df = pd.read_csv("data/processed/fact_sales.csv")
customer_df = pd.read_csv("data/processed/customers.csv")

fact_df.to_sql(
    "factsales",
    engine,
    if_exists="replace",
    index=False
)

customer_df.to_sql(
    "dimcustomer",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into PostgreSQL!")