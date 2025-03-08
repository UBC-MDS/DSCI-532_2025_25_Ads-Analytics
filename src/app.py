# app.py
from dash import Dash
import dash_bootstrap_components as dbc
from data_import import load_data
from layout import create_layout
from callbacks import register_callbacks

# Load the data
df = load_data("data/preprocessed/sampled_clean_data.csv")

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
server = app.server

# Create the layout
app.layout = create_layout(df)

# Register callbacks
register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=False)