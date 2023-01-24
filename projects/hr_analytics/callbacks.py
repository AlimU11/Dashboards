from dash import Input, Output, callback

from utils.AppData import app_data
from utils.IdHolder import IdHolder

from .utils import (
    plot_attrition_by_department,
    plot_attrition_by_education,
    plot_attrition_by_gender,
    plot_attrition_by_gender_age,
    plot_employees_by_age,
    plot_job_satisfaction_rating,
    plot_kpi,
)


@callback(
    Output(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
    [
        Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.hr_education_dropdown.name, 'value'),
    ],
)
def dispatcher(_, value):
    hr_analytics = app_data.hr_analytics
    hr_analytics['education'] = value
    return _


@callback(
    [
        Output(IdHolder.hr_employee_count.name, 'children'),
        Output(IdHolder.hr_attrition_count.name, 'children'),
        Output(IdHolder.hr_attrition_rate.name, 'children'),
        Output(IdHolder.hr_active_employee_count.name, 'children'),
        Output(IdHolder.hr_average_age.name, 'children'),
    ],
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def kpi(_):
    return plot_kpi()


@callback(
    Output(IdHolder.hr_attrition_by_gender_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def attrition_by_gender(_):
    return plot_attrition_by_gender()


@callback(
    Output(IdHolder.hr_attrition_by_department_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def attrition_by_department(_):
    return plot_attrition_by_department()


@callback(
    Output(IdHolder.hr_employees_by_age_group_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def employees_by_age_group(_):
    return plot_employees_by_age()


@callback(
    Output(IdHolder.hr_job_satisfaction_table.name, 'children'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def job_satisfaction_table(_):
    return plot_job_satisfaction_rating()


@callback(
    Output(IdHolder.hr_attrition_by_education_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def attrition_by_education(_):
    return plot_attrition_by_education()


@callback(
    Output(IdHolder.hr_attrition_by_gender_age_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def attrition_by_gender_age(_):
    return plot_attrition_by_gender_age()
