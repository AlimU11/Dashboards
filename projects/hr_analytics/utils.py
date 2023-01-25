import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils.AppData import app_data


def get_kpi():
    employee_count = app_data.hr_analytics_data.shape[0]
    attrition_count = app_data.hr_attrition.shape[0]
    attrition_rate = f'{round(attrition_count / employee_count * 100, 2)} %'
    active_employee = employee_count - attrition_count
    average_age = round(app_data.hr_analytics_data.Age.mean())
    average_income = f'$ {round(app_data.hr_analytics_data["Monthly Income"].mean())}'

    return [
        employee_count,
        attrition_count,
        attrition_rate,
        active_employee,
        average_age,
        average_income,
    ]


def plot_attrition_by_gender():
    fig = go.Figure()
    by_gender = app_data.hr_attrition.Gender.value_counts()

    fig.add_trace(
        go.Bar(
            x=[by_gender.values[0]],
            y=[by_gender.index[0]],
            orientation='h',
            marker_color=['#636EFA'],
            showlegend=False,
            textposition='outside',
            text=[by_gender.values[0]],
        ),
    )

    fig.add_trace(
        go.Bar(
            x=[by_gender.values[1]],
            y=[by_gender.index[1]],
            orientation='h',
            marker_color=['#FF6692'],
            showlegend=False,
            textposition='outside',
            text=[by_gender.values[1]],
        ),
    )

    fig.update_layout(
        yaxis=dict(
            autorange='reversed',
            # TODO: add postfix icons
            tickmode='array',
            tickvals=[0, 1],
            ticktext=[f'<b>{i}</b>' for i in by_gender.index],
        ),
        xaxis=dict(
            range=[0, by_gender.max() * 1.17],
            visible=False,
        ),
        height=100,
        margin=dict(l=0, r=0, t=0, b=0),
        font=dict(
            size=16,
            family='Inter',
            color='#FFFFFF',
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    return fig


def plot_attrition_by_department():
    fig = go.Figure()
    by_department = app_data.hr_attrition.Department.value_counts()

    fig.add_trace(
        go.Pie(
            labels=by_department.index,
            values=by_department.values,
            sort=True,
            direction='clockwise',
            textposition='outside',
            textinfo='percent+label+value',
            texttemplate='<b>%{label}</b> <br> %{value} (%{percent:.1%})',
        ),
    )

    fig.update_layout(
        legend=dict(
            orientation='h',
            y=1.2,
            font=dict(
                size=18,
            ),
            x=1.5,
            xanchor='right',
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        font=dict(
            family='Inter',
            size=16,
            color='#FFFFFF',
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    return fig


def plot_employees_by_age(binsize):
    fig = go.Figure()

    ages = app_data.hr_analytics_data.Age
    by_age_group = pd.cut(
        ages,
        bins=range(
            ages.min(),
            ages.max() + binsize,
            binsize,
        ),
    )

    fig.add_trace(
        go.Bar(
            x=[i.left for i in by_age_group.value_counts().index],
            y=by_age_group.value_counts().values,
            texttemplate='<b>%{y}</b>',
            textposition='outside',
            textfont=dict(
                size=14,
            ),
        ),
    )

    fig.update_layout(
        bargap=0.2,
        xaxis=dict(
            tickmode='array',
            tickvals=[i.left for i in by_age_group.value_counts().index],
            tickfont=dict(
                size=14,
            ),
        ),
        yaxis=dict(
            visible=False,
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        font=dict(
            family='Inter',
            color='#FFFFFF',
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    return fig


def plot_job_satisfaction_rating():
    pivot = pd.pivot_table(
        app_data.hr_analytics_data,
        values='Age',
        index='Job Role',
        columns='Job Satisfaction',
        aggfunc='count',
        margins=True,
        fill_value=0,
    )

    pivot = pivot.rename(index={pivot.index[-1]: 'Grand Total'})

    pivot = pd.concat(
        [
            pd.concat(
                [
                    pd.Series(pivot.index, index=pivot.index),
                    pivot,
                ],
                axis=1,
            ),
        ],
        keys=['Job Satisfaction'],
        names=[''],
        axis=1,
    )

    arr = np.array(
        [
            ('', 'Job Role'),
            ('Job Satisfaction', 1),
            ('Job Satisfaction', 2),
            ('Job Satisfaction', 3),
            ('Job Satisfaction', 4),
            ('Job Satisfaction', 'Grand Total'),
        ],
    )

    pivot.columns = pd.MultiIndex.from_arrays(arr.T)

    return dbc.Table.from_dataframe(pivot, bordered=True, size='sm')


def plot_attrition_by_education():
    fig = go.Figure()

    by_education = app_data.hr_attrition['Education Field'].value_counts()

    fig.add_trace(
        go.Bar(
            x=by_education.values,
            y=by_education.index,
            orientation='h',
            texttemplate='%{x}',
            textposition='outside',
            textfont=dict(
                size=14,
            ),
        ),
    )

    fig.update_layout(
        yaxis=dict(
            tickfont=dict(
                size=14,
            ),
            autorange='reversed',
            tickmode='array',
            tickvals=by_education.index,
            ticktext=[f'<b>{i}</b>' for i in by_education.index],
        ),
        xaxis=dict(
            range=[0, by_education.max() * 1.08],
            visible=False,
        ),
        margin=dict(l=0, r=25, t=25, b=25),
        font=dict(
            family='Inter',
            color='#FFFFFF',
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        bargap=0.2,
    )

    return fig


def plot_attrition_by_gender_age():

    groups = (
        pd.concat(
            [
                app_data.hr_attrition[['Attrition', 'Gender']],
                pd.cut(
                    app_data.hr_attrition.Age,
                    bins=[0, 25, 35, 45, 55, 100],
                    labels=['Under 25', '25-34', '35-44', '45-54', '55+'],
                ),
            ],
            axis=1,
        )
        .groupby(['Age', 'Gender'], as_index=False)
        .count()
    )

    groups = groups.query('Attrition > 0').assign(
        color=lambda _df: _df.Gender.apply(lambda x: '#FF6692' if x == 'Female' else '#636EFA'),
    )

    fig = make_subplots(
        rows=1,
        cols=groups.Age.nunique(),
        specs=[[{'type': 'domain'}] * groups.Age.nunique()],
    )

    for i, age_group in enumerate(groups.Age.unique()):
        pie_group = groups[groups.Age == age_group]

        fig.add_trace(
            go.Pie(
                labels=pie_group.Gender.unique(),
                values=pie_group.Attrition.values,
                sort=True,
                direction='clockwise',
                textinfo='percent+value',
                marker_colors=pie_group.color.unique(),
                textfont=dict(
                    size=15,
                ),
                name=age_group,
                title=dict(
                    text=f'<br><b>{age_group}</b>',
                    font=dict(
                        size=18,
                    ),
                ),
                titleposition='bottom center',
            ),
            row=1,
            col=i + 1,
        )

    fig.update_layout(
        legend=dict(
            orientation='h',
            y=1,
            font=dict(
                size=18,
            ),
            x=1,
            xanchor='right',
        ),
        margin=dict(l=0, r=0, t=25, b=0),
        font=dict(
            family='Inter',
            color='#FFFFFF',
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )

    return fig
