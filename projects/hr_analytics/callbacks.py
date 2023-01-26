from dash import Input, Output, callback, dcc, html

from utils.AppData import data
from utils.IdHolder import IdHolder

from .utils import (
    get_kpi,
    plot_attrition_by_department,
    plot_attrition_by_education,
    plot_attrition_by_gender,
    plot_attrition_by_gender_age,
    plot_employees_by_age,
    plot_job_satisfaction_rating,
)


@callback(
    Output(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
    [
        Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.hr_education_dropdown.name, 'value'),
    ],
)
def dispatcher(_, value):
    data.hr.education = value
    return _


@callback(
    [
        Output(IdHolder.hr_bin_slider.name, 'max'),
        Output(IdHolder.hr_bin_slider.name, 'marks'),
    ],
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_bin_slider(_):
    max_val = data.hr.by_education.Age.max() - data.hr.by_education.Age.min()
    return [
        max_val,
        {i: str(i) for i in range(1, int(max_val * 1.1), int(max_val * 0.25))},
    ]


@callback(
    [
        Output(IdHolder.hr_employee_count.name, 'children'),
        Output(IdHolder.hr_attrition_count.name, 'children'),
        Output(IdHolder.hr_attrition_rate.name, 'children'),
        Output(IdHolder.hr_active_employee_count.name, 'children'),
        Output(IdHolder.hr_average_age.name, 'children'),
        Output(IdHolder.hr_average_income.name, 'children'),
    ],
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_kpi(_):
    return get_kpi()


@callback(
    Output(IdHolder.hr_attrition_by_gender_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_attrition_by_gender(_):
    return plot_attrition_by_gender()


@callback(
    Output(IdHolder.hr_attrition_by_department_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_attrition_by_department(_):
    return plot_attrition_by_department()


@callback(
    Output(IdHolder.hr_employees_by_age_group_graph.name, 'figure'),
    [
        Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
        Input(IdHolder.hr_bin_slider.name, 'value'),
    ],
)
def update_employees_by_age_group(_, binsize):
    return plot_employees_by_age(binsize)


@callback(
    Output(IdHolder.hr_job_satisfaction_table.name, 'children'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_job_satisfaction_table(_):
    return plot_job_satisfaction_rating()


@callback(
    Output(IdHolder.hr_attrition_by_education_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_attrition_by_education(_):
    return plot_attrition_by_education()


@callback(
    Output(IdHolder.hr_attrition_by_gender_age_graph.name, 'figure'),
    Input(IdHolder.hr_callback_dispatcher.name, 'n_clicks'),
)
def update_attrition_by_gender_age(_):
    return plot_attrition_by_gender_age()
