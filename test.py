# test_insert.py
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Create a small test DataFrame
df = pd.DataFrame({
    "player": ["Player1", "Player2", "Player3"],
    "goals": [1, 0, 2],
    "assists": [0, 1, 1],
    "match_id": [1001, 1001, 1001]
})

# Safe test table name
table_name = "test_player_stats"

# SQLAlchemy engine
db_url = (
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
engine = create_engine(db_url)

# Insert test data
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Test data saved to table '{table_name}'")
print(df)