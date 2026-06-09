import sys
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import text
from football_analytics.database import get_engine

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SQL_DIR = BASE_DIR / 'sql'
load_dotenv(BASE_DIR / '.env')

def run_sql(quickstart: bool = False):
    engine = get_engine()

    if quickstart:
        sql_files = [
            'player_mappings.sql',
            'market_values_with_age.sql',
            'ratings_with_age.sql',
            'values_ratings_with_age.sql',
            'avg_market_value_with_age.sql',
            'change_in_market_value.sql',
            'avg_rating_with_age.sql',
        ]
    else:
        sql_files = [
            'sofascore_player_stats.sql',
            'sofascore_player_match_data.sql',
            'player_mappings.sql',
            'market_values_with_age.sql',
            'ratings_with_age.sql',
            'values_ratings_with_age.sql',
            'avg_market_value_with_age.sql',
            'change_in_market_value.sql',
            'avg_rating_with_age.sql',
        ]

    with engine.begin() as conn:
        for sql_file in sql_files:
            sql_query = text((SQL_DIR / sql_file).read_text())
            conn.execute(sql_query)
            print(f"Executed {sql_file}")

if __name__ == '__main__':
    is_quick = '--quick' in sys.argv
    run_sql(quickstart=is_quick)