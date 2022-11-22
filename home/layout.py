import dash_bootstrap_components as dbc
from dash import html

layout = html.Div(
    children=[
        html.H1(children='This is our Home page'),
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Video Game Sales', className='card-title'),
                            html.P('This is some card text', className='card-text'),
                            dbc.Button('Explore', href='/videogame-sales', color='primary'),
                        ],
                    ),
                ),
            ],
            className='projects-container',
        ),
    ],
    className='main-container',
    style={'margin': '1.5rem'},
)
