import sys
from src.football_analytics.load_csv_data import load_csv
from src.football_analytics.download_transfermarkt_data import download
from src.football_analytics.run_sql import run_sql

def main():
    is_quick = "--quick" in sys.argv
    
    download()

    if is_quick:
        load_csv()
        run_sql(quickstart=True)
    else:
        run_sql(quickstart=False)

if __name__ == "__main__":
    main()
