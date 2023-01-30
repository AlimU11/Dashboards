import pkgutil

import dash
import dash_bootstrap_components as dbc
from dash import html

import projects
from utils import LayoutBuilder as LB
from utils.Config import config

app = dash.Dash(
    __name__,
    pages_folder='',
    use_pages=True,
    external_stylesheets=[dbc.icons.FONT_AWESOME, dbc.themes.BOOTSTRAP],
)

for module in pkgutil.iter_modules(projects.__path__):
    module = getattr(projects, module.name)

    dash.register_page(
        module.__name__.replace('projects.', ''),
        layout=module.layout,
    )

dash.register_page(
    'home',
    path='/',
    redirect_from=['/index'],
    layout=html.Div(
        children=[
            html.H1(children='Dashboards'),
            html.Div(
                children=[
                    *[
                        LB.project_card(
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
        className='main-container card',
        style={'margin': '1.5rem'},
    ),
)

app.layout = dash.page_container

if __name__ == '__main__':
    app.run_server(debug=True)
