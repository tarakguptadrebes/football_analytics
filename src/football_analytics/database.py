import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_engine():

    db_url = os.getenv('DATABASE_URL') or st.secrets["DATABASE_URL"]

    if not db_url:
        raise ValueError("DATABASE_URL is not set in environment variables")
    
    return create_engine(db_url)

def clean_for_sql(df):

    if df.empty:
        return df
   
    df = df.loc[:, ~df.columns.duplicated()]

    dict_cols = [col for col in df.columns if df[col].apply(lambda x: isinstance(x, (dict, list))).any()]
    df = df.drop(columns=dict_cols)

    df = df.drop_duplicates()

    return df