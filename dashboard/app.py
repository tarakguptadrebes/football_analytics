import pandas as pd
import streamlit as st
import plotly.express as px
import statsmodels.api as sm
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
def load_values_ratings_with_age():
    return pd.read_sql("SELECT age, market_value_in_eur, rating FROM values_ratings_with_age", engine)

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

df_change['color_status'] = df_change['change_in_value'].apply(lambda x: 'Positive' if x >= 0 else 'Negative')

fig = px.bar(
    df_change,
    x="age",
    y="change_in_value",
    color="color_status",
    title="Change in Market Value by Age",
    labels={"age": "Age", "change_in_value": "Change in Market Value (€)"},
    color_discrete_map={
        'Positive': '#00cc96', # Professional green
        'Negative': '#ef553b'  # Professional red
    }
)

fig.update_layout(showlegend=False)

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

df_values_ratings = load_values_ratings_with_age()

def get_age_group(age):
    if age < 24:
        return "18-24"
    elif 24 <= age < 30:
        return "24-29"
    elif 30 <= age < 36:
        return "30-35"
    
df_values_ratings['age_group'] = df_values_ratings['age'].apply(get_age_group)

fig = px.scatter(
    df_values_ratings,
    x="market_value_in_eur",
    y="rating",
    trendline="ols",
    title="Average Rating by Market Value",
    labels={"market_value_in_eur": "Market Value (€)", "rating": "Average Rating"},
    color="age_group",
    color_discrete_map={
        "18-24": "#00CC96", 
        "24-29": "#636EFA", 
        "30-35": "#EF553B"
    }
)
results = px.get_trendline_results(fig)
model = results.iloc[0]["px_fit_results"]

alpha = model.params[0]
beta = model.params[1]
r_squared = model.rsquared

fig.update_traces(
    marker=dict(
        size=2,    
        opacity=0.3, 
    )
)

st.plotly_chart(fig, width='stretch')