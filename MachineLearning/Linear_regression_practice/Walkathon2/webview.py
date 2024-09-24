import streamlit as st
import requests
import pandas as pd
import json
import joblib

st.title("Prediction App")
st.write("This is a test")


df = pd.read_csv('data.csv')

# CONSOLE = st.text_input('CONSOLE')
CONSOLE = st.selectbox("CONSOLE",pd.unique(df['CONSOLE']))
YEAR = st.number_input("YEAR",step=1,value=df['YEAR'].min())
CATEGORY = st.selectbox("CATEGORY",pd.unique(df['CATEGORY']))
PUBLISHER = st.selectbox("PUBLISHER",pd.unique(df['PUBLISHER']))
RATING = st.selectbox("RATING",pd.unique(df['RATING']))
CRITICS_POINTS = st.number_input("CRITICS_POINTS",step=0.1)
USER_POINTS = st.number_input("USER_POINTS",step=0.1)

inputs={
    "CONSOLE":CONSOLE,
    "YEAR":YEAR,
    "CATEGORY":CATEGORY,
    "PUBLISHER":PUBLISHER,
    "RATING": RATING,
    "CRITICS_POINTS":CRITICS_POINTS,
    "USER_POINTS":USER_POINTS
}


if st.button('Predict'):
    model = joblib.load('vgsales_pipeline_model.pkl')
    X_input = pd.DataFrame(inputs,index=[0])
    
    str.text(X_input)



    #  working code
    # res = requests.post(url = "http://127.0.0.1:8000/predict", data = json.dumps(inputs))
    # st.json(res.text)
    # st.text(res.text)





# '''
#     CONSOLE:object
#     YEAR:int
#     CATEGORY:object
#     PUBLISHER:object
#     RATING:object
#     CRITICS_POINTS:float
#     USER_POINTS:float



#     % streamlit run webview.py 
#     '''