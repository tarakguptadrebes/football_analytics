import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_engine():

    db_url = os.getenv('DB_URL') or st.secrets.get("DB_URL")

    if not db_url:
        raise ValueError("DB_URL is not set in environment variables")
    
    return create_engine(db_url)

def clean_for_sql(df):

    if df.empty:
        return df
   
    df = df.loc[:, ~df.columns.duplicated()]

    dict_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, (dict, list))).any()]
    df = df.drop(columns=dict_cols)

    df = df.drop_duplicates()

    return df