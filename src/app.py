from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
from install_chart import installs_chart
from engagement_chart import engagement_chart

# Loading dataset
df = pd.read_csv("data/preprocessed/clean_data.csv")

# **** Global Variables **** #
title = [html.H1("Google Playstore Apps Ads Analytics", className="text-center mb-3"),
        html.H6('This dashboard helps advertisement companies identify the most promising Google Play Store apps for ad placements by analyzing app metrics such as user engagement and ratings', 
                className="text-center fw-light mb-4",
                style={"maxWidth": "60%", "margin": "auto", "whiteSpace": "normal", "wordWrap": "break-word"}
                )]

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
        ),
    html.Br(),

    dbc.Label("Select Content Rating:"),
    dcc.Dropdown(
        id="content-rating-filter",
        options=[{"label": rating, "value": rating} for rating in sorted(df["Content Rating"].dropna().unique())],
        value=["Everyone"], 
        multi=True
    )

]

install_chart = dvc.Vega(
    id="category-chart",
    spec=installs_chart(df).to_dict(format="vega") 
)

make_engagement_chart = dvc.Vega(
    id="engagement-chart",
    spec=engagement_chart(df).to_dict(format="vega")   
)

# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row(dbc.Col(title)), 
    
    dbc.Row([
  
        dbc.Col(global_filters, width=2,
                className="border-end pe-3"),

        dbc.Col([
            dbc.Row([
                dbc.Col(install_chart, md=6),  
                dbc.Col(make_engagement_chart, md=6)   
            ])
        ], md=9)
    ], className="border-top pt-3") 
], fluid=True)


# Server side callbacks/reactivity
@app.callback(
    [Output("category-chart", "spec"),
    Output("engagement-chart", "spec")],
    [Input("app-type-filter", "value"),
    Input("rating-slider", "value"),
    Input("content-rating-filter", "value")]
)

def update_charts(selected_types, min_rating, selected_ratings):

    if isinstance(selected_types, str):
        selected_types = [selected_types]
    if isinstance(selected_ratings, str):
        selected_ratings = [selected_ratings]

    filtered_df = df[
        (df["Type"].isin(selected_types)) &  
        (df["Rating"] >= min_rating) &  
        (df["Content Rating"].isin(selected_ratings))  
    ]

    return installs_chart(filtered_df).to_dict(format="vega"), engagement_chart(filtered_df).to_dict(format="vega") 

# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
