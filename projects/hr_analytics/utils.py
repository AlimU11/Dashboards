import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utils import data
from utils.Colors import Colors


def get_kpi():
    employee_count = data.hr.by_education.shape[0]
    attrition_count = data.hr.attrition.shape[0]
    attrition_rate = f'{round(attrition_count / employee_count * 100, 2)} %'
    active_employee = employee_count - attrition_count
    average_age = round(data.hr.by_education.Age.mean())
    average_income = f'${round(data.hr.by_education["Monthly Income"].mean())}'

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
    by_gender = data.hr.attrition.Gender.value_counts()

    fig.add_trace(
        go.Bar(
            x=[by_gender.values[0]],
            y=[by_gender.index[0]],
            orientation='h',
            marker_color=[Colors.blue],
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
            marker_color=[Colors.pink],
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
            color=Colors.white,
        ),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
    )
    return fig


def plot_attrition_by_department():
    fig = go.Figure()
    by_department = data.hr.attrition.Department.value_counts()

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
            color=Colors.white,
        ),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
    )

    return fig


def plot_employees_by_age(binsize):
    fig = go.Figure()

    ages = data.hr.by_education.Age
    by_age_group = pd.cut(
        ages,
        bins=range(
            ages.min(),
            ages.max() + binsize,
            binsize,
        ),
    )

    by_age_group_attrition = by_age_group[data.hr.is_attrition]

    fig.add_trace(
        go.Bar(
            x=[i.left for i in by_age_group.value_counts().index],
            y=by_age_group.value_counts().values,
            texttemplate='<b>%{y}</b>',
            textposition='outside',
            textfont=dict(
                size=14,
            ),
            width=binsize - 1 or 0.5,
            name='All Employees',
        ),
    )

    fig.add_trace(
        go.Bar(
            x=[i.left for i in by_age_group_attrition.value_counts().index],
            y=by_age_group_attrition.value_counts().values,
            width=max(binsize - 3, 0.5),
            name='Attrition',
        ),
    )

    fig.update_layout(
        bargap=0.2,
        barmode='overlay',
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
            color=Colors.white,
        ),
        legend=dict(
            orientation='h',
            y=1.2,
        ),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
    )

    return fig


def plot_job_satisfaction_rating():
    pivot = pd.pivot_table(
        data.hr.by_education,
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

    by_education = data.hr.attrition['Education Field'].value_counts()

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
            color=Colors.white,
        ),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        bargap=0.2,
    )

    return fig


def plot_attrition_by_gender_age():

    groups = (
        pd.concat(
            [
                data.hr.attrition[['Attrition', 'Gender']],
                pd.cut(
                    data.hr.attrition.Age,
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
        color=lambda _df: _df.Gender.apply(lambda x: Colors.pink if x == 'Female' else Colors.blue),
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
                    color=Colors.white,
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
            color=Colors.white,
        ),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
    )

    return fig
