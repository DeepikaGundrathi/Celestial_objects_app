import streamlit as st
import pandas as pd
import pickle

# Function to load the model and predict
def load_model_and_predict(ra, dec, u, g, r, i, z, redshift):
    # Load the trained model from pickle file
    filename = 'decision_tree_model.pkl'
    with open(filename, 'rb') as f:
        model = pickle.load(f)

    # Prepare input data as a DataFrame for prediction
    input_data = pd.DataFrame([[ra, dec, u, g, r, i, z, redshift]],
                              columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z', 'redshift'])

    # Perform prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    return prediction, prediction_proba

# Main function to create the Streamlit app
def main():
    st.title('Galaxy Type Classifier')

    # User inputs
    ra = st.number_input('RA (Right Ascension)', format="%.6f")
    dec = st.number_input('Dec (Declination)', format="%.6f")
    u = st.number_input('u (u-band magnitudes)')
    g = st.number_input('g (g-band magnitudes)')
    r = st.number_input('r (r-band magnitudes)')
    i = st.number_input('i (i-band magnitudes)')
    z = st.number_input('z (z-band magnitudes)')
    redshift = st.number_input('redshift', min_value=-1.0, format="%.8f")

    if st.button('Classify'):
        prediction, prediction_proba = load_model_and_predict(ra, dec, u, g, r, i, z, redshift)

        st.write('## Prediction Results')
        st.write(f'Predicted Class: {prediction[0]}')
        st.write('Class Probabilities:')
        st.write(prediction_proba)

if __name__ == '__main__':
    main()
