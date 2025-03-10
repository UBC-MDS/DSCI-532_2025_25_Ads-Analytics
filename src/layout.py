# layout.py
from dash import Dash, dcc, html, Input, Output, dash_table
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from src.data_import import get_dropdown_options
from src.charts.engagement_chart import engagement_chart
from src.get_summary_stats import get_summary_stats
from src.charts.make_density_plot import make_density_plot
from src.charts.make_reviews_histogram import make_reviews_histogram
from src.charts.ranking_chart import create_wordcloud 
from src.charts.make_popularity_score import make_popularity_score
from src.charts.install_chart import installs_chart

def create_global_filters(df):
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
        html.Br()
        ],
        className="h-80",
        style={
            'background-color': '#e6e6e6',
            'padding': 10,
            'border-radius': 3,
        }) 
    ]

def create_layout(df):
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
        dbc.CardHeader('Reviews vs. Installs for Top Apps', style={'fontWeight': 'bold', "textAlign": "center"}),
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
        dbc.CardHeader('Density Plot for Ratings', style={'fontWeight': 'bold', "textAlign": "center"}),
        dbc.CardBody(
            dvc.Vega(
            id="density-plot",
            spec=make_density_plot(df, ["All"]).to_dict(format="vega"),
            style={"padding": "20%", 
                   "justifyContent": "center",  
                   "alignItems": "center",
                   'width': '100%',
                   'height': '100%' 
                   }
        ))
    ],
    className="shadow-sm h-100")

    popularity_histogram = dbc.Card([
        dbc.CardHeader('Average Popularity Score by Categories', style={'fontWeight': 'bold', "textAlign": "center"}),
        dbc.CardBody(
            dvc.Vega(
            id="popularity-histogram",
            spec=make_popularity_score(df, ["All"]).to_dict(format="vega"),
            style={"padding": "20%", 
                   "justifyContent": "center",  
                   "alignItems": "center",
                   'width': '100%',
                   'height': '100%' 
                   }
        ))
    ],
    className="shadow-sm h-100")

    wordcloud_component = dbc.Card([
        dbc.CardHeader('Word Cloud of Top Apps', style={'fontWeight': 'bold', "textAlign": "center"}),
        dbc.CardBody(
            dcc.Graph(
                id="wordcloud",
                figure=create_wordcloud(df, ["All"]),
                config={"displayModeBar": False},
                style={'width': '100%', 'height': '100%'}
            )
        )
    ],
    className="shadow-sm h-100")

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
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Rating", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(id="mean-rating", className="fw-bold", style={"color": "#34A853"}), 
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Reviews", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(id="mean-reviews", className="fw-bold", style={"color": "#4285F4"}),  
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader(html.Span("Average Installs", className="fw-bold text-dark"),
                                           className="text-center bg-light border-bottom border-3",
                                           style={"borderImage": "linear-gradient(to right, #4285F4, #EA4335, #FBBC05, #34A853) 1"}),
                            dbc.CardBody(html.H3(id="mean-installs", className="fw-bold", style={"color": "#FBBC05"}), 
                                         className="d-flex align-items-center justify-content-center p-4"),
                        ], className="text-center shadow-sm border-0 rounded mb-3"),
                        md=4
                    ),
                ], className="mt-3 mb-4", justify="center"),

                dbc.Row([
                    dbc.Col(popularity_histogram, md=6),  # Moved to top-left
                    dbc.Col(make_engagement_chart, md=6)
                ]),

                dbc.Row([
                    dbc.Col(density_plot, md=6),
                    dbc.Col(wordcloud_component, md=6)  # Moved Word Cloud here
                ])
            ], md=10)
        ], className="border-top pt-3")
    ], fluid=True)
