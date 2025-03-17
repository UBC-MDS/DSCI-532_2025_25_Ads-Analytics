from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc

from src.charts.engagement_chart import engagement_chart
from src.charts.make_density_plot import make_density_plot
from src.charts.ranking_chart import create_wordcloud 
from src.charts.make_popularity_score import make_popularity_score
from src.charts.pie_chart import create_pie
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
    """
    Creates a Dash Bootstrap Card component displaying the 'Reviews vs. Installs' engagement chart.

    This function generates a card containing an interactive Vega-Lite chart that visualizes 
    the relationship between the number of reviews and installs for the top apps. The chart 
    dynamically updates based on selected filters.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including installs, reviews, and categories.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A header with the chart title.
        - A Vega-Lite chart rendered via `dash_vega_components` (`dvc.Vega`).
        - A loading indicator (`dcc.Loading`) to enhance user experience while the chart loads.
    
    Example Usage:
    --------------
    app.layout = dbc.Container([
        engagement_chart_component(df)
    ])
    """
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
    """
    Creates a Dash Bootstrap Card component displaying the 'Density Plot for Ratings'.

    This function generates a card containing an interactive Vega-Lite density plot 
    that visualizes the distribution of app ratings. The chart dynamically updates 
    based on selected filters.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including ratings, installs, and reviews.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A header with the chart title.
        - A Vega-Lite density plot rendered via `dash_vega_components` (`dvc.Vega`).
        - A loading indicator (`dcc.Loading`) to enhance user experience while the chart loads.

    Example Usage:
    --------------
    app.layout = dbc.Container([
        density_plot_component(df)
    ])
    """
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
    """
    Creates a Dash Bootstrap Card component displaying the 'Average Popularity Score by Categories' histogram.

    This function generates a card containing an interactive Vega-Lite histogram that visualizes 
    the average popularity score for different app categories. The chart dynamically updates 
    based on selected filters.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including categories, installs, and ratings.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A header with the chart title.
        - A Vega-Lite histogram rendered via `dash_vega_components` (`dvc.Vega`).
        - A loading indicator (`dcc.Loading`) to enhance user experience while the chart loads.

    Example Usage:
    --------------
    app.layout = dbc.Container([
        popularity_histogram_component(df)
    ])
    """
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
    """
    Creates a Dash Bootstrap Card component displaying a 'Word Cloud of Top Apps'.

    This function generates a card containing an interactive word cloud visualization, 
    where the size of each word represents the popularity of app names based on installs 
    or reviews. The word cloud dynamically updates based on selected filters.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including names, installs, and reviews.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A header with the title 'Word Cloud of Top Apps'.
        - A word cloud rendered via `dcc.Graph`.
        - A loading indicator (`dcc.Loading`) to enhance user experience while the chart loads.

    Example Usage:
    --------------
    app.layout = dbc.Container([
        wordcloud_component(df)
    ])
    """
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
                ],
                className="d-flex align-items-center justify-content-center p-0" 
            ),
            
        )
    ],
    className="shadow-sm h-100 border-0 rounded")

    

def pie_chart_component(df):
    """
    Creates a Dash Bootstrap Card component displaying a 'Pie Chart for Top Apps'.

    This function generates a card containing an interactive Vega-Lite pie chart 
    that visualizes the distribution of top apps based on a selected metric (e.g., installs, 
    category, or rating). The pie chart dynamically updates based on selected filters.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including categories, installs, 
        and ratings.

    Returns:
    --------
    dbc.Card
        A Dash Bootstrap Card containing:
        - A header with the title 'Pie Chart for Top Apps'.
        - A pie chart rendered via `dash_vega_components` (`dvc.Vega`).
        - A loading indicator (`dcc.Loading`) to enhance user experience while the chart loads.

    Example Usage:
    --------------
    app.layout = dbc.Container([
        pie_chart_component(df)
    ])
    """
    make_pie_chart = dbc.Card([
        dbc.CardHeader('Pie Chart for Top Apps', 
                       className="fw-bold text-center bg-light border-bottom border-secondary"),
        dbc.CardBody(
            dcc.Loading(  # Add loading indicator
                id="loading-pie-chart",
                children=[
                    dvc.Vega(
                    id="pie-chart",
                    spec=create_pie(df, ["All"]).to_dict(format="vega"),
                    style={'width': '100%',
                        'height': '100%' 
                        }
                    )
                    ],
            className="d-flex align-items-center justify-content-center p-0"
            ),
        )
    ],
    className="shadow-sm h-100 border-0 rounded")

    return make_pie_chart