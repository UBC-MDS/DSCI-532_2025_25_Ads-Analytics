# app.py
from dash import Dash
import dash_bootstrap_components as dbc

from src.utils.cache import cache
from src.data.data_import import load_data
from src.components.layout import create_layout
from src.callbacks.callbacks import register_callbacks

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.title = 'Ads Analytics'
app._favicon = ("src/assets/favicon.ico")

cache.init_app(
    app.server,
    config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'tmp'
    }
)

server = app.server

# Load the data
df = load_data("data/preprocessed/clean_data_score.parquet")

# Create the layout
app.layout = create_layout(df)

# Register callbacks
register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=False)
