import pandas as pd
import streamlit as st
import datetime
import requests

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

# API call returning prediction

prediction = pd.

# Display Chart with Prediction Results

#Display Best time to Buy

#
