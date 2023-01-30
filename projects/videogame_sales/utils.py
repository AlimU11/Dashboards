from datetime import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import html

from utils import data
from utils.Colors import Colors


def update_app_data(years_range=None, region=None, top_n_publishers=None, top_n_games=None):
    data.vg.years_range = years_range or data.vg.years_range
    data.vg.top_n_publishers = top_n_publishers or data.vg.top_n_publishers
    data.vg.top_n_games = top_n_games or data.vg.top_n_games
    data.vg.region = region or data.vg.region
    data.vg.ranged_data = data.vg.data[
        data.vg.data.Year.between(
            *data.vg.years_range,
            inclusive='both',
        )
    ]


def get_sales_amount():
    return f'''$ {data.vg.ranged_data[data.vg.region].sum():,.2f}M'''


def get_top_game():
    title = data.vg.ranged_data.sort_values(by=data.vg.region, ascending=False)['Name'].iloc[0]
    return title  # [:12] + ('' if len(title) < 12 else '...')


def get_top_freq_platform():
    return data.vg.ranged_data.groupby('Platform')[data.vg.region].sum().idxmax()


def get_trending_genre():
    genre_sum = (
        data.vg.ranged_data.groupby(
            'Genre',
        )[data.vg.region]
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
        f'Top {data.vg.top_n_games} Games {region}',
    ]


def get_kpi_descriptions(region, platform, second_max, diff_second_max, g_min, diff_min):
    return [
        [
            f'Total Sales ',
            html.Span(
                f'{region}',
                style={
                    'color': Colors.green,
                    'font-weight': 'bold',
                },
            ),
            html.Br(),
            f'from ',
            html.Span(
                f'''{data.vg.ranged_data.Year.min():.0f}''',
                style={
                    'color': Colors.green,
                    'font-weight': 'bold',
                },
            ),
            f' to ',
            html.Span(
                f'''{data.vg.ranged_data.Year.max():.0f}''',
                style={
                    'color': Colors.green,
                    'font-weight': 'bold',
                },
            ),
        ],
        [
            f'(',
            html.Span(
                f'''{data.vg.ranged_data.sort_values(by=data.vg.region, ascending=False).iloc[0].Genre}''',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            '/',
            html.Span(
                f'''{data.vg.ranged_data.sort_values(by=data.vg.region, ascending=False).iloc[0].Year:.0f}''',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            '), ',
            html.Span(
                f'''{data.vg.ranged_data.sort_values(by=data.vg.region, ascending=False).iloc[0].Publisher}''',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            html.Br(),
            'Has the biggest sales',
            html.Br(),
            html.Span(
                f'''$ {data.vg.ranged_data[data.vg.region].iloc[0]:,.2f}M''',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
        ],
        [
            'Most popular platform for game developers',
            html.Br(),
            html.Span(
                f'''{data.vg.ranged_data[data.vg.region][data.vg.ranged_data.Platform == platform].count():,}''',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            ' games developed',
        ],
        [
            f'Trending Genre {region}',
            html.Br(),
            html.Span(
                f'+{diff_second_max}%',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            f' compared to {second_max}',
            html.Br(),
            html.Span(
                f'+{diff_min}%',
                style={'color': Colors.green, 'font-weight': 'bold'},
            ),
            f' compared to {g_min}',
        ],
    ]


def get_genres():
    genres = data.vg.ranged_data['Genre'].value_counts()

    return [
        [html.I(className=f'''fa-solid {getattr(data.vg.Genre, str(i).lower().replace('-', '_'))}'''), i]
        for i in genres.index
    ] + [html.B(f'{value:,.0f}') for value in genres.values]


def plot_sales_by_publisher():
    sales_by_publisher = (
        data.vg.ranged_data.groupby(
            'Publisher',
        )[data.vg.region]
        .sum()
        .sort_values()
    )

    top_n_publishers = sales_by_publisher[-data.vg.top_n_publishers :].index

    sales_by_year_publisher = (
        data.vg.ranged_data[data.vg.ranged_data['Publisher'].isin(top_n_publishers)]
        .groupby(['Year', 'Publisher'])[data.vg.region]
        .sum()
        .unstack()
    )

    sales_other = (
        data.vg.ranged_data[~data.vg.ranged_data['Publisher'].isin(top_n_publishers)]
        .groupby('Year')[data.vg.region]
        .sum()
    )

    fig = go.Figure()

    for publisher in top_n_publishers:
        fig.add_trace(
            go.Scatter(
                x=[
                    datetime.strptime(str(i), '%Y')
                    for i in range(
                        data.vg.years_range[0],
                        data.vg.years_range[1] + 1,
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
                    data.vg.years_range[0],
                    data.vg.years_range[1] + 1,
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
        )[data.vg.region]
        .sum()
        .sort_values()
    )

    top_n_games = sales_by_game[-data.vg.top_n_games :].index

    fig = go.Figure()

    for game, sales in zip(
        top_n_games,
        sales_by_game[-data.vg.top_n_games :],
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
        data.vg.ranged_data.groupby(
            'Publisher',
        )[data.vg.region]
        .sum()
        .sort_values()
    )

    top_n_publishers = sales_by_publisher[-data.vg.top_n_publishers :].index

    sales_by_genre_publisher = pd.concat(
        [
            (
                data.vg.ranged_data[data.vg.ranged_data['Publisher'].isin(top_n_publishers)]
                .groupby(['Genre', 'Publisher'])[data.vg.region]
                .sum()
                .unstack()
            ),
            (
                data.vg.ranged_data[~data.vg.ranged_data['Publisher'].isin(top_n_publishers)]
                .groupby('Genre')[data.vg.region]
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
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
    )

    return fig


def plot_genre_by_year():
    sales_by_genre_year = data.vg.ranged_data.groupby(['Year', 'Genre'])[data.vg.region].sum().reset_index()

    fig = go.Figure(
        data=go.Scatter(
            x=sales_by_genre_year.Year,
            y=sales_by_genre_year.Genre,
            text=['$' + str(i) + 'M' for i in sales_by_genre_year[data.vg.region]],
            mode='markers',
            marker=dict(
                size=sales_by_genre_year[data.vg.region],
                sizemode='area',
                sizeref=2.0 * max(sales_by_genre_year[data.vg.region]) / (40.0**2),
                sizemin=4,
                color=sales_by_genre_year[data.vg.region],
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
        data.vg.ranged_data.groupby(['Platform', 'Genre'])[data.vg.region]
        .sum()
        .reset_index()
        .sort_values(
            by=['Platform', data.vg.region],
            ascending=False,
        )
        .groupby('Platform')
        .head(top_n_genres)
    )

    top_platforms = data.vg.ranged_data.groupby('Platform')[data.vg.region].sum().sort_values().index[-top_n_platforms:]

    top_genres_top_platforms = (
        data.vg.ranged_data.groupby(['Platform', 'Genre'])[data.vg.region]
        .sum()
        .reset_index()
        .sort_values(
            by=['Platform', data.vg.region],
            ascending=False,
        )
        .groupby('Platform')
        .head(top_n_genres)
    )

    fig = go.Figure()

    for genre in top_genres_top_platforms.Genre.unique():
        x = top_genres_top_platforms[top_genres_top_platforms['Genre'] == genre][data.vg.region]
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
    df = data.vg.data_region[
        data.vg.data_region['Year'].between(
            *data.vg.years_range,
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
    df = data.vg.ranged_data.sort_values(by='Rank').iloc[:100]

    fig = go.Figure(
        data=go.Scatter(
            y=df.Year,
            x=df.Rank,
            text=df.Name + ' $' + df[data.vg.region].astype(str) + 'M',
            hoverinfo='text',
            mode='markers',
            marker=dict(
                size=df[data.vg.region],
                sizemode='area',
                sizeref=2.0 * max(df[data.vg.region]) / (40.0**2),
                sizemin=4,
                color=df[data.vg.region],
            ),
        ),
    )

    fig.update_layout(
        margin=dict(t=25, l=25, r=25, b=25),
    )

    return fig
