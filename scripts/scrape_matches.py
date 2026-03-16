import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

from scrapers.sofascore_matches_scraper import scrape_matches

load_dotenv()

def main():
    df = scrape_matches()
    table_name = "sofascore_matches"

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
    
