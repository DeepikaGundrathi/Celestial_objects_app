import streamlit as st
import pandas as pd
import pickle

# Load the model and predict
def load_model_and_predict(ra, dec, u, g, r, i, z, redshift):
    filename = 'decision_tree_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]],
                              columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])

    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    return prediction, prediction_proba

# Main function to create the Streamlit app
def main():
    st.set_page_config(
        page_title="Galaxy Type Classifier",
        page_icon=":milky_way:",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'About': "This app classifies celestial objects into stars, galaxies, or quasars based on photometric and spectral features."
        }
    )

    # CSS for custom background and styling
    st.markdown("""
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1575464675312-6c64631f980c");
            background-size: cover;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title('Galaxy Type Classifier :milky_way:')
    st.markdown("## Identify the type of celestial object using its features!")

    # User inputs
    st.sidebar.header("Input Parameters")
    ra = st.sidebar.number_input('RA (Right Ascension)', format="%.6f")
    dec = st.sidebar.number_input('Dec (Declination)', format="%.6f")
    u = st.sidebar.number_input('u (u-band magnitudes)')
    g = st.sidebar.number_input('g (g-band magnitudes)')
    r = st.sidebar.number_input('r (r-band magnitudes)')
    i = st.sidebar.number_input('i (i-band magnitudes)')
    z = st.sidebar.number_input('z (z-band magnitudes)')
    redshift = st.sidebar.number_input('redshift', min_value=-1.0, format="%.8f")

    if st.sidebar.button('Classify'):
        prediction, prediction_proba = load_model_and_predict(ra, dec, u, g, r, i, z, redshift)

        st.write('## Prediction Results :sparkles:')
        st.markdown(f"### Predicted Class: **{prediction[0]}**")
        st.markdown("### Class Probabilities:")
        class_names = ['Galaxy', 'Quasar', 'Star']
        for i, prob in enumerate(prediction_proba[0]):
            st.markdown(f"**{class_names[i]}**: {prob * 100:.2f}%")

        # Add a visual representation (e.g., bar chart) for the class probabilities
        st.bar_chart(pd.DataFrame(prediction_proba[0], index=class_names, columns=["Probability"]))

# Run the main function
if __name__ == '__main__':
    main()
