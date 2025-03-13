from dash import html
import dash_bootstrap_components as dbc

def footer_component():
    # Make footer
    footer = dbc.Row(dbc.Col([
        html.Hr(),
        html.H6('This dashboard helps advertisement companies identify the most promising Google Play Store apps for ad placements by analyzing app metrics such as user engagement and ratings',
                className="text-center fw-light mb-4",
                style={"maxWidth": "60%", "margin": "auto",
                       "whiteSpace": "normal", "wordWrap": "break-word"}
                ),
        html.P("Project by: Quanhua Huang, Yeji Sohn, Lukman Lateef, Ismail (Husain) Bhinderwala",
               className="text-center fw-light"),
        html.P(["GitHub Repository: ", html.A("Link to Repo",
                                              href="https://github.com/UBC-MDS/DSCI-532_2025_25_Ads-Analytics", target="_blank")], className="text-center"),
        html.P("Last Updated: March 2025", className="text-center fw-light"),
        html.P([html.A("Adwords icons created by Freepik - Flaticon", href="https://www.flaticon.com/free-icons/adwords",
                       title="adwords icons")], className="text-center fw-light mt-3")
    ],
        width=12,
        className="text-center mt-4")
    )

    return footer
