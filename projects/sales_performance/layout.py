import dash_bootstrap_components as dbc
from dash import dcc, html

from utils.AppData import data
from utils.IdHolder import IdHolder
from utils.LayoutBuilder import LayoutBuilder as lb

layout = lb.layout(
    callback_dispatcher_id=IdHolder.sp_callback_dispatcher.name,
    project_class='sales-performance',
    title=html.H1('Sales Performance'),
    children=[
        dbc.Card('A1'),
        dbc.Card('A2'),
        dbc.Card('A3'),
        dbc.Card('A4'),
        dbc.Card('A5'),
        dbc.Card('A6'),
        dbc.Card('A7'),
        dbc.Card('A8'),
        dbc.Card('A9'),
        dbc.Card('A10'),
        lb.graph_card(
            graph_id=IdHolder.sp_area_code_graph.name,
        ),
        lb.graph_card(
            graph_id=IdHolder.sp_avg_calls_graph.name,
        ),
        dbc.Card('A13'),
        dbc.Card('A14'),
        dbc.Card('A15'),
        dbc.Card('A16'),
        dbc.Card('A17'),
        lb.graph_card(
            graph_id=IdHolder.sp_fees_by_model_team_graph.name,
        ),
        dbc.Card('A19'),
    ],
)
