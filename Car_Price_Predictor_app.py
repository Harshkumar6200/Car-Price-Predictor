import streamlit as st
import pickle 
import numpy as np
import pandas as pd

# Load the model
rf1 = pickle.load(open("Random_Forest_Regressor.pkl", 'rb'))

# Display an image
st.image(r"C:\Users\Lenovo\Downloads\Audi Car.jpg")
st.title('Car Price Predictor App')
st.header('Fill the Details to Predict Car Price')

# User input
fuel = st.selectbox('Fuel Type', ['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer', 'Trustmark Dealer']) 
year = st.slider('Year', 1992, 2020)
owner = st.selectbox('Owner Type', ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
km_driven = st.slider('Km Driven', 1, 223159) 
brand = st.selectbox('Brand', ['Maruti', 'Hyundai', 'Mahindra', 'Tata', 'Ford', 'Honda', 'Toyota', 'Chevrolet', 'Renault', 'Volkswagen', 'Nissan', 'Skoda', 'Others', 'Fiat', 'Audi', 'Datsun', 'BMW', 'Mercedes'])

# Define a mapping for categorical values to numerical values
fuel_map = {'Diesel': 1, 'Petrol': 4, 'CNG': 0, 'LPG': 3, 'Electric': 2}
seller_type_map = {'Individual': 1, 'Dealer': 0, 'Trustmark Dealer': 2}
transmission_map = {'Manual': 1, 'Automatic': 0}
owner_map = {'First Owner': 0, 'Second Owner': 2, 'Third Owner': 4, 'Fourth & Above Owner': 1, 'Test Drive Car': 3}
brand_map = {'Maruti': 9, 'Hyundai': 7, 'Mahindra': 8, 'Tata': 15, 'Ford': 5, 'Honda': 6, 'Toyota': 16, 'Chevrolet': 2, 'Renault': 13, 'Volkswagen': 17, 'Nissan': 11, 'Skoda': 14, 'Others': 12, 'Fiat': 4, 'Audi': 0, 'Datsun': 3, 'BMW': 1, 'Mercedes': 10}

# Convert categorical inputs to numerical values
fuel = fuel_map[fuel]
seller_type = seller_type_map[seller_type]
transmission = transmission_map[transmission]
owner = owner_map[owner]
brand = brand_map[brand]

# Create an input array for the model
test = np.array([year, km_driven, fuel, seller_type, transmission, owner, brand]).reshape(1, -1)

# Predict the price
if st.button('Predict'):
    prediction = rf1.predict(test)
    st.success(f"Predicted Car Price: {prediction[0]:.2f}")

st.image(r"C:\Users\Lenovo\Downloads\model.jpeg")

#streamlit issue reolved.
Resolved [2024-07-05 14:56:17.016450] 45 packages[2024-07-05 14:56:17.016730]  in 181ms[2024-07-05 14:56:17.016991]
Audited [2024-07-05 14:56:17.017852] 45 packages[2024-07-05 14:56:17.018110]  in 0.21ms[2024-07-05 14:56:17.018495]

Checking if Streamlit is installed
Found Streamlit version 1.36.0 in the environment


