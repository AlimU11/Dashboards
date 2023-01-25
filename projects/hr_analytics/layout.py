import dash_bootstrap_components as dbc
from dash import dcc, html

from utils.AppData import app_data
from utils.IdHolder import IdHolder
from utils.LayoutBuilder import LayoutBuilder as lb

layout = lb.layout(
    project_class='hr-analytics',
    title=html.Div(
        children=[
            html.H1('HR Analytics'),
            html.Div(
                children=[
                    html.Label('Education'),
                    dcc.Dropdown(
                        id=IdHolder.hr_education_dropdown.name,
                        options=['All'] + app_data.hr_education,
                        value='All',
                        clearable=False,
                    ),
                ],
            ),
        ],
        className='title-container--hr-analytics',
    ),
    children=[
        dbc.Card(
            dbc.CardBody(
                children=[
                    dbc.Button(
                        id=IdHolder.hr_callback_dispatcher.name,
                        style={'display': 'none'},
                    ),
                    lb.kpi_card(
                        title='Employee Count',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_employee_count_title.name,
                        id_description=IdHolder.hr_employee_count.name,
                    ),
                    lb.kpi_card(
                        title='Attrition Count',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_attrition_count_title.name,
                        id_description=IdHolder.hr_attrition_count.name,
                    ),
                    lb.kpi_card(
                        title='Attrition Rate',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_attrition_rate_title.name,
                        id_description=IdHolder.hr_attrition_rate.name,
                    ),
                    lb.kpi_card(
                        title='Active Employee',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_active_employee_count_title.name,
                        id_description=IdHolder.hr_active_employee_count.name,
                    ),
                    lb.kpi_card(
                        title='Average Age',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_average_age_title.name,
                        id_description=IdHolder.hr_average_age.name,
                    ),
                    lb.kpi_card(
                        title='Average Income',
                        size=4,
                        description='0',
                        id_title=IdHolder.hr_average_income_title.name,
                        id_description=IdHolder.hr_average_income.name,
                    ),
                ],
            ),
        ),
        lb.graph_card(
            title='Attrition by Gender',
            size=4,
            id_title=IdHolder.hr_attrition_by_gender_title.name,
            id_graph=IdHolder.hr_attrition_by_gender_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition by Department',
            size=4,
            id_title=IdHolder.hr_attrition_by_department_title.name,
            id_graph=IdHolder.hr_attrition_by_department_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title=html.Div(
                children=[
                    'No. of Employees by Age',
                ],
            ),
            size=4,
            id_title=IdHolder.hr_employees_by_age_group_title.name,
            id_graph=IdHolder.hr_employees_by_age_group_graph.name,
            config={'displayModeBar': False},
            controls=html.Div(
                children=[
                    html.Label('Bin Size'),
                    dcc.Slider(
                        id=IdHolder.hr_bin_slider.name,
                        min=1,
                        max=2,
                        step=1,
                        value=4,
                        tooltip={'placement': 'bottom'},
                    ),
                ],
                id=IdHolder.hr_bin_slider_container.name,
            ),
        ),
        dbc.Card(
            dbc.CardBody(
                children=[
                    html.H4('Job Satisfaction Rating'),
                    dbc.Spinner(
                        dbc.Table(
                            id=IdHolder.hr_job_satisfaction_table.name,
                        ),
                    ),
                ],
            ),
        ),
        lb.graph_card(
            title='Attrition by Education Field',
            size=4,
            id_title=IdHolder.hr_attrition_by_education_title.name,
            id_graph=IdHolder.hr_attrition_by_education_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition Rate by Gender and Age Group',
            size=4,
            id_title=IdHolder.hr_attrition_by_gender_age_title.name,
            id_graph=IdHolder.hr_attrition_by_gender_age_graph.name,
            config={'displayModeBar': False},
        ),
    ],
)
