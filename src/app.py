from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
import pandas as pd
from install_chart import installs_chart
from engagement_chart import engagement_chart

# Loading dataset
df = pd.read_csv("../data/preprocessed/clean_data.csv")

# Helper function to get options with "All"
def get_dropdown_options(column):
    unique_values = sorted(df[column].dropna().unique())
    options = [{"label": "All", "value": "All"}] + [{"label": value, "value": value} for value in unique_values]
    return options

# Function to calculate mean, min, max for rating, installs, and reviews
def get_summary_stats(filtered_df):
    mean_rating = filtered_df['Rating'].mean()
    min_rating = filtered_df['Rating'].min()
    max_rating = filtered_df['Rating'].max()

    mean_installs = filtered_df['Installs'].mean()
    min_installs = filtered_df['Installs'].min()
    max_installs = filtered_df['Installs'].max()

    mean_reviews = filtered_df['Reviews'].mean()
    min_reviews = filtered_df['Reviews'].min()
    max_reviews = filtered_df['Reviews'].max()

    return {
        "mean_rating": round(mean_rating, 2),
        "min_rating": min_rating,
        "max_rating": max_rating,
        "mean_installs": round(mean_installs, 0),
        "min_installs": min_installs,
        "max_installs": max_installs,
        "mean_reviews": round(mean_reviews, 0),
        "min_reviews": min_reviews,
        "max_reviews": max_reviews,
    }

# Global Filters
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
                # Table Row - Summary Stats Table
                dbc.Col(
                    html.Div([
                        html.H5("Summary Statistics:"),
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

            # Charts Row
            dbc.Row([
                dbc.Col(install_chart, md=6),  
                dbc.Col(make_engagement_chart, md=6)
            ]),

        ], md=9)
    ], className="border-top pt-3"),

    dbc.Row(dbc.Col(
        html.H6('This dashboard helps advertisement companies identify the most promising Google Play Store apps for ad placements by analyzing app metrics such as user engagement and ratings', 
                className="text-center fw-light mb-4",
                style={"maxWidth": "60%", "margin": "auto", "whiteSpace": "normal", "wordWrap": "break-word"}
                ),
        width=12, className="text-center mt-4"
    ))
], fluid=True)

# Server side callbacks/reactivity
@app.callback(
    [Output("category-chart", "spec"),
     Output("engagement-chart", "spec"),
     Output("summary-stats-table", "data"),
     Output("category-filter", "value")],
    [Input("app-type-filter", "value"),
     Input("rating-slider", "value"),
     Input("content-rating-filter", "value"),
     Input("category-filter", "value")]
)

def update_charts(selected_types, rating_range, selected_ratings, selected_categories):

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
    
    # Get summary statistics for the filtered data
    stats = get_summary_stats(filtered_df)

    # Prepare the data for the summary stats table
    summary_data = [
        {"Metric": "Rating", "Mean": stats["mean_rating"], "Min": stats["min_rating"], "Max": stats["max_rating"]},
        {"Metric": "Installs", "Mean": stats["mean_installs"], "Min": stats["min_installs"], "Max": stats["max_installs"]},
        {"Metric": "Reviews", "Mean": stats["mean_reviews"], "Min": stats["min_reviews"], "Max": stats["max_reviews"]}
    ]

    # Return the updated chart specs, summary statistics, and selected categories
    return (
        installs_chart(filtered_df).to_dict(format="vega"),
        engagement_chart(filtered_df).to_dict(format="vega"),
        summary_data,
        ["All"] if len(selected_categories) == len(df["Category"].unique()) else selected_categories
    )

# Run the app/dashboard
if __name__ == "__main__":
    server.run(debug=False)
