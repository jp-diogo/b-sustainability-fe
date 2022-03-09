import pandas as pd
from sklearn.model_selection import PredefinedSplit
import streamlit as st
import datetime
import requests
from fe_utils import create_prediction_results_df

st.set_page_config(layout="centered",
                   page_icon="💡",
                   page_title="NYISO Predictor")
st.title("💡 Predict NYISO Electricity Prices for the Next 5 days")

st.write(
    "This app enables you to predict the NYISO electricity price for the following 5 days so you can decide the best time to buy & sell power"
)

'''
#### Let us know more about your energy needs below:

'''

# Get user inputs for Date, Time, Buy / Sell, Power Amount
d = st.date_input(
    "Which day would you like to predict for?",
    datetime.date(2022, 1, 5))
st.write('Your chosen date is:', d)

t = st.time_input('What time would you like to transact?', datetime.time(8, 00))
st.write('Selected time is', t)

input_timestamp = datetime.datetime.combine(d,t)

# Testing format with dummy prediction results

# model_results = pd.read_csv('./raw_data/example_prediction.csv')
# results_df = create_prediction_dataframe(model_results, input_timestamp)

# API Call & Response Handling

# Set url & paramaters
url = 'http://127.0.0.1:8000/predict'
params = dict(timestamp=input_timestamp)

# Retrieve the response
response = requests.get(
    url,
    params
)
# Asign results to list
prediction_list = response.json().get('prediction')[0]

# Create dataframe of results for use on front end site
results_df = create_prediction_results_df(prediction_list, input_timestamp)
st.dataframe(results_df)

# Display Chart with Prediction Results
#st.line_chart(results_df['Predicted Price'])

# Display Best time to Buy

# Display Best time to Sell
