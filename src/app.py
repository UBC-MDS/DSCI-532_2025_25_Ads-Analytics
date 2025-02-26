from dash import Dash, html


# Initiatlize the app
app = Dash(__name__)

# Layout
app.layout = html.Div('I am alive')

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
if __name__ == '__main__':
    app.server.run(port= 8001, host='0.0.0.0')