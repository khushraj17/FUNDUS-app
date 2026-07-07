import streamlit as st
import pandas as pd
import pickle
import numpy as np


st.set_page_config(
    page_title="Recommendation",
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded",)


location_df = pickle.load(open("location_df.pkl",'rb'))

cosine_sim1 = pickle.load(open("cosine_sim1.pkl",'rb'))
cosine_sim2 = pickle.load(open("cosine_sim2.pkl",'rb'))
cosine_sim3 = pickle.load(open("cosine_sim3.pkl",'rb'))

def recommend_properties_with_scores(property_name, top_n=247):
    
    cosine_sim_matrix = 0.5*cosine_sim1 + 0.8*cosine_sim2 + 1*cosine_sim3
    # cosine_sim_matrix = cosine_sim3
    
    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    
    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n+1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n+1]]
    
    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()
    
    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })
    
    return recommendations_df

# Test the recommender function using a property name
recommend_properties_with_scores('Ireo Victory Valley')

# st.markdown("""
# <style>
# div.stButton > button {
#     width:100%;
#     text-align:left;
#     padding:18px;
#     border-radius:12px;
#     border:1px solid #ddd;
#     background:#ffffff;
#     font-size:18px;
#     margin-bottom:10px;
# }

# div.stButton > button:hover{
#     border:2px solid #ff4b4b;
#     box-shadow:0px 2px 12px rgba(0,0,0,0.2);
# }
# </style>
# """, unsafe_allow_html=True)


st.title("Select Location and Radius")


col1, col2, col3 = st.columns([4,2,1])

with col1:
    selected_location = st.selectbox("location",sorted(location_df.columns.tolist()))

with col2:
    radius = st.number_input("radius in km",)

with col3:
    st.space()
    search = st.button("search")

if search :
    result_ser = location_df[location_df[selected_location] < radius][selected_location].sort_values()
    st.session_state.result_ser = result_ser
    st.session_state.selected_property = None

#-------------------------------

if "result_ser" in st.session_state:

    st.subheader("Nearby Properties")

    if len(st.session_state.result_ser) == 0:

        st.warning("No properties found.")

    else:

        for property_name, distance in st.session_state.result_ser.items():

            if st.button(
                f"🏠 {property_name}\n\n📍 {distance:.2f} km",
                key=f"btn_{property_name}"
            ):

                st.session_state.selected_property = property_name
                st.text("ss mai prop gai")

if (
    "selected_property" in st.session_state
    and st.session_state.selected_property is not None
):

    st.divider()

    st.subheader(
        f"Recommended for : {st.session_state.selected_property}"
    )

    recommendations = recommend_properties_with_scores(
        st.session_state.selected_property
    )

    st.dataframe(
        recommendations,
        use_container_width=True,
        hide_index=True
    )

