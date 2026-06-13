import sys
from football_analytics.load_csv_data import load_csv
from football_analytics.download_transfermarkt_data import download
from football_analytics.run_sql import run_sql

def main():
    is_all = '--all' in sys.argv
    
    download()

    if is_all:
        run_sql(quickstart=False)
    else:
        load_csv()
        run_sql(quickstart=True)

if __name__ == '__main__':
    main()
