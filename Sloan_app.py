import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import base64

# Load the trained model
model_path = 'decision_tree_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Set page config
st.set_page_config(page_title="Celestial Object Classifier", page_icon=":star:", layout="wide")

# Load background image
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('assets/pexels-minan1398-813269.jpg')

# Custom CSS for a colorful look
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: white; 
        color: black; 
        border: 2px solid #4CAF50;
    }
    .stTextInput>div>input {
        border: 2px solid #4CAF50;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title(":star: Celestial Object Classifier :star:")

def main():
    st.header("Enter the parameters to classify the object")

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            ra = st.number_input('Right Ascension (ra)', format="%.8f")
            u = st.number_input('u-band magnitude', format="%.8f")
            r = st.number_input('r-band magnitude', format="%.8f")
            z = st.number_input('z-band magnitude', format="%.8f")

        with col2:
            dec = st.number_input('Declination (dec)', format="%.8f")
            g = st.number_input('g-band magnitude', format="%.8f")
            i = st.number_input('i-band magnitude', format="%.8f")
            redshift = st.number_input('Redshift', format="%.8f")

        submit_button = st.form_submit_button(label='Classify')

    if submit_button:
        input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]], columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
        prediction = model.predict(input_data)
        object_type = prediction[0]

        st.success(f"The object is classified as: {object_type}")
        st.balloons()

if __name__ == "__main__":
    main()
