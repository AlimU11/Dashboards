from dash import Input, Output, State, callback, html

from utils import IdHolder as ID
from utils import data

from .utils import (
    get_genres,
    get_kpi_descriptions,
    get_sales_amount,
    get_titles,
    get_top_freq_platform,
    get_top_game,
    get_trending_genre,
    plot_by_genre,
    plot_genre_by_platform,
    plot_genre_by_year,
    plot_rank_by_year,
    plot_region_platform_genre,
    plot_sales_by_publisher,
    plot_top_games,
    update_app_data,
)


@callback(
    Output(ID.vg_callback_dispatcher, 'n_clicks'),
    [
        Input(ID.vg_callback_dispatcher, 'n_clicks'),
        Input(ID.vg_years_range, 'value'),
        Input(ID.vg_region, 'value'),
    ],
    [
        State(ID.vg_top_n_games, 'value'),
        State(ID.vg_top_n_publishers, 'value'),
    ],
)
def dispatcher(_, years_range, region, top_n_games, top_n_publishers):
    update_app_data(years_range=years_range, region=region, top_n_games=top_n_games, top_n_publishers=top_n_publishers)
    return _


@callback(
    Output(ID.vg_by_publisher, 'figure'),
    [
        Input(ID.vg_callback_dispatcher, 'n_clicks'),
        Input(ID.vg_top_n_publishers, 'value'),
    ],
)
def update_by_publisher(_, top_n_publishers):
    update_app_data(top_n_publishers=top_n_publishers)
    return plot_sales_by_publisher()


@callback(
    Output(ID.vg_top_games, 'figure'),
    [
        Input(ID.vg_callback_dispatcher, 'n_clicks'),
        Input(ID.vg_top_n_games, 'value'),
    ],
)
def update_top_games(_, top_n_games):
    update_app_data(top_n_games=top_n_games)
    return plot_top_games(data.vg.ranged_data)


@callback(
    Output(ID.vg_by_genre, 'figure'),
    [
        Input(ID.vg_callback_dispatcher, 'n_clicks'),
        Input(ID.vg_top_n_publishers, 'value'),
    ],
)
def update_by_genre(_, top_n_publishers):
    update_app_data(top_n_publishers=top_n_publishers)
    return plot_by_genre()


@callback(
    Output(ID.vg_genre_by_year, 'figure'),
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_genre_by_year(_):
    return plot_genre_by_year()


@callback(
    Output(ID.vg_genre_by_platform, 'figure'),
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_genre_by_platform(_):
    return plot_genre_by_platform()


@callback(
    Output(ID.vg_region_platform_genre, 'figure'),
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_region_platform_genre(_):
    return plot_region_platform_genre()


@callback(
    Output(ID.vg_rank_by_year, 'figure'),
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_rank_by_year(_):
    return plot_rank_by_year()


@callback(
    [
        Output(ID.vg_sales_amount_title, 'children'),
        Output(ID.vg_top_game_title, 'children'),
        Output(ID.vg_top_freq_platform_title, 'children'),
        Output(ID.vg_trending_genre_title, 'children'),
        Output(ID.vg_sales_amount_description, 'children'),
        Output(ID.vg_top_game_description, 'children'),
        Output(ID.vg_top_freq_platform_description, 'children'),
        Output(ID.vg_trending_genre_description, 'children'),
    ],
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
    [
        State(ID.vg_top_game_title, 'children'),
        State(ID.vg_top_freq_platform_title, 'children'),
        State(ID.vg_trending_genre_title, 'children'),
        State(ID.vg_trending_genre_description, 'children'),
    ],
)
def update_kpi(_, __, ___, ____, _____):
    region = getattr(data.vg.Region, data.vg.region.lower())

    platform = get_top_freq_platform()

    genre, second_max, diff_second_max, g_min, diff_min = get_trending_genre()

    return [
        get_sales_amount(),
        get_top_game(),
        platform,
        (
            [
                html.I(className=f'''fa-solid {getattr(data.vg.Genre, str(genre).lower().replace('-', '_'))}'''),
                html.Span(genre),
                html.I(className='fa-solid fa-arrow-trend-up'),
            ]
        ),
        *get_kpi_descriptions(
            region,
            platform,
            second_max,
            diff_second_max,
            g_min,
            diff_min,
        ),
    ]


@callback(
    [
        Output(ID.vg_genre_1_title, 'children'),
        Output(ID.vg_genre_2_title, 'children'),
        Output(ID.vg_genre_3_title, 'children'),
        Output(ID.vg_genre_4_title, 'children'),
        Output(ID.vg_genre_5_title, 'children'),
        Output(ID.vg_genre_6_title, 'children'),
        Output(ID.vg_genre_7_title, 'children'),
        Output(ID.vg_genre_8_title, 'children'),
        Output(ID.vg_genre_9_title, 'children'),
        Output(ID.vg_genre_10_title, 'children'),
        Output(ID.vg_genre_11_title, 'children'),
        Output(ID.vg_genre_12_title, 'children'),
        Output(ID.vg_genre_1, 'children'),
        Output(ID.vg_genre_2, 'children'),
        Output(ID.vg_genre_3, 'children'),
        Output(ID.vg_genre_4, 'children'),
        Output(ID.vg_genre_5, 'children'),
        Output(ID.vg_genre_6, 'children'),
        Output(ID.vg_genre_7, 'children'),
        Output(ID.vg_genre_8, 'children'),
        Output(ID.vg_genre_9, 'children'),
        Output(ID.vg_genre_10, 'children'),
        Output(ID.vg_genre_11, 'children'),
        Output(ID.vg_genre_12, 'children'),
    ],
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_genres(_):
    return get_genres()


@callback(
    [
        Output(ID.vg_by_publisher_title, 'children'),
        Output(ID.vg_by_genre_title, 'children'),
        Output(ID.vg_genre_by_year_title, 'children'),
        Output(ID.vg_genre_by_platform_title, 'children'),
        Output(ID.vg_rank_by_year_title, 'children'),
        Output(ID.vg_top_games_title, 'children'),
    ],
    Input(ID.vg_callback_dispatcher, 'n_clicks'),
)
def update_titles(_):
    region = getattr(data.vg.Region, data.vg.region.lower())

    return get_titles(region)
