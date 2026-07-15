import streamlit as st
from component.ai_assistant import render_ai
from component.footer import render_footer

st.set_page_config(
    page_title="FUNDUS",
    page_icon="🏡",
    layout="wide"
)

home = st.Page("pages/home.py", title="Home", icon="🏠")
analytics = st.Page("pages/page2.py", title="Price Prediction", icon="📈")
prediction = st.Page("pages/page3.py", title="Analysis", icon="📊")
recommendation = st.Page("pages/page4.py", title="Recommendation", icon="🏘️")

pg = st.navigation(
    {
        "FUNDUS": [
            home,
            analytics,
            prediction,
            recommendation
        ]
    },
    position="top" 
)

pg.run()

render_ai()
render_footer()