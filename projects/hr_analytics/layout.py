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
            dcc.Dropdown(
                id=IdHolder.hr_education_dropdown.name,
                options=['All'] + app_data.hr_education,
                value='All',
                clearable=False,
            ),
        ],
        className='title-container--hr-analytics',
    ),  # TODO: add controller education
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
                ],
            ),
        ),
        lb.graph_card(
            title='Attrition by Gender',
            id_title=IdHolder.hr_attrition_by_gender_title.name,
            id_graph=IdHolder.hr_attrition_by_gender_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition by Department',
            id_title=IdHolder.hr_attrition_by_department_title.name,
            id_graph=IdHolder.hr_attrition_by_department_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Number of Employees by Age Group',
            id_title=IdHolder.hr_employees_by_age_group_title.name,
            id_graph=IdHolder.hr_employees_by_age_group_graph.name,
            config={'displayModeBar': False},
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
            id_title=IdHolder.hr_attrition_by_education_title.name,
            id_graph=IdHolder.hr_attrition_by_education_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition Rate by Gender and Age Group',
            id_title=IdHolder.hr_attrition_by_gender_age_title.name,
            id_graph=IdHolder.hr_attrition_by_gender_age_graph.name,
            config={'displayModeBar': False},
        ),
    ],
)
