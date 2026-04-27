import pandas as pd
from sqlalchemy import create_engine

# Create connection to PostgreSQL database
engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/retail_db"
)

# Load processed datasets
# -> Fact table (transactions)
fact_df = pd.read_csv("data/processed/fact_sales.csv")

# -> Dimension table (customers)
customer_df = pd.read_csv("data/processed/customers.csv")


# Load data into FactSales table
# -> append data to existing table (do not overwrite schema)
fact_df.to_sql(
    "factsales",
    engine,
    if_exists="append",
    index=False
)


# Load data into DimCustomer table
# -> append data to existing table
customer_df.to_sql(
    "dimcustomer",
    engine,
    if_exists="append",
    index=False
)


print("Data successfully loaded into PostgreSQL (FactSales & DimCustomer)")