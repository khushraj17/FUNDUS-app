import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn

st.set_page_config(
    page_title="Price Prediction",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded")


st.sidebar.markdown("# Priz prediction")

st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0rem;
    }
    .subtitle {
        color: #808495;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 0.5rem;
        margin-bottom: 0.3rem;
        border-bottom: 1px solid rgba(128,128,128,0.25);
        padding-bottom: 0.3rem;
    }
    div.stButton > button {
        width: 100%;
        padding: 0.6rem 0;
        font-size: 1.05rem;
        font-weight: 600;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)



@st.cache_resource
def load_artifacts():
    with open('df.pkl', 'rb') as file:
        df = pickle.load(file)
    with open('ETRmodel2.pkl', 'rb') as file:
        model = pickle.load(file)
    return df, model

df, model = load_artifacts()


st.sidebar.info(
    "Fill in the property details on the main page and click **Predict** "
    "to get an estimated price range in Crores (₹)."
)
st.sidebar.markdown("---")
st.sidebar.caption("Model: Regression on log-transformed price")



st.markdown('<div class="main-title">Price Prediction Page! 📈</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter the property details below to estimate its price.</div>', unsafe_allow_html=True)



with st.form("prediction_form"):

    st.markdown('<div class="section-header">📍 Basic Details</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        property_type = st.selectbox("Property Type", sorted(df["property_type"].unique()))
    with col2:
        sector = st.selectbox("Sector", sorted(df["sector"].unique()))
    with col3:
        agePossession = st.selectbox("Age / Possession", sorted(df["agePossession"].unique()))

    st.markdown('<div class="section-header">🛏️ Rooms & Area</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        bedRoom = st.number_input("Bedrooms", min_value=1.0, max_value=20.0, value=3.0, step=1.0)
    with col2:
        bathroom = st.number_input("Bathrooms", min_value=1.0, max_value=20.0, value=2.0, step=1.0)
    with col3:
        balcony = st.selectbox("Balcony", sorted(df["balcony"].unique()))

    col1, col2 = st.columns(2)
    with col1:
        built_up_area = st.number_input("Built-up Area (sq.ft.)", min_value=100.0, value=1200.0, step=50.0)
    with col2:
        floor_category = st.selectbox("Floor Category", sorted(df["floor_category"].unique()))

    st.markdown('<div class="section-header">✨ Extra Features</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        servant_room = st.selectbox("Servant Room", [0.0, 1.0], format_func=lambda x: "Yes" if x == 1.0 else "No")
    with col2:
        store_room = st.selectbox("Store Room", [0.0, 1.0], format_func=lambda x: "Yes" if x == 1.0 else "No")
    with col3:
        furnishing_type = st.selectbox("Furnishing Type", sorted(df["furnishing_type"].unique()))

    luxury_category = st.selectbox("Luxury Category", sorted(df["luxury_category"].unique()))

    st.markdown("")
    submitted = st.form_submit_button("🔮 Predict Price")


if submitted:
    input_df = pd.DataFrame({
        "property_type": [property_type],
        "sector": [sector],
        "bedRoom": [bedRoom],
        "bathroom": [bathroom],
        "balcony": [balcony],
        "agePossession": [agePossession],
        "built_up_area": [built_up_area],
        "servant room": [servant_room],
        "store room": [store_room],
        "furnishing_type": [furnishing_type],
        "luxury_category": [luxury_category],
        "floor_category": [floor_category]
    })

    with st.spinner("Calculating estimate..."):
        base_price = np.expm1(model.predict(input_df))[0]
        low = base_price - 0.11
        high = base_price + 0.11

    st.markdown("---")
    res_col1, res_col2, res_col3 = st.columns([1, 4, 1])
    with res_col2:
        st.success(
            f"""
            ### 💰 Estimated Price

            **₹ {low:.2f} Cr**  ➜  **₹ {high:.2f} Cr**
            """
        )

    with st.expander("📋 View Input Summary"):
        st.dataframe(input_df.T.rename(columns={0: "Value"}), use_container_width=True)