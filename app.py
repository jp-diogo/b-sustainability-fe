from distutils.command.config import config
from time import strftime
import pandas as pd
from sklearn.model_selection import PredefinedSplit
import streamlit as st
import datetime
import requests
from fe_utils import create_prediction_results_df, best_buy_sell, plot_predictions
#import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(layout="wide",
                   page_icon="⚡",
                   page_title="NYISO Predictor"

)



#header image
st.image('./_methode_times_prod_web_bin_912d36b0-3bfe-11ec-a9ce-48a11f44f00d.jpeg')

st.title("⚡ Predict NYISO Electricity Prices for the Next 5 days")

st.write(
    "This app enables you to predict the NYISO electricity price for the following 5 days so you can decide the best time to buy & sell power"
)

'''
## Let us know more about your energy needs below:

'''

# Get user inputs for Date, Time, Buy / Sell, Power Amount
d = st.date_input(
    "📅  Which day would you like to predict for?",
    datetime.date(2022, 1, 13))
#st.write('Your chosen date is:', d)

t = st.time_input('⏰ What time would you like to transact?', datetime.time(8, 00))
#st.write('Selected time is', t)

input_timestamp = datetime.datetime.combine(d,t)

#selectbox
buy_sell = st.selectbox('Would you like to buy or sell?', ['Buy', 'Sell'])

energy_quantity = st.slider(label="How much energy would you like to trade?", value=(100), min_value=1, max_value=100, step=1,key="Kw/h")

st.write("You will trade", energy_quantity, "kW/h")
'''
--------------------------------------------------------------------------
'''

'''
 ## Predicted Hourly Electricity Price for next 5 Days
'''

# Set url & paramaters
url = 'https://sustainability-bsfx5bk64a-ew.a.run.app/predict'
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
#st.dataframe(results_df)

# Display Chart with Prediction Results
st.plotly_chart(plot_predictions(results_df))

#pyplot



best_sell_price, best_sell_time, best_buy_price, best_buy_time = best_buy_sell(results_df)

sell_profit = round(energy_quantity * best_sell_price)

buy_costs = round(energy_quantity * best_buy_price)

time_lag = best_buy_time - best_sell_time

#def sell_before_buy():
    #if best_sell_time[0] < best_buy_time[0]:
    #    st.write(" ⚠️  Reminder: you will need to sell before you buy")
    #    st.write("First, you sell at", energy_quantity, "and after" ,  time_lag, "you will buy at " , best_buy_time)
    #else:
      #  pass


'''
## Our suggestion is to:
'''

'''
### 🤑 Sell
'''
st.write(f'Sell {energy_quantity} kW/h on the {best_sell_time} h for {best_sell_price} \$ per kW and your profit will be {sell_profit} $ ')

'''
### 🔋 Buy
'''
st.write(f'Buy {energy_quantity} kW/h on the {best_buy_time} h for {best_buy_price} \$ per kW and it will cost you {buy_costs} $ ')

'''
### ⏱️ Wait
'''
st.write(f'There is a {time_lag} h gap between the two trades')

'''
--------------------------------------------------------------------------
'''
