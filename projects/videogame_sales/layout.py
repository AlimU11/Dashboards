import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import IdHolder as ID
from utils import data
from utils.LayoutBuilder import LayoutBuilder as LB

layout = LB.layout(
    callback_dispatcher_id=ID.vg_callback_dispatcher,
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
                                        id=ID.vg_years_range,
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
                                        id=ID.vg_region,
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
                        LB.kpi_card(
                            title='$0M',
                            title_size=1,
                            description='Video Game Sales',
                            title_id=ID.vg_sales_amount_title,
                            description_id=ID.vg_sales_amount_description,
                        ),
                        LB.kpi_card(
                            title='None',
                            title_size=1,
                            description='$0M',
                            title_id=ID.vg_top_game_title,
                            description_id=ID.vg_top_game_description,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    children=[
                        LB.kpi_card(
                            title='None',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_top_freq_platform_title,
                            description_id=ID.vg_top_freq_platform_description,
                        ),
                        LB.kpi_card(
                            title='None',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_trending_genre_title,
                            description_id=ID.vg_trending_genre_description,
                        ),
                    ],
                    className='kpi-container',
                ),
                html.Div(
                    [
                        LB.kpi_card(
                            title='Genre 1',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_1_title,
                            description_id=ID.vg_genre_1,
                        ),
                        LB.kpi_card(
                            title='Genre 2',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_2_title,
                            description_id=ID.vg_genre_2,
                        ),
                        LB.kpi_card(
                            title='Genre 3',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_3_title,
                            description_id=ID.vg_genre_3,
                        ),
                        LB.kpi_card(
                            title='Genre 4',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_4_title,
                            description_id=ID.vg_genre_4,
                        ),
                        LB.kpi_card(
                            title='Genre 5',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_5_title,
                            description_id=ID.vg_genre_5,
                        ),
                        LB.kpi_card(
                            title='Genre 6',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_6_title,
                            description_id=ID.vg_genre_6,
                        ),
                    ],
                    className='genre-container',
                ),
                html.Div(
                    [
                        LB.kpi_card(
                            title='Genre 7',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_7_title,
                            description_id=ID.vg_genre_7,
                        ),
                        LB.kpi_card(
                            title='Genre 8',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_8_title,
                            description_id=ID.vg_genre_8,
                        ),
                        LB.kpi_card(
                            title='Genre 9',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_9_title,
                            description_id=ID.vg_genre_9,
                        ),
                        LB.kpi_card(
                            title='Genre 10',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_10_title,
                            description_id=ID.vg_genre_10,
                        ),
                        LB.kpi_card(
                            title='Genre 11',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_11_title,
                            description_id=ID.vg_genre_11,
                        ),
                        LB.kpi_card(
                            title='Genre 12',
                            title_size=1,
                            description='0',
                            title_id=ID.vg_genre_12_title,
                            description_id=ID.vg_genre_12,
                        ),
                    ],
                    className='genre-container',
                ),
                LB.graph_card(
                    title='Sales by Publisher over the Years',
                    title_size=4,
                    title_id=ID.vg_by_publisher_title,
                    graph_id=ID.vg_by_publisher,
                    controls=dbc.InputGroup(
                        [
                            dbc.InputGroupText(
                                'Number of Publishers',
                            ),
                            dbc.Input(
                                type='number',
                                value=data.vg.top_n_publishers,
                                id=ID.vg_top_n_publishers,
                            ),
                        ],
                    ),
                ),
                LB.graph_card(
                    title='Sales by Genre and Publisher',
                    title_size=4,
                    title_id=ID.vg_by_genre_title,
                    graph_id=ID.vg_by_genre,
                ),
                LB.graph_card(
                    title='Top Games',
                    title_size=4,
                    title_id=ID.vg_top_games_title,
                    graph_id=ID.vg_top_games,
                    controls=dbc.InputGroup(
                        [
                            dbc.InputGroupText('Number of Games'),
                            dbc.Input(
                                type='number',
                                value=data.vg.top_n_games,
                                id=ID.vg_top_n_games,
                            ),
                        ],
                    ),
                ),
                LB.graph_card(
                    title='Sales by Genre over the Years',
                    title_size=4,
                    title_id=ID.vg_genre_by_year_title,
                    graph_id=ID.vg_genre_by_year,
                ),
                LB.graph_card(
                    title='Sales by Genre and Platform',
                    title_size=4,
                    title_id=ID.vg_genre_by_platform_title,
                    graph_id=ID.vg_genre_by_platform,
                ),
                LB.graph_card(
                    title='Sales by Rank over the Years',
                    title_size=4,
                    title_id=ID.vg_rank_by_year_title,
                    graph_id=ID.vg_rank_by_year,
                ),
                LB.graph_card(
                    title='Sales by Region, Platform and Genre',
                    title_size=4,
                    title_id=ID.vg_region_platform_genre_title,
                    graph_id=ID.vg_region_platform_genre,
                ),
            ],
            className='main-grid main-grid--video-game-sales',
        ),
    ],
)
