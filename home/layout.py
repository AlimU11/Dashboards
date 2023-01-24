import dash_bootstrap_components as dbc
from dash import html

from utils.Config import config
from utils.LayoutBuilder import LayoutBuilder as lb
from utils.PreviewGraphs import preview_graphs as pg

layout = html.Div(
    children=[
        html.H1(children='This is our Home page'),
        html.Div(
            children=[
                *[
                    lb.project_card(
                        title=project.name,
                        fig=project.fig,
                        description=project.description,
                        button_text=project.button_text,
                        icon=project.icon,
                    )
                    for project in config.projects
                ],
            ],
            className='projects-container',
        ),
    ],
    className='main-container',
    style={'margin': '1.5rem'},
)
