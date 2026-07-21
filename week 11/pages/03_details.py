import streamlit as st
import plotly.express as px
from utils import load_data

st.set_page_config(
    page_title="Details",
    page_icon="🔍",
    layout="wide"
)

df = load_data()

st.title("🔍 Which country would you like to explore?")

# -------- Session State --------
if "country" not in st.session_state:
    st.session_state.country = "Germany"

country = st.selectbox(
    "Choose a country",
    sorted(df["country"].unique()),
    index=sorted(df["country"].unique()).index(st.session_state.country)
)

st.session_state.country = country

filtered = df[df["country"] == st.session_state.country]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Life Expectancy")

    # Colour type: Sequential (year)
    fig1 = px.line(
        filtered,
        x="year",
        y="lifeExp",
        markers=True,
        color="year",
        title=f"Life Expectancy - {country}"
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("GDP Per Capita")

    # Colour type: Sequential (year)
    fig2 = px.bar(
        filtered,
        x="year",
        y="gdpPercap",
        color="year",
        title=f"GDP Per Capita - {country}"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.success(f"You selected: **{st.session_state.country}**")
