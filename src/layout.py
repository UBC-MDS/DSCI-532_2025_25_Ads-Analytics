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
        dbc.Col([
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
        ],
        style={
            'background-color': '#e6e6e6',
            'padding': 10,
            'border-radius': 3,
        }
        ) 
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

    install_chart = dbc.Card([
        dbc.CardHeader('Top 10 App Categories by Installs', style={'fontWeight': 'bold',
                                                                   "textAlign": "center",}),
        dbc.CardBody(
            dvc.Vega(
            id="category-chart",
            spec=installs_chart(df).to_dict(format="vega"),
            style={"padding": "20px", 
                   "justifyContent": "center",  
                   "alignItems": "center", 
                   'width': '100%',
                   'height': '100%' 
                   }
            ))
    ],
    className="shadow-sm h-100")

    make_engagement_chart = dbc.Card([
        dbc.CardHeader('Reviews vs. Installs for Top Apps', style={'fontWeight': 'bold',
                                                                   "textAlign": "center",}),
        dbc.CardBody(
            dvc.Vega(
            id="engagement-chart",
            spec=engagement_chart(df, ["All"]).to_dict(format="vega"),
            style={"padding": "20px", 
                   "justifyContent": "center",  
                   "alignItems": "center",
                   'width': '100%',
                   'height': '100%' 
                   }
            ))
    ],
    className="shadow-sm h-100")

    density_plot = dbc.Card([
        dbc.CardHeader('Density Plot for Ratings', style={'fontWeight': 'bold',
                                                          "textAlign": "center",}),
        dbc.CardBody(
            dvc.Vega(
            id="density-plot",
            spec=make_density_plot(df, ["All"]).to_dict(format="vega"),
            style={"padding": "1rem 4rem 1rem"}
        ))
    ],
    className="shadow-sm h-100")

    reviews_histogram = dbc.Card([
        dbc.CardHeader('Histogram for Number of Reviews', style={'fontWeight': 'bold',
                                                          "textAlign": "center",}),
        dbc.CardBody(
            dvc.Vega(
            id="reviews-histogram",
            spec=make_reviews_histogram(df, ["All"]).to_dict(format="vega"),
            style={"padding": "1rem 4rem 1rem"}
        ))
    ],
    className="shadow-sm h-100")

    wordcloud_component = dbc.Card([
        dbc.CardHeader('Word Cloud of Top Apps', style={'fontWeight': 'bold',
                                                          "textAlign": "center",}),
        dbc.CardBody(
            dcc.Graph(
            id="wordcloud",
            figure=create_wordcloud(df, ["All"]),
            config={"displayModeBar": False}
        ))
    ])

    return dbc.Container([
        dbc.Row([
            dbc.Col([ 
                html.H1([
                    html.Span("G", style={"color": "#4285F4", "fontWeight": "bold"}), 
                    html.Span("o", style={"color": "#EA4335", "fontWeight": "bold"}),
                    html.Span("o", style={"color": "#FBBC05", "fontWeight": "bold"}), 
                    html.Span("g", style={"color": "#4285F4", "fontWeight": "bold"}), 
                    html.Span("l", style={"color": "#34A853", "fontWeight": "bold"}),  
                    html.Span("e", style={"color": "#EA4335", "fontWeight": "bold"}), 
                    " Playstore Apps Ads Analytics"], className="text-center mb-3"),
                html.Br(),
                *global_filters
            ], md=2),

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
                    dbc.Col(wordcloud_component, md=12)
                ])
            ], md=10)
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
