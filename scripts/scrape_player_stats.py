import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

from scrapers.sofascore_player_stats_scraper import scrape_player_stats

load_dotenv()

def main():
    LEAGUES = [
        {"name": "England Premier League", "slug": "premier_league"},
        {"name": "Spain La Liga", "slug": "la_liga"},
        {"name": "Germany Bundesliga", "slug": "bundesliga"},
        {"name": "Italy Serie A", "slug": "serie_a"},
        {"name": "France Ligue 1", "slug": "ligue_1"}
    ]

    league_slug = sys.argv[1]

    league = next(league for league in LEAGUES if league["slug"] == league_slug)

    seasons = ["20/21", "21/22", "22/23", "23/24", "24/25"]

    df = scrape_player_stats(league["name"], seasons)
    table_name = f"sofascore_{league_slug}_player_stats"

    db_url = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    engine = create_engine(db_url)

    dict_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, dict)).any()]
    df = df.drop(columns=dict_cols)

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to table '{table_name}' in the database.")

if __name__ == "__main__":
    main()
    
