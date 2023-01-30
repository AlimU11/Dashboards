import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, html
from dash.exceptions import PreventUpdate

from utils import Colors, data
from utils.IdHolder import IdHolder as ID

from .utils import (
    plot_advertisement_channel,
    plot_advertisements,
    plot_area_code,
    plot_average_call,
    plot_avg_calls,
    plot_courses_by_time,
    plot_fees_by_consultant,
    plot_fees_by_model_team,
    plot_fees_by_month,
    plot_paid_unpaid_calls,
    plot_sales_by_consultant,
    plot_sales_by_team,
    plot_training_levels_courses,
    plot_training_levels_fees,
    plot_training_models,
    top_list,
)


@callback(
    Output(ID.sp_callback_dispatcher, 'n_clicks'),
    [
        Input(ID.sp_callback_dispatcher, 'n_clicks'),
        Input(ID.sp_sales_team_radio, 'value'),
        Input(ID.sp_sales_month_radio, 'value'),
    ],
)
def dispatcher(_, team, month):
    data.sp.sales_team = team if team else data.sp.unique_teams
    data.sp.sales_month = month if month else data.sp.unique_months

    return _


@callback(
    Output(ID.sp_avg_calls_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_avg_calls_graph(_):
    return plot_avg_calls()


@callback(
    Output(ID.sp_area_code_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_area_code_graph(_):
    return plot_area_code()


@callback(
    Output(ID.sp_fees_by_model_team_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_fees_by_model_team_graph(_):
    return plot_fees_by_model_team()


@callback(
    Output(ID.sp_training_models_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_training_models_graph(_):
    return plot_training_models()


@callback(
    Output(ID.sp_sales_by_team_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_sales_by_team_graph(_):
    return plot_sales_by_team()


@callback(
    Output(ID.sp_fees_by_consultant_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_fees_by_consultant_graph(_):
    return plot_fees_by_consultant()


@callback(
    [
        Output(ID.sp_fees_by_month_graph, 'figure'),
        Output(ID.sp_fees_by_month_title, 'children'),
    ],
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_fees_by_month_graph(_):
    fig, high, avg, low = plot_fees_by_month()
    return [
        fig,
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div('Highest'),
                        html.Div('Monthly Revenue'),
                        html.Div(f'{high:,}'),
                        html.I(className='fa-solid fa-chevron-up'),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div('Average'),
                        html.Div('Monthly Revenue'),
                        html.Div(f'{avg:,}'),
                        html.I(className='fa-solid fa-chart-simple'),
                    ],
                ),
                html.Div(
                    children=[
                        html.Div('Lowest'),
                        html.Div('Monthly Revenue'),
                        html.Div(f'{low:,}'),
                        html.I(className='fa-solid fa-chevron-down'),
                    ],
                ),
            ],
        ),
    ]


@callback(
    Output(ID.sp_courses_by_time_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_courses_by_time_graph(_):
    return plot_courses_by_time()


@callback(
    Output(ID.sp_paid_unpdaid_calls_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_paid_unpaid_calls_graph(_):
    return plot_paid_unpaid_calls()


@callback(
    Output(ID.sp_sales_by_concultant_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_sales_by_consultant_graph(_):
    return plot_sales_by_consultant()


@callback(
    Output(ID.sp_sales_team_radio, 'value'),
    Input(ID.sp_sales_team_radio, 'value'),
)
def disable_sales_team_radio(value):
    if not value:
        raise PreventUpdate

    return value if len(value) == 1 else [value[-1]]


@callback(
    Output(ID.sp_sales_month_radio, 'value'),
    Input(ID.sp_sales_month_radio, 'value'),
)
def disable_sales_month_radio(value):
    if not value:
        raise PreventUpdate

    return value if len(value) == 1 else [value[-1]]


@callback(
    Output(ID.sp_team_offcanvas, 'is_open'),
    Input(ID.sp_show_data_by_team_button, 'n_clicks'),
    State(ID.sp_team_offcanvas, 'is_open'),
)
def toggle_team_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    Output(ID.sp_month_offcanvas, 'is_open'),
    Input(ID.sp_show_data_by_month_button, 'n_clicks'),
    State(ID.sp_month_offcanvas, 'is_open'),
)
def toggle_month_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    Output(ID.sp_team_offcanvas_data_container, 'children'),
    Input(ID.sp_team_offcanvas, 'is_open'),
    State(ID.sp_sales_team_radio, 'value'),
)
def update_team_offcanvas_data_container(_, value):
    # TODO: off canvas nav buttons
    return dbc.Table.from_dataframe(
        data.sp.raw_data.query('`Sale Team` == @value') if value else data.sp.raw_data.head(100),
        striped=True,
        bordered=True,
        hover=True,
        size='sm',
    )


@callback(
    Output(ID.sp_month_offcanvas_data_container, 'children'),
    Input(ID.sp_month_offcanvas, 'is_open'),
    State(ID.sp_sales_month_radio, 'value'),
)
def update_month_offcanvas_data_container(_, value):
    # TODO: off canvas nav buttons
    return dbc.Table.from_dataframe(
        data.sp.raw_data.query('Month == @value') if value else data.sp.raw_data.head(100),
        striped=True,
        bordered=True,
        hover=True,
        size='sm',
    )


@callback(
    Output(ID.sp_top_training_levels_container, 'children'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_top_training_levels_container(_):
    return top_list('Training Levels', 5)


@callback(
    Output(ID.sp_top_consultants_fee_container, 'children'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_top_consultants_fee_container(_):
    return top_list('Consultant', 5)


@callback(
    Output(ID.sp_advertisements_graph, 'figure'),
    [
        Input(ID.sp_advertisements_input, 'value'),
        Input(ID.sp_callback_dispatcher, 'n_clicks'),
    ],
)
def update_advertisements_graph(value, _):
    return plot_advertisements(value)


@callback(
    Output(ID.sp_advertisements_input, 'value'),
    Input(ID.sp_advertisements_input, 'value'),
)
def update_advertisements_input(value):
    return 1 if not value or value < 1 else 5 if value > 5 else value


@callback(
    Output(ID.sp_total_earnings_description, 'children'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_total_earnings_description(_):
    return html.Div(
        children=[
            html.Span(f"{data.sp.data['Paid Fees'].sum():,.0f}"),
            html.Br(),
            html.Span('Egyptian Pounds'),
        ],
    )


@callback(
    Output(ID.sp_total_paid_calls_description, 'children'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_total_paid_calls_description(_):
    return html.Div(
        children=[
            html.Span(
                f"{data.sp.data.query('`Paid Fees` > 0')['Paid Fees'].count():,.0f}",
            ),
            html.Br(),
            html.Span('Calls'),
        ],
    )


@callback(
    Output(ID.sp_training_levels_fees_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_training_levels_fees_graph(_):
    return plot_training_levels_fees()


@callback(
    Output(ID.sp_training_levels_courses_graph, 'figure'),
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_training_levels_courses_graph(_):
    return plot_training_levels_courses()


@callback(
    [
        Output(ID.sp_average_call_graph, 'figure'),
        Output(ID.sp_average_call_title, 'children'),
    ],
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_average_call(_):
    fig, average, min_call, max_call, dt = plot_average_call()
    return [
        fig,
        html.Div(
            children=[
                html.Div('Average'),
                html.Div('Paid Calls Duration'),
                html.Div(f'by {dt}'),
                html.Div(f'{average} mm:ss'),
                html.Div(
                    children=[
                        html.Span('Minimum'),
                        html.Span('Call Duration'),
                        html.Span(f'{min_call}'),
                        html.Span('mm:ss'),
                    ],
                ),
                html.Div(
                    children=[
                        html.Span('Maximum'),
                        html.Span('Call Duration'),
                        html.Span(f'{max_call}'),
                        html.Span('mm:ss'),
                    ],
                ),
            ],
        ),
    ]


@callback(
    [
        Output(ID.sp_advertisement_channel_graph, 'figure'),
        Output(ID.sp_advertisement_channel_title, 'children'),
    ],
    Input(ID.sp_callback_dispatcher, 'n_clicks'),
)
def update_advertisement_channel(_):
    return [
        plot_advertisement_channel(),
        top_list('Advertising Channel', 6),
    ]
