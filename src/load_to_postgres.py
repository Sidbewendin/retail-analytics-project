from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://postgres:25Fondy93?@localhost:5433/retail_db"
)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print(result.fetchone())

print("Connection successful!")