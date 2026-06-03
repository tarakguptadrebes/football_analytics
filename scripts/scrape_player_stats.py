import sys
from football_analytics.database import get_engine
from football_analytics.sofascore_player_stats_scraper import scrape_player_stats
from football_analytics.config import LEAGUES, SEASONS

def main():

    slug = sys.argv[1]
    name = LEAGUES.get(slug)

    if not name:
        print(f"Error: '{slug}' is not valid. Check config.py.")
        return

    df = scrape_player_stats(name, SEASONS)

    engine = get_engine()
    table_name = f"sofascore_{slug}_player_stats"

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to table '{table_name}' in the database.")

if __name__ == "__main__":
    main()