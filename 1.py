import streamlit as st
import pickle
import numpy as np
import pandas as pd

RF = pickle.load(open('RF_final_03-05-2024.pkl','rb')) 
df1 = pickle.load(open('df1_03-05-2024.pkl','rb'))

# Function to decode encoded values
def decode_value(column_name, encoded_value):
    if column_name == 'Car_Name':
        return df1['Car_Name'].unique()[encoded_value]
    elif column_name == 'Model':
        return df1['Model'].unique()[encoded_value]
    elif column_name == 'Type':
        return df1['Type'].unique()[encoded_value]
    elif column_name == 'year':
        return df1['year'].unique()[encoded_value]
    elif column_name == 'fuel':
        return df1['fuel'].unique()[encoded_value]
    elif column_name == 'seller_type':
        return df1['seller_type'].unique()[encoded_value]
    elif column_name == 'transmission':
        return df1['transmission'].unique()[encoded_value]
    elif column_name == 'owner':
        return df1['owner'].unique()[encoded_value]
    else:
        return None

st.title('Used Car Price Prediction')
st.header('Fill The Used Car Details to Predict The Price')

Car_Name=st.selectbox('Car_Name', [decode_value('Car_Name', i) for i in range(len(df1['Car_Name'].unique()))])
Model=st.selectbox('Model', [decode_value('Model', i) for i in range(len(df1['Model'].unique()))])
Type=st.selectbox('Type', [decode_value('Type', i) for i in range(len(df1['Type'].unique()))])
year=st.selectbox('year', [decode_value('year', i) for i in range(len(df1['year'].unique()))])
km_driven=st.number_input('KM(between 1.0 - 806599.0)')
fuel=st.selectbox('fuel', [decode_value('fuel', i) for i in range(len(df1['fuel'].unique()))])
seller_type=st.selectbox('seller_type', [decode_value('seller_type', i) for i in range(len(df1['seller_type'].unique()))])
transmission=st.selectbox('transmission', [decode_value('transmission', i) for i in range(len(df1['transmission'].unique()))])
owner=st.selectbox('owner', [decode_value('owner', i) for i in range(len(df1['owner'].unique()))])

if st.button('Predict'):
    input_data = np.array([Car_Name, Model, Type, year, km_driven, fuel, seller_type, transmission, owner]).reshape(1, -1)
    prediction = RF.predict(input_data)
    st.write('The predicted price of the used car is:', prediction[0])
