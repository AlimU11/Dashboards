from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import html

from utils.AppData import app_data

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


def update_app_data(years_range=None, region=None, top_n_publishers=None, top_n_games=None):
    app_data.videogame_sales['years_range'] = years_range or app_data.videogame_sales['years_range']
    app_data.videogame_sales['top_n_publishers'] = top_n_publishers or app_data.videogame_sales['top_n_publishers']
    app_data.videogame_sales['top_n_games'] = top_n_games or app_data.videogame_sales['top_n_games']
    app_data.videogame_sales['region'] = region or app_data.videogame_sales['region']
    app_data.videogame_sales['ranged_data'] = app_data.videogame_sales['data'][
        app_data.videogame_sales['data']['Year'].between(
            *app_data.videogame_sales['years_range'],
            inclusive='both',
        )
    ]


def get_sales_amount():
    return f'''$ {app_data.videogame_sales['ranged_data'][app_data.videogame_sales['region']].sum():,.2f}M'''


def get_top_game():
    title = (
        app_data.videogame_sales['ranged_data']
        .sort_values(by=app_data.videogame_sales['region'], ascending=False)['Name']
        .iloc[0]
    )
    return title  # [:12] + ('' if len(title) < 12 else '...')


def get_top_freq_platform():
    return (
        app_data.videogame_sales['ranged_data'].groupby('Platform')[app_data.videogame_sales['region']].sum().idxmax()
    )


def get_trending_genre():
    genre_sum = (
        app_data.videogame_sales['ranged_data']
        .groupby(
            'Genre',
        )[app_data.videogame_sales['region']]
        .sum()
        .sort_values(ascending=False)
    )
    genre_sum = genre_sum / genre_sum.sum() * 100

    genre = genre_sum.index[0]

    second_max = genre_sum.index[1]
    diff_second_max = genre_sum.iloc[0] - genre_sum.iloc[1]
    g_min = genre_sum.index[-1]
    diff_min = genre_sum.iloc[0] - genre_sum.iloc[-1]

    return genre, second_max, round(diff_second_max, 2), g_min, round(diff_min, 2)


def get_titles(region):
    return [
        f'Sales by Publisher over the Years {region}',
        f'Sales by Genre and Publisher {region}',
        f'Sales by Genre over the Years {region}',
        f'Sales for top {5} Platform and their top {3} Genres {region}',
        f'Sales by Rank over the Years {region}',
        f'Top {app_data.videogame_sales["top_n_games"]} Games {region}',
    ]


def get_kpi_descriptions(region, platform, second_max, diff_second_max, g_min, diff_min):
    return [
        [
            f'Total Sales ',
            html.Span(
                f'{region}',
                style={
                    'color': '#00CC96',
                    'font-weight': 'bold',
                },
            ),
            html.Br(),
            f'from ',
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'].Year.min():.0f}''',
                style={
                    'color': '#00CC96',
                    'font-weight': 'bold',
                },
            ),
            f' to ',
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'].Year.max():.0f}''',
                style={
                    'color': '#00CC96',
                    'font-weight': 'bold',
                },
            ),
        ],
        [
            f'(',
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'].sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Genre}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            '/',
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'].sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Year:.0f}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            '), ',
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'].sort_values(by=app_data.videogame_sales['region'], ascending=False).iloc[0].Publisher}''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
            html.Br(),
            'Has the biggest sales',
            html.Br(),
            html.Span(
                f'''$ {app_data.videogame_sales['ranged_data'][app_data.videogame_sales['region']].iloc[0]:,.2f}M''',
                style={'color': '#00CC96', 'font-weight': 'bold'},
            ),
        ],
        [
            'Most popular platform for game developers',
            html.Br(),
            html.Span(
                f'''{app_data.videogame_sales['ranged_data'][app_data.videogame_sales['region']][app_data.videogame_sales['ranged_data'].Platform == platform].count():,}''',
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


def get_genres():
    genres = app_data.videogame_sales['ranged_data']['Genre'].value_counts()

    return [[html.I(className=f'fa-solid {genres_dict[i]}'), i] for i in genres.index] + [
        html.B(f'{value:,.0f}') for value in genres.values
    ]


def plot_sales_by_publisher():
    sales_by_publisher = (
        app_data.videogame_sales['ranged_data']
        .groupby(
            'Publisher',
        )[app_data.videogame_sales['region']]
        .sum()
        .sort_values()
    )

    top_n_publishers = sales_by_publisher[-app_data.videogame_sales['top_n_publishers'] :].index

    sales_by_year_publisher = (
        app_data.videogame_sales['ranged_data'][
            app_data.videogame_sales['ranged_data']['Publisher'].isin(top_n_publishers)
        ]
        .groupby(['Year', 'Publisher'])[app_data.videogame_sales['region']]
        .sum()
        .unstack()
    )

    sales_other = (
        app_data.videogame_sales['ranged_data'][
            ~app_data.videogame_sales['ranged_data']['Publisher'].isin(top_n_publishers)
        ]
        .groupby('Year')[app_data.videogame_sales['region']]
        .sum()
    )

    fig = go.Figure()

    for publisher in top_n_publishers:
        fig.add_trace(
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

    fig.add_trace(
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

    fig.update_layout(
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

    return fig


def plot_top_games(df):
    sales_by_game = (
        df.groupby(
            'Name',
        )[app_data.videogame_sales['region']]
        .sum()
        .sort_values()
    )

    top_n_games = sales_by_game[-app_data.videogame_sales['top_n_games'] :].index

    fig = go.Figure()

    for game, sales in zip(
        top_n_games,
        sales_by_game[-app_data.videogame_sales['top_n_games'] :],
    ):
        fig.add_trace(
            go.Bar(
                x=[game],
                y=[sales],
                name=game,
                text=f'${sales:,.0f}M',
                textposition='outside',
            ),
        )

    fig.update_layout(
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

    return fig


def plot_by_genre():
    sales_by_publisher = (
        app_data.videogame_sales['ranged_data']
        .groupby(
            'Publisher',
        )[app_data.videogame_sales['region']]
        .sum()
        .sort_values()
    )

    top_n_publishers = sales_by_publisher[-app_data.videogame_sales['top_n_publishers'] :].index

    sales_by_genre_publisher = pd.concat(
        [
            (
                app_data.videogame_sales['ranged_data'][
                    app_data.videogame_sales['ranged_data']['Publisher'].isin(top_n_publishers)
                ]
                .groupby(['Genre', 'Publisher'])[app_data.videogame_sales['region']]
                .sum()
                .unstack()
            ),
            (
                app_data.videogame_sales['ranged_data'][
                    ~app_data.videogame_sales['ranged_data']['Publisher'].isin(top_n_publishers)
                ]
                .groupby('Genre')[app_data.videogame_sales['region']]
                .sum()
                .rename('Others')
            ),
        ],
        axis=1,
        sort=False,
    )

    sales_by_genre_publisher = (
        sales_by_genre_publisher.div(
            sales_by_genre_publisher.sum(axis=1),
            axis=0,
        )
        * 100
    )

    fig = go.Figure()

    for publisher in sales_by_genre_publisher.columns:
        x = sales_by_genre_publisher[publisher]
        fig.add_trace(
            go.Bar(
                x=x,
                y=sales_by_genre_publisher.index,
                name=publisher,
                orientation='h',
                text=x.apply(lambda x: f'{x:.0f}%'),
            ),
        )

    fig.update_layout(
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

    return fig


def plot_genre_by_year():
    sales_by_genre_year = (
        app_data.videogame_sales['ranged_data']
        .groupby(['Year', 'Genre'])[app_data.videogame_sales['region']]
        .sum()
        .reset_index()
    )

    fig = go.Figure(
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

    fig.update_layout(
        margin=dict(t=25, l=25, r=25, b=25),
    )

    return fig


def plot_genre_by_platform():
    top_n_platforms = 5
    top_n_genres = 3

    top_3_genres = (
        app_data.videogame_sales['ranged_data']
        .groupby(['Platform', 'Genre'])[app_data.videogame_sales['region']]
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
        app_data.videogame_sales['ranged_data']
        .groupby('Platform')[app_data.videogame_sales['region']]
        .sum()
        .sort_values()
        .index[-top_n_platforms:]
    )

    top_genres_top_platforms = (
        app_data.videogame_sales['ranged_data']
        .groupby(['Platform', 'Genre'])[app_data.videogame_sales['region']]
        .sum()
        .reset_index()
        .sort_values(
            by=['Platform', app_data.videogame_sales['region']],
            ascending=False,
        )
        .groupby('Platform')
        .head(top_n_genres)
    )

    fig = go.Figure()

    for genre in top_genres_top_platforms.Genre.unique():
        x = top_genres_top_platforms[top_genres_top_platforms['Genre'] == genre][app_data.videogame_sales['region']]
        fig.add_trace(
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

    fig.update_layout(
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

    return fig


def plot_region_platform_genre():
    df = app_data.videogame_sales['data_region'][
        app_data.videogame_sales['data_region']['Year'].between(
            *app_data.videogame_sales['years_range'],
            inclusive='both',
        )
    ]

    fig = px.treemap(
        df,
        path=[px.Constant('Global Sales'), 'Region', 'Platform', 'Genre'],
        values='Sales',
    )

    fig.update_layout(
        margin=dict(t=0, l=0, r=0, b=0),
        height=600,
    )

    return fig


def plot_rank_by_year():
    df = app_data.videogame_sales['ranged_data'].sort_values(by='Rank').iloc[:100]

    fig = go.Figure(
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

    fig.update_layout(
        margin=dict(t=25, l=25, r=25, b=25),
    )

    return fig
