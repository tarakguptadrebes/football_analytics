import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import football_analytics
from football_analytics.database import get_engine

PACKAGE_ROOT = Path(football_analytics.__file__).parent
PROJECT_ROOT = PACKAGE_ROOT.parent.parent

load_dotenv(PROJECT_ROOT / '.env')

def load_csv():
    engine = get_engine()
    csv_path = PROJECT_ROOT / 'data' / 'sofascore_player_match_data.csv'
    df = pd.read_csv(csv_path)
    df.to_sql("sofascore_player_match_data", engine, if_exists="replace", index=False)
    print("Data saved to table sofascore_player_match_data in the database.")

if __name__ == "__main__":
    load_csv()