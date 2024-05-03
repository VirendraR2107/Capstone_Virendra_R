import streamlit as st
import pickle
import numpy as np

# Load the trained model and dataframe
RF = pickle.load(open('RF_final_03-05-2024.pkl','rb'))
df1 = pickle.load(open('df1_03-05-2024.pkl','rb'))

# Title and header
st.title('Used Car Price Prediction')
st.header('Fill The Used Car Details to Predict The Price')

# User inputs
car_name_map = {'Maruti': 5, 'Hyundai': 3, 'Mahindra': 4, 'Tata': 10, 'Ford': 1, 'Honda': 2, 'Other': 7, 'Toyota': 11, 'Chevrolet': 0, 'Renault': 8, 'Volkswagen': 12, 'Nissan': 6, 'Skoda': 9}
model_map = {'Other': 13, 'Swift': 16, 'Alto': 1, 'Wagon': 18, 'i20': 22, 'Verna': 17, 'Innova': 11, 'Indica': 9, 'Scorpio': 15, 'Santro': 14, 'Figo': 7, 'City': 4, 'EON': 5, 'Grand': 8, 'XUV500': 19, 'i10': 21, 'Bolero': 3, 'Beat': 2, 'KWID': 12, 'Ertiga': 6, 'Zen': 20, '800': 0, 'Indigo': 10}
type_map = {'Other': 7, 'Dzire VDI': 2, 'LX': 5, '800 LXI': 0, 'LXi': 6, 'VDI': 37, 'Era Plus': 3, 'VDI BSIV': 11, 'R VXI BS IV': 9, 'VXI': 13, 'VDi': 12, 'R LXI Minor': 8, 'AC': 1, 'Xing GLS': 14, 'K10 VXI': 4}
fuel_map = {'Diesel': 1, 'Petrol': 4, 'CNG': 0, 'LPG': 3, 'Electric': 2}
seller_type_map = {'Individual': 1, 'Dealer': 0, 'Trustmark Dealer': 2}
transmission_map = {'Manual': 1, 'Automatic': 0}
owner_map = {'First Owner': 0, 'Second Owner': 2, 'Third Owner': 4, 'Fourth & Above Owner': 1, 'Test Drive Car': 3}

Car_Name = st.selectbox('Car_Name', df1['Car_Name'].unique(), format_func=lambda x: car_name_map.get(x, 'Enter Correct Car_Name'))
Model = st.selectbox('Model', df1['Model'].unique(), format_func=lambda x: model_map.get(x, 'Enter Correct Model'))
Type = st.selectbox('Type', df1['Type'].unique(), format_func=lambda x: type_map.get(x, 'Enter Correct Type'))
year = st.selectbox('Year', df1['year'].unique())
km_driven = st.number_input('KM(between 1.0 - 806599.0)')
fuel = st.selectbox('Fuel', df1['fuel'].unique(), format_func=lambda x: fuel_map.get(x, 'Select Valid Fuel Type'))
seller_type = st.selectbox('Seller Type', df1['seller_type'].unique(), format_func=lambda x: seller_type_map.get(x, 'Select Valid Category'))
transmission = st.selectbox('Transmission', df1['transmission'].unique(), format_func=lambda x: transmission_map.get(x, 'Select Valid Type'))
owner = st.selectbox('Owner', df1['owner'].unique(), format_func=lambda x: owner_map.get(x, 'Select Valid Category'))

# Predict button
if st.button('Predict'):
    try:
        year = int(year)
        if year not in df1['year'].unique():
            st.write("Select Valid Year")
        else:
            # Make prediction
            input_data = np.array([[Car_Name, Model, Type, year, km_driven, fuel, seller_type, transmission, owner]])
            prediction = RF.predict(input_data)
            
            # Display prediction
            prediction_text = f"Predicted Price: {prediction[0]}"
            st.write(prediction_text)
    except ValueError:
        st.write("Select Valid Year")
    except Exception as e:
        st.write("An error occurred:", e)
