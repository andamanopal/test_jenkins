import dash

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                title='Page Not Found')
server = app.server
