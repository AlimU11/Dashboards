from dash import Input, Output, callback

from utils.IdHolder import IdHolder

from .utils import plot_area_code, plot_avg_calls, plot_fees_by_model_team


@callback(
    Output(IdHolder.sp_callback_dispatcher.name, 'n_clicks'),
    [
        Input(IdHolder.sp_callback_dispatcher.name, 'n_clicks'),
    ],
)
def dispatcher(_):
    return _


@callback(
    Output(IdHolder.sp_avg_calls_graph.name, 'figure'),
    Input(IdHolder.sp_callback_dispatcher.name, 'n_clicks'),
)
def update_avg_calls_graph(_):
    return plot_avg_calls()


@callback(
    Output(IdHolder.sp_area_code_graph.name, 'figure'),
    Input(IdHolder.sp_callback_dispatcher.name, 'n_clicks'),
)
def update_area_code_graph(_):
    return plot_area_code()


@callback(
    Output(IdHolder.sp_fees_by_model_team_graph.name, 'figure'),
    Input(IdHolder.sp_callback_dispatcher.name, 'n_clicks'),
)
def update_fees_by_model_team_graph(_):
    return plot_fees_by_model_team()
