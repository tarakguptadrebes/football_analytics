import pandas as pd
import streamlit as st
import plotly.express as px
from database import get_engine

st.set_page_config(page_title="Football Analytics Dashboard", layout="wide")

engine = get_engine()

st.title("Football Analytics Dashboard")

@st.cache_data
def load_avg_market_value_with_age():
    return pd.read_sql("SELECT age, avg_market_value FROM avg_market_value_with_age", engine)

@st.cache_data
def load_avg_rating_with_age():
    return pd.read_sql("SELECT age, avg_rating FROM avg_rating_with_age", engine)

@st.cache_data
def load_change_in_market_value():
    return pd.read_sql("SELECT age, change_in_value FROM change_in_market_value", engine)

@st.cache_data
def load_market_values_with_age():
    return pd.read_sql("SELECT age, market_value_in_eur FROM market_values_with_age", engine)

@st.cache_data
def load_ratings_with_age():
    return pd.read_sql("SELECT age, rating FROM ratings_with_age", engine)

df_value = load_avg_market_value_with_age()

fig = px.line(
    df_value,
    x="age",
    y="avg_market_value",
    title="Average Market Value by Age",
    labels={"age": "Age", "avg_market_value": "Average Market Value (€)"},
    markers=True
)

st.plotly_chart(fig, width='stretch')

df_rating = load_avg_rating_with_age()

fig = px.line(
    df_rating,
    x="age",
    y="avg_rating",
    title="Average Rating by Age",
    labels={"age": "Age", "avg_rating": "Average Rating"},
    markers=True
)

st.plotly_chart(fig, width='stretch')

df_change = load_change_in_market_value()

fig = px.bar(
    df_change,
    x="age",
    y="change_in_value",
    title="Change in Market Value by Age",
    labels={"age": "Age", "change_in_value": "Change in Market Value (€)"},
)

st.plotly_chart(fig, width='stretch')

df_values = load_market_values_with_age()

fig = px.box(
    df_values,
    x="age",
    y="market_value_in_eur",
    title="Market Value Distribution by Age",
    labels={"age": "Age", "market_value_in_eur": "Market Value (€)"},  
)
fig.update_traces(
    marker=dict(
        size=2,    
        opacity=0.3, 
        outliercolor='rgba(0,0,0,0)'
    )
)

st.plotly_chart(fig, width='stretch')

df_ratings = load_ratings_with_age()

min_age = int(df_ratings['age'].min())
max_age = int(df_ratings['age'].max())

ages = st.slider("Select Age Range", min_age, max_age, (min_age, max_age))
filtered_df = df_ratings[(df_ratings['age'] >= ages[0]) & (df_ratings['age'] <= ages[1])]

fig = px.box(
    filtered_df,
    y="rating",
    title="Rating Distribution by Age",
    labels={"age": "Age", "rating": "Rating"},  
)
fig.update_traces(
    marker=dict(
        size=2,    
        opacity=0.3, 
        outliercolor='rgba(0,0,0,0)'
    )
)

st.plotly_chart(fig, width='stretch')