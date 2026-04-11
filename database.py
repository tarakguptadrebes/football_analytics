import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    db_url = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return create_engine(db_url)

def clean_for_sql(df):
    if df.empty:
        return df
    dict_cols = [col for col in df.columns if isinstance(df[col].iloc[0], dict)]
    return df.drop(columns=dict_cols)