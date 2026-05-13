import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def get_engine():
    if not os.getenv('DB_USER'):
        raise ConnectionError("Missing environment variables. Did you create a .env file?")
    db_url = (
        f"postgresql+psycopg2://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    return create_engine(db_url)

def clean_for_sql(df):
    if df.empty:
        return df
   
    df = df.loc[:, ~df.columns.duplicated()]

    dict_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, (dict, list))).any()]
    df = df.drop(columns=dict_cols)

    df = df.drop_duplicates()

    return df