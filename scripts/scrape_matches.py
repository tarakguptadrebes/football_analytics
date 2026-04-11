from database import get_engine, clean_for_sql
from config import LEAGUES, SEASONS
from scrapers.sofascore_matches_scraper import scrape_matches

def main():
    league_names = list(LEAGUES.values())
    df = scrape_matches(league_names, SEASONS)

    df = clean_for_sql(df)
    engine = get_engine()
    table_name = "sofascore_matches"

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data saved to table '{table_name}' in the database.")

if __name__ == "__main__":
    main()
    
