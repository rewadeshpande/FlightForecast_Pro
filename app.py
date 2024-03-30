import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('Flight_Prediction_Model.sav', 'rb') as file:
    model = pickle.load(file)

# Load the dataset to fetch options for categorical variables
data_flight = pd.read_csv('data_flight.csv')

# Extract options for categorical variables from the dataset
airlines = sorted(data_flight['airline'].unique().tolist())
source_cities = sorted(data_flight['source_city'].unique().tolist())
destination_cities = sorted(data_flight['destination_city'].unique().tolist())
classes = sorted(data_flight['class'].unique().tolist())
stops = sorted(data_flight['stops'].unique().tolist())

# Define the input form
st.title('Flight Price Prediction')

airline = st.selectbox('Select Airline', airlines)
source_city = st.selectbox('Select Source City', source_cities)
destination_city = st.selectbox('Select Destination City', destination_cities)
class_type = st.selectbox('Select Class', classes)
stop_count = st.selectbox('Select Number of Stops', stops)

# Create button to trigger prediction
if st.button('Predict Price', key='predict_button'):
    # Create input data dictionary
    input_data = {
        'airline': [airline],
        'source_city': [source_city],
        'destination_city': [destination_city],
        'class': [class_type],
        'stops': [stop_count]
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame(input_data)

    # Convert categorical variables to dummy variables
    input_df = pd.get_dummies(input_df)

    # Load original column names used during training
    data_flight = pd.get_dummies(data_flight, columns=['airline', 'source_city', 'destination_city', 'class', 'stops'])
    X = data_flight.drop(columns=['Unnamed: 0', 'arrival_time', 'departure_time', 'flight','price'])
    # Ensure consistency in columns by aligning with training data columns
    input_df = input_df.reindex(columns=X.columns, fill_value=0)

    # Make prediction
    prediction = model.predict(input_df)
    rounded_prediction = np.round(prediction[0], 2)

    # Display prediction
    st.success(f'Predicted Price: {rounded_prediction} INR')
