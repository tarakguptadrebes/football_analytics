import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

from scrapers.sofascore_player_stats_scraper import scrape_player_stats
from scrapers.sofascore_matches_scraper import scrape_matches

load_dotenv()

def main():
    print("1. Scrape Player Stats")
    print("2. Scrape Matches")
    option = input("Enter the number of the scraper to run: ")

    if option == "1":
        
        LEAGUES = [
            {"name": "England Premier League", "slug": "premier_league"},
            {"name": "Spain La Liga", "slug": "la_liga"},
            {"name": "Germany Bundesliga", "slug": "bundesliga"},
            {"name": "Italy Serie A", "slug": "serie_a"},
            {"name": "France Ligue 1", "slug": "ligue_1"}
        ]

        for i, league in enumerate(LEAGUES, start=1):
            print(f"{i}. {league['name']}")
            
        league_option = input("Select a league by entering the corresponding number: ")
        
        try:
            league_index = int(league_option) - 1
        except ValueError:
            print("Invalid input")
            return

        if league_index < 0 or league_index >= len(LEAGUES):
            print("Invalid league option")
            return

        league = LEAGUES[league_index]
        league_slug = league["slug"]

        seasons = ["20/21", "21/22", "22/23", "23/24", "24/25"]

        df = scrape_player_stats(league["name"], seasons)
        table_name = f"sofascore_{league_slug}_player_stats"

    elif option == "2":
        df = scrape_matches()
        table_name = "sofascore_matches"

    else:
        print("Invalid option")
        return
    
    if df.empty:
        print("No data scraped.")
        return

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
    
