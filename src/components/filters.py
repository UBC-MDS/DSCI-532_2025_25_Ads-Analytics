from dash import dcc, html
import dash_bootstrap_components as dbc
from src.data.data_import import get_dropdown_options

def create_global_filters(df):
    """
    Creates a set of global filter components for the dashboard.

    This function generates a collection of dropdowns, sliders, and other UI 
    elements that allow users to filter the dataset dynamically based on 
    criteria such as app type, rating, content rating, and category.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including type, rating, 
        content rating, and categories.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A dropdown for selecting app type (Free/Paid).
        - A slider for filtering by rating.
        - A dropdown for selecting content rating.
        - A multi-select dropdown for filtering by app category.
        - Proper layout and styling for ease of use.

    Example Usage:
    --------------
    app.layout = dbc.Container([
        create_global_filters(df)
    ])
    """
    return [
        dbc.Col([
            html.H1([
                html.Img(src='assets/android-chrome-192x192.png', height='50px'),
                " Playstore Apps Ads Analytics"
            ], 
            className="text-center mb-3",
            style={
                'padding': '5px',
                'backgroundColor': 'white'
            }),
            html.Br(),

            html.H5('Global controls'),
            html.Br(),

            dbc.Label("Select Category:"),
            dcc.Dropdown(
                id="category-filter",
                options=get_dropdown_options(df, "Category"),
                value=["All"],
                multi=True,
                maxHeight=200
            ),
            html.Br(),

            dbc.Label("Rating Range:"),
            dcc.RangeSlider(
                id="rating-slider",
                min=1,
                max=5,
                step=0.5,
                marks={i: str(i) for i in range(1, 6)},
                value=[1, 5],
                updatemode='mouseup',
                tooltip={"always_visible": True, "placement": "bottom"}
            ),
            html.Br(),

            dbc.Label("Select App Type:"),
            dcc.Dropdown(id="app-type-filter", 
                         options=get_dropdown_options(df, "Type"),
                         value=["All"], 
                         multi=True),
            html.Br(),

            dbc.Label("Select Content Rating:"),
            dcc.Dropdown(
                id="content-rating-filter",
                options=get_dropdown_options(df, "Content Rating"),
                value=["All"], 
                multi=True
            ),
            html.Br(),

            dbc.Button("Apply Filters", id="apply-filters", color="primary", style={'width': '100%'}, className="mt-3")
        ],
        className="filter-80",
        style={
            'background-color': 'white',
            'padding': 10,
            'border-radius': 3,
            'height': '100%'
        }),

        dcc.Store(id="filters-store", storage_type="memory")
    ]
