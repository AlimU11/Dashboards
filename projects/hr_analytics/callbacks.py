from dash import Input, Output, callback, dcc, html

from utils import data
from utils.IdHolder import IdHolder as ID

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
    Output(ID.hr_callback_dispatcher, 'n_clicks'),
    [
        Input(ID.hr_callback_dispatcher, 'n_clicks'),
        Input(ID.hr_education_dropdown, 'value'),
    ],
)
def dispatcher(_, value):
    data.hr.education = value
    return _


@callback(
    [
        Output(ID.hr_bin_slider, 'max'),
        Output(ID.hr_bin_slider, 'marks'),
    ],
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_bin_slider(_):
    max_val = data.hr.by_education.Age.max() - data.hr.by_education.Age.min()
    return [
        max_val,
        {i: str(i) for i in range(1, int(max_val * 1.1), int(max_val * 0.25))},
    ]


@callback(
    [
        Output(ID.hr_employee_count, 'children'),
        Output(ID.hr_attrition_count, 'children'),
        Output(ID.hr_attrition_rate, 'children'),
        Output(ID.hr_active_employee_count, 'children'),
        Output(ID.hr_average_age, 'children'),
        Output(ID.hr_average_income, 'children'),
    ],
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_kpi(_):
    return get_kpi()


@callback(
    Output(ID.hr_attrition_by_gender_graph, 'figure'),
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_attrition_by_gender(_):
    return plot_attrition_by_gender()


@callback(
    Output(ID.hr_attrition_by_department_graph, 'figure'),
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_attrition_by_department(_):
    return plot_attrition_by_department()


@callback(
    Output(ID.hr_employees_by_age_group_graph, 'figure'),
    [
        Input(ID.hr_callback_dispatcher, 'n_clicks'),
        Input(ID.hr_bin_slider, 'value'),
    ],
)
def update_employees_by_age_group(_, binsize):
    return plot_employees_by_age(binsize)


@callback(
    Output(ID.hr_job_satisfaction_table, 'children'),
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_job_satisfaction_table(_):
    return plot_job_satisfaction_rating()


@callback(
    Output(ID.hr_attrition_by_education_graph, 'figure'),
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_attrition_by_education(_):
    return plot_attrition_by_education()


@callback(
    Output(ID.hr_attrition_by_gender_age_graph, 'figure'),
    Input(ID.hr_callback_dispatcher, 'n_clicks'),
)
def update_attrition_by_gender_age(_):
    return plot_attrition_by_gender_age()
