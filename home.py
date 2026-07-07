import streamlit as st

st.set_page_config(
    page_title="Real Estate Investment Analyst",
    page_icon="🏡",
    layout="wide"
)

st.title("🏡 Real Estate Investment Analyst")

st.markdown("""
### Predict • Analyze • Invest

An AI-powered application that predicts property prices in Gurugram
using Machine Learning and provides investment insights.
""")

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric("🏘️ Properties", "3,800+")
col2.metric("📍 Sectors", "104")
col3.metric("💰 Avg Price", "₹2.45 Cr")
col4.metric("🎯 Model R²", "0.91")

st.divider()

st.subheader("✨ Features")

c1, c2 = st.columns(2)

with c1:
    st.success("🤖 AI Price Prediction")
    st.success("🗺️ Interactive Property Map")
    st.success("📈 Market Trends")

with c2:
    st.success("🏡 Similar Property Recommendation")
    st.success("💹 Investment Analysis")
    st.success("📊 Feature Importance")

st.divider()

st.subheader("⚙️ Machine Learning Pipeline")

st.code("""
Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
ColumnTransformer
    ↓
ExtraTreesRegressor
    ↓
Predicted Property Price
""")

st.divider()

st.info(
    "This application predicts property prices using Machine Learning "
    "and helps users make informed real estate investment decisions."
)