# Football Analytics

## Prerequisites

- Python 3.11+
- PostgreSQL
- Poetry installed (https://python-poetry.org/docs/#installation)

## Setup

```bash
# Clone the repository
git clone https://github.com/tarakguptadrebes/football_analytics.git
cd football_analytics

# Install dependencies
poetry install

# Create the PostgreSQL database
psql -U postgres -c "CREATE DATABASE football_db;"

# Initialize credentials
cp .env.example .env
# STOP: Open .env and enter your PostgreSQL password now!
```

## Quick Start (Recommended)

```bash
# Data collection
poetry run python -m scripts.load_csv_data
poetry run python -m scripts.download_transfermarkt_data

# Transform
poetry run python -m scripts.run_sql --quick

# Dashboard
poetry run streamlit run app.py
```

## Full Pipeline (Not Recommended)

```bash
# Data collection
poetry run python -m scripts.scrape_matches

poetry run python -m scripts.scrape_player_stats premier_league
poetry run python -m scripts.scrape_player_stats la_liga
poetry run python -m scripts.scrape_player_stats bundesliga
poetry run python -m scripts.scrape_player_stats serie_a
poetry run python -m scripts.scrape_player_stats ligue_1

poetry run python -m scripts.download_transfermarkt_data

# Transform
poetry run python -m scripts.run_sql

# Dashboard
poetry run streamlit run app.py
```