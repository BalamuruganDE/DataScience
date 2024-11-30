# creating api endpoints using fastapi
# pip install uvicorn
# pip install fastapi

#load libraires

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

import warnings
warnings.filterwarnings('ignore')

#create object for FastAPI
app=FastAPI()

# Class for input features/columns
class Input(BaseModel):
    # pass # pass --> A lawful way to say that there will be new components that will added to this class and make the class valid for now
    department             : object
    region                 : object
    education              : object
    gender                 : object
    recruitment_channel    : object
    no_of_trainings        : int
    age                    : int
    previous_year_rating   : float
    length_of_service      : int
    KPIs_met_80            : int
    awards_won             : int
    avg_training_score     : int
    
# Class for output features/columns
class Output(BaseModel):
    is_promoted : int


@app.post("/predict")
def predict(data:Input)->Output:

    # Creating Dataframe from the inpout data recieved and mapping it with data
    X_input = pd.DataFrame([[data.department,
    data.region,
    data.education,
    data.gender,
    data.recruitment_channel,
    data.no_of_trainings,
    data.age,
    data.previous_year_rating,
    data.length_of_service,
    data.KPIs_met_80,
    data.awards_won,
    data.avg_training_score]])

    #Defining columns for X_input
    X_input.columns=['department', 'region', 'education', 'gender', 'recruitment_channel',
       'no_of_trainings', 'age', 'previous_year_rating', 'length_of_service',
       'KPIs_met >80%', 'awards_won?', 'avg_training_score']

    #loading the model
    model = joblib.load('promote_pipeline_model.pkl')
    prediction = model.predict(X_input)

    # result/output
    return Output(is_promoted = prediction)
    
    
'''
# Stub creation
class Input():
    pass 


employee_id               int64
department               object
region                   object
education                object
gender                   object
recruitment_channel      object
no_of_trainings           int64
age                       int64
previous_year_rating    float64
length_of_service         int64
KPIs_met >80%             int64
awards_won?               int64
avg_training_score        int64
is_promoted               int64

# Uvicron execution 
uvicron model_app:app --reload

{
  "department": "HR",
  "region": "region_22",
  "education": "Bachelor's",
  "gender": "m",
  "recruitment_channel": "other",
  "no_of_trainings": 1,
  "age": 27,
  "previous_year_rating": 1,
  "length_of_service": 5,
  "KPIs_met_80": 0,
  "awards_won": 0,
  "avg_training_score": 49
}
    '''