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
                    html.H4(title, className='card-title', style={'text-align': 'center'}),
                    dcc.Graph(
                        figure=fig,
                        config={'displayModeBar': False},
                    ),
                    html.P(description, className='card-text', style={'margin-top': '1rem'}),
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
            style={'padding': '1rem', 'height': '28rem'},
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
    def kpi_card(title, title_size, description, title_id, description_id):
        return dbc.Card(
            dbc.CardBody(
                [
                    dbc.Spinner(
                        [
                            getattr(html, f'H{title_size}')(title, className='card-title', id=title_id),
                            html.P(
                                description,
                                className='card-text',
                                id=description_id,
                            ),
                        ],
                    ),
                ],
            ),
        )

    @staticmethod
    def graph_card(title, title_size, title_id, graph_id, config={}, controls=None):
        return dbc.Card(
            dbc.CardBody(
                [
                    getattr(html, f'H{title_size}')(title, className='card-title', id=title_id),
                    controls,
                    dbc.Spinner(
                        [
                            dcc.Graph(id=graph_id, config=config),
                        ],
                    ),
                ],
            ),
        )
