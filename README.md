# Football Analytics

## Dashboard Link
- https://tarakguptadrebes-football-analytics-app-zaylna.streamlit.app

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

# Initialize environment variables
cp .env.example .env
# Open .env and set your DATABASE_URL.
```

## Quick Start (Recommended)

```bash
# Load and transform data
poetry run python main.py --quick

# Launch dashboard
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

# Load and transform data
poetry run python main.py

# Launch dashboard
poetry run streamlit run app.py
```