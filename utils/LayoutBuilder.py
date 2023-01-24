import dash_bootstrap_components as dbc
from dash import dcc, html

from .Config import config
from .IdHolder import IdHolder


class LayoutBuilder:
    @staticmethod
    def project_card(title, fig, description, button_text, icon):
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(title, className='card-title'),
                    dcc.Graph(
                        figure=fig,
                    ),
                    html.P(description, className='card-text'),
                    dbc.Button(
                        children=[
                            html.I(
                                className=f'fa-solid fa-{icon}',
                                style={'margin-right': '0.5rem'},
                            ),
                            button_text,
                        ],
                        href=f'/{title.lower().replace(" ", "-")}',
                        color='primary',
                        size='lg',
                        style={'width': '100%'},
                    ),
                ],
            ),
            # TODO: move style to css
            style={'padding': '1rem', 'height': '26rem'},
        )

    @staticmethod
    def layout(project_class, title, children):
        return html.Div(
            children=[
                title,
                html.Div(
                    children=children,
                    className=f'main-grid main-grid--{project_class}',
                ),
            ],
            className=f'main-container main-container--{project_class}',
        )

    @staticmethod
    def sidebar(project_name):
        return html.Div(
            children=[
                html.A(
                    children=html.I(className='fa-solid fa-house-chimney'),
                    href='/',
                    id=IdHolder.home.name,
                ),
                *[
                    html.A(
                        children=html.I(className=f'fa-solid fa-{project.icon}'),
                        href=f'/{project.name.lower().replace(" ", "-")}',
                        id=getattr(
                            IdHolder,
                            project.name.lower().replace(' ', '_'),
                        ).name,
                    )
                    for project in config.projects
                ],
                dbc.Tooltip('Home', target=IdHolder.home.name),
                *[
                    dbc.Tooltip(
                        project.name,
                        target=getattr(
                            IdHolder,
                            project.name.lower().replace(' ', '_'),
                        ).name,
                    )
                    for project in config.projects
                ],
            ],
            className=f'sidebar sidebar--{project_name}',
        )

    @staticmethod
    def kpi_card(title, size, description, id_title, id_description):
        return dbc.Card(
            dbc.CardBody(
                [
                    dbc.Spinner(
                        [
                            getattr(html, f'H{size}')(title, className='card-title', id=id_title),
                            html.P(
                                description,
                                className='card-text',
                                id=id_description,
                            ),
                        ],
                    ),
                ],
            ),
        )

    @staticmethod
    def graph_card(title, id_title, id_graph, config={}):
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(title, className='card-title', id=id_title),
                    dbc.Spinner(
                        [
                            dcc.Graph(id=id_graph, config=config),
                        ],
                    ),
                ],
            ),
        )
