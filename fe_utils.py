import pandas as pd
import datetime
from datetime import timedelta
import requests

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
