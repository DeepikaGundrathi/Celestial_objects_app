import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the model from the pickle file
model_filename = 'decision_tree_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Function to preprocess input data
def preprocess_input(input_data):
    # Your preprocessing steps here
    # Example: Scaling, handling missing values, feature engineering
    return input_data

# Function to predict the object type
def predict_object_type(input_features):
    # Preprocess input features
    input_features = preprocess_input(input_features)
    
    # Predict using the loaded model
    prediction = model.predict(input_features)
    prediction_proba = model.predict_proba(input_features)
    
    return prediction, prediction_proba

# Main Streamlit app
def main():
    st.title('Celestial Object Classifier')
    st.sidebar.header('Input Features')
    
    # Example input features
    input_features = {
        'u': st.sidebar.slider('u', 10.0, 30.0, 18.0),
        'g': st.sidebar.slider('g', 10.0, 30.0, 18.0),
        'r': st.sidebar.slider('r', 10.0, 30.0, 18.0),
        'i': st.sidebar.slider('i', 10.0, 30.0, 18.0),
        'z': st.sidebar.slider('z', 10.0, 30.0, 18.0),
        'redshift': st.sidebar.slider('redshift', 0.0, 2.0, 0.5)
    }
    
    st.sidebar.markdown('---')
    
    if st.sidebar.button('Classify'):
        # Predict object type
        prediction, prediction_proba = predict_object_type(pd.DataFrame([input_features]))
        
        # Visualize prediction results
        st.subheader('Prediction')
        object_type = ['Galaxy', 'QSO', 'Star']
        st.write(f"The object is classified as: **{object_type[int(prediction[0])]}**")
        
        st.subheader('Prediction Probability')
        st.write(pd.DataFrame(prediction_proba, columns=object_type))

if __name__ == '__main__':
    main()
