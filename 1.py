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
Car_Name=st.selectbox('Car_Name', df1['Car_Name'].unique())
Model=st.selectbox('Model', df1['Model'].unique())
Type=st.selectbox('Type', df1['Type'].unique())
year=st.selectbox('year', df1['year'].unique())
km_driven=st.number_input('KM(between 1.0 - 806599.0)')
fuel=st.selectbox('fuel', df1['fuel'].unique())
seller_type=st.selectbox('seller_type', df1['seller_type'].unique())
transmission=st.selectbox('transmission', df1['transmission'].unique())
owner=st.selectbox('owner', df1['owner'].unique())



# Predict button
if st.button('Predict'):
    try:
        # Convert categorical variables to numerical
        car_name_map = {'Maruti': 5, 'Hyundai': 3, 'Mahindra': 4, 'Tata': 10, 'Ford': 1, 'Honda': 2, 'Other': 7, 'Toyota': 11, 'Chevrolet': 0, 'Renault': 8, 'Volkswagen': 12, 'Nissan': 6, 'Skoda': 9}
        model_map = {'Other': 13, 'Swift': 16, 'Alto': 1, 'Wagon': 18, 'i20': 22, 'Verna': 17, 'Innova': 11, 'Indica': 9, 'Scorpio': 15, 'Santro': 14, 'Figo': 7, 'City': 4, 'EON': 5, 'Grand': 8, 'XUV500': 19, 'i10': 21, 'Bolero': 3, 'Beat': 2, 'KWID': 12, 'Ertiga': 6, 'Zen': 20, '800': 0, 'Indigo': 10}
        type_map = {'Other': 7, 'Dzire VDI': 2, 'LX': 5, '800 LXI': 0, 'LXi': 6, 'VDI': 37, 'Era Plus': 3, 'VDI BSIV': 11, 'R VXI BS IV': 9, 'VXI': 13, 'VDi': 12, 'R LXI Minor': 8, 'AC': 1, 'Xing GLS': 14, 'K10 VXI': 4}
        
        Car_Name = car_name_map.get(Car_Name, 'Enter Correct Car_Name')
        Model = model_map.get(Model, 'Enter Correct Model')
        Type = type_map.get(Type, 'Enter Correct Type')
        
        try:
            year = int(year) if year.isdigit() and int(year) in df1['year'].unique() else 'Select Valid Year'
        except ValueError:
            year = 'Select Valid Year'
        
        fuel_map = {'Diesel': 1, 'Petrol': 4, 'CNG': 0, 'LPG': 3, 'Electric': 2}
        seller_type_map = {'Individual': 1, 'Dealer': 0, 'Trustmark Dealer': 2}
        transmission_map = {'Manual': 1, 'Automatic': 0}
        owner_map = {'First Owner': 0, 'Second Owner': 2, 'Third Owner': 4, 'Fourth & Above Owner': 1, 'Test Drive Car': 3}
        
        fuel = fuel_map.get(fuel, 'Select Valid Fuel Type')
        seller_type = seller_type_map.get(seller_type, 'Select Valid Category')
        transmission = transmission_map.get(transmission, 'Select Valid Type')
        owner = owner_map.get(owner, 'Select Valid Category')
        
        # Check if all inputs are valid
        if all(isinstance(val, int) for val in [Car_Name, Model, Type, year, fuel, seller_type, transmission, owner]):
            # Make prediction
            input_data = np.array([[Car_Name, Model, Type, year, km_driven, fuel, seller_type, transmission, owner]])
            prediction = RF.predict(input_data)
            
            # Display prediction
            prediction_text = f"Predicted Price: {prediction[0]}"
            st.write(prediction_text)
        else:
            st.write("Please enter valid values for all input fields.")
    except Exception as e:
        st.write("An error occurred:", e)
