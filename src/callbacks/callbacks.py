from dash import Dash
import pandas as pd
from src.callbacks import register_charts_callbacks, register_filters_callbacks

def register_callbacks(app, df):
    """
    Register all callbacks for the Dash app.

    Parameters:
    app (Dash): The Dash app instance.
    df (pd.DataFrame): The DataFrame containing the data.
    """
    register_charts_callbacks(app, df)
    register_filters_callbacks(app)