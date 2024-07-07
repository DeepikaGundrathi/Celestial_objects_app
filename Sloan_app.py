import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
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

# Add welcome page with 3D rotating moon
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    st.markdown("""
    <style>
    .welcome-container {
        text-align: center;
        color: white;
    }
    .welcome-title {
        font-size: 3em;
        animation: sparkles 2s infinite;
    }
    .welcome-subtitle {
        font-size: 1.5em;
    }
    @keyframes sparkles {
        0% { text-shadow: 0 0 5px #ffffff; }
        50% { text-shadow: 0 0 20px #ffffff; }
        100% { text-shadow: 0 0 5px #ffffff; }
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-container">
        <div class="welcome-title">✨ Welcome to the Galaxy App! ✨</div>
        <div class="welcome-subtitle">Discover and classify celestial objects: Stars, Galaxies, or Quasars</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 3D rotating moon model using Plotly
    fig = go.Figure(go.Surface(
        z=[[0, 0], [0, 0]],
        surfacecolor=[[0, 0], [0, 0]],
        cmin=0,
        cmax=0,
        colorscale=[[0, "gray"], [1, "gray"]],
        showscale=False,
        opacity=0.8
    ))
    
    fig.update_layout(
        title='🌙 Rotating Moon 🌙',
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            annotations=[dict(
                showarrow=False,
                text="Click Here to Begin 🚀",
                x=0,
                y=0,
                z=0,
                xanchor="left",
                xshift=0,
                opacity=1,
                font=dict(color="white", size=15)
            )]
        ),
        width=800,
        height=800,
        margin=dict(l=0, r=0, b=0, t=40)
    )
    
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", project_z=True))

    st.plotly_chart(fig)

    if st.button("Click Here to Begin 🚀"):
        st.session_state.page = "main"

# Main classifier page
if st.session_state.page == "main":
    # Add title with emojis
    st.title("🌌 Sloan Digital Sky Survey (SDSS) Classifier ✨")

    # Add subtitle and description
    st.markdown("## Classify Celestial Objects: Stars, Galaxies, or Quasars 🌠")
    st.markdown("""
    Welcome to the SDSS classifier app! This app helps you classify celestial objects into stars, galaxies, or quasars based on their photometric and spectral features. Please enter the parameters below to get started.
    """)

    # Emoji separator
    st.markdown("### 🚀 Input Parameters 👇")

    # Manual entry of parameters with colorful input widgets
    with st.expander("Manual Entry"):
        with st.form(key='manual_entry_form'):
            st.markdown("#### 📐 Coordinates")
            ra = st.text_input('Right Ascension (ra)', value='0.0')
            dec = st.text_input('Declination (dec)', value='0.0')

            st.markdown("#### 📊 Magnitudes")
            u = st.text_input('u-band magnitude', value='0.0')
            g = st.text_input('g-band magnitude', value='0.0')
            r = st.text_input('r-band magnitude', value='0.0')
            i = st.text_input('i-band magnitude', value='0.0')
            z = st.text_input('z-band magnitude', value='0.0')

            st.markdown("#### 🌌 Redshift")
            redshift = st.text_input('Redshift', value='0.0')

            manual_submit_button = st.form_submit_button(label='Classify 🔭')

    # File upload for parameters
    with st.expander("Upload CSV File"):
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            input_data = pd.read_csv(uploaded_file)
            st.write("Uploaded Data Preview:")
            st.write(input_data)
            file_submit_button = st.button("Classify from File 🔭")

    # Handling the prediction for manual entry
    if manual_submit_button:
        with st.spinner('Classifying... 🚀'):
            input_data = pd.DataFrame([[float(ra), float(dec), float(u), float(g), float(r), float(i), float(z), float(redshift)]], columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])
            prediction = model.predict(input_data)[0]
        st.success(f"### 🛸 Predicted Object Type: **{prediction}**")
        st.balloons()
        st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")

    # Handling the prediction for file upload
    if 'file_submit_button' in locals() and file_submit_button and uploaded_file is not None:
        with st.spinner('Classifying... 🚀'):
            predictions = model.predict(input_data)
            input_data['Predicted Class'] = predictions
            st.write("Classification Results:")
            st.write(input_data)
        st.success("### 🛸 Classification Completed!")
        st.balloons()
        st.markdown("### 🌟 Thank you for using the SDSS Classifier! 🌟")

    # Add some colorful elements and animations
    st.markdown("""
    <style>
        .stApp {
            color: #ffffff;
        }
        .stTextInput>div>input {
            border: 2px solid #ff4b4b;
            background-color: #ffffff;
            color: #000000;
            font-size: 16px;
            padding: 5px;
            border-radius: 10px;
            box-shadow: 0 0 5px #ff4b4b;
            animation: inputglow 1.5s infinite;
        }
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
        @keyframes inputglow {
            0% { box-shadow: 0 0 5px #ff4b4b; }
            50% { box-shadow: 0 0 10px #ff4b4b; }
            100% { box-shadow: 0 0 5px #ff4b4b; }
        }
        .stMarkdown h2 {
            color: #ff4b4b;
            animation: colorchange 5s infinite;
        }
        .stMarkdown p {
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
