import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('decision_tree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Input features
st.title('Celestial Object Classification')
st.write('Enter values for the following features:')

ra = st.number_input('ra', min_value=0.0, max_value=360.0)
dec = st.number_input('dec', min_value=-90.0, max_value=90.0)
u = st.number_input('u', min_value=0.0)
g = st.number_input('g', min_value=0.0)
r = st.number_input('r', min_value=0.0)
i = st.number_input('i', min_value=0.0)
z = st.number_input('z', min_value=0.0)

if st.button('Classify'):
    # Create a DataFrame for prediction
    input_data = pd.DataFrame([[ra, dec, u, g, r, i, z]], columns=['ra', 'dec', 'u', 'g', 'r', 'i', 'z'])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Visualize prediction results
    st.subheader('Prediction')
    object_type = ['Galaxy', 'QSO', 'Star']
    st.write(f"The object is classified as: **{object_type[int(prediction[0])]}**")

    st.subheader('Prediction Probability')
    st.write(pd.DataFrame(prediction_proba, columns=object_type))
