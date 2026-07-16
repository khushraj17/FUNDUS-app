import streamlit as st
from streamlit_float import *

st.title("🏡 FUNDUS")

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

st.divider()
st.subheader("⚙️ Machine Learning Workflow")

workflow = """
<div style="display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
gap:10px;">

<div style="padding:18px;border-radius:12px;background:#262730;">
📂<br><b>Raw Data</b>
</div>

➡️

<div style="padding:18px;border-radius:12px;background:#262730;">
🧹<br><b>Cleaning</b>
</div>

➡️

<div style="padding:18px;border-radius:12px;background:#262730;">
⚙️<br><b>Feature Engineering</b>
</div>

➡️

<div style="padding:18px;border-radius:12px;background:#262730;">
🔄<br><b>Preprocessing</b>
</div>

➡️

<div style="padding:18px;border-radius:12px;background:#262730;">
🤖<br><b>ExtraTrees</b>
</div>

➡️

<div style="padding:18px;border-radius:12px;background:#262730;">
💰<br><b>Prediction</b>
</div>

</div>
"""

st.markdown(workflow, unsafe_allow_html=True)

st.divider()

st.subheader("🛠️ Built With")
st.caption("Technologies powering the FUNDUS platform")

techs = [
    {
        "name": "Python",
        "desc": "Core Programming Language",
        "logo": "https://cdn.simpleicons.org/python/3776AB"
    },
    {
        "name": "Streamlit",
        "desc": "Interactive Web Framework",
        "logo": "https://cdn.simpleicons.org/streamlit/FF4B4B"
    },
    {
        "name": "Pandas",
        "desc": "Data Analysis",
        "logo": "https://cdn.simpleicons.org/pandas/150458"
    },
    {
        "name": "NumPy",
        "desc": "Numerical Computing",
        "logo": "https://cdn.simpleicons.org/numpy/013243"
    },
    {
        "name": "Scikit-Learn",
        "desc": "Machine Learning",
        "logo": "https://cdn.simpleicons.org/scikitlearn/F7931E"
    },
    {
        "name": "Extra Trees",
        "desc": "Regression Model",
        "logo": "https://cdn.simpleicons.org/scikitlearn/F7931E"
    },
    {
        "name": "Plotly",
        "desc": "Interactive Visualization",
        "logo": "https://cdn.simpleicons.org/plotly/3F4F75"
    },
    {
        "name": "Joblib",
        "desc": "Model Serialization",
        "logo": "https://cdn.simpleicons.org/python/3776AB"
    },
    {
        "name": "Category Encoder",
        "desc": "Feature Encoding",
        "logo": "https://cdn.simpleicons.org/scikitlearn/F7931E"
    },
    {
        "name": "XGBoost",
        "desc": "Gradient Boosting",
        "logo": "https://cdn.simpleicons.org/xgboost/EE4C2C"
    }
]

html = """
<style>

.tech-grid{

    display:grid;

    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));

    gap:28px;

    margin-top:30px;

}

.tech-card{

    background:#161616;

    border:1px solid rgba(255,255,255,.08);

    border-radius:22px;

    padding:35px 25px;

    text-align:center;

    transition:.35s;

    cursor:pointer;

    position:relative;

    overflow:hidden;

}

.tech-card:hover{

    transform:translateY(-10px);

    border-color:#FF4B4B;

    box-shadow:0 18px 40px rgba(255,75,75,.22);

}

.tech-card::before{

    content:"";

    position:absolute;

    top:0;

    left:0;

    width:100%;

    height:5px;

    background:linear-gradient(
        90deg,
        #FF4B4B,
        #FF7A59
    );

}

.tech-logo{

    width:70px;

    height:70px;

    object-fit:contain;

    margin-bottom:22px;

}

.tech-title{

    color:white;

    font-size:23px;

    font-weight:700;

    margin-bottom:12px;

}

.tech-desc{

    color:#B8B8B8;

    line-height:1.6;

    font-size:15px;

}

</style>

<div class="tech-grid">
"""

for tech in techs:

    html += f"""
    <div class="tech-card">

        <img
            class="tech-logo"
            src="{tech['logo']}">

        <div class="tech-title">
            {tech['name']}
        </div>

        <div class="tech-desc">
            {tech['desc']}
        </div>

    </div>
    """

html += "</div>"

st.html(html)