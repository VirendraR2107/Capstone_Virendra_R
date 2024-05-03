import streamlit as st
import pickle
import numpy as np
import pandas as pd

RF = pickle.load(open('RF_final_03-05-2024.pkl','rb')) 
df1 = pickle.load(open('df1_03-05-2024.pkl','rb'))

st.title('Used Car Price Prediction')
st.header('Fill The Used Car Details to Predict The Price')

# User inputs
Car_Name=st.selectbox('Car_Name', df1['Car_Name'].unique())
Model=st.selectbox('Model', df1['Model'].unique())
Type=st.selectbox('Type', df1['Type'].unique())
year=st.selectbox('year', df1['year'].unique())
km_driven=st.number_input('KM(between 1.0 - 806599.0)')
fuel=st.selectbox('fuel', df1['fuel'].unique())
seller_type=st.selectbox('seller_type', df1['seller_type'].unique())
transmission=st.selectbox('transmission', df1['transmission'].unique())
owner=st.selectbox('owner', df1['owner'].unique())




if st.button('Predict'):
    if Car_Name == 'Maruti':
        Car_Name=5
    elif Car_Name == 'Hyundai':
        Car_Name=3
    elif Car_Name == 'Mahindra':
        Car_Name=4
    elif Car_Name=='Tata':
        Car_Name=10
    elif Car_Name=='Ford':
        Car_Name=1
    elif Car_Name=='Honda':
        Car_Name=2
    elif Car_Name=='Other':
        Car_Name=7
    elif Car_Name=='Toyota':
        Car_Name=11
    elif Car_Name=='Chevrolet':
        Car_Name=0
    elif Car_Name=='Renault':
        Car_Name=8
    elif Car_Name=='Volkswagen':
        Car_Name=12
    elif Car_Name=='Nissan':
        Car_Name=6
    elif Car_Name=='Skoda':
        Car_Name=9
    else:
        Car_Name ='Enter Correct Name'




if st.button('Predict'):
    # Encoding the selected values
    encoded_car_name = encode_car_name(Car_Name)
    encoded_model = encode_model(Model)
    # Encode other columns similarly

    # Construct input data array
    input_data = np.array([encoded_car_name, encoded_model, Type, year, km_driven, fuel, seller_type, transmission, owner]).reshape(1, -1)
    # Predict using the trained model
    prediction = RF.predict(input_data)
    st.write('The predicted price of the used car is:', prediction[0])




