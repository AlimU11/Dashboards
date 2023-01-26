import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import IdHolder, data
from utils.LayoutBuilder import LayoutBuilder as lb

layout = lb.layout(
    project_class='videogame-sales',
    title=html.H1(
        children=[
            'Video Game Sales',
            dbc.Button(
                id=IdHolder.vg_callback_dispatcher.name,
                style={'display': 'none'},
            ),
        ],
    ),
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
                                        min=data.vg.data.Year.min(),
                                        max=data.vg.data.Year.max(),
                                        step=1,
                                        allowCross=False,
                                        pushable=1,
                                        tooltip={
                                            'placement': 'bottom',
                                            'always_visible': True,
                                        },
                                        marks={
                                            i: str(i)
                                            for i in range(
                                                int(data.vg.data.Year.min()),
                                                int(data.vg.data.Year.max()) + 1,
                                                5,
                                            )
                                        },
                                        value=[
                                            data.vg.data.Year.min(),
                                            data.vg.data.Year.max(),
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
                                            {
                                                'label': 'Europe',
                                                'value': 'EU_Sales',
                                            },
                                            {
                                                'label': 'Japan',
                                                'value': 'JP_Sales',
                                            },
                                            {
                                                'label': 'Other',
                                                'value': 'Other_Sales',
                                            },
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
                    style={
                        'position': 'sticky',
                        'top': '1rem',
                        'z-index': '1',
                    },
                ),
                html.Div(
                    children=[
                        lb.kpi_card(
                            title='$0M',
                            title_size=1,
                            description='Video Game Sales',
                            title_id=IdHolder.vg_sales_amount_title.name,
                            description_id=IdHolder.vg_sales_amount_description.name,
                        ),
                        lb.kpi_card(
                            title='None',
                            title_size=1,
                            description='$0M',
                            title_id=IdHolder.vg_top_game_title.name,
                            description_id=IdHolder.vg_top_game_description.name,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    children=[
                        lb.kpi_card(
                            title='None',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_top_freq_platform_title.name,
                            description_id=IdHolder.vg_top_freq_platform_description.name,
                        ),
                        lb.kpi_card(
                            title='None',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_trending_genre_title.name,
                            description_id=IdHolder.vg_trending_genre_description.name,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    [
                        lb.kpi_card(
                            title='Genre 1',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_1_title.name,
                            description_id=IdHolder.vg_genre_1.name,
                        ),
                        lb.kpi_card(
                            title='Genre 2',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_2_title.name,
                            description_id=IdHolder.vg_genre_2.name,
                        ),
                        lb.kpi_card(
                            title='Genre 3',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_3_title.name,
                            description_id=IdHolder.vg_genre_3.name,
                        ),
                        lb.kpi_card(
                            title='Genre 4',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_4_title.name,
                            description_id=IdHolder.vg_genre_4.name,
                        ),
                        lb.kpi_card(
                            title='Genre 5',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_5_title.name,
                            description_id=IdHolder.vg_genre_5.name,
                        ),
                        lb.kpi_card(
                            title='Genre 6',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_6_title.name,
                            description_id=IdHolder.vg_genre_6.name,
                        ),
                    ],
                    className='genre-container',
                ),
                html.Div(
                    [
                        lb.kpi_card(
                            title='Genre 7',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_7_title.name,
                            description_id=IdHolder.vg_genre_7.name,
                        ),
                        lb.kpi_card(
                            title='Genre 8',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_8_title.name,
                            description_id=IdHolder.vg_genre_8.name,
                        ),
                        lb.kpi_card(
                            title='Genre 9',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_9_title.name,
                            description_id=IdHolder.vg_genre_9.name,
                        ),
                        lb.kpi_card(
                            title='Genre 10',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_10_title.name,
                            description_id=IdHolder.vg_genre_10.name,
                        ),
                        lb.kpi_card(
                            title='Genre 11',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_11_title.name,
                            description_id=IdHolder.vg_genre_11.name,
                        ),
                        lb.kpi_card(
                            title='Genre 12',
                            title_size=1,
                            description='0',
                            title_id=IdHolder.vg_genre_12_title.name,
                            description_id=IdHolder.vg_genre_12.name,
                        ),
                    ],
                    className='genre-container',
                ),
                lb.graph_card(
                    title='Sales by Publisher over the Years',
                    title_size=4,
                    title_id=IdHolder.vg_by_publisher_title.name,
                    graph_id=IdHolder.vg_by_publisher.name,
                    config={'displayModeBar': False},
                    controls=dbc.InputGroup(
                        [
                            dbc.InputGroupText(
                                'Number of Publishers',
                            ),
                            dbc.Input(
                                type='number',
                                value=data.vg.top_n_publishers,
                                id=IdHolder.vg_top_n_publishers.name,
                            ),
                        ],
                    ),
                ),
                lb.graph_card(
                    title='Sales by Genre and Publisher',
                    title_size=4,
                    title_id=IdHolder.vg_by_genre_title.name,
                    graph_id=IdHolder.vg_by_genre.name,
                    config={'displayModeBar': False},
                ),
                lb.graph_card(
                    'Top Games',
                    title_size=4,
                    title_id=IdHolder.vg_top_games_title.name,
                    graph_id=IdHolder.vg_top_games.name,
                    config={'displayModeBar': False},
                    controls=dbc.InputGroup(
                        [
                            dbc.InputGroupText('Number of Games'),
                            dbc.Input(
                                type='number',
                                value=data.vg.top_n_games,
                                id=IdHolder.vg_top_n_games.name,
                            ),
                        ],
                    ),
                ),
                lb.graph_card(
                    title='Sales by Genre over the Years',
                    title_size=4,
                    title_id=IdHolder.vg_genre_by_year_title.name,
                    graph_id=IdHolder.vg_genre_by_year.name,
                    config={'displayModeBar': False},
                ),
                lb.graph_card(
                    title='Sales by Genre and Platform',
                    title_size=4,
                    title_id=IdHolder.vg_genre_by_platform_title.name,
                    graph_id=IdHolder.vg_genre_by_platform.name,
                    config={'displayModeBar': False},
                ),
                lb.graph_card(
                    title='Sales by Rank over the Years',
                    title_size=4,
                    title_id=IdHolder.vg_rank_by_year_title.name,
                    graph_id=IdHolder.vg_rank_by_year.name,
                    config={'displayModeBar': False},
                ),
                lb.graph_card(
                    title='Sales by Region, Platform and Genre',
                    title_size=4,
                    title_id=IdHolder.vg_region_platform_genre_title.name,
                    graph_id=IdHolder.vg_region_platform_genre.name,
                    config={'displayModeBar': False},
                ),
            ],
            className='main-grid main-grid--video-game-sales',
        ),
    ],
)
