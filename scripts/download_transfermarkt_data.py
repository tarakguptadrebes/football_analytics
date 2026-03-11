import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("davidcariboo/player-scores")
print("Path to dataset files:", path)

players = pd.read_csv(os.path.join(path, "players.csv"))

print(players.head())