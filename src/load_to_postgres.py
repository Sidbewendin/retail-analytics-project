import pandas as pd
from sqlalchemy import create_engine

username = "retailadmin"
password = "25Fondy93?"
host = "retail-postgres-yameogo.postgres.database.azure.com"
port = "5432"
database = "postgres"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

df = pd.read_csv("data/processed/fact_sales.csv")

df.to_sql(
    "fact_sales_cloud",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into Azure PostgreSQL!")