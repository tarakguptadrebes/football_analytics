import os
import sys

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from football_analytics.database import get_engine

st.set_page_config(page_title='Football Analytics Dashboard', layout='wide')

st.title('Football Analytics Dashboard')

st.caption(
    '**Methodology Note:** Cohorts consist of the top 500 highest-valued players '
    'at each age who possess complete rating profiles. Players with missing source metrics '
    'are omitted prior to ranking.'
)

@st.cache_resource
def get_db_engine():
    engine = get_engine()
    return engine

@st.cache_data
def load_avg_market_value_with_age():
    return pd.read_sql('SELECT age, avg_market_value FROM avg_market_value_with_age', get_db_engine())

@st.cache_data
def load_avg_rating_with_age():
    return pd.read_sql('SELECT age, avg_rating FROM avg_rating_with_age', get_db_engine())

@st.cache_data
def load_change_in_market_value():
    return pd.read_sql('SELECT age, change_in_value FROM change_in_market_value', get_db_engine())

@st.cache_data
def load_values_ratings_with_age():
    return pd.read_sql('SELECT age, market_value_in_eur, rating FROM values_ratings_with_age', get_db_engine())

df_value = load_avg_market_value_with_age()

fig = px.line(
    df_value,
    x='age',
    y='avg_market_value',
    title='Average Market Value by Age for Top 500 Players By Market Value at Each Age',
    labels={'age': 'Age', 'avg_market_value': 'Average Market Value (€)'},
    markers=True
)

st.plotly_chart(fig, width='stretch')

df_rating = load_avg_rating_with_age()

fig = px.line(
    df_rating,
    x='age',
    y='avg_rating',
    title='Average Rating by Age for Top 500 Players By Market Value at Each Age',
    labels={'age': 'Age', 'avg_rating': 'Average Rating'},
    markers=True
)

st.plotly_chart(fig, width='stretch')

df_change = load_change_in_market_value()

df_change['color_status'] = df_change['change_in_value'].apply(lambda x: 'Positive' if x >= 0 else 'Negative')

fig = px.bar(
    df_change,
    x='age',
    y='change_in_value',
    color='color_status',
    hover_data={'color_status':False},
    title='Change in Market Value by Age for Top 500 Players By Market Value at Each Age',
    labels={'age': 'Age', 'change_in_value': 'Change in Market Value (€)'},
    color_discrete_map={
        'Positive': '#10B981', 
        'Negative': '#EF4444' 
    }
)

fig.update_layout(showlegend=False)

st.plotly_chart(fig, width='stretch')

df_values_ratings = load_values_ratings_with_age()

fig = px.box(
    df_values_ratings,
    x='age',
    y='market_value_in_eur',
    title='Market Value Distribution by Age for Top 500 Players By Market Value at Each Age',
    labels={'age': 'Age', 'market_value_in_eur': 'Market Value (€)'},  
)

fig.update_layout(yaxis=dict(range=[0, 80_000_000]))

fig.update_traces(
    marker=dict(
        size=4,    
        opacity=0.1, 
        outliercolor='rgba(0,0,0,0)'
    )
)

st.plotly_chart(fig, width='stretch')

def get_age_group(age):
    if age < 21:
        return '18-20'
    elif 21 <= age < 24:
        return '21-23'
    elif 24 <= age < 27:
        return '24-26'
    elif 27 <= age < 30:
        return '27-29'
    elif 30 <= age < 33:
        return '30-32'
    elif 33 <= age < 36:
        return '33-35'
    
df_values_ratings['age_group'] = df_values_ratings['age'].apply(get_age_group)

fig = go.Figure()

colors={
    '18-20': '#8B5CF6', '21-23': '#3B82F6', '24-26': '#10B981',
    '27-29': '#FACC15', '30-32': '#F97316', '33-35': '#EF4444'
}

for group in ['18-20', '21-23', '24-26', '27-29', '30-32', '33-35']:
    subset = df_values_ratings[df_values_ratings['age_group'] == group]
    if subset.empty: continue

    fig.add_scatter(
            x=subset['rating'],
            y=subset['market_value_in_eur'],
            mode='markers',
            name=group,
            showlegend=False,
            marker=dict(
                size=4,
                color=colors[group],
                opacity=0.1
            )
        )

for group in ['18-20', '21-23', '24-26', '27-29', '30-32', '33-35']:
    subset = df_values_ratings[df_values_ratings['age_group'] == group]
    if subset.empty: continue
    
    m, c = np.polyfit(subset['rating'], subset['market_value_in_eur'], 1)
                      
    formula_text = f"y = {m/1e6:.2f}Mx + {c/1e6:.2f}M"

    min_y, max_y = subset['market_value_in_eur'].min(), subset['market_value_in_eur'].max()
    min_x, max_x = subset['rating'].min(), subset['rating'].max()

    x_start, x_end = min_x, max_x
    y_start, y_end = m * x_start + c, m * x_end + c

    if y_start < min_y:
        y_start = min_y
        x_start = (y_start - c) / m
    if y_end > max_y:
        y_end = max_y
        x_end = (y_end - c) / m

    x_start = max(x_start, min_x)
    x_end = min(x_end, max_x)
    y_start, y_end = m * x_start + c, m * x_end + c

    fig.add_scatter(
        x=[x_start, x_end],
        y=[y_start, y_end],
        mode='lines',
        name=f"<b>{group}</b> | {formula_text}",
        hoverinfo='skip', 
        line=dict(color=colors[group], width=3)
    )

fig.update_layout(
    title='Market Value vs Rating by Age (Top 500 Players By Market Value at Each Age)',
    xaxis_title='Rating',
    yaxis_title='Market Value (€)',
    xaxis=dict(
        range=[6.0, 9.0] 
    ),
    yaxis=dict(
        range=[0, 100_000_000] 
    ),
    legend=dict(
        title='Age Group & Trendline',
    )
)

st.plotly_chart(fig, use_container_width=True)