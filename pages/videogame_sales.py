import dash
from dash import html

from projects.videogame_sales import layout
from utils import LayoutBuilder as lb

dash.register_page(__name__, name='Video Game Sales')

layout = html.Div(
    children=[
        lb.sidebar('videogame-sales'),
        layout,
    ],
    className='page-container',
)
