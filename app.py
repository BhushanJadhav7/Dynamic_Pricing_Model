import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('dynamic_pricing_model.pkl')

# Streamlit UI for user inputs
st.title("Dynamic Pricing Predictor")
st.write("Enter features to predict the price")

# Example input fields for features
input1 = st.number_input('Feature 1', min_value=0.0, max_value=100.0, value=50.0)
input2 = st.number_input('Feature 2', min_value=0.0, max_value=100.0, value=25.0)

# Create a DataFrame from the inputs
new_data = pd.DataFrame({
    'feature_1': [input1],
    'feature_2': [input2],
    # Add more features if needed
})

# Predict when button is pressed
if st.button('Predict'):
    prediction = model.predict(new_data)
    st.write(f"Predicted Price: {prediction[0]}")

