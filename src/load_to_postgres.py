import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
username = "postgres"
password = "admin"
host = "localhost"
port = "5432"
database = "retail_db"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Load CSV
df = pd.read_csv("data/processed/fact_sales.csv")

# Send to PostgreSQL
df.to_sql("fact_sales", engine, if_exists="replace", index=False)

print("Data loaded successfully into PostgreSQL!")