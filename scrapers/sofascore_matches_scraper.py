from ScraperFC.sofascore import Sofascore
import pandas as pd

def scrape_matches(leagues, seasons):

    ss = Sofascore()
    matches = []

    # Loop through each season and league to get match info
    for season in seasons:
        for league in leagues:
            for m in ss.get_match_dicts(year=season, league=league):
                matches.append(m)

    df = pd.DataFrame(matches)
    return df