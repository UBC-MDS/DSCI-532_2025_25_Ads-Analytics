from dash import Dash, html


# Initiatlize the app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div('I am alive')

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == "__main__":
    app.run(debug=False)
