from __future__ import annotations

from typing import Sequence

import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.development.base_component import Component
from plotly.graph_objects import Figure

from .Config import config
from .IdHolder import IdHolder


class LayoutBuilder:
    @staticmethod
    def project_card(title: str, fig: Figure, description: str, button_text: str, icon: str):
        """Project card template for main page"""
        return dbc.Card(
            dbc.CardBody(
                [
                    html.H4(
                        title,
                        className='card-title',
                        style={'text-align': 'center'},
                    ),
                    dcc.Graph(
                        figure=fig,
                        config={'displayModeBar': False},
                    ),
                    html.P(
                        description,
                        className='card-text',
                        style={'margin-top': '1rem'},
                    ),
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
    def layout(
        project_class: str,
        title: str | Component | None,
        children: str | Sequence[Component],
        callback_dispatcher_id: str = IdHolder.UNDEFINED.name,
    ) -> Component:
        """Layout template for all project pages"""
        return html.Div(
            children=[
                LayoutBuilder.sidebar(project_class),
                html.Div(
                    children=[
                        dbc.Button(
                            id=callback_dispatcher_id,
                            style={'display': 'none'},
                        ),
                        title,
                        html.Div(
                            children=children,
                            className=f'main-grid main-grid--{project_class}',
                        ),
                    ],
                    className=f'main-container main-container--{project_class}',
                ),
            ],
            className='page-container',
        )

    @staticmethod
    def sidebar(project_name: str) -> Component:
        """Sidebar template for all project pages"""
        return html.Div(
            children=[
                html.A(
                    children=html.I(className='fa-solid fa-house-chimney'),
                    href='/',
                    id=IdHolder.home.name,
                ),
                *[
                    html.A(
                        children=html.I(
                            className=f'fa-solid fa-{project.icon}',
                        ),
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
    def kpi_card(
        title: str,
        title_size: int | str,
        description: str,
        title_id: str,
        description_id: str,
    ) -> Component:
        """KPI card template"""
        return dbc.Card(
            dbc.CardBody(
                [
                    dbc.Spinner(
                        [
                            getattr(html, f'H{title_size}')(
                                title,
                                className='card-title',
                                id=title_id,
                            ),
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
    def graph_card(
        graph_id: str,
        title: str | Component = '',
        title_size: int | str = 1,
        title_id: str = IdHolder.UNDEFINED.name,
        config: dict = {'displayModeBar': False},
        controls=None,
    ) -> Component:
        """Graph card template"""
        return dbc.Card(
            dbc.CardBody(
                [
                    getattr(html, f'H{title_size}')(
                        title,
                        className='card-title',
                        id=title_id,
                        style={
                            'display': 'none',
                        }
                        if title_id == IdHolder.UNDEFINED.name
                        else {},
                    ),
                    controls,
                    dbc.Spinner(
                        [
                            dcc.Graph(id=graph_id, config=config),
                        ],
                    ),
                ],
            ),
        )
