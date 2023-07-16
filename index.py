import logging
import os
from typing import Union

from dash import dcc, html
from dash.dependencies import Input, Output

from app import app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(
        id='page-content',
        style={'margin-left': '2rem', 'margin-right': '2rem', 'padding': '1rem' '1rem'}
    )
], style={'background-color': '#F7F8FE'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname'),
               Input('url', 'search')])
def display_page(pathname, query_params) -> Union[html.Div, str]:
    """ Display the page based on the URL pathname

    Args:
        pathname (str): URL pathname
        query_params (str): URL query parameters

    Returns:
        html.Div: HTML div element
    """
    # Step 1: Parse the query params
    return html.Div('Hello World')


if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8801)
