import sys
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import text
import football_analytics
from football_analytics.database import get_engine

PACKAGE_ROOT = Path(football_analytics.__file__).parent
SQL_DIR = PACKAGE_ROOT / "sql"

PROJECT_ROOT = PACKAGE_ROOT.parent.parent
load_dotenv(PROJECT_ROOT / '.env')

engine = get_engine()

quickstart = "--quick" in sys.argv

if quickstart:
    sql_files = [
        "player_mappings.sql",
        "market_values_with_age.sql",
        "ratings_with_age.sql",
        "values_ratings_with_age.sql",
        "avg_market_value_with_age.sql",
        "change_in_market_value.sql",
        "avg_rating_with_age.sql",
    ]
else:
    sql_files = [
        "sofascore_player_stats.sql",
        "sofascore_player_match_data.sql",
        "player_mappings.sql",
        "market_values_with_age.sql",
        "ratings_with_age.sql",
        "values_ratings_with_age.sql",
        "avg_market_value_with_age.sql",
        "change_in_market_value.sql",
        "avg_rating_with_age.sql",
    ]

with engine.connect() as connection:
    with connection.begin():
        for sql_file in sql_files:
            with open(SQL_DIR / sql_file, 'r') as file:
                sql_query = text(file.read())
                connection.execute(sql_query)
                print(f"Executed {sql_file}")