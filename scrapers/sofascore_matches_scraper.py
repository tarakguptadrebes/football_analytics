from ScraperFC.sofascore import Sofascore
import pandas as pd

def scrape_matches():

    ss = Sofascore()

    # Seasons and leagues to scrape
    seasons = ["20/21", "21/22", "22/23", "23/24", "24/25"]
    leagues = [
        "England Premier League",
        "Germany Bundesliga",
        "Spain La Liga",
        "Italy Serie A",
        "France Ligue 1",
        ]

    matches = []

    # Loop through each season and league to get match info
    for season in seasons:
        for league in leagues:
            for m in ss.get_match_dicts(year=season, league=league):
                matches.append(m)

    df = pd.DataFrame(matches)
    df = df.loc[:, ~df.columns.duplicated()]
    return df