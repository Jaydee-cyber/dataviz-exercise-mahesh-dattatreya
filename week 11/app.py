import streamlit as st

st.set_page_config(
    page_title="Gapminder Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Gapminder Dashboard")

st.write("Welcome to the Week 11 Data Visualization Exercise!")

st.markdown("""
### Dashboard Pages

- 📊 Summary
- 📈 Trends
- 🔍 Details

Use the sidebar to navigate between the pages.
""")
