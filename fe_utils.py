import pandas as pd
import datetime
from datetime import timedelta
import requests
import plotly.express as px

def create_prediction_results_df(prediction_list, pred_timestamp):
    results_df = pd.DataFrame(prediction_list, columns=['Predicted Price'])
    results_df['Hours from Pred'] = results_df.index + 1
    results_df['Prediction_Timestamp'] = results_df['Hours from Pred'].map(
        lambda x: pred_timestamp + timedelta(hours=x))
    results_df['Predicted Price'] = results_df['Predicted Price'].map(
        lambda x: round(x,2))
    results_df['Date'] = results_df['Prediction_Timestamp'].dt.date
    results_df = results_df.set_index(['Prediction_Timestamp'])
    return results_df

def best_buy_sell(results_df):
    # Returns best time & price to buy & sell based on the results dataframe
    best_sell_price = results_df['Predicted Price'].loc[results_df['Predicted Price'].idxmax()]
    best_sell_time = results_df['Predicted Price'].idxmax()
    best_buy_price = results_df['Predicted Price'].loc[results_df['Predicted Price'].idxmin()]
    best_buy_time = results_df['Predicted Price'].idxmin()
    return best_sell_price, best_sell_time, best_buy_price, best_buy_time


def plot_predictions(pred_df):
    # Calls best_buy_sell
    best_sell_price, best_sell_time, best_buy_price, best_buy_time = best_buy_sell(pred_df)
    # Creates interactive chart of predictions
    fig = px.line(pred_df,
              x=pred_df.index,
              y='Predicted Price',
              )
    fig.update_layout(xaxis_title='Date',
                    yaxis_title="$ MWh Electricity Price")
    fig.add_annotation(
                x=best_buy_time, y=best_buy_price,
                text='Best time to Buy')
    fig.add_annotation(
                x=best_sell_time, y=best_sell_price,
                text='Best time to Sell')
    fig.update_annotations(
                xref="x", yref="y",
                font=dict(color="#004AAD"),
                showarrow=True,
                arrowhead=1,
                arrowcolor='#004AAD'
                )
    return fig
