from fastapi import FastAPI
import pandas as pd
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()


class Input(BaseModel):
    Item_Identifier:object
    Item_Weight:float
    Item_Fat_Content:object
    Item_Visibility:float
    Item_Type:object
    Item_MRP:float
    Outlet_Identifier:object
    Outlet_Establishment_Year:int
    Outlet_Size:object
    Outlet_Location_Type:object
    Outlet_Type:object

class Output(BaseModel):
    predicted_output:float

@app.post("/predict-model",response_model=Output)
def predict(data:Input)->Output:
    X_input=pd.DataFrame([data.model_dump()])
    # model = joblib.load('../Linear_regression_practice/bm_pipeline.pkl')
    model = joblib.load('bm_pipeline.pkl')
    test_pred = model.predict(X_input)
    return Output(predicted_output=round(float(test_pred),2))

# @app.post("/predict")
# def predict(data:input):
#     # X_input=np.array([[data.Item_Identifier,	data.Item_Weight,	data.Item_Fat_Content,	data.Item_Visibility,	data.Item_Type,	data.Item_MRP,	data.Outlet_Identifier,	data.Outlet_Establishment_Year,	data.Outlet_Size,	data.Outlet_Location_Type,	data.Outlet_Type]])
#     X_input = pd.DataFrame([{'Item_Identifier':  data.Item_Identifier,
# 'Item_Weight':  data.Item_Weight,
# 'Item_Fat_Content':  data.Item_Fat_Content,
# 'Item_Visibility':  data.Item_Visibility,
# 'Item_Type':  data.Item_Type,
# 'Item_MRP':  data.Item_MRP,
# 'Outlet_Identifier':  data.Outlet_Identifier,
# 'Outlet_Establishment_Year':  data.Outlet_Establishment_Year,
# 'Outlet_Size':  data.Outlet_Size,
# 'Outlet_Location_Type':  data.Outlet_Location_Type,
# 'Outlet_Type':  data.Outlet_Type}])
#     model = joblib.load('/Users/bkannadasan/Documents/GitHub/DataScience/MachineLearning/Linear_regression_practice/bm_pipeline.pkl')
#     pred=model.predict(X_input)
#     # print(type(pred))
#     # print(list(pred))
#     # print(pred.tolist())
#     return {'prediction':pred.tolist()[0]} # output2
#     # return {'prediction':pred.tolist()} # output1
#     # prediction = pred.tolist()  # Convert numpy array to list
#     # response_obj = {'prediction': prediction[0]}  # Using index [0] to unwrap single value predictions
#     # return response_obj

# output1

# {
#   "prediction": [
#     [
#       3876.0016126337196
#     ]
#   ]
# }

# # output2
# {
#   "prediction": [
#     3876.0016126337196
#   ]
# }

