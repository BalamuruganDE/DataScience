# %%writefile model_app.py 
#When using colab this magic command %%writefile will create a realtime-copy of the file in colab content folder 
#for the file we work-on here in our case model_app.py 
    
import streamlit as st
import numpy as np
import pandas as pd

import joblib

import warnings
warnings.filterwarnings('ignore')

file_path = '/Users/bkannadasan/Documents/GitHub/DS_New_30_Nov_2024/MachineLearning/Unsupervised_Learning/Customer_Data.csv'

df = pd.read_csv(file_path)

selected_values = {}
for col in df.drop(columns=['CUST_ID']).columns:
    selected_values[col] = st.number_input(
        f'select a value for {col}'
    )

picklefile = 'model_kmeans_k4.pkl'

if st.button('submit'):
    #load model
    model = joblib.load (picklefile)

    input_data = list(selected_values.values())

    print('input1:\n',input_data)
    
    input_data = [list(selected_values.values())]

    print('input2:\n',input_data)
    
    #prediction
    prediction = model.predict(input_data)

    #write the ouput
    st.write(f'Predicted input belongs to cluster:{prediction[0]}')


### !streamlit run model_app.py --> For running streamlit application
### !pip install streamlit -q --> For installing streamlit in quite mode
