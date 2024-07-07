import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Load the trained model
model_path = "decision_tree_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Set background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url({image_url});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
background_image_url = "https://github.com/SriKumar1313/Sloan_app/raw/main/assets/pexels-minan1398-813269.jpg"
set_background(background_image_url)

# Add title and emojis
st.title("🌌 Sloan Digital Sky Survey (SDSS) Classifier ✨")

# Add subtitle and description
st.markdown("## Classify Celestial Objects: Stars, Galaxies, or Quasars 🌠")
st.markdown("""
Welcome to the SDSS classifier app! This app helps you classify celestial objects into stars, galaxies, or quasars based on their photometric and spectral features. Please enter the parameters below to get started.
""")

# Emoji separator
st.markdown("### 🚀 Input Parameters 👇")

# Option to upload a CSV file or use the form
upload_option = st.radio("Choose an input method:", ('Interactive Form', 'Upload CSV'))

if upload_option == 'Interactive Form':
    with st.form(key='parameters_form'):
        ra = st.slider('Right Ascension (ra) 📐', min_value=0.0, max_value=360.0, step=0.0001)
        dec = st.slider('Declination (dec) 📐', min_value=-90.0, max_value=90.0, step=0.0001)
        u = st.slider('u-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
        g = st.slider('g-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
        r = st.slider('r-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
        i = st.slider('i-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
        z = st.slider('z-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
        redshift = st.slider('Redshift 🌌', min_value=-1.0, max_value=10.0, step=0.0001)
        
        submit_button = st.form_submit_button(label='Classify 🔭')

    if submit_button:
        with st.spinner('Classifying... 🚀'):
            input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]], columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
            prediction = model.predict(input_data)[0]
        st.success(f"### 🛸 Predicted Object Type: **{prediction}**")
        st.balloons()
else:
    uploaded_file = st.file_uploader("Upload a CSV file with columns ['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift']", type="csv")
    if uploaded_file is not None:
        input_data = pd.read_csv(uploaded_file)
        if st.button('Classify 🔭'):
            with st.spinner('Classifying... 🚀'):
                predictions = model.predict(input_data)
            st.success("### 🛸 Predicted Object Types:")
            st.dataframe(pd.DataFrame(predictions, columns=["Prediction"]))
            st.balloons()

# Footer with emoji
st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")

# Add some colorful elements and animations
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
        font-size: 20px;
        font-weight: bold;
        animation: glow 1.5s infinite;
    }
    .stButton>button:hover {
        background-color: white;
        color: #ff4b4b;
    }
    @keyframes glow {
        0% { box-shadow: 0 0 5px #ff4b4b; }
        50% { box-shadow: 0 0 20px #ff4b4b; }
        100% { box-shadow: 0 0 5px #ff4b4b; }
    }
    .stMarkdown h2 {
        color: #ff4b4b;
        animation: colorchange 5s infinite;
    }
    .stMarkdown p {
        color: #ff4b4b;
    }
    .stRadio>label {
        color: #ff4b4b;
    }
    .stMarkdown img {
        border-radius: 10px;
    }
    @keyframes colorchange {
        0% { color: #ff4b4b; }
        25% { color: #ff0000; }
        50% { color: #ff4b4b; }
        75% { color: #ff0000; }
        100% { color: #ff4b4b; }
    }
</style>
""", unsafe_allow_html=True)
