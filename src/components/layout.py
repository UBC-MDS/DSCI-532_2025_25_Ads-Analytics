# layout.py
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from src.components.filters import create_global_filters
from src.components.get_summary_stats import get_summary_stats
from src.components.chart_components import (engagement_chart_component, 
                                             density_plot_component, 
                                             popularity_histogram_component, 
                                             wordcloud_component,
                                             pie_chart_component)
from src.components.footer_components import footer_component


def create_layout(df):
    """
    Generates the complete layout for the Sales Analytics Dashboard.

    This function initializes the dashboard structure by organizing:
    - Filters for user interaction.
    - Summary statistics.
    - Various interactive charts for data visualization.
    - A footer section with additional information.

    Parameters:
    -----------
    df : pandas.DataFrame
        The dataset containing app-related information, including installs, 
        ratings, categories, and customer engagement data.

    Returns:
    --------
    dbc.Container
        A Dash Bootstrap Container with the following sections:
        - Global Filters (app type, ratings, content rating, and category filters).
        - Summary Statistics Cards displaying key metrics.
        - Multiple interactive charts:
            - Popularity Histogram
            - Engagement Chart (Reviews vs Installs)
            - Density Plot (Rating Distribution)
            - Word Cloud of Top Apps
            - Pie Chart (Category Distribution)
        - Footer Section containing additional details.

    Example Usage:
    --------------
    app.layout = create_layout(df)
    """

    global_filters = create_global_filters(df)

    # Summary cards
    summary_stats = get_summary_stats(df)

    # Charts
    popularity_histogram = popularity_histogram_component(df)
    make_engagement_chart = engagement_chart_component(df)
    density_plot = density_plot_component(df)
    wordcloud_chart = wordcloud_component(df)
    pie_chart = pie_chart_component(df)

    # Footers
    footer = footer_component()

    return dbc.Container([
        dbc.Row([
            dbc.Col([
                *global_filters
            ], md=2),

            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Rating", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(summary_stats['mean_rating'], id="mean-rating", className="fw-bold", style={"color": "#34A853"}),
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Reviews", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(summary_stats['mean_reviews'], id="mean-reviews", className="fw-bold", style={"color": "#4285F4"}),
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Installs", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(summary_stats['mean_installs'], id="mean-installs", className="fw-bold", style={"color": "#FBBC05"}),
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                ],
                    className="mt-3 mb-4",
                    justify="center"),

                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardBody([
                            dbc.Row([
                                dbc.Col(popularity_histogram, md=6),
                                dbc.Col(make_engagement_chart, md=6)
                            ]),
                            dbc.Row([
                                dbc.Col(density_plot, md=6),
                                dbc.Col(pie_chart, md=6)
                            ]),
                            dbc.Row([
                                dbc.Col(wordcloud_chart, md=12)
                            ])
                        ])
                    ], style={"backgroundColor": "#f8f9fa", "paddingTop": "10px", "paddingBottom": "10px"}), md=12)
                ])

            ], md=10)
        ], className="border-top pt-3"),

        # Footer
        footer
    ], fluid=True, style={"backgroundColor": "#add8e6"})
