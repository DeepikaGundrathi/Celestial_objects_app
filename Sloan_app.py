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

# Option to upload a CSV file
upload_option = st.radio("Choose an input method:", ('Interactive Entry', 'Upload CSV'))

if upload_option == 'Interactive Entry':
    # Create sliders for the user to enter parameters interactively
    ra = st.slider('Right Ascension (ra) 📐', min_value=0.0, max_value=360.0, step=0.0001)
    dec = st.slider('Declination (dec) 📐', min_value=-90.0, max_value=90.0, step=0.0001)
    u = st.slider('u-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
    g = st.slider('g-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
    r = st.slider('r-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
    i = st.slider('i-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
    z = st.slider('z-band magnitude 📊', min_value=0.0, max_value=30.0, step=0.0001)
    redshift = st.slider('Redshift 🌌', min_value=-1.0, max_value=10.0, step=0.0001)
    
    if st.button('Classify 🔭'):
        # Show a progress bar
        with st.spinner('Classifying... 🚀'):
            # Create a DataFrame for prediction
            input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]],
                                      columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
            
            # Make a prediction
            prediction = model.predict(input_data)[0]
        
        # Display the prediction
        st.success(f"### 🛸 Predicted Object Type: **{prediction}**")
        st.balloons()
else:
    uploaded_file = st.file_uploader("Upload a CSV file with columns ['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift']", type="csv")
    
    if uploaded_file is not None:
        input_data = pd.read_csv(uploaded_file)
        if st.button('Classify 🔭'):
            # Show a progress bar
            with st.spinner('Classifying... 🚀'):
                # Make predictions
                predictions = model.predict(input_data)
            
            # Display the predictions
            st.success("### 🛸 Predicted Object Types:")
            st.dataframe(pd.DataFrame(predictions, columns=["Prediction"]))
            st.balloons()

# Footer with emoji
st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")

# Add some colorful elements
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        border: 2px solid #ff4b4b;
        font-size: 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: white;
        color: #ff4b4b;
    }
    .stMarkdown h2 {
        color: #ff4b4b;
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
</style>
""", unsafe_allow_html=True)
