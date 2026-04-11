import kagglehub
import pandas as pd
import os
from database import get_engine

def main():
    path = kagglehub.dataset_download("davidcariboo/player-scores")
    print("Path to dataset files:", path)

    engine = get_engine()

    players = pd.read_csv(os.path.join(path, "players.csv"))
    player_valuations = pd.read_csv(os.path.join(path, "player_valuations.csv"))
    players.to_sql("transfermarkt_players", engine, if_exists="replace", index=False)
    player_valuations.to_sql("transfermarkt_player_valuations", engine, if_exists="replace", index=False)
    print(f"Data saved to table 'transfermarkt_players' in the database.")
    print(f"Data saved to table 'transfermarkt_player_valuations' in the database.")

if __name__ == "__main__":
    main()