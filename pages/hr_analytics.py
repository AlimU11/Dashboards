import dash
from dash import html

import projects
from projects.hr_analytics import layout
from utils import LayoutBuilder as lb

dash.register_page(__name__, name='HR Analytics')

layout = html.Div(
    children=[
        lb.sidebar('hr-analytics'),
        layout,
    ],
    className='page-container',
)
