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
        Car_Name ='Enter Correct Car_Name'


if st.button('Predict'):
    if Model == 'Other':
        Model=13
    elif Model=='Swift':
        Model=16
    elif Model=='Alto':
        Model=1
    elif Model=='Wagon':
        Model=18
    elif Model=='i20':
        Model=22
    elif Model=='Verna':
        Model=17
    elif Model=='Innova':
        Model=11
    elif Model=='Indica':
        Model=9
    elif Model=='Scorpio':
        Model=15
    elif Model=='Santro':
        Model=14
    elif Model=='Figo':
        Model=7
    elif Model=='City':
        Model=4
    elif Model=='EON':
        Model=5
    elif Model=='Grand':
        Model=8
    elif Model=='XUV500':
        Model=19
    elif Model=='i10':
        Model=21
    elif Model=='Bolero':
        Model=3
    elif Model=='Beat':
        Model=2
    elif Model=='KWID':
        Model=12
    elif Model=='Ertiga':
        Model=6
    elif Model=='Zen':
        Model=20
    elif Model=='800':
        Model=0
    elif Model=='Indigo':
        Model=10
    else:
        Model='Enter Correct Model'

if st.button('Predict'):
    if Type == 'Other':
        Type=7
    elif Type=='Dzire VDI':
        Type=2
    elif Type=='LX':
        Type=5
    elif Type=='800 LXI':
        Type=0
    elif Type=='LXi':
        Type=6
    elif Type=='VDI':
        Type=37
    elif Type=='Era Plus':
        Type=3
    elif Type=='VDI BSIV':
        Type=11
    elif Type=='R VXI BS IV':
        Type=9
    elif Type=='VXI':
        Type=13
    elif Type=='VDi':
        Type=12
    elif Type=='R LXI Minor':
        Type=8
    elif Type=='AC':
        Type=1
    elif Type=='Xing GLS':
        Type=14
    elif Type=='K10 VXI':
        Type=4
    else:
        Type='Enter Correct Type'


if st.button('Predict'):
    if year == 'Other':
        year=11
    elif year=='2017':
        year=8
    elif year=='2012':
        year=3
    elif year=='2015':
        year=6
    elif year=='2014':
        year=5
    elif year=='2013':
        year=4
    elif year=='2018':
        year=9
    elif year=='2016':
        year=7
    elif year=='2011':
        year=2
    elif year=='2010':
        year=1
    elif year=='2009':
        year=0
    elif year=='2019':
        year=10
    else:
        year='Select Valid Year'

if st.button('Predict'):
    if fuel == 'Diesel':
        fuel=1
    elif fuel=='Petrol':
        fuel=4
    elif fuel=='CNG':
        fuel=0
    elif fuel=='LPG':
        fuel=3
    elif fuel=='Electric':
        fuel=2
    else:
        fuel='Select Valid Fuel Type'


if st.button('Predict'):
    if seller_type == 'Individual':
        seller_type=1
    elif seller_type=='Dealer':
        seller_type=0
    elif seller_type=='Trustmark Dealer':
        seller_type=2
    else:
        seller_type='Select Valid Category'



if st.button('Predict'):
    if transmission == 'Manual':
        transmission=1
    elif transmission=='Automatic':
        transmission=0
    else:
        transmission='Select Valid Type'


if st.button('Predict'):
    if owner == 'First Owner':
        owner=0
    elif owner=='Second Owner':
        owner=2
    elif owner=='Third Owner':
        owner=4
    elif owner=='Fourth & Above Owner':
        owner=1
    elif owner=='Test Drive Car':
        owner=3
    else:
        owner='Select Valid Category'



prediction_text = ''

if st.button('Predict'):
    # Preprocess inputs
    Car_Name = int(Car_Name) if isinstance(Car_Name, str) else Car_Name
    Model = int(Model) if isinstance(Model, str) else Model
    Type = int(Type) if isinstance(Type, str) else Type
    year = int(year) if isinstance(year, str) else year
    fuel = int(fuel) if isinstance(fuel, str) else fuel
    seller_type = int(seller_type) if isinstance(seller_type, str) else seller_type
    transmission = int(transmission) if isinstance(transmission, str) else transmission
    owner = int(owner) if isinstance(owner, str) else owner
    
    # Make prediction
    input_data = np.array([[Car_Name, Model, Type, year, km_driven, fuel, seller_type, transmission, owner]])
    prediction = RF.predict(input_data)
    
    # Display prediction
    prediction_text = f"Predicted Price: {prediction[0]}"
    
# Display prediction result
st.write(prediction_text)








