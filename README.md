# Football Analytics

## Setup

```bash
# Clone the repository
git clone https://github.com/tarakguptadrebes/football_analytics.git
cd football_analytics

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create the PostgreSQL database
psql -U postgres -c "CREATE DATABASE football_db;"

# Initialize credentials
cp .env.example .env
# STOP: Open .env and enter your PostgreSQL password now!
```

## Quick Start (Recommended)

```bash
# Data collection
python -m scripts.load_csv_data
python -m scripts.download_transfermarkt_data

# Transform + load
python -m scripts.run_sql --quick

# Dashboard
python -m streamlit run dashboard/app.py
```

## Full Pipeline

```bash
# Data collection
python -m scripts.scrape_matches

python -m scripts.scrape_player_stats premier_league
python -m scripts.scrape_player_stats la_liga
python -m scripts.scrape_player_stats bundesliga
python -m scripts.scrape_player_stats serie_a
python -m scripts.scrape_player_stats ligue_1

python -m scripts.download_transfermarkt_data

# Transform + load
python -m scripts.run_sql

# Dashboard
python -m streamlit run dashboard/app.py
```