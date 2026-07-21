import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Trends", page_icon="📈", layout="wide")

df = load_data()

st.title("📈 How has life expectancy changed over time?")

tab1, tab2 = st.tabs(["Life Expectancy", "GDP Per Capita"])

with tab1:

    st.subheader("Life Expectancy Over Time")

    continent = st.selectbox(
        "Select a continent",
        sorted(df["continent"].unique())
    )

    filtered = df[df["continent"] == continent]

    # Colour type: Qualitative (countries)
    fig = px.line(
        filtered,
        x="year",
        y="lifeExp",
        color="country",
        title=f"Life Expectancy in {continent}"
    )

    st.plotly_chart(fig, use_container_width=True)

with tab2:

    st.subheader("GDP Per Capita Over Time")

    fig = px.line(
        df,
        x="year",
        y="gdpPercap",
        color="continent",
        title="GDP Per Capita by Continent"
    )

    st.plotly_chart(fig, use_container_width=True)
