import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
import numpy as np

df = pd.read_csv("data.csv")
df1 = pd.read_csv("final_data.csv")

st.set_page_config(
    page_title="Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",)

st.title("📊 Gurugram Market Analytics")

st.markdown("### AI-powered insights from the Gurugram housing market")

st.divider()

col1, col2, col3, col4 = st.columns(4)

col1.metric("🏘 Properties", len(df))
col2.metric("📍 Sectors", df["sector"].nunique())
col3.metric("💰 Avg Price", f"{df['price'].mean():.2f} Cr")
col4.metric("⭐ Median Price", f"{df['price'].median():.2f} Cr")


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

fig = px.pie(
    df,
    names="property_type"
)
st.divider()
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("## 🏡 Property Type Insights")

    st.info("""
    **What does this chart show?**

    • Distribution of different property types across Gurugram.
    • Helps identify which property types dominate the market.
    • Useful for understanding supply patterns and investment opportunities.
    """)

    st.success(f"""
    **Key Insight**

    • Most Common Property Type: **{df['property_type'].mode()[0]}**
    • Total Property Types: **{df['property_type'].nunique()}**
    """)

fig2 = px.sunburst(
    df,
    path=["luxury_category", "property_type"],
    values="price",
    color="price",
    color_continuous_scale="Blues"
)

fig2.update_traces(
    hovertemplate=
    "<b>%{label}</b><br>"
    "Total Price : ₹%{value:.2f} Cr<br>"
    "Parent : %{parent}<br>"
    "Percentage : %{percentParent:.2%}<br>"
    "<extra></extra>"
)


st.divider()
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 📊 Luxury Category Insights")

    st.info("""
    **What does this chart show?**

    • Distribution of properties based on luxury categories.
    • Helps identify which luxury categories dominate the market.
    • Useful for understanding market segmentation and investment opportunities.
    """)

    st.success(f"""
    **Key Insight**

    • Most Common Luxury Category: **{df['luxury_category'].mode()[0]}**
    • Total Luxury Categories: **{df['luxury_category'].nunique()}**
    """)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.markdown("## 🗺️ Geographic Market Insights")

fig3 = px.scatter_map(
    df1,
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
fig3.update_traces(
    hovertemplate="""
<b>%{hovertext}</b><br>
Price: ₹%{marker.size:.2f} Cr<br>
<extra></extra>
"""
)

fig3.update_layout(
     template="plotly_dark",
    height=400,
    margin=dict(l=0, r=0, t=50, b=0)
)

st.plotly_chart(fig3, use_container_width=True)

st.info("""
### What does this map show?

This interactive map visualizes the geographical distribution of properties across **Gurugram**.

- 📍 Each marker represents a property listing.
- 🎨 Marker color identifies the sector.
- 📏 Marker size reflects the property's price.
- 🖱️ Hover over a marker to view sector information and property details.

This visualization helps identify property clusters, premium locations, and price concentration across the city.
""")

st.success(f"""
### 📊 Market Summary

🏘️ Total Properties: **{len(df1):,}**

📍 Total Sectors: **{df1['sector'].nunique()}**

💰 Average Price: **₹{df1['price'].mean():.2f} Cr**
""")

st.divider()



sector_price = (
    df.groupby("sector")["price"]
      .mean()
      .sort_values(ascending=False)
      .head(15)
)

fig2 = px.bar(
    sector_price,
    color=sector_price.index,
    title="Top 15 Expensive Sectors"
)


fig4 = px.sunburst(
    df,
    path=["luxury_category", "property_type"],
    values="price",
    color="price",
    color_continuous_scale="Blues",
    title="Luxury Category and Property Type Distribution"
)

fig4.update_traces(
    hovertemplate=
    "<b>%{label}</b><br>"
    "Total Price : ₹%{value:.2f} Cr<br>"
    "Parent : %{parent}<br>"
    "Percentage : %{percentParent:.2%}<br>"
    "<extra></extra>"
)


corr = df.select_dtypes("number").corr()

fig5 = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="reds",
    aspect="auto"
)


st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)