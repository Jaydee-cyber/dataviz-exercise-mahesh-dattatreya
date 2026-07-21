import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Summary", page_icon="📊", layout="wide")

df = load_data()

st.title("📊 What does the Gapminder dataset tell us at a glance?")

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Countries", df["country"].nunique())

with col2:
    st.metric("Continents", df["continent"].nunique())

with col3:
    st.metric("Years", df["year"].nunique())

st.divider()

# Colour type: Qualitative colours (continent categories)
fig = px.scatter(
    df,
    x="gdpPercap",
    y="lifeExp",
    color="continent",
    hover_name="country",
    size="pop",
    log_x=True,
    title="GDP per Capita vs Life Expectancy"
)

st.plotly_chart(fig, use_container_width=True)

