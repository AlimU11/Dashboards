import dash_bootstrap_components as dbc
from dash import dcc, html

from utils.AppData import data
from utils.IdHolder import IdHolder
from utils.LayoutBuilder import LayoutBuilder as lb

layout = lb.layout(
    project_class='hr-analytics',
    title=html.Div(
        children=[
            html.H1('HR Analytics'),
            dbc.Button(
                id=IdHolder.hr_callback_dispatcher.name,
                style={'display': 'none'},
            ),
            html.Div(
                children=[
                    html.Label('Education'),
                    dcc.Dropdown(
                        id=IdHolder.hr_education_dropdown.name,
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
                    lb.kpi_card(
                        title='Employee Count',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_employee_count_title.name,
                        description_id=IdHolder.hr_employee_count.name,
                    ),
                    lb.kpi_card(
                        title='Attrition Count',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_attrition_count_title.name,
                        description_id=IdHolder.hr_attrition_count.name,
                    ),
                    lb.kpi_card(
                        title='Attrition Rate',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_attrition_rate_title.name,
                        description_id=IdHolder.hr_attrition_rate.name,
                    ),
                    lb.kpi_card(
                        title='Active Employee',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_active_employee_count_title.name,
                        description_id=IdHolder.hr_active_employee_count.name,
                    ),
                    lb.kpi_card(
                        title='Average Age',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_average_age_title.name,
                        description_id=IdHolder.hr_average_age.name,
                    ),
                    lb.kpi_card(
                        title='Average Income',
                        title_size=4,
                        description='0',
                        title_id=IdHolder.hr_average_income_title.name,
                        description_id=IdHolder.hr_average_income.name,
                    ),
                ],
            ),
        ),
        lb.graph_card(
            title='Attrition by Gender',
            title_size=4,
            title_id=IdHolder.hr_attrition_by_gender_title.name,
            graph_id=IdHolder.hr_attrition_by_gender_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition by Department',
            title_size=4,
            title_id=IdHolder.hr_attrition_by_department_title.name,
            graph_id=IdHolder.hr_attrition_by_department_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title=html.Div(
                children=[
                    'No. of Employees by Age',
                ],
            ),
            title_size=4,
            title_id=IdHolder.hr_employees_by_age_group_title.name,
            graph_id=IdHolder.hr_employees_by_age_group_graph.name,
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
            title_size=4,
            title_id=IdHolder.hr_attrition_by_education_title.name,
            graph_id=IdHolder.hr_attrition_by_education_graph.name,
            config={'displayModeBar': False},
        ),
        lb.graph_card(
            title='Attrition Rate by Gender and Age Group',
            title_size=4,
            title_id=IdHolder.hr_attrition_by_gender_age_title.name,
            graph_id=IdHolder.hr_attrition_by_gender_age_graph.name,
            config={'displayModeBar': False},
        ),
    ],
)
