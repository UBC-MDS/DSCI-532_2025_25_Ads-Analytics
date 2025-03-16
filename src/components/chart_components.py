from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from src.charts.engagement_chart import engagement_chart
from src.charts.make_density_plot import make_density_plot
from src.charts.ranking_chart import create_wordcloud 
from src.charts.make_popularity_score import make_popularity_score
#from src.charts.install_chart import installs_chart

# def install_chart_component(df):
#     # Make charts
#     install_chart = dbc.Card([
#         dbc.CardHeader('Top 10 App Categories by Installs', style={'fontWeight': 'bold',
#                                                                    "textAlign": "center",}),
#         dbc.CardBody(
#             dvc.Vega(
#             id="category-chart",
#             spec=installs_chart(df).to_dict(format="vega"),
#             style={"padding": "20px", 
#                    "justifyContent": "center",  
#                    "alignItems": "center", 
#                    'width': '100%',
#                    'height': '100%' 
#                    }
#             ))
#     ],
#     className="shadow-sm h-100")

#     return install_chart

def engagement_chart_component(df):
    return dbc.Card([
        dbc.CardHeader(
            'Reviews vs. Installs for Top Apps',
            className="fw-bold text-center bg-light border-bottom border-secondary"
        ),
        dbc.CardBody(
            dcc.Loading(  # Add loading indicator
                id="loading-engagement-chart",
                children=[
                    dvc.Vega(
                        id="engagement-chart",
                        spec=engagement_chart(df, ["All"]).to_dict(format="vega"),
                        style={'width': '100%', 'height': '100%'}
                    )
                ]
            ),
            className="d-flex align-items-center justify-content-center p-0"
        )
    ], className="shadow-sm h-100 border-0 rounded")

def density_plot_component(df):
    return dbc.Card([
            dbc.CardHeader(
                "Density Plot for Ratings",
                className="fw-bold text-center bg-light border-bottom border-secondary"
            ),
            dbc.CardBody(
                dcc.Loading(  # Add loading indicator
                id="loading-density-plot",
                children=[
                    dvc.Vega(
                        id="density-plot",
                        spec=make_density_plot(df, ["All"]).to_dict(format="vega"),
                        style={'width': '100%',
                            'height': '100%' 
                            }
                    )
                ]
                ),
            className="d-flex align-items-center justify-content-center p-0"
            )
        ],
        className="shadow-sm h-100 border-0 rounded")
    
    

def popularity_histogram_component(df):
    return dbc.Card(
        [
            dbc.CardHeader(
                "Average Popularity Score by Categories",
                className="fw-bold text-center bg-light border-bottom border-secondary"
            ),
            dbc.CardBody(
                dcc.Loading(  # Add loading indicator
                id="loading-pop-histogram",
                children=[
                    dvc.Vega(
                        id="popularity-histogram",
                        spec=make_popularity_score(df, ["All"]).to_dict(format="vega"),
                        style={
                            "width": "100%",
                            "height": "100%" 
                        }
                    )
                ]
                ),
                className="d-flex align-items-center justify-content-center p-0" 
            )
        ],
        className="shadow-sm h-100 border-0 rounded"
    )

    

def wordcloud_component(df):
    return dbc.Card([
        dbc.CardHeader('Word Cloud of Top Apps', 
                       className="fw-bold text-center bg-light border-bottom border-primary"),
        dbc.CardBody(
            dcc.Loading(  # Add loading indicator
                id="loading-wordcloud",
                children=[
                    dcc.Graph(
                        id="wordcloud",
                        figure=create_wordcloud(df, ["All"]),
                        config={"displayModeBar": False},
                        style={'width': '100%', 
                            'height': '100%'}
                    )
                ]
            ),
            className="d-flex align-items-center justify-content-center p-0" 
        )
    ],
    className="shadow-sm h-100 border-0 rounded")

    