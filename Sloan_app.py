import streamlit as st
import pandas as pd
import pickle
from PIL import Image

# Load the trained model
model_path = "decision_tree_model.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Set background image
def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_path});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
background_image_url = "https://github.com/SriKumar1313/Sloan_app/raw/main/assets/pexels-minan1398-813269.jpg"
set_background(background_image_url)

# Add a title and some emojis
st.title("🌌 Sloan Digital Sky Survey (SDSS) Classifier ✨")

# Add a subtitle
st.markdown("## Classify Celestial Objects: Stars, Galaxies, or Quasars 🌠")

# Add some descriptive text
st.markdown("""
Welcome to the SDSS classifier app! 
This app helps you classify celestial objects into stars, galaxies, or quasars based on their photometric and spectral features. 
Please enter the parameters below to get started.
""")

# Add emoji separator
st.markdown("### 🚀 Input Parameters 👇")

# Create input fields for the user to enter parameters
ra = st.number_input('Right Ascension (ra) 📐', min_value=0.0, format="%.8f")
dec = st.number_input('Declination (dec) 📐', min_value=0.0, format="%.8f")
u = st.number_input('u-band magnitude 📊', min_value=0.0, format="%.8f")
g = st.number_input('g-band magnitude 📊', min_value=0.0, format="%.8f")
r = st.number_input('r-band magnitude 📊', min_value=0.0, format="%.8f")
i = st.number_input('i-band magnitude 📊', min_value=0.0, format="%.8f")
z = st.number_input('z-band magnitude 📊', min_value=0.0, format="%.8f")
redshift = st.number_input('Redshift 🌌', min_value=-1.0, format="%.8f")

# Add a predict button
if st.button('Classify 🔭'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]],
                              columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
    
    # Make a prediction
    prediction = model.predict(input_data)[0]
    
    # Display the prediction
    st.markdown(f"### 🛸 Predicted Object Type: **{prediction}**")

# Footer with emoji
st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")
