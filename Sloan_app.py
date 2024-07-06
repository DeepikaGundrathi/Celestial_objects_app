import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Input features
st.title('SDSS Object Classification')
st.write('Enter values for the following features:')
ra = st.number_input('Right Ascension (ra)')
dec = st.number_input('Declination (dec)')
u = st.number_input('u')
g = st.number_input('g')
r = st.number_input('r')
i = st.number_input('i')
z = st.number_input('z')

# Make prediction
if st.button('Predict'):
    input_features = [[ra, dec, u, g, r, i, z]]
    prediction = model.predict(input_features)
    prediction_proba = model.predict_proba(input_features)

    # Visualize prediction results
    st.subheader('Prediction')
    object_type = ['Galaxy', 'QSO', 'Star']
    try:
        st.write(f"The object is classified as: **{object_type[int(prediction[0])]}**")
    except IndexError:
        st.write("Prediction result is out of the expected range. Check the input features or model.")

    st.subheader('Prediction Probability')
    st.write(pd.DataFrame(prediction_proba, columns=object_type))
