import pandas as pd
import pickle

# Function to load the saved model and make predictions
def load_model_and_predict(input_data):
    # Load the saved model
    filename = 'decision_tree_model.pkl'
    loaded_model = pickle.load(open(filename, 'rb'))

    # Predict with input_data
    predictions = loaded_model.predict(input_data)

    return predictions

# Example usage for manual input
def predict_from_input():
    print("Enter values for the following features:")
    ra = float(input("ra: "))
    dec = float(input("dec: "))
    u = float(input("u: "))
    g = float(input("g: "))
    r = float(input("r: "))
    i = float(input("i: "))
    z = float(input("z: "))
    redshift = float(input("redshift: "))

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'ra': [ra],
        'dec': [dec],
        'u': [u],
        'g': [g],
        'r': [r],
        'i': [i],
        'z': [z],
        'redshift': [redshift]
    })

    # Make predictions using the loaded model
    predictions = load_model_and_predict(input_data)

    # Print the predictions
    print("\nPrediction:")
    for prediction in predictions:
        print(f"It's classified as: {prediction}")

# Run the prediction function
predict_from_input()
