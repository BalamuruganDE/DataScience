{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6103047f-ff52-4f8b-a346-12c8220afe30",
   "metadata": {},
   "outputs": [],
   "source": [
    "# %%writefile model_app.py \n",
    "'''When using colab this magic command %%writefile will create a realtime-copy of the file in colab content folder \n",
    "    for the file we work-on here in our case model_app.py '''\n",
    "\n",
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "import joblib\n",
    "\n",
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "file_path = '/Users/bkannadasan/Documents/GitHub/DS_New_30_Nov_2024/MachineLearning/Unsupervised_Learning/Customer_Data.csv'\n",
    "\n",
    "df = pd.read_csv(file_path)\n",
    "\n",
    "selected_values = {}\n",
    "for col in df.columns.drop(columns=['CUST_ID'].columns):\n",
    "    selected_values[col] = st.number_imput(\n",
    "        f'select a value for {col}'\n",
    "    )\n",
    "\n",
    "picklefile = ''\n",
    "\n",
    "if st.button():\n",
    "    #load model\n",
    "    model = joblib.load (picklefile)\n",
    "\n",
    "    input_data = list(selected_values.values())\n",
    "    #prediction\n",
    "    prediction = model.predict(input_data)\n",
    "\n",
    "    #write the ouput\n",
    "    st.write(f'Predicted input belongs to cluster:{prediction}')\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
