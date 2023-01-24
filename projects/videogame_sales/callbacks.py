from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, State, callback, ctx, html

from utils import IdHolder, app_data

genres_dict = {
    'Action': 'fa-dragon',
    'Adventure': 'fa-compass',
    'Fighting': 'fa-fist-raised',
    'Misc': 'fa-circle-question',
    'Platform': 'fa-gamepad',
    'Puzzle': 'fa-puzzle-piece',
    'Racing': 'fa-car',
    'Role-Playing': 'fa-masks-theater',
    'Shooter': 'fa-gun',
    'Simulation': 'fa-robot',
    'Sports': 'fa-futbol',
    'Strategy': 'fa-chess',
}

region_dict = {
    'Global_Sales': 'Globally',
    'NA_Sales': 'in North America',
    'EU_Sales': 'in Europe',
    'JP_Sales': 'in Japan',
    'Other_Sales': 'in other regions',
}


def update_app_data(years_range, region, top_n_publishers, top_n_games):
    app_data.videogame_sales['years_range'] = years_range or app_data.videogame_sales['years_range']
    app_data.videogame_sales['top_n_publishers'] = top_n_publishers or app_data.videogame_sales['top_n_publishers']
    app_data.videogame_sales['top_n_games'] = top_n_games or app_data.videogame_sales['top_n_games']
    app_data.videogame_sales['region'] = region or app_data.videogame_sales['region']


# TODO refactor callback, separate into smaller callbacks
# TODO add utils, make callbacks effectively empty
@callback(
    [
        # Parameters
        Output(IdHolder.vg_years_range.name, 'value'),
        Output(IdHolder.vg_region.name, 'value'),
        Output(IdHolder.vg_top_n_publishers.name, 'value'),
        Output(IdHolder.vg_top_n_games.name, 'value'),
        # Graphs
        Output(IdHolder.vg_by_publisher.name, 'figure'),
        Output(IdHolder.vg_top_games.name, 'figure'),
        Output(IdHolder.vg_by_genre.name, 'figure'),
        Output(IdHolder.vg_genre_by_year.name, 'figure'),
        Output(IdHolder.vg_genre_by_platform.name, 'figure'),
        Output(IdHolder.vg_region_platform_genre.name, 'figure'),
        Output(IdHolder.vg_rank_by_year.name, 'figure'),
        # KPIs
        Output(IdHolder.vg_sales_amount_title.name, 'children'),
        Output(IdHolder.vg_top_game_title.name, 'children'),
        Output(IdHolder.vg_top_freq_platform_title.name, 'children'),
        Output(IdHolder.vg_trending_genre_title.name, 'children'),
        # KPIs Description
        Output(IdHolder.vg_sales_amount_description.name, 'children'),
        Output(IdHolder.vg_top_game_description.name, 'children'),
        Output(IdHolder.vg_top_freq_platform_description.name, 'children'),
        Output(IdHolder.vg_trending_genre_description.name, 'children'),
        # Genre Title
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
        # Genres
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
        # Titles
        Output(IdHolder.vg_by_publisher_title.name, 'children'),
        Output(IdHolder.vg_by_genre_title.name, 'children'),
        Output(IdHolder.vg_genre_by_year_title.name, 'children'),
        Output(IdHolder.vg_genre_by_platform_title.name, 'children'),
        Output(IdHolder.vg_rank_by_year_title.name, 'children'),
        Output(IdHolder.vg_top_games_title.name, 'children'),
    ],
    [
        Input(IdHolder.vg_years_range.name, 'value'),
        Input(IdHolder.vg_region.name, 'value'),
        Input(IdHolder.vg_top_n_publishers.name, 'value'),
        Input(IdHolder.vg_top_n_games.name, 'value'),
    ],
    [
        State(IdHolder.vg_by_publisher.name, 'figure'),
        State(IdHolder.vg_top_games.name, 'figure'),
        State(IdHolder.vg_by_genre.name, 'figure'),
        State(IdHolder.vg_genre_by_year.name, 'figure'),
        State(IdHolder.vg_genre_by_platform.name, 'figure'),
        State(IdHolder.vg_region_platform_genre.name, 'figure'),
        State(IdHolder.vg_rank_by_year.name, 'figure'),
        State(IdHolder.vg_sales_amount_title.name, 'children'),
        State(IdHolder.vg_top_game_title.name, 'children'),
        State(IdHolder.vg_top_freq_platform_title.name, 'children'),
        State(IdHolder.vg_trending_genre_title.name, 'children'),
        State(IdHolder.vg_trending_genre_description.name, 'children'),
    ],
)
def videogame_sales_filter(
    v_years_range,
    v_region,
    v_top_n_publishers,
    v_top_n_games,
    g_by_publisher,
    g_top_games,
    g_by_genre,
    g_genre_by_year,
    g_genre_by_platform,
    g_region_platform_genre,
    g_rank_by_year,
    k_amount_title,
    k_top_game_title,
    k_top_freq_platform_title,
    k_trending_genre_title,
    k_trending_genre_description,
):
    update_app_data(v_years_range, v_region, v_top_n_publishers, v_top_n_games)

    df = app_data.videogame_sales['data'][
        app_data.videogame_sales['data']['Year'].between(
            *app_data.videogame_sales['years_range'],
            inclusive='both',
        )
    ]

    region = region_dict[app_data.videogame_sales['region']]

    platform = (
        update_videogame_sales_top_freq_platform(df)
        if not ctx.triggered_id
        or ctx.triggered_id == IdHolder.vg_years_range.name
        or ctx.triggered_id == IdHolder.vg_region.name
        else k_top_freq_platform_title
    )

    genre, second_max, diff_second_max, g_min, diff_min = (
        update_videogame_sales_trending_genre(df)
        if not ctx.triggered_id
        or ctx.triggered_id == IdHolder.vg_years_range.name
        or ctx.triggered_id == IdHolder.vg_region.name
        else (
            k_trending_genre_title[1]['props']['children'],
            k_trending_genre_description[3].split(' ')[-1],
            k_trending_genre_description[2]['props']['children'][1:-1],
            k_trending_genre_description[6].split(' ')[-1],
            k_trending_genre_description[5]['props']['children'][1:-1],
        )
    )

    return [
        # Parameters
        app_data.videogame_sales['years_range'],
        app_data.videogame_sales['region'],
        app_data.videogame_sales['top_n_publishers'],
        app_data.videogame_sales['top_n_games'],
        # Graphs
        (
            update_videogame_sales_by_publisher(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            or ctx.triggered_id == IdHolder.vg_top_n_publishers.name
            else g_by_publisher
        ),
        (
            update_videogame_sales_top_games(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            or ctx.triggered_id == IdHolder.vg_top_n_games.name
            else g_top_games
        ),
        (
            update_videogame_sales_by_genre(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            or ctx.triggered_id == IdHolder.vg_top_n_publishers.name
            else g_by_genre
        ),
        (
            update_videogame_sales_genre_by_year(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else g_genre_by_year
        ),
        (
            update_videogame_sales_genre_by_platform(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else g_genre_by_platform
        ),
        (
            update_videogame_sales_region_platform_genre()
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else g_region_platform_genre
        ),
        (
            update_videogame_sales_rank_by_year(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else g_rank_by_year
        ),
        # KPIs
        (
            update_videogame_sales_amount(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else k_amount_title
        ),
        (
            update_videogame_sales_top_game(df)
            if not ctx.triggered_id
            or ctx.triggered_id == IdHolder.vg_years_range.name
            or ctx.triggered_id == IdHolder.vg_region.name
            else k_top_game_title
        ),
        platform,
        (
            [
                html.I(className=f'fa-solid {genres_dict[genre]}'),
                html.Span(genre),
                html.I(className='fa-solid fa-arrow-trend-up'),
            ]
        ),
        # KPIs Description
        *update_kpi_descriptions(df, region, platform, second_max, diff_second_max, g_min, diff_min),
        # Genre Title & Genres
        *update_videogame_sales_genres(df),
        # Titles
        *update_titles(region),
    ]


def update_videogame_sales_amount(df):
    return f"""$ {df[app_data.videogame_sales['region']].sum():,.2f}M"""


def update_videogame_sales_top_game(df):
    title = df.sort_values(by=app_data.videogame_sales['region'], ascending=False)['Name'].iloc[0]
    return title  # [:12] + ('' if len(title) < 12 else '...')


def update_videogame_sales_top_freq_platform(df):
    return df.groupby('Platform')[app_data.videogame_sales['region']].sum().idxmax()


def update_videogame_sales_trending_genre(df):
    genre_sum = df.groupby('Genre')[app_data.videogame_sales['region']].sum().sort_values(ascending=False)
    genre_sum = genre_sum / genre_sum.sum() * 100

    genre = genre_sum.index[0]

    second_max = genre_sum.index[1]
    diff_second_max = genre_sum.iloc[0] - genre_sum.iloc[1]
    g_min = genre_sum.index[-1]
    diff_min = genre_sum.iloc[0] - genre_sum.iloc[-1]

    return genre, second_max, round(diff_second_max, 2), g_min, round(diff_min, 2)


def update_titles(region):
    return [
        f'Sales by Publisher over the Years {region}',
        f'Sales by Genre and Publisher {region}',
        f'Sales by Genre over the Years {region}',
        f'Sales for top {5} Platform and their top {3} Genres {region}',
        f'Sales by Rank over the Years {region}',
        f'Top {app_data.videogame_sales["top_n_games"]} Games {region}',
    ]


def update_kpi_descriptions(df, region, platform, second_max, diff_second_max, g_min, diff_min):
    return [
        [
            f'Total Sales ',
            html.Span(f'{region}', style={'color': '#00CC96', 'font-weight': 'bold'}),
            html.Br(),
            f'from ',
            html.Span(f'{df.Year.min():.0f}', style={'color': '#00CC96', 'font-weight': 'bold'}),
            f' to ',
            html.Span(f'{df.Year.max():.0f}', style={'color': '#00CC96', 'font-weight': 'bold'}),
        ],
        [
            f'(',
            html.Span(
                f'''{df.sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Genre}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            '/',
            html.Span(
                f'''{df.sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Year:.0f}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            '), ',
            html.Span(
                f'''{df.sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Publisher}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            html.Br(),
            'Has the biggest sales',
            html.Br(),
            html.Span(
                f'$ {df[app_data.videogame_sales["region"]].iloc[0]:,.2f}M',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
        ],
        [
            'Most popular platform for game developers',
            html.Br(),
            html.Span(
                f'{df[app_data.videogame_sales["region"]][df.Platform == platform].count():,}',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            ' games developed',
        ],
        [
            f'Trending Genre {region}',
            html.Br(),
            html.Span(
                f'+{diff_second_max}%',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            f' compared to {second_max}',
            html.Br(),
            html.Span(
                f'+{diff_min}%',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            f' compared to {g_min}',
        ],
    ]


def update_videogame_sales_genres(df):
    genres = df['Genre'].value_counts()

    return [[html.I(className=f'fa-solid {genres_dict[i]}'), i] for i in genres.index] + [
        html.B(f'{value:,.0f}') for value in genres.values
    ]


def update_videogame_sales_by_publisher(df):
    sales_by_publisher = df.groupby('Publisher')[app_data.videogame_sales['region']].sum().sort_values()

    top_n_publishers = sales_by_publisher[-app_data.videogame_sales['top_n_publishers'] :].index

    sales_by_year_publisher = (
        df[df['Publisher'].isin(top_n_publishers)]
        .groupby(['Year', 'Publisher'])[app_data.videogame_sales['region']]
        .sum()
        .unstack()
    )

    sales_other = df[~df['Publisher'].isin(top_n_publishers)].groupby('Year')[app_data.videogame_sales['region']].sum()

    figure = go.Figure()

    for publisher in top_n_publishers:
        figure.add_trace(
            go.Scatter(
                x=[
                    datetime.strptime(str(i), '%Y')
                    for i in range(
                        app_data.videogame_sales['years_range'][0],
                        app_data.videogame_sales['years_range'][1] + 1,
                    )
                ],
                y=sales_by_year_publisher[publisher],
                name=publisher,
                stackgroup='one',
            ),
        )

    figure.add_trace(
        go.Scatter(
            x=[
                datetime.strptime(str(i), '%Y')
                for i in range(
                    app_data.videogame_sales['years_range'][0],
                    app_data.videogame_sales['years_range'][1] + 1,
                )
            ],
            y=sales_other,
            name='Others',
            stackgroup='one',
        ),
    )

    figure.update_layout(
        yaxis=dict(
            tickprefix='$',
            ticksuffix='M',
        ),
        margin=dict(
            t=75,
            l=0,
            r=0,
            b=0,
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='left',
            x=0,
        ),
    )

    return figure


def update_videogame_sales_top_games(df):
    sales_by_game = df.groupby('Name')[app_data.videogame_sales['region']].sum().sort_values()

    top_n_games = sales_by_game[-app_data.videogame_sales['top_n_games'] :].index

    figure = go.Figure()

    for game, sales in zip(
        top_n_games,
        sales_by_game[-app_data.videogame_sales['top_n_games'] :],
    ):
        figure.add_trace(
            go.Bar(
                x=[game],
                y=[sales],
                name=game,
                text=f'${sales:,.0f}M',
                textposition='outside',
            ),
        )

    figure.update_layout(
        yaxis=dict(
            tickprefix='$',
            ticksuffix='M',
        ),
        margin=dict(
            t=25,
            l=0,
            r=0,
            b=0,
        ),
    )

    return figure


def update_videogame_sales_by_genre(df):
    sales_by_publisher = df.groupby('Publisher')[app_data.videogame_sales['region']].sum().sort_values()

    top_n_publishers = sales_by_publisher[-app_data.videogame_sales['top_n_publishers'] :].index

    sales_by_genre_publisher = pd.concat(
        [
            (
                df[df['Publisher'].isin(top_n_publishers)]
                .groupby(['Genre', 'Publisher'])[app_data.videogame_sales['region']]
                .sum()
                .unstack()
            ),
            (
                df[~df['Publisher'].isin(top_n_publishers)]
                .groupby('Genre')[app_data.videogame_sales['region']]
                .sum()
                .rename('Others')
            ),
        ],
        axis=1,
        sort=False,
    )

    sales_by_genre_publisher = sales_by_genre_publisher.div(sales_by_genre_publisher.sum(axis=1), axis=0) * 100

    figure = go.Figure()

    for publisher in sales_by_genre_publisher.columns:
        x = sales_by_genre_publisher[publisher]
        figure.add_trace(
            go.Bar(
                x=x,
                y=sales_by_genre_publisher.index,
                name=publisher,
                orientation='h',
                text=x.apply(lambda x: f'{x:.0f}%'),
            ),
        )

    figure.update_layout(
        barmode='stack',
        yaxis=dict(
            categoryorder='total ascending',
        ),
        xaxis=dict(
            range=[0, 100],
            ticksuffix='%',
        ),
        margin=dict(
            t=75,
            l=0,
            r=0,
            b=0,
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='left',
            x=-0.1,
        ),
        dragmode=False,
    )

    return figure


def update_videogame_sales_genre_by_year(df):

    sales_by_genre_year = df.groupby(['Year', 'Genre'])[app_data.videogame_sales['region']].sum().reset_index()

    figure = go.Figure(
        data=go.Scatter(
            x=sales_by_genre_year.Year,
            y=sales_by_genre_year.Genre,
            text=['$' + str(i) + 'M' for i in sales_by_genre_year[app_data.videogame_sales['region']]],
            mode='markers',
            marker=dict(
                size=sales_by_genre_year[app_data.videogame_sales['region']],
                sizemode='area',
                sizeref=2.0 * max(sales_by_genre_year[app_data.videogame_sales['region']]) / (40.0**2),
                sizemin=4,
                color=sales_by_genre_year[app_data.videogame_sales['region']],
                colorscale='Viridis',
            ),
        ),
    )

    figure.update_layout(
        margin=dict(t=25, l=25, r=25, b=25),
    )

    return figure


def update_videogame_sales_genre_by_platform(df):

    top_n_platforms = 5
    top_n_genres = 3

    top_3_genres = (
        df.groupby(['Platform', 'Genre'])[app_data.videogame_sales['region']]
        .sum()
        .reset_index()
        .sort_values(
            by=['Platform', app_data.videogame_sales['region']],
            ascending=False,
        )
        .groupby('Platform')
        .head(top_n_genres)
    )

    top_platforms = (
        df.groupby('Platform')[app_data.videogame_sales['region']].sum().sort_values().index[-top_n_platforms:]
    )

    top_genres_top_platforms = (
        df.groupby(['Platform', 'Genre'])[app_data.videogame_sales['region']]
        .sum()
        .reset_index()
        .sort_values(
            by=['Platform', app_data.videogame_sales['region']],
            ascending=False,
        )
        .groupby('Platform')
        .head(top_n_genres)
    )

    figure = go.Figure()

    for genre in top_genres_top_platforms.Genre.unique():
        x = top_genres_top_platforms[top_genres_top_platforms['Genre'] == genre][app_data.videogame_sales['region']]
        figure.add_trace(
            go.Bar(
                y=top_genres_top_platforms[
                    (top_genres_top_platforms['Genre'] == genre)
                    & (top_genres_top_platforms['Platform'].isin(top_platforms))
                ].Platform,
                x=x,
                text=x.apply(lambda x: '$' + str(round(x)) + 'M'),
                name=genre,
                orientation='h',
            ),
        )

    figure.update_layout(
        xaxis=dict(
            tickprefix='$',
            ticksuffix='M',
        ),
        margin=dict(
            t=25,
            l=25,
            r=25,
            b=25,
        ),
        barmode='stack',
        yaxis=dict(
            categoryorder='total ascending',
        ),
    )

    return figure


def update_videogame_sales_region_platform_genre():
    df = app_data.videogame_sales['data_region'][
        app_data.videogame_sales['data_region']['Year'].between(
            *app_data.videogame_sales['years_range'],
            inclusive='both',
        )
    ]

    figure = px.treemap(
        df,
        path=[px.Constant('Global Sales'), 'Region', 'Platform', 'Genre'],
        values='Sales',
    )

    figure.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        height=600,
    )

    return figure


def update_videogame_sales_rank_by_year(df):

    df = df.sort_values(by='Rank').iloc[:100]

    figure = go.Figure(
        data=go.Scatter(
            y=df.Year,
            x=df.Rank,
            text=df.Name + ' $' + df[app_data.videogame_sales['region']].astype(str) + 'M',
            hoverinfo='text',
            mode='markers',
            marker=dict(
                size=df[app_data.videogame_sales['region']],
                sizemode='area',
                sizeref=2.0 * max(df[app_data.videogame_sales['region']]) / (40.0**2),
                sizemin=4,
                color=df[app_data.videogame_sales['region']],
            ),
        ),
    )

    figure.update_layout(
        margin=dict(t=25, l=25, r=25, b=25),
    )

    return figure
