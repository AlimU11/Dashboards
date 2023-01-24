import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import IdHolder, app_data
from utils.LayoutBuilder import LayoutBuilder as lb

layout = lb.layout(
    project_class='videogame-sales',
    title=html.H1('Video Game Sales'),
    children=[
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4('Filters', className='card-title'),
                            dbc.InputGroup(
                                [
                                    html.Label('Years'),
                                    dcc.RangeSlider(
                                        id=IdHolder.vg_years_range.name,
                                        min=app_data.videogame_sales['data'].Year.min(),
                                        max=app_data.videogame_sales['data'].Year.max(),
                                        step=1,
                                        allowCross=False,
                                        pushable=1,
                                        updatemode='drag',
                                        tooltip={
                                            'placement': 'bottom',
                                            'always_visible': True,
                                        },
                                        marks={
                                            i: str(i)
                                            for i in range(
                                                int(
                                                    app_data.videogame_sales['data'].Year.min(),
                                                ),
                                                int(
                                                    app_data.videogame_sales['data'].Year.max(),
                                                )
                                                + 1,
                                                5,
                                            )
                                        },
                                        value=[
                                            app_data.videogame_sales['data'].Year.min(),
                                            app_data.videogame_sales['data'].Year.max(),
                                        ],
                                    ),
                                ],
                            ),
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupText('Region'),
                                    dcc.Dropdown(
                                        options=[
                                            {
                                                'label': 'North America',
                                                'value': 'NA_Sales',
                                            },
                                            {'label': 'Europe', 'value': 'EU_Sales'},
                                            {'label': 'Japan', 'value': 'JP_Sales'},
                                            {'label': 'Other', 'value': 'Other_Sales'},
                                            {
                                                'label': 'Global',
                                                'value': 'Global_Sales',
                                            },
                                        ],
                                        value='Global_Sales',
                                        clearable=False,
                                        id=IdHolder.vg_region.name,
                                    ),
                                ],
                            ),
                        ],
                        class_name='filter-container',
                    ),
                    style={'position': 'sticky', 'top': '1rem', 'z-index': '1'},
                ),
                html.Div(
                    children=[
                        lb.kpi_card(
                            '$0M',
                            1,
                            'Video Game Sales',
                            IdHolder.vg_sales_amount_title.name,
                            IdHolder.vg_sales_amount_description.name,
                        ),
                        lb.kpi_card(
                            'None',
                            1,
                            '$0M',
                            IdHolder.vg_top_game_title.name,
                            IdHolder.vg_top_game_description.name,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    children=[
                        lb.kpi_card(
                            'None',
                            1,
                            '0',
                            IdHolder.vg_top_freq_platform_title.name,
                            IdHolder.vg_top_freq_platform_description.name,
                        ),
                        lb.kpi_card(
                            'None',
                            1,
                            '0',
                            IdHolder.vg_trending_genre_title.name,
                            IdHolder.vg_trending_genre_description.name,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    [
                        lb.kpi_card(
                            'Genre 1',
                            1,
                            '0',
                            IdHolder.vg_genre_1_title.name,
                            IdHolder.vg_genre_1.name,
                        ),
                        lb.kpi_card(
                            'Genre 2',
                            1,
                            '0',
                            IdHolder.vg_genre_2_title.name,
                            IdHolder.vg_genre_2.name,
                        ),
                        lb.kpi_card(
                            'Genre 3',
                            1,
                            '0',
                            IdHolder.vg_genre_3_title.name,
                            IdHolder.vg_genre_3.name,
                        ),
                        lb.kpi_card(
                            'Genre 4',
                            1,
                            '0',
                            IdHolder.vg_genre_4_title.name,
                            IdHolder.vg_genre_4.name,
                        ),
                        lb.kpi_card(
                            'Genre 5',
                            1,
                            '0',
                            IdHolder.vg_genre_5_title.name,
                            IdHolder.vg_genre_5.name,
                        ),
                        lb.kpi_card(
                            'Genre 6',
                            1,
                            '0',
                            IdHolder.vg_genre_6_title.name,
                            IdHolder.vg_genre_6.name,
                        ),
                    ],
                    className='genre-container',
                ),
                html.Div(
                    [
                        lb.kpi_card(
                            'Genre 7',
                            1,
                            '0',
                            IdHolder.vg_genre_7_title.name,
                            IdHolder.vg_genre_7.name,
                        ),
                        lb.kpi_card(
                            'Genre 8',
                            1,
                            '0',
                            IdHolder.vg_genre_8_title.name,
                            IdHolder.vg_genre_8.name,
                        ),
                        lb.kpi_card(
                            'Genre 9',
                            1,
                            '0',
                            IdHolder.vg_genre_9_title.name,
                            IdHolder.vg_genre_9.name,
                        ),
                        lb.kpi_card(
                            'Genre 10',
                            1,
                            '0',
                            IdHolder.vg_genre_10_title.name,
                            IdHolder.vg_genre_10.name,
                        ),
                        lb.kpi_card(
                            'Genre 11',
                            1,
                            '0',
                            IdHolder.vg_genre_11_title.name,
                            IdHolder.vg_genre_11.name,
                        ),
                        lb.kpi_card(
                            'Genre 12',
                            1,
                            '0',
                            IdHolder.vg_genre_12_title.name,
                            IdHolder.vg_genre_12.name,
                        ),
                    ],
                    className='genre-container',
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                'Sales by Publisher over the Years',
                                className='card-title',
                                id=IdHolder.vg_by_publisher_title.name,
                            ),
                            dbc.Spinner(
                                [
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupText('Number of Publishers'),
                                            dbc.Input(
                                                type='number',
                                                value=app_data.videogame_sales['top_n_publishers'],
                                                id=IdHolder.vg_top_n_publishers.name,
                                            ),
                                        ],
                                    ),
                                    dcc.Graph(
                                        id=IdHolder.vg_by_publisher.name,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                lb.graph_card(
                    'Sales by Genre and Publisher',
                    IdHolder.vg_by_genre_title.name,
                    IdHolder.vg_by_genre.name,
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                'Top Games by Sales',
                                className='card-title',
                                id=IdHolder.vg_top_games_title.name,
                            ),
                            dbc.Spinner(
                                [
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupText('Number of Games'),
                                            dbc.Input(
                                                type='number',
                                                value=app_data.videogame_sales['top_n_games'],
                                                id=IdHolder.vg_top_n_games.name,
                                            ),
                                        ],
                                    ),
                                    dcc.Graph(
                                        id=IdHolder.vg_top_games.name,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                lb.graph_card(
                    'Sales by Genre over the Years',
                    IdHolder.vg_genre_by_year_title.name,
                    IdHolder.vg_genre_by_year.name,
                ),
                lb.graph_card(
                    'Sales by Genre and Platform',
                    IdHolder.vg_genre_by_platform_title.name,
                    IdHolder.vg_genre_by_platform.name,
                ),
                lb.graph_card(
                    'Sales by Rank over the Years',
                    IdHolder.vg_rank_by_year_title.name,
                    IdHolder.vg_rank_by_year.name,
                ),
                lb.graph_card(
                    'Sales by Region, Platform and Genre',
                    IdHolder.vg_region_platform_genre_title.name,
                    IdHolder.vg_region_platform_genre.name,
                ),
            ],
            className='main-grid main-grid--video-game-sales',
        ),
    ],
)
