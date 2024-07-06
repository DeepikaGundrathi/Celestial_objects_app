import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the pickle file
model_filename = 'decision_tree_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Define the app
st.set_page_config(page_title="SDSS Object Classification", layout="centered", initial_sidebar_state="expanded")

st.title('Sloan Digital Sky Survey Object Classification')
st.write('Predict whether an object is a star, galaxy, or QSO based on its features.')

# Define the input fields for user to enter data
def user_input_features():
    st.sidebar.header('User Input Features')
    ra = st.sidebar.number_input('Right Ascension (ra)', min_value=0.0)
    dec = st.sidebar.number_input('Declination (dec)', min_value=0.0)
    u = st.sidebar.number_input('u')
    g = st.sidebar.number_input('g')
    r = st.sidebar.number_input('r')
    i = st.sidebar.number_input('i')
    z = st.sidebar.number_input('z')
    redshift = st.sidebar.number_input('Redshift')
    
    data = {
        'ra': ra,
        'dec': dec,
        'u': u,
        'g': g,
        'r': r,
        'i': i,
        'z': z,
        'redshift': redshift
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Display the input data
st.subheader('User Input features')
st.write(input_df)

# Make predictions
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

# Visualize prediction results
st.subheader('Prediction')
object_type = ['Galaxy', 'QSO', 'Star']
st.write(f"The object is classified as: **{object_type[prediction[0]]}**")

st.subheader('Prediction Probability')
st.write(pd.DataFrame(prediction_proba, columns=object_type))

# Add a footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed by [Your Name]</p>
    </div>
    """,
    unsafe_allow_html=True
)
