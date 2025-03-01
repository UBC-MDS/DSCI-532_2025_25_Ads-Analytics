from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
from installs import installs_chart

# Loading dataset
df = pd.read_csv("data/preprocessed/clean_data.csv")

# **** Global Variables **** #
title = html.H1("Google Playstore Apps Ads Analytics", className="text-center")

global_filters = [
    dbc.Label("Select App Type:"),
    dcc.Dropdown(id="app-type-filter", 
                 options=[{"label": type_, "value": type_} for type_ in sorted(df["Type"].dropna().unique())],
                 value = ["Free"], 
                 multi= True),
    html.Br(),
    dbc.Label("Minimum Rating:"),
    dcc.Slider(
            id="rating-slider",
            min=1,
            max=5,
            step=0.5,
            marks={i: str(i) for i in range(1, 6)},
            value=4,
            updatemode='drag'
        )

]

install_chart = dvc.Vega(
    id="category-chart",
    spec=installs_chart(df).to_dict(format="vega") 
)



# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)),  # Title at the top
    
    dbc.Row([
        # Left Column (Filters)
        dbc.Col(global_filters, md=2),

        # Right Column (Chart)
        dbc.Col(install_chart, md=8)
    ])
], fluid=True)

# Server side callbacks/reactivity
@app.callback(
    Output("category-chart", "spec"),
    Input("app-type-filter", "value"),
    Input("rating-slider", "value")
)

def update_charts(selected_types, min_rating):
    # filtered_df = df[(df["Type"] == selected_type) & (df["Rating"] >= min_rating)]
    # chart_html = installs_chart(filtered_df, selected_type, min_rating)
    # return chart_html

    if isinstance(selected_types, str):  
        selected_types = [selected_types]  # Ensure it's always a list

    # Apply filters
    filtered_df = df[df["Type"].isin(selected_types) & (df["Rating"] >= min_rating)]

    # Ensure installs_chart() returns a Vega JSON object
    return installs_chart(filtered_df).to_dict(format="vega")

# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
