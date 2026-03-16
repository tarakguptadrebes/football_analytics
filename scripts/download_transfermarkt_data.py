import kagglehub
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

path = kagglehub.dataset_download("davidcariboo/player-scores")
print("Path to dataset files:", path)

db_url = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
engine = create_engine(db_url)

players = pd.read_csv(os.path.join(path, "players.csv"))
player_valuations = pd.read_csv(os.path.join(path, "player_valuations.csv"))
players.to_sql("transfermarkt_players", engine, if_exists="replace", index=False)
player_valuations.to_sql("transfermarkt_player_valuations", engine, if_exists="replace", index=False)
print(f"Data saved to table 'transfermarkt_players' in the database.")
print(f"Data saved to table 'transfermarkt_player_valuations' in the database.")