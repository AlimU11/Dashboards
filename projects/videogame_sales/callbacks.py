from dash import Input, Output, State, callback, html

from utils import IdHolder, data

from .utils import (
    genres_dict,
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
    region_dict,
    update_app_data,
)


@callback(
    Output(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
    [
        Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.vg_years_range.name, 'value'),
        Input(IdHolder.vg_region.name, 'value'),
    ],
    [
        State(IdHolder.vg_top_n_games.name, 'value'),
        State(IdHolder.vg_top_n_publishers.name, 'value'),
    ],
)
def dispatcher(_, years_range, region, top_n_games, top_n_publishers):
    update_app_data(years_range=years_range, region=region, top_n_games=top_n_games, top_n_publishers=top_n_publishers)
    return _


@callback(
    Output(IdHolder.vg_by_publisher.name, 'figure'),
    [
        Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.vg_top_n_publishers.name, 'value'),
    ],
)
def update_by_publisher(_, top_n_publishers):
    update_app_data(top_n_publishers=top_n_publishers)
    return plot_sales_by_publisher()


@callback(
    Output(IdHolder.vg_top_games.name, 'figure'),
    [
        Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.vg_top_n_games.name, 'value'),
    ],
)
def update_top_games(_, top_n_games):
    update_app_data(top_n_games=top_n_games)
    return plot_top_games(data.vg.ranged_data)


@callback(
    Output(IdHolder.vg_by_genre.name, 'figure'),
    [
        Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.vg_top_n_publishers.name, 'value'),
    ],
)
def update_by_genre(_, top_n_publishers):
    update_app_data(top_n_publishers=top_n_publishers)
    return plot_by_genre()


@callback(
    Output(IdHolder.vg_genre_by_year.name, 'figure'),
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_genre_by_year(_):
    return plot_genre_by_year()


@callback(
    Output(IdHolder.vg_genre_by_platform.name, 'figure'),
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_genre_by_platform(_):
    return plot_genre_by_platform()


@callback(
    Output(IdHolder.vg_region_platform_genre.name, 'figure'),
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_region_platform_genre(_):
    return plot_region_platform_genre()


@callback(
    Output(IdHolder.vg_rank_by_year.name, 'figure'),
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_rank_by_year(_):
    return plot_rank_by_year()


@callback(
    [
        Output(IdHolder.vg_sales_amount_title.name, 'children'),
        Output(IdHolder.vg_top_game_title.name, 'children'),
        Output(IdHolder.vg_top_freq_platform_title.name, 'children'),
        Output(IdHolder.vg_trending_genre_title.name, 'children'),
        Output(IdHolder.vg_sales_amount_description.name, 'children'),
        Output(IdHolder.vg_top_game_description.name, 'children'),
        Output(IdHolder.vg_top_freq_platform_description.name, 'children'),
        Output(IdHolder.vg_trending_genre_description.name, 'children'),
    ],
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
    [
        State(IdHolder.vg_top_game_title.name, 'children'),
        State(IdHolder.vg_top_freq_platform_title.name, 'children'),
        State(IdHolder.vg_trending_genre_title.name, 'children'),
        State(IdHolder.vg_trending_genre_description.name, 'children'),
    ],
)
def update_kpi(_, __, ___, ____, _____):
    region = region_dict[data.vg.region]

    platform = get_top_freq_platform()

    genre, second_max, diff_second_max, g_min, diff_min = get_trending_genre()

    return [
        get_sales_amount(),
        get_top_game(),
        platform,
        (
            [
                html.I(className=f'fa-solid {genres_dict[genre]}'),
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
        Output(IdHolder.vg_genre_1_title.name, 'children'),
        Output(IdHolder.vg_genre_2_title.name, 'children'),
        Output(IdHolder.vg_genre_3_title.name, 'children'),
        Output(IdHolder.vg_genre_4_title.name, 'children'),
        Output(IdHolder.vg_genre_5_title.name, 'children'),
        Output(IdHolder.vg_genre_6_title.name, 'children'),
        Output(IdHolder.vg_genre_7_title.name, 'children'),
        Output(IdHolder.vg_genre_8_title.name, 'children'),
        Output(IdHolder.vg_genre_9_title.name, 'children'),
        Output(IdHolder.vg_genre_10_title.name, 'children'),
        Output(IdHolder.vg_genre_11_title.name, 'children'),
        Output(IdHolder.vg_genre_12_title.name, 'children'),
        Output(IdHolder.vg_genre_1.name, 'children'),
        Output(IdHolder.vg_genre_2.name, 'children'),
        Output(IdHolder.vg_genre_3.name, 'children'),
        Output(IdHolder.vg_genre_4.name, 'children'),
        Output(IdHolder.vg_genre_5.name, 'children'),
        Output(IdHolder.vg_genre_6.name, 'children'),
        Output(IdHolder.vg_genre_7.name, 'children'),
        Output(IdHolder.vg_genre_8.name, 'children'),
        Output(IdHolder.vg_genre_9.name, 'children'),
        Output(IdHolder.vg_genre_10.name, 'children'),
        Output(IdHolder.vg_genre_11.name, 'children'),
        Output(IdHolder.vg_genre_12.name, 'children'),
    ],
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_genres(_):
    return get_genres()


@callback(
    [
        Output(IdHolder.vg_by_publisher_title.name, 'children'),
        Output(IdHolder.vg_by_genre_title.name, 'children'),
        Output(IdHolder.vg_genre_by_year_title.name, 'children'),
        Output(IdHolder.vg_genre_by_platform_title.name, 'children'),
        Output(IdHolder.vg_rank_by_year_title.name, 'children'),
        Output(IdHolder.vg_top_games_title.name, 'children'),
    ],
    Input(IdHolder.vg_callback_dispatcher.name, 'n_clicks'),
)
def update_titles(_):
    region = region_dict[data.vg.region]

    return get_titles(region)
