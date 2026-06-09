from src.football_analytics.database import clean_for_sql
from ScraperFC.sofascore import Sofascore
import pandas as pd
import random
import time

# Loop through each season to get all match IDs
def scrape_player_stats(league, seasons):
    
    ss = Sofascore()
    player_stats = []
    match_ids = []

    for season in seasons:
        matches = ss.get_match_dicts(year=season, league=league)    
        match_ids.extend([int(m['id']) for m in matches if 'id' in m])

    random.shuffle(match_ids)

    total_matches = len(match_ids)

    # Loop through each match ID and scrape player stats
    for i, match_id in enumerate(match_ids):
        time.sleep(random.uniform(5, 10)) 

        try:
            df = ss.scrape_player_match_stats(match_id)

        except UnboundLocalError:
            print(f"Skipping match {match_id}")
            df = None
        
        if df is not None and not df.empty:
                df['match_id'] = match_id
                df_cleaned = clean_for_sql(df)
                player_stats.append(df_cleaned)

        print(f"{i+1}/{total_matches}", end='\r')    # simple progress counter

    return pd.concat(player_stats, ignore_index=True)