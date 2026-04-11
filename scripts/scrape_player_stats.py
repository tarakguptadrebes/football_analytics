import sys
from database import get_engine, clean_for_sql
from config import LEAGUES, SEASONS
from scrapers.sofascore_player_stats_scraper import scrape_player_stats

def main():

    slug = sys.argv[1]
    name = LEAGUES.get(slug)

    if not name:
        print(f"Error: '{slug}' is not valid. Check config.py.")
        return

    df = scrape_player_stats(name, SEASONS)

    df = clean_for_sql(df)
    engine = get_engine()
    table_name = f"sofascore_{slug}_player_stats"

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to table '{table_name}' in the database.")

if __name__ == "__main__":
    main()
    
