import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import IdHolder, app_data


def kpi_card(title, description, id_title, id_description):
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.Spinner(
                    [
                        html.H1(title, className="card-title", id=id_title),
                        html.P(description, className="card-text", id=id_description),
                    ],
                ),
            ],
        ),
    )


def graph_card(title, id_title, id_graph):
    return dbc.Card(
        dbc.CardBody(
            [
                html.H1(title, className="card-title", id=id_title),
                dbc.Spinner(
                    [
                        dcc.Graph(id=id_graph),
                    ],
                ),
            ],
        ),
    )


layout = html.Div(
    children=[
        html.H1(children="Video Game Sales"),
        html.Div(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4("Filters", className="card-title"),
                            dbc.InputGroup(
                                [
                                    html.Label("Years"),
                                    dcc.RangeSlider(
                                        id=IdHolder.videogame_sales_years_range.name,
                                        min=app_data.videogame_sales["data"].Year.min(),
                                        max=app_data.videogame_sales["data"].Year.max(),
                                        step=1,
                                        allowCross=False,
                                        pushable=1,
                                        updatemode="drag",
                                        tooltip={
                                            "placement": "bottom",
                                            "always_visible": True,
                                        },
                                        marks={
                                            i: str(i)
                                            for i in range(
                                                int(
                                                    app_data.videogame_sales[
                                                        "data"
                                                    ].Year.min(),
                                                ),
                                                int(
                                                    app_data.videogame_sales[
                                                        "data"
                                                    ].Year.max(),
                                                )
                                                + 1,
                                                5,
                                            )
                                        },
                                        value=[
                                            app_data.videogame_sales["data"].Year.min(),
                                            app_data.videogame_sales["data"].Year.max(),
                                        ],
                                    ),
                                ],
                            ),
                            dbc.InputGroup(
                                [
                                    dbc.InputGroupText("Region"),
                                    dcc.Dropdown(
                                        options=[
                                            {
                                                "label": "North America",
                                                "value": "NA_Sales",
                                            },
                                            {"label": "Europe", "value": "EU_Sales"},
                                            {"label": "Japan", "value": "JP_Sales"},
                                            {"label": "Other", "value": "Other_Sales"},
                                            {
                                                "label": "Global",
                                                "value": "Global_Sales",
                                            },
                                        ],
                                        value="Global_Sales",
                                        clearable=False,
                                        id=IdHolder.videogame_sales_region.name,
                                    ),
                                ],
                            ),
                        ],
                        class_name="filter-container",
                    ),
                    style={"position": "sticky", "top": "1rem", "z-index": "1"},
                ),
                html.Div(
                    children=[
                        kpi_card(
                            "$0M",
                            "Video Game Sales",
                            IdHolder.videogame_sales_amount_title.name,
                            IdHolder.videogame_sales_amount_description.name,
                        ),
                        kpi_card(
                            "None",
                            "$0M",
                            IdHolder.videogame_sales_top_game_title.name,
                            IdHolder.videogame_sales_top_game_description.name,
                        ),
                    ],
                    className="kpi-container",
                ),
                html.Div(
                    children=[
                        kpi_card(
                            "None",
                            "0",
                            IdHolder.videogame_sales_top_freq_platform_title.name,
                            IdHolder.videogame_sales_top_freq_platform_description.name,
                        ),
                        kpi_card(
                            "None",
                            "0",
                            IdHolder.videogame_sales_trending_genre_title.name,
                            IdHolder.videogame_sales_trending_genre_description.name,
                        ),
                    ],
                    className="kpi-container",
                ),
                html.Div(
                    [
                        kpi_card(
                            "Genre 1",
                            "0",
                            IdHolder.videogame_sales_genre_1_title.name,
                            IdHolder.videogame_sales_genre_1.name,
                        ),
                        kpi_card(
                            "Genre 2",
                            "0",
                            IdHolder.videogame_sales_genre_2_title.name,
                            IdHolder.videogame_sales_genre_2.name,
                        ),
                        kpi_card(
                            "Genre 3",
                            "0",
                            IdHolder.videogame_sales_genre_3_title.name,
                            IdHolder.videogame_sales_genre_3.name,
                        ),
                        kpi_card(
                            "Genre 4",
                            "0",
                            IdHolder.videogame_sales_genre_4_title.name,
                            IdHolder.videogame_sales_genre_4.name,
                        ),
                        kpi_card(
                            "Genre 5",
                            "0",
                            IdHolder.videogame_sales_genre_5_title.name,
                            IdHolder.videogame_sales_genre_5.name,
                        ),
                        kpi_card(
                            "Genre 6",
                            "0",
                            IdHolder.videogame_sales_genre_6_title.name,
                            IdHolder.videogame_sales_genre_6.name,
                        ),
                    ],
                    className="genre-container",
                ),
                html.Div(
                    [
                        kpi_card(
                            "Genre 7",
                            "0",
                            IdHolder.videogame_sales_genre_7_title.name,
                            IdHolder.videogame_sales_genre_7.name,
                        ),
                        kpi_card(
                            "Genre 8",
                            "0",
                            IdHolder.videogame_sales_genre_8_title.name,
                            IdHolder.videogame_sales_genre_8.name,
                        ),
                        kpi_card(
                            "Genre 9",
                            "0",
                            IdHolder.videogame_sales_genre_9_title.name,
                            IdHolder.videogame_sales_genre_9.name,
                        ),
                        kpi_card(
                            "Genre 10",
                            "0",
                            IdHolder.videogame_sales_genre_10_title.name,
                            IdHolder.videogame_sales_genre_10.name,
                        ),
                        kpi_card(
                            "Genre 11",
                            "0",
                            IdHolder.videogame_sales_genre_11_title.name,
                            IdHolder.videogame_sales_genre_11.name,
                        ),
                        kpi_card(
                            "Genre 12",
                            "0",
                            IdHolder.videogame_sales_genre_12_title.name,
                            IdHolder.videogame_sales_genre_12.name,
                        ),
                    ],
                    className="genre-container",
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                "Sales by Publisher over the Years",
                                className="card-title",
                                id=IdHolder.videogame_sales_by_publisher_title.name,
                            ),
                            dbc.Spinner(
                                [
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupText("Number of Publishers"),
                                            dbc.Input(
                                                type="number",
                                                value=app_data.videogame_sales[
                                                    "top_n_publishers"
                                                ],
                                                id=IdHolder.videogame_sales_top_n_publishers.name,
                                            ),
                                        ],
                                    ),
                                    dcc.Graph(
                                        id=IdHolder.videogame_sales_by_publisher.name,
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                graph_card(
                    "Sales by Genre and Publisher",
                    IdHolder.videogame_sales_by_genre.name,
                    IdHolder.videogame_sales_by_genre_title.name,
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                "Top Games by Sales",
                                className="card-title",
                                id=IdHolder.videogame_sales_top_games_title.name,
                            ),
                            dbc.Spinner(
                                [
                                    dbc.InputGroup(
                                        [
                                            dbc.InputGroupText("Number of Games"),
                                            dbc.Input(
                                                type="number",
                                                value=app_data.videogame_sales[
                                                    "top_n_games"
                                                ],
                                                id=IdHolder.videogame_sales_top_n_games.name,
                                            ),
                                        ],
                                    ),
                                    dcc.Graph(
                                        id=IdHolder.videogame_sales_top_games.name
                                    ),
                                ],
                            ),
                        ],
                    ),
                ),
                graph_card(
                    "Sales by Genre over the Years",
                    IdHolder.videogame_sales_genre_by_year_title.name,
                    IdHolder.videogame_sales_genre_by_year.name,
                ),
                graph_card(
                    "Sales by Genre and Platform",
                    IdHolder.videogame_sales_genre_by_platform_title.name,
                    IdHolder.videogame_sales_genre_by_platform.name,
                ),
                graph_card(
                    "Sales by Rank over the Years",
                    IdHolder.videogame_sales_rank_by_year_title.name,
                    IdHolder.videogame_sales_rank_by_year.name,
                ),
                graph_card(
                    "Sales by Region, Platform and Genre",
                    IdHolder.videogame_sales_region_platform_genre_title.name,
                    IdHolder.videogame_sales_region_platform_genre.name,
                ),
            ],
            className="main-grid main-grid--video-game-sales",
        ),
    ],
    className="main-container",
)
