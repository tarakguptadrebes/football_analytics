from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

sql_files = [
    "sofascore_player_stats.sql",
    "sofascore_player_match_data.sql",
    "player_mappings.sql",
    "market_values_with_age.sql",
    "avg_market_value_with_age.sql",
    "change_in_market_value.sql",
    "ratings_with_age.sql",
    "avg_rating_with_age.sql",
]

with engine.connect() as connection:
    with connection.begin():
        for sql_file in sql_files:
            with open(BASE_DIR / 'sql' / sql_file, 'r') as file:
                sql_query = text(file.read())
                connection.execute(sql_query)
                print(f"Executed {sql_file}")