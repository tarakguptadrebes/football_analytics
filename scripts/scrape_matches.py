from football_analytics.database import get_engine
from football_analytics.sofascore_matches_scraper import scrape_matches
from football_analytics.config import LEAGUES, SEASONS

def main():
    league_names = list(LEAGUES.values())
    df = scrape_matches(league_names, SEASONS)

    engine = get_engine()
    table_name = "sofascore_matches"

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to table '{table_name}' in the database.")

if __name__ == "__main__":
    main()
    
