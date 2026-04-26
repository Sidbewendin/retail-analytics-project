import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/retail_db"
)

df = pd.read_csv("data/processed/fact_sales.csv")

df.to_sql(
    "fact_sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into PostgreSQL!")