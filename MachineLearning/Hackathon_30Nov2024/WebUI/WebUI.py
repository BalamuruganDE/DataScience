
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title('Response Prediction')


df = pd.read_csv('train.csv')

#categorical inputs
Gender = st.selectbox("Gender",pd.unique(df['Gender']))
Vehicle_Age = st.selectbox("Vehicle_Age",pd.unique(df['Vehicle_Age']))
Vehicle_Damage = st.selectbox("Vehicle_Damage",pd.unique(df['Vehicle_Damage']))

#Numerical inputs
Age = st.number_input("Age",min_value=20,max_value=90,step=1)
Driving_License = st.selectbox("Driving_License",pd.unique(df['Driving_License']))
Region_Code  = st.selectbox("Region_Code",pd.unique(df['Region_Code']))
Previously_Insured = st.selectbox("Previously_Insured",pd.unique(df['Previously_Insured']))
Annual_Premium = st.number_input("Annual_Premium")
Policy_Sales_Channel = st.selectbox("Policy_Sales_Channel",pd.unique(df['Policy_Sales_Channel']))
Vintage = st.selectbox("Vintage",pd.unique(df['Vintage']))

inputs = {
'Gender'                  :   Gender,
'Age'                     :   Age,
'Driving_License'         :   Driving_License,
'Region_Code'             :   Region_Code,
'Previously_Insured'      :   Previously_Insured,
'Vehicle_Age'             :   Vehicle_Age,
'Vehicle_Damage'          :   Vehicle_Damage,
'Annual_Premium'          :   Annual_Premium,
'Policy_Sales_Channel'    :   Policy_Sales_Channel,
'Vintage'                 :   Vintage
}



# loading ML-Model from the pickel-file
model = joblib.load('cross-sell-pred-pkl.gz')


if st.button('predict'):
    X_input = pd.DataFrame(inputs,index=[0])
    prediction = model.predict(X_input)
    st.write(prediction)


