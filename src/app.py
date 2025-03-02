from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

import pandas as pd

from install_chart import installs_chart
from engagement_chart import engagement_chart
from get_summary_stats import get_summary_stats
from make_density_plot import make_density_plot
from make_reviews_histogram import make_reviews_histogram
from ranking_chart import ranking_chart

import altair as alt

df = pd.read_csv("data/preprocessed/sampled_clean_data.csv")

def get_dropdown_options(column):
    """
    Generates a list of options for a dropdown menu based on the unique values in a specified column of the DataFrame.

    Parameters:
    column (str): The name of the column in the DataFrame for which to generate dropdown options.

    Returns:
    list: A list of dictionaries, where each dictionary contains 'label' and 'value' keys, 
          with 'All' as the first option and the unique values of the specified column as subsequent options.

    Example:
    >>> get_dropdown_options("Category")
    [
        {"label": "All", "value": "All"},
        {"label": "Action", "value": "Action"},
        {"label": "Adventure", "value": "Adventure"},
        ...
    ]
    """
    unique_values = sorted(df[column].dropna().unique())
    options = [{"label": "All", "value": "All"}] + [{"label": value, "value": value} for value in unique_values]
    return options

global_filters = [
    dbc.Label("Select Category:"),
    dcc.Dropdown(
        id="category-filter",
        options=get_dropdown_options("Category"),
        value=["All"],
        multi=True,
        maxHeight=200
    ),

    dbc.Label("Rating Range:"),
    dcc.RangeSlider(
        id="rating-slider",
        min=1,
        max=5,
        step=0.5,
        marks={i: str(i) for i in range(1, 6)},
        value=[1, 5],
        updatemode='drag'
    ),
    html.Br(),

    dbc.Label("Select App Type:"),
    dcc.Dropdown(id="app-type-filter", 
                 options=get_dropdown_options("Type"),
                 value=["All"], 
                 multi=True),
    html.Br(),

    dbc.Label("Select Content Rating:"),
    dcc.Dropdown(
        id="content-rating-filter",
        options=get_dropdown_options("Content Rating"),
        value=["All"], 
        multi=True
    ),
    html.Br()
]

install_chart = dvc.Vega(
    id="category-chart",
    spec=installs_chart(df).to_dict(format="vega") 
)

make_engagement_chart = dvc.Vega(
    id="engagement-chart",
    spec=engagement_chart(df).to_dict(format="vega")   
)

density_plot = dvc.Vega(
    id="density-plot",
    spec=make_density_plot(df, ["All"]).to_dict(format="vega")
)

reviews_histogram = dvc.Vega(
    id="reviews-histogram",
    spec=make_reviews_histogram(df, ["All"]).to_dict(format="vega")
)

ranking_chart_component = dvc.Vega(
    id="ranking-chart",
    spec=ranking_chart(df, selected_type="Free", min_rating=4).to_dict(format="vega")
)

# Initialize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
server = app.server

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Google Playstore Apps Ads Analytics", className="text-center mb-3"),
            html.Br(),
            *global_filters
        ], width=2, className="border-end pe-3"),

        dbc.Col([
            dbc.Row([
                dbc.Col(
                    html.Div([
                        dash_table.DataTable(
                            id='summary-stats-table',
                            columns=[
                                {"name": "Metric", "id": "Metric"},
                                {"name": "Mean", "id": "Mean"},
                                {"name": "Min", "id": "Min"},
                                {"name": "Max", "id": "Max"},
                            ],
                            style_table={'overflowX': 'auto'},
                            style_cell={'textAlign': 'center', 'minWidth': '100px', 'width': '150px'},
                            style_header={'fontWeight': 'bold'},
                        ),
                    ], className="ticker-container", style={"maxWidth": "80%", "margin": "auto"})
                ),
            ]),

            dbc.Row([
                dbc.Col(install_chart, md=6),  
                dbc.Col(make_engagement_chart, md=6)
            ]),

            dbc.Row([
                dbc.Col(density_plot, md=6),
                dbc.Col(reviews_histogram, md=6)
            ]),

            dbc.Row([
                dbc.Col(ranking_chart_component, md=6)
            ])

        ], md=9)
    ], className="border-top pt-3"),

    # Footer
    dbc.Row(dbc.Col([
        html.Hr(),
        html.H6('This dashboard helps advertisement companies identify the most promising Google Play Store apps for ad placements by analyzing app metrics such as user engagement and ratings', 
                className="text-center fw-light mb-4",
                style={"maxWidth": "60%", "margin": "auto", "whiteSpace": "normal", "wordWrap": "break-word"}
                ),
        html.P("Project by: Quanhua Huang, Yeji Sohn, Lukman Lateef, Ismail (Husain) Bhinderwala", className="text-center fw-light"),
        html.P(["GitHub Repository: ", html.A("Link to Repo", href="https://github.com/UBC-MDS/DSCI-532_2025_25_Ads-Analytics", target="_blank")], className="text-center"),
        html.P("Last Updated: March 2025", className="text-center fw-light")
    ], width=12, className="text-center mt-4"))
], fluid=True)

@app.callback(
    [Output("category-chart", "spec"),
     Output("engagement-chart", "spec"),
     Output("summary-stats-table", "data"),
     Output("category-filter", "value"),
     Output("density-plot", "spec"),
     Output("reviews-histogram", "spec"),
     Output("ranking-chart", "spec")],
    [Input("app-type-filter", "value"),
     Input("rating-slider", "value"),
     Input("content-rating-filter", "value"),
     Input("category-filter", "value")]
)
def update_charts(selected_types, rating_range, selected_ratings, selected_categories):
    # Apply all filters to the dataset (filtering based on all inputs)
    if "All" in selected_types:
        selected_types = df["Type"].unique()
    if "All" in selected_ratings:
        selected_ratings = df["Content Rating"].unique()
    if "All" in selected_categories:
        selected_categories = df["Category"].unique()
    elif len(selected_categories) > 4:
        selected_categories = selected_categories[:4]

    min_rating, max_rating = rating_range

    filtered_df = df[
        (df["Type"].isin(selected_types)) &  
        (df["Rating"] >= min_rating) & (df["Rating"] <= max_rating) &
        (df["Content Rating"].isin(selected_ratings)) &
        (df["Category"].isin(selected_categories))
    ]

    stats = get_summary_stats(filtered_df)

    summary_data = [
        {"Metric": "Rating", "Mean": stats["mean_rating"], "Min": stats["min_rating"], "Max": stats["max_rating"]},
        {"Metric": "Installs", "Mean": stats["mean_installs"], "Min": stats["min_installs"], "Max": stats["max_installs"]},
        {"Metric": "Reviews", "Mean": stats["mean_reviews"], "Min": stats["min_reviews"], "Max": stats["max_reviews"]}
    ]

    return (
        installs_chart(filtered_df).to_dict(format="vega"),
        engagement_chart(filtered_df).to_dict(format="vega"),
        summary_data,
        ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories,
        make_density_plot(filtered_df, selected_categories).to_dict(format="vega"),  
        make_reviews_histogram(filtered_df, selected_categories).to_dict(format="vega"),  
        ranking_chart(filtered_df, selected_types[0], min_rating).to_dict(format="vega") 
    )

if __name__ == "__main__":
    app.run(debug=False)