import dash_bootstrap_components as dbc
from dash import dcc, html

from utils import data
from utils.Config import config
from utils.IdHolder import IdHolder as ID
from utils.LayoutBuilder import LayoutBuilder as LB

layout = LB.layout(
    callback_dispatcher_id=ID.hr_callback_dispatcher,
    project_class='hr-analytics',
    title=html.Div(
        children=[
            html.H1('HR Analytics'),
            html.Div(
                children=[
                    html.Label('Education'),
                    dcc.Dropdown(
                        id=ID.hr_education_dropdown,
                        options=['All'] + data.hr.education_list,
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
                    LB.kpi_card(
                        title='Employee Count',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_employee_count_title,
                        description_id=ID.hr_employee_count,
                    ),
                    LB.kpi_card(
                        title='Attrition Count',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_attrition_count_title,
                        description_id=ID.hr_attrition_count,
                    ),
                    LB.kpi_card(
                        title='Attrition Rate',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_attrition_rate_title,
                        description_id=ID.hr_attrition_rate,
                    ),
                    LB.kpi_card(
                        title='Active Employee',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_active_employee_count_title,
                        description_id=ID.hr_active_employee_count,
                    ),
                    LB.kpi_card(
                        title='Average Age',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_average_age_title,
                        description_id=ID.hr_average_age,
                    ),
                    LB.kpi_card(
                        title='Average Income',
                        title_size=4,
                        description='0',
                        title_id=ID.hr_average_income_title,
                        description_id=ID.hr_average_income,
                    ),
                ],
            ),
        ),
        LB.graph_card(
            title='Attrition by Gender',
            title_size=4,
            title_id=ID.hr_attrition_by_gender_title,
            graph_id=ID.hr_attrition_by_gender_graph,
        ),
        LB.graph_card(
            title='Attrition by Department',
            title_size=4,
            title_id=ID.hr_attrition_by_department_title,
            graph_id=ID.hr_attrition_by_department_graph,
        ),
        LB.graph_card(
            title=html.Div(
                children=[
                    'Attrition by Age',
                ],
            ),
            title_size=4,
            title_id=ID.hr_employees_by_age_group_title,
            graph_id=ID.hr_employees_by_age_group_graph,
            controls=html.Div(
                children=[
                    html.Label('Bin Size'),
                    dcc.Slider(
                        id=ID.hr_bin_slider,
                        min=1,
                        max=2,
                        step=1,
                        value=config.hr_default_bin_size,
                        tooltip={'placement': 'bottom'},
                    ),
                ],
                id=ID.hr_bin_slider_container,
            ),
        ),
        dbc.Card(
            dbc.CardBody(
                children=[
                    html.H4('Job Satisfaction Rating'),
                    dbc.Spinner(
                        dbc.Table(
                            id=ID.hr_job_satisfaction_table,
                        ),
                    ),
                ],
            ),
        ),
        LB.graph_card(
            title='Attrition by Education Field',
            title_size=4,
            title_id=ID.hr_attrition_by_education_title,
            graph_id=ID.hr_attrition_by_education_graph,
        ),
        LB.graph_card(
            title='Attrition Rate by Gender and Age Group',
            title_size=4,
            title_id=ID.hr_attrition_by_gender_age_title,
            graph_id=ID.hr_attrition_by_gender_age_graph,
        ),
    ],
)
