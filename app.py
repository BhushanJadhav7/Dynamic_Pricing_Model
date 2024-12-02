import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('dynamic_pricing_model.pkl')

# Title of the app
st.title("Dynamic Pricing Model Prediction")

# Input fields for features
feature_1 = st.number_input("Enter value for Feature 1 (e.g., competitor price or demand)", min_value=0.0)
feature_2 = st.number_input("Enter value for Feature 2 (e.g., stock level or historical price)", min_value=0.0)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'feature_1': [feature_1],
    'feature_2': [feature_2]
})

# Make prediction when the button is pressed
if st.button("Predict"):
    # Use the loaded model to predict
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f"The predicted dynamic price is: {prediction[0]}")




