import streamlit as st
import pickle

# Load the machine learning model and dataframe
RF = pickle.load(open('RF_final_03-05-2024.pkl','rb')) 
df1 = pickle.load(open('df1_03-05-2024.pkl','rb'))

# Define the app title and header
st.title('Used Car Price Prediction')
st.header('Fill The Used Car Details to Predict The Price')

# User inputs
Car_Name = st.selectbox('Car_Name', df1['Car_Name'].unique())
Model = st.selectbox('Model', df1['Model'].unique())
Type = st.selectbox('Type', df1['Type'].unique())

# Mapping function for encoding categorical variables
def encode_input(input_value, mapping_dict):
    if input_value in mapping_dict:
        return mapping_dict[input_value]
    else:
        return 'Enter Correct Value'

# Button for prediction
if st.button('Predict'):
    # Encoding categorical inputs
    Car_Name = encode_input(Car_Name, {'Maruti': 5, 'Hyundai': 3, 'Mahindra': 4, 'Tata': 10, 'Ford': 1,
                                       'Honda': 2, 'Other': 7, 'Toyota': 11, 'Chevrolet': 0, 'Renault': 8,
                                       'Volkswagen': 12, 'Nissan': 6, 'Skoda': 9})
    Model = encode_input(Model, {'Other': 13, 'Swift': 16, 'Alto': 1, 'Wagon': 18, 'i20': 22,
                                 'Verna': 17, 'Innova': 11, 'Indica': 9, 'Scorpio': 15, 'Santro': 14,
                                 'Figo': 7, 'City': 4, 'EON': 5, 'Grand': 8, 'XUV500': 19, 'i10': 21,
                                 'Bolero': 3, 'Beat': 2, 'KWID': 12, 'Ertiga': 6, 'Zen': 20, '800': 0,
                                 'Indigo': 10})
    Type = encode_input(Type, {'Other': 7, 'Dzire VDI': 2, 'LX': 5, '800 LXI': 0, 'LXi': 6,
                               'VDI': 37, 'Era Plus': 3, 'VDI BSIV': 11, 'R VXI BS IV': 9, 'VXI': 13,
                               'VDi': 12, 'R LXI Minor': 8, 'AC': 1, 'Xing GLS': 14, 'K10 VXI': 4})

    # Perform prediction with encoded inputs using the RF model
    # ...

