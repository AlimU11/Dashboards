import dash_bootstrap_components as dbc
from dash import html

from .IdHolder import IdHolder

sidebar = html.Div(
    children=[
        html.A(children=html.I(className='fa-solid fa-house-chimney'), href='/', id=IdHolder.home.name),
        html.A(
            children=html.I(className='fa-solid fa-gamepad'),
            href='/videogame-sales',
            id=IdHolder.videogame_sales.name,
        ),
        dbc.Tooltip('Home', target=IdHolder.home.name),
        dbc.Tooltip('Video Game Sales', target=IdHolder.videogame_sales.name),
    ],
    className='sidebar',
)
