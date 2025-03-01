from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from installs import installs_chart

# Loading dataset
df = pd.read_csv("../data/preprocessed/clean_data.csv")

# **** Global Variables **** #
title = html.H3("Google Playstore Apps Ads Analytics", className="text-center")

global_filters = dbc.Row([
    dbc.Col([
        html.Label("Select App Type:"),
        dcc.RadioItems(
            id="app-type-filter",
            options=[{"label": "Free", "value": "Free"}, {"label": "Paid", "value": "Paid"}],
            value="Free",
            inline=True
        )
    ], width=3),

    dbc.Col([
        html.Label("Minimum Rating:"),
        dcc.Slider(
            id="rating-slider",
            min=1,
            max=5,
            step=0.5,
            marks={i: str(i) for i in range(1, 6)},
            value=4
        )
    ], width=6)
])

install_chart = dbc.Card([
    dbc.CardHeader("Installs by Category"),
    dbc.CardBody(dcc.Markdown(id="category-chart", dangerously_allow_html=True)) 
])


# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),  # Title at the top
    
    dbc.Row([
        # Left Column (Filters)
        dbc.Col(global_filters, md=4),

        # Right Column (Chart)
        dbc.Col(install_chart, md=8)
    ])
], fluid=True)

# Server side callbacks/reactivity
@app.callback(
    Output("category-chart", "children"),
    Input("app-type-filter", "value"),
    Input("rating-slider", "value")
)

def update_chart(selected_type, min_rating):
    filtered_df = df[(df["Type"] == selected_type) & (df["Rating"] >= min_rating)]
    chart_html = installs_chart(filtered_df, selected_type, min_rating)
    return chart_html

# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
