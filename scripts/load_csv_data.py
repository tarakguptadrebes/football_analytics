import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
from database import get_engine

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

def load_csv():
    engine = get_engine()
    csv_path = BASE_DIR / 'data' / 'sofascore_player_match_data.csv'
    df = pd.read_csv(csv_path)
    df.to_sql("sofascore_player_match_data", engine, if_exists="replace", index=False)
    print("Data saved to table sofascore_player_match_data in the database.")

if __name__ == "__main__":
    load_csv()