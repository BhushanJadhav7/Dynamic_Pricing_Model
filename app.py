import streamlit as st
import pandas as pd
import joblib

# Load the trained model
def load_model():
    model = joblib.load('dynamic_pricing_model.pkl')
    return model

# Function to predict based on user inputs
def predict(model, feature_1, feature_2):
    # Create a DataFrame with the user's input
    input_data = pd.DataFrame({
        'feature_1': [feature_1],
        'feature_2': [feature_2],
        # Add other features if needed
    })
    
    # Use the model to make predictions
    prediction = model.predict(input_data)
    return prediction

# Streamlit user interface
st.title('Dynamic Pricing Model for E-commerce')

# Load the model when the app runs
model = load_model()

# Create input fields for users
feature_1 = st.number_input('Enter Feature 1', min_value=0.0, step=0.1)
feature_2 = st.number_input('Enter Feature 2', min_value=0.0, step=0.1)

# When the user presses the 'Predict' button
if st.button('Predict'):
    # Get the prediction
    prediction = predict(model, feature_1, feature_2)
    st.write(f'Predicted Price: {prediction[0]}')



