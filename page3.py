import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import numpy as np

st.set_page_config(
    page_title="Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",)

st.markdown("""
# Welcome to the Analysis Page! 📊""")

df = pd.read_csv("final_data.csv")

neon = [
    "#FF1919", "#FF2619", "#FF3319", "#FF4119", "#FF4E19", "#FF5B19",
    "#FF6819", "#FF7619", "#FF8319", "#FF9019", "#FF9D19", "#FFAB19",
    "#FFB819", "#FFC519", "#FFD219", "#FFE019", "#FFED19", "#FFFA19",
    "#F6FF19", "#E8FF19", "#DBFF19", "#CEFF19", "#C1FF19", "#B3FF19",
    "#A6FF19", "#99FF19", "#8CFF19", "#7FFF19", "#71FF19", "#64FF19",
    "#57FF19", "#4AFF19", "#3CFF19", "#2FFF19", "#22FF19", "#19FF1D",
    "#19FF2B", "#19FF38", "#19FF45", "#19FF52", "#19FF60", "#19FF6D",
    "#19FF7A", "#19FF87", "#19FF95", "#19FFA2", "#19FFAF", "#19FFBC",
    "#19FFCA", "#19FFD7", "#19FFE4", "#19FFF1", "#19FFFF", "#19F1FF",
    "#19E4FF", "#19D7FF", "#19CAFF", "#19BCFF", "#19AFFF", "#19A2FF",
    "#1995FF", "#1987FF", "#197AFF", "#196DFF", "#1960FF", "#1952FF",
    "#1945FF", "#1938FF", "#192BFF", "#191DFF", "#2219FF", "#2F19FF",
    "#3C19FF", "#4A19FF", "#5719FF", "#6419FF", "#7119FF", "#7F19FF",
    "#8C19FF", "#9919FF", "#A619FF", "#B319FF", "#C119FF", "#CE19FF",
    "#DB19FF", "#E819FF", "#F619FF", "#FF19FA", "#FF19ED", "#FF19E0",
    "#FF19D2", "#FF19C5", "#FF19B8", "#FF19AB", "#FF199D", "#FF1990",
    "#FF1983", "#FF1976", "#FF1968", "#FF195B", "#FF194E", "#FF1941",
    "#FF1933", "#FF1926"
]

fig = px.scatter_map(
    df,
    lat="latitude",
    lon="longitude",
    color="sector",
    color_discrete_sequence=neon,
    size="price",
    hover_name="sector",
    map_style="carto-darkmatter",
    zoom=10,
    opacity=0.85,
    size_max=18
)

fig.update_traces(
    hovertemplate="""
<b>%{hovertext}</b><br>
Price: ₹%{marker.size:.2f} Cr<br>
<extra></extra>
"""
)

fig.update_layout(
     template="plotly_dark",
    height=400,
    margin=dict(l=0, r=0, t=50, b=0)
)

st.plotly_chart(fig, use_container_width=True)
