# layout.py
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from src.data_import import get_dropdown_options
from src.charts.install_chart import installs_chart
from src.charts.engagement_chart import engagement_chart
from src.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.make_reviews_histogram import make_reviews_histogram
from src.charts.ranking_chart import create_wordcloud 

def create_global_filters(df):
    """
    Create the global filters for the Dash app.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    list: A list of Dash components representing the global filters.
    """
    return [
        dbc.Label("Select Category:"),
        dcc.Dropdown(
            id="category-filter",
            options=get_dropdown_options(df, "Category"),
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
        html.Br()
    ]

def create_layout(df):
    """
    Create the layout for the Dash app.
    
    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    
    Returns:
    dbc.Container: The layout of the Dash app.
    """
    global_filters = create_global_filters(df)

    install_chart = dvc.Vega(
        id="category-chart",
        spec=installs_chart(df).to_dict(format="vega"),
        style={"padding": "1rem 4rem 1rem"}
    )

    make_engagement_chart = dvc.Vega(
        id="engagement-chart",
        spec=engagement_chart(df).to_dict(format="vega"),
        style={"padding": "1rem 4rem 1rem"}
    )

    density_plot = dvc.Vega(
        id="density-plot",
        spec=make_density_plot(df, ["All"]).to_dict(format="vega"),
        style={"padding": "1rem 4rem 1rem"}
    )

    reviews_histogram = dvc.Vega(
        id="reviews-histogram",
        spec=make_reviews_histogram(df, ["All"]).to_dict(format="vega"),
        style={"padding": "1rem 4rem 1rem"}
    )

    wordcloud_component = dcc.Graph(
        id="wordcloud",
        figure=create_wordcloud(df, ["All"]),
        config={"displayModeBar": False}
    )

    return dbc.Container([
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
                    dbc.Col(make_engagement_chart, md=3)
                ]),

                dbc.Row([
                    dbc.Col(density_plot, md=6),
                    dbc.Col(reviews_histogram, md=3)
                ]),

                dbc.Row([ 
                    dbc.Col(wordcloud_component, md=12)
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
