
import streamlit as st
import pickle
import pandas as pd

# Load the Random Forest model
RF = pickle.load(open('RF_final_03-05-2024.pkl','rb')) 

# Load the DataFrame
df1 = pickle.load(open('df1_03-05-2024.pkl','rb'))

# Streamlit app title and header
st.title('Used Car Price Prediction')
st.header('Fill The Used Car Details to Predict The Price')

# Dropdown for selecting car name, model, type, year, fuel, seller type, transmission, and owner
Car_Name = st.selectbox('Car Name', df1['Car_Name'].unique())
Model = st.selectbox('Model', df1['Model'].unique())
Type = st.selectbox('Type', df1['Type'].unique())
Year = st.selectbox('Year', df1['year'].unique())
Km_Driven = st.number_input('KM Driven (between 1.0 - 806599.0)')
Fuel = st.selectbox('Fuel', df1['fuel'].unique())
Seller_Type = st.selectbox('Seller Type', df1['seller_type'].unique())
Transmission = st.selectbox('Transmission', df1['transmission'].unique())
Owner = st.selectbox('Owner', df1['owner'].unique())

# Function to preprocess user input data and make predictions
def preprocess_input_data(Car_Name, Model, Type, Year, Km_Driven, Fuel, Seller_Type, Transmission, Owner):
    input_data = pd.DataFrame({
        'Car_Name': [Car_Name],
        'Model': [Model],
        'Type': [Type],
        'year': [Year],
        'km_driven': [Km_Driven],
        'fuel': [Fuel],
        'seller_type': [Seller_Type],
        'transmission': [Transmission],
        'owner': [Owner]
    })
    return input_data

# Predict button
if st.button('Predict'):
    input_data = preprocess_input_data(Car_Name, Model, Type, Year, Km_Driven, Fuel, Seller_Type, Transmission, Owner)
    prediction = RF.predict(input_data)
    st.success('The predicted price of the used car is ₹{}'.format(prediction[0]))
