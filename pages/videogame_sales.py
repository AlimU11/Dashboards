import dash
from dash import html

from utils import sidebar
from videogame_sales import layout

dash.register_page(__name__, name='Video Game Sales')

layout = html.Div(
    children=[
        sidebar,
        layout,
    ],
    className='page-container',
)
