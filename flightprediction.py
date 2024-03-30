import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

# Loading the dataset
data_flight = pd.read_csv('data_flight.csv')

# Data Preprocessing - Dropping unnecessary columns
data_flight.drop(columns=['Unnamed: 0', 'flight', 'departure_time', 'arrival_time'], inplace=True)

data_flight = pd.get_dummies(data_flight, columns=['airline', 'source_city', 'destination_city', 'class', 'stops'])
X = data_flight.drop(columns=['price'])
y = data_flight['price']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

# Train the model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate R-squared score
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

with open('Flight_Prediction_Model.sav', 'wb') as file:
    pickle.dump(model, file)

# Prediction code
input_data = {
    'airline': ['AirAsia'],
    'source_city': ['Delhi'],
    'destination_city': ['Mumbai'],
    'class': ['Economy'],
    'stops': ['zero']
}

# Convert input data to DataFrame
input_df = pd.DataFrame(input_data)

# Convert categorical variables to dummy variables
input_df = pd.get_dummies(input_df)

input_df = input_df.reindex(columns=X.columns, fill_value=0)

# Make prediction
prediction = model.predict(input_df)
prediction = np.round(prediction, 2)
print(prediction)
