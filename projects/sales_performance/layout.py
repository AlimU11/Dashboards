import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import data
from utils.Colors import Colors
from utils.Config import config
from utils.IdHolder import IdHolder as ID
from utils.LayoutBuilder import LayoutBuilder as LB

layout = LB.layout(
    callback_dispatcher_id=ID.sp_callback_dispatcher,
    project_class='sales-performance',
    title=html.H1('Sales Performance'),
    children=[
        dbc.Card(
            children=[
                dbc.Spinner(
                    children=[
                        LB.kpi_card(
                            title='Total Earnings',
                            title_id=ID.sp_total_earnings_title,
                            title_size=6,
                            description='12345',
                            description_id=ID.sp_total_earnings_description,
                        ),
                        LB.kpi_card(
                            title='Total Paid Calls',
                            title_id=ID.sp_total_paid_calls_title,
                            title_size=6,
                            description='12345',
                            description_id=ID.sp_total_paid_calls_description,
                        ),
                        html.I(className='fa-solid fa-money-bill-wave'),
                        html.I(className='fa-solid fa-phone-volume'),
                    ],
                ),
            ],
        ),
        LB.kpi_card(
            title=html.Div(
                children=[
                    html.H6('Top'),
                    html.H5('Consultant'),
                    html.H6('Sales Revenue'),
                    html.I(
                        className='fa-solid fa-star',
                        style={'color': Colors.yellow},
                    ),
                ],
            ),
            title_id=ID.sp_top_consultants_fee_title,
            title_size=4,
            description='',
            description_id=ID.sp_top_consultants_fee_container,
        ),
        LB.graph_card(
            graph_id=ID.sp_fees_by_month_graph,
            title_id=ID.sp_fees_by_month_title,
        ),
        LB.graph_card(
            graph_id=ID.sp_paid_unpdaid_calls_graph,
        ),
        dbc.Card(
            children=[
                html.H6('Month'),
                dbc.Checklist(
                    options=[{'label': value, 'value': value} for value in data.sp.unique_months],
                    id=ID.sp_sales_month_radio,
                ),
                dbc.Button(
                    html.I(
                        className='fa-solid fa-arrow-up-right-from-square',
                        style={'color': Colors.white},
                    ),
                    id=ID.sp_show_data_by_month_button,
                    outline=True,
                ),
                dbc.Offcanvas(
                    children=[
                        html.Div(
                            id=ID.sp_month_offcanvas_data_container,
                        ),
                    ],
                    id=ID.sp_month_offcanvas,
                    title='Data for Month',
                    is_open=False,
                    scrollable=True,
                    placement='end',
                ),
            ],
        ),
        LB.graph_card(
            graph_id=ID.sp_courses_by_time_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_advertisement_channel_graph,
            title_id=ID.sp_advertisement_channel_title,
        ),
        LB.graph_card(
            graph_id=ID.sp_average_call_graph,
            title_id=ID.sp_average_call_title,
        ),
        LB.kpi_card(
            title=html.Div(
                children=[
                    html.H6('Top'),
                    html.H5('Training Levels'),
                    html.H6('Revenue'),
                    html.I(
                        className='fa-solid fa-star',
                        style={'color': Colors.yellow},
                    ),
                ],
            ),
            title_id=ID.sp_top_training_levels_title,
            title_size=4,
            description='',
            description_id=ID.sp_top_training_levels_container,
        ),
        dbc.Card(
            children=[
                LB.graph_card(
                    graph_id=ID.sp_training_levels_fees_graph,
                ),
                LB.graph_card(
                    graph_id=ID.sp_training_levels_courses_graph,
                ),
            ],
        ),
        LB.graph_card(
            graph_id=ID.sp_area_code_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_avg_calls_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_sales_by_team_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_sales_by_concultant_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_training_models_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_fees_by_consultant_graph,
        ),
        dbc.Card(
            children=[
                html.H6('Sales Team'),
                html.Hr(),
                dbc.Checklist(
                    options=[{'label': value, 'value': value} for value in data.sp.unique_teams],
                    id=ID.sp_sales_team_radio,
                ),
                dbc.Button(
                    html.I(
                        className='fa-solid fa-arrow-up-right-from-square',
                        style={'color': Colors.white},
                    ),
                    id=ID.sp_show_data_by_team_button,
                    outline=True,
                ),
                dbc.Offcanvas(
                    children=[
                        html.Div(
                            id=ID.sp_team_offcanvas_data_container,
                        ),
                    ],
                    id=ID.sp_team_offcanvas,
                    title='Data for Sales Team',
                    is_open=False,
                    scrollable=True,
                ),
            ],
        ),
        LB.graph_card(
            graph_id=ID.sp_fees_by_model_team_graph,
        ),
        LB.graph_card(
            graph_id=ID.sp_advertisements_graph,
            controls=dbc.InputGroup(
                [
                    dbc.Input(
                        type='number',
                        value=config.sp_default_total_advetisement,
                        id=ID.sp_advertisements_input,
                    ),
                    dbc.InputGroupText('Total Advertisements'),
                ],
                id=ID.sp_advertisements_input_group,
                size='sm',
            ),
        ),
    ],
)
