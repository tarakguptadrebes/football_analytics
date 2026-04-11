import pandas as pd
import streamlit as st
from database import get_engine

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

engine = get_engine()

st.title("Football Analytics Dashboard")

@st.cache_data
def test_connection():
    query = "SELECT 1 AS test"
    return pd.read_sql(query, engine)

df = test_connection()

st.dataframe(df)
