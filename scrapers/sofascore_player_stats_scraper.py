from ScraperFC.sofascore import Sofascore
import pandas as pd
import random
import time

ss = Sofascore()

# Loop through each season to get all match IDs
def scrape_player_stats(league, league_slug, seasons):

    player_stats = []
    match_ids = []

    for season in seasons:
        matches = ss.get_match_dicts(year=season, league=league)    
        match_ids.extend([int(m["id"]) for m in matches if "id" in m])

    random.shuffle(match_ids)

    total_matches = len(match_ids)

    # Loop through each match ID and scrape player stats
    for i, match_id in enumerate(match_ids):
        try:
            time.sleep(random.uniform(0.5, 1)) 
            df = ss.scrape_player_match_stats(match_id)
            if df is not None and not df.empty:
                df = df.loc[:, ~df.columns.duplicated()]    # remove duplicate columns
                df["match_id"] = match_id
                player_stats.append(df)
        except Exception as e:
            print(f"Error scraping match {match_id}: {e}")
            break
        
        print(f"{i+1}/{total_matches}", end="\r")    # simple progress counter

    # Save the combined player stats to a CSV file
    if player_stats:
        return pd.concat(player_stats, ignore_index=True)
    else:
        return pd.DataFrame()