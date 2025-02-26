from dash import Dash, html


# Initiatlize the app
app = Dash()
server = app.server

# Layout
app.layout = html.Div('I am alive')

# Server side callbacks/reactivity
# ...

# Run the app/dashboard
app.run()