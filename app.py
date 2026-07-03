import streamlit as st

Home_page = st.Page("home.py", title="Home", icon="🏠")
page_2 = st.Page("page2.py", title="Price Prediction", icon="📈")
page_3 = st.Page("page3.py", title="Analysis", icon="📊")


pg = st.navigation([Home_page, page_2, page_3 ])
pg.run()