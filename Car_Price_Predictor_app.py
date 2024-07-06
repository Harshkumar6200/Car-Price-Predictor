import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import altair as alt

# Load the model
rf1 = pickle.load(open("Random_Forest_Regressor.pkl", 'rb'))

# Display an image
st.image(r"Audi Car.jpg")
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

# Line Chart of km_driven and Selling Price

st.title("Line Chart of km_Driven and Selling Price")

data = pd.read_csv(r"D:\PYTHON1\Capstone Project\Car Details 2.csv")

line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='km_driven',
    y='selling_price',
    tooltip=['km_driven', 'selling_price']
).properties(
    title='Line Plot of km_driven vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(line_chart, use_container_width=True)

# Line Chart of Year and Selling Price

st.title("Line Chart of Year and Selling Price")

line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='year',
    y='selling_price',
    tooltip=['year', 'selling_price']
).properties(
    title='Line Plot of year vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(line_chart, use_container_width=True)

# Bar Chart of Year and Selling Price

st.title("Bar Chart of Fuel and Selling Price")

bar_chart = alt.Chart(data).mark_bar(point=True).encode(
    x='fuel',
    y='selling_price',
    tooltip=['fuel', 'selling_price']
).properties(
    title='Bar Plot of Fuel vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

# Bar Chart of Brand and Selling Price

st.title("Bar Chart of Brand and Selling Price")

bar_chart = alt.Chart(data).mark_bar(point=True).encode(
    x='brands',
    y='selling_price',
    tooltip=['brands', 'selling_price']
).properties(
    title='Bar Plot of Brand vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

# pie Chart of Seller Type and Selling Price

st.title("Pie Chart of Seller Type and Selling Price")

data_aggregated = data.groupby('seller_type').sum().reset_index()

pie_chart = alt.Chart(data_aggregated).mark_arc().encode(
    theta=alt.Theta(field='selling_price', type='quantitative'),
    color=alt.Color(field='seller_type', type='nominal'),
    tooltip=['seller_type', 'selling_price']
).properties(
    title='Pie Chart of Seller Type vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(pie_chart, use_container_width=True)


# Bar Chart of Transmission Type and Selling Price

st.title("Bar Chart of Transmission Type and Selling Price")

bar_chart = alt.Chart(data).mark_bar(point=True).encode(
    x='selling_price',
    y='transmission',
    tooltip=['transmission', 'selling_price']
).properties(
    title='Bar Plot of Transmission Type vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)

# Bar Chart of Owner Type and Selling Price

st.title("Bar Chart of Owner Type and Selling Price")

bar_chart = alt.Chart(data).mark_bar(point=True).encode(
    x='owner',
    y='selling_price',
    tooltip=['owner', 'selling_price']
).properties(
    title='Bar Plot of Owner Type vs Selling Price',
    width=600,
    height=400
)

st.altair_chart(bar_chart, use_container_width=True)




