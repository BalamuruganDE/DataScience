from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

class Input(BaseModel):
    input:float

class Output(BaseModel):
    output:float
    slope:float
    intercept:float

model = joblib.load('pipline_lr_deploy.pkl')

@app.post("/predict")
def predict(data:Input)->Output:
    X_input=np.array([[data.input]])
    prediction = model.predict(X_input)
    intercept = model.named_steps['model'].intercept_
    slope = model.named_steps['model'].coef_
    return Output(output=prediction,slope=slope,intercept=intercept)
