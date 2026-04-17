# Football Analytics

## Setup

```bash
# Clone the repository
git clone https://github.com/tarakguptadrebes/football_analytics.git
cd football_analytics

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip3 install -r requirements.txt

# Create the PostgreSQL database
psql -U postgres -c "CREATE DATABASE football_db;"

# Initialize credentials
cp .env.example .env
# STOP: Open .env and enter your PostgreSQL password now!
```

## Quick Start (Recommended)

```bash
# Data collection
python3 -m scripts.load_csv_data
python3 -m scripts.download_transfermarkt_data

# Transform + load
python3 -m scripts.run_sql --quick

# Dashboard
python3 -m streamlit run dashboard/app.py
```

## Full Pipeline

```bash
# Data collection
python3 -m scripts.scrape_matches

python3 -m scripts.scrape_player_stats premier_league
python3 -m scripts.scrape_player_stats la_liga
python3 -m scripts.scrape_player_stats bundesliga
python3 -m scripts.scrape_player_stats serie_a
python3 -m scripts.scrape_player_stats ligue_1

python3 -m scripts.download_transfermarkt_data

# Transform + load
python3 -m scripts.run_sql

# Dashboard
python3 -m streamlit run dashboard/app.py
```