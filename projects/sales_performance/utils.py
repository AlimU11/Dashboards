import pandas as pd
import plotly.graph_objects as go
from dash import html
from pandas import Series
from plotly.subplots import make_subplots

from utils import Colors, data


def __get_colors(column: Series):
    return (
        Colors.colorpalette()
        + Colors.colorpalette() * (len(column.dropna().unique()) // len(Colors.colorpalette()))
        + Colors.colorpalette() * (len(column.dropna().unique()) % len(Colors.colorpalette()))
    )


def top_list(column: str, n: int):
    return html.Div(
        children=[
            html.Div([html.Div(i[0]), html.Div(i[1])])
            for i in data.sp.data.groupby(column)['Paid Fees']
            .sum()
            .head(n)
            .sort_values(ascending=False)
            .loc[lambda x: x > 0]
            .apply(lambda x: '{:,}'.format(x))
            .reset_index()
            .values[:, [1, 0]]
        ],
    )


def plot_avg_calls():
    fig = go.Figure()

    df = data.sp.data.groupby('Month').Day.count()

    fig.add_trace(
        go.Scatter(
            x=list(range(0, len(df))),
            y=df.values,
            name='Calls',
            mode='lines',
            line_shape='spline',
            # TODO: gradient fill
            line=dict(
                color=Colors.red,
            ),
        ),
    )

    fig.update_layout(
        annotations=[
            dict(
                x=0.05,
                y=0.85,
                xref='paper',
                yref='paper',
                text='<b>Average</b>',
                showarrow=False,
                font=dict(
                    size=12,
                ),
            ),
            dict(
                x=0.05,
                y=0.20,
                xref='paper',
                yref='paper',
                text='<b>Calls by Month</b>',
                showarrow=False,
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=0.55,
                y=0.95,
                xref='paper',
                yref='paper',
                text=f'<b>{df.mean():.0f}</b>',
                showarrow=False,
                font=dict(
                    size=20,
                ),
            ),
            dict(
                x=0.7,
                y=0.8,
                xref='paper',
                yref='paper',
                text='<b>Calls</b>',
                showarrow=False,
                font=dict(
                    size=11,
                    color=Colors.grey,
                ),
            ),
        ],
        xaxis=dict(
            visible=False,
            range=[-12, 12],  # Double range
            fixedrange=True,
        ),
        yaxis=dict(
            visible=False,
            range=[-df.max() * 0.3, df.max() * 1.5],
            fixedrange=True,
        ),
        height=56,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
        ),
    )

    return fig


def plot_area_code():
    fig = go.Figure()

    df = data.sp.data.groupby('Area Code').Day.count().sort_index()

    fig.update_layout(
        title='<b>Area Code</b>',
        title_x=0.5,
        title_font=dict(
            color=Colors.black,
        ),
        height=222,
        margin=dict(l=0, r=0, t=50, b=25),
        paper_bgcolor=Colors.transparent,
        polar=dict(
            bgcolor=Colors.transparent,
            radialaxis=dict(
                side='counterclockwise',
                showline=False,
                linewidth=1,
                gridcolor=Colors.grey,
                gridwidth=1,
                showticklabels=False,
                range=[0, df.max() * 1.15],
                dtick=df.max() * 0.4,
            ),
            sector=[-180, 180],
            angularaxis=dict(
                direction='clockwise',
                rotation=90,
                showline=True,
                linecolor=Colors.grey,
            ),
            gridshape='linear',
        ),
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
    )

    fig.add_trace(
        go.Scatterpolar(
            r=df.values.tolist() + [df.values[0]],
            theta=[f'<b>{i}</b>' for i in df.index.tolist() + [df.index[0]]],
            fill='toself',
            fillcolor=Colors.green.opacity(0.1),
            mode='lines',
            name='Area Code',
        ),
    )

    return fig


def plot_fees_by_model_team():
    df = data.sp.data.groupby(['Sale Team', 'Training Models'], as_index=False)['Paid Fees'].sum()

    df['Sale Team'] = df['Sale Team'].apply(lambda x: f'<b>{x}</b>')
    df['Training Models'] = df['Training Models'].apply(
        lambda x: f'<b>{x}</b>',
    )

    fig = go.Figure(
        [
            go.Bar(
                x=df[df['Training Models'] == model][
                    [
                        'Sale Team',
                        'Training Models',
                    ]
                ].T,
                y=df[df['Training Models'] == model]['Paid Fees'],
                name=model,
                marker_color=Colors.blue,
            )
            for model in df['Training Models'].unique()
        ],
    )

    fig.update_layout(
        title=f'''<b>Training Models Fees <span style='color: {Colors.grey}'>by Sales Team</span></b>''',
        title_font=dict(
            size=15,
            color=Colors.black,
        ),
        title_x=0.05,
        bargap=0.6,
        showlegend=False,
        yaxis=dict(
            visible=False,
        ),
        xaxis=dict(
            # TODO: disable separator
        ),
        height=224,
        margin=dict(l=10, r=10, t=50, b=45),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
            size=11,
            color=Colors.grey,
        ),
    )

    fig.update_xaxes(tickangle=0)
    return fig


def plot_training_models():
    fig = go.Figure()

    df = data.sp.data['Training Models'].value_counts() / 10

    fig.add_trace(
        go.Pie(
            labels=df.index,
            values=df.values,
            hole=0.9,
            textposition='outside',
            textinfo='value',
            texttemplate='%{value}B',
            sort=True,
            direction='clockwise',
        ),
    )

    fig.update_layout(
        legend=dict(
            orientation='h',
            y=0,
            x=0.2,
            font=dict(
                size=11,
            ),
        ),
        annotations=[
            dict(
                x=0.5,
                y=0.5,
                text=f'<b>Training<br>Models</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=16,
                ),
            ),
        ],
        margin=dict(l=0, r=0, t=0, b=50),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
        ),
        height=224,
    )

    return fig


def plot_sales_by_team():
    df = data.sp.data.groupby('Sale Team')['Paid Fees'].sum().sort_values(ascending=False)

    fig = make_subplots(
        rows=len(df.index),
        cols=1,
        subplot_titles=[i for i in df.index],
        shared_xaxes=True,
        print_grid=False,
        vertical_spacing=(0.45 / len(df.index)),
    )

    for i, team in enumerate(df.index):
        fig.add_trace(
            go.Bar(
                x=[df.loc[team]],
                y=[team],
                orientation='h',
                marker_color=Colors.blue,
                text=[df.loc[team] / 1e9],
                textposition='outside',
                # TODO: add text as separate trace with second y axis
            ),
            row=i + 1,
            col=1,
        )

    for annotation in fig['layout']['annotations']:
        annotation['x'] = 0.025
        annotation['xanchor'] = 'left'
        annotation['align'] = 'left'
        annotation['font'] = dict(
            size=12,
        )

    for axis in fig['layout']:
        if axis.startswith('yaxis') or axis.startswith('xaxis'):
            fig['layout'][axis]['visible'] = False

    fig.update_layout(
        annotations=[
            # TODO: add annotations
            # dict(
            #     x=0.9,
            #     y=2.45,
            #     text=f'''<b>{df.index[0]}</b>''',
            #     showarrow=False,
            #     xref='paper',
            #     yref='paper',
            #     font=dict(
            #         size=16,
            #         color=Colors.black,
            #     ),
            # ),
            # dict(
            #     x=0.93,
            #     y=2.15,
            #     text=f'''<b>{df.max()/1e9}M</b>''',
            #     showarrow=False,
            #     xref='paper',
            #     yref='paper',
            #     font=dict(
            #         size=18,
            #         color=Colors.black,
            #     ),
            # ),
            # dict(
            #     # x=0.97,
            #     # y=1.85,
            #     text=f'<b>Top selling Sales Team</b>',
            #     showarrow=False,
            #     xref='x1',
            #     yref='y1',
            #     font=dict(
            #         size=10,
            #         color=Colors.grey,
            #     ),
            # ),
        ],
        showlegend=False,
        bargap=0.6,
        title=f'''<b>Total sales <span style='color: {Colors.grey}'>by <br>Sales Team</span></b>''',
        title_font=dict(
            size=14,
        ),
        title_y=0.87,
        title_x=0.05,
        margin=dict(l=15, r=25, t=90, b=10),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        xaxis=dict(
            range=[0, df.max() * 1.1],
            visible=False,
        ),
        yaxis=dict(
            visible=False,
        ),
        font=dict(
            family='Inter',
        ),
    )

    return fig


def plot_fees_by_consultant():
    fig = go.Figure()

    df = data.sp.data.groupby(['Consultant', 'Training Models'], as_index=False)['Paid Fees'].sum()

    colors = __get_colors(df['Training Models'])

    for i, model in enumerate(df['Training Models'].unique()):
        model_part = df.query(
            '`Training Models` == @model',
        ).sort_values(by='Consultant')
        fig.add_trace(
            go.Scatter(
                x=model_part.Consultant,
                y=model_part['Paid Fees'],
                name=model,
                marker_color=colors[i],
                mode='lines',
            ),
        )

    fig.update_layout(
        title=f'''<b>Training Models Fees <span style='color: {Colors.grey}'>by Consultant</span></b>''',
        title_x=0.03,
        title_y=0.1,
        title_font=dict(
            size=13,
            color=Colors.black,
        ),
        legend=dict(
            orientation='h',
            y=-0.3,
            x=0.45,
            # xanchor='left',
            font=dict(
                size=11,
            ),
        ),
        xaxis_tickangle=-45,
        yaxis=dict(
            range=[0, df['Paid Fees'].max() * 1.25],
            gridcolor=Colors.grey.opacity(0.5),
            dtick=df['Paid Fees'].max() / 5,
        ),
        margin=dict(l=15, r=10, t=25, b=75),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        font=dict(
            family='Inter',
            color=Colors.grey,
            size=11,
        ),
        hovermode='x unified',
    )

    return fig


def plot_fees_by_month():
    fig = go.Figure()

    df = data.sp.data.groupby('Month', as_index=False)['Paid Fees'].sum()

    high = df['Paid Fees'].max()
    avg = df['Paid Fees'].mean()
    low = df['Paid Fees'].min()

    fig.add_trace(
        go.Scatter(
            x=df.Month,
            y=df['Paid Fees'],
            mode='lines',
            line_shape='spline',
            line=dict(
                color=Colors.blue,
                width=2,
            ),
            text=[str(i) + 'B' for i in df['Paid Fees'] / 1e9],
            textposition='top center',
        ),
    )

    fig.update_layout(
        title='<b>Total Earnings by Month</b>',
        title_font=dict(
            size=15,
        ),
        title_y=1,
        title_x=0.05,
        margin=dict(l=25, r=25, t=0, b=25),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=140,
        xaxis=dict(
            visible=False,
        ),
        yaxis=dict(
            visible=False,
            range=[-high * 0.1, high * 1.5],
        ),
    )

    return fig, high, avg, low


def plot_courses_by_time():
    fig = go.Figure()

    df = data.sp.data.groupby(
        'Month'
        if len(
            data.sp.data.Month.unique(),
        )
        > 1
        else 'Day',
    )['Enrolled Courses'].count()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df,
            mode='lines',
            line=dict(
                color=Colors.blue,
                width=2,
            ),
        ),
    )

    fig.update_layout(
        title='<b>Enrolled Courses</b>',
        title_font=dict(
            size=14,
            color=Colors.black,
        ),
        title_x=0.07,
        title_y=0.9,
        margin=dict(l=10, r=10, t=100, b=20),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        xaxis=dict(
            visible=False,
        ),
        yaxis=dict(
            visible=False,
        ),
        annotations=[
            dict(
                x=0.0,
                y=1.5,
                text=f'<b>{df.sum():,}</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    color=Colors.blue,
                    size=25,
                ),
            ),
            dict(
                x=0.825,
                y=1.37,
                text='<b>Courses</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=10,
                ),
            ),
            dict(
                x=0.01,
                y=1.1,
                text='<b>Average</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=0.01,
                y=0.85,
                text=f'<b>{data.sp.data.groupby("Consultant")["Enrolled Courses"].mean().mean():.3} ~</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=18,
                    color=Colors.orange,
                ),
            ),
        ],
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        dragmode=False,
    )

    return fig


def plot_paid_unpaid_calls():
    fig = make_subplots(
        rows=2,
        cols=1,
        specs=[[{'type': 'domain'}], [{'type': 'domain'}]],
    )

    paid = (data.sp.data['Paid Fees'] != 0).sum()
    unpaid = (data.sp.data['Paid Fees'] == 0).sum()

    fig.add_trace(
        go.Pie(
            labels=['Paid', 'Total'],
            values=[paid, unpaid],
            hole=0.85,
            marker_colors=[Colors.green, Colors.grey.opacity(0.5)],
            textinfo='none',
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Pie(
            labels=['Unpaid', 'Total'],
            values=[unpaid, paid],
            hole=0.85,
            marker_colors=[Colors.red, Colors.grey.opacity(0.5)],
            textinfo='none',
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=100, t=25, b=25),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        annotations=[
            dict(
                x=1.6,
                y=0.95,
                text=f'<b>Total Paid</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=1.27,
                y=0.825,
                text=f'<b>{paid:,}</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    color=Colors.black,
                    size=16,
                ),
            ),
            dict(
                x=1.23,
                y=0.7,
                text=f'<b>Calls</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=10,
                ),
            ),
            dict(
                x=1.8,
                y=0.28,
                text=f'<b>Total Unpaid</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=14,
                ),
            ),
            dict(
                x=1.24,
                y=0.155,
                text=f'<b>{unpaid:,}</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    color=Colors.black,
                    size=16,
                ),
            ),
            dict(
                x=1.24,
                y=0.06,
                text=f'<b>Calls</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=10,
                ),
            ),
            dict(
                x=0.5,
                y=0.85,
                text=f'<b>{paid/(paid+unpaid):.0%}</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=16,
                    color=Colors.black,
                ),
            ),
            dict(
                x=0.5,
                y=0.15,
                text=f'<b>{unpaid/(paid+unpaid):.0%}</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=16,
                    color=Colors.black,
                ),
            ),
        ],
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
    )

    return fig


def plot_sales_by_consultant():
    fig = go.Figure()

    df = data.sp.data.groupby('Consultant', as_index=False)['Paid Fees'].sum().sort_values('Consultant')

    fig.add_trace(
        go.Bar(
            x=df['Consultant'],
            y=df['Paid Fees'],
            marker_color=Colors.blue,
            text=df['Paid Fees'] / 1e9,
            textposition='outside',
            texttemplate='%{text:.2s}',
            textangle=-90,
        ),
    )

    fig.update_layout(
        bargap=0.4,
        showlegend=False,
        margin=dict(l=10, r=10, t=100, b=25),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        title=f'''<b>Consultant <span style='color: {Colors.grey}; font-size: 14px;'><br>by total sales</span></b>''',
        title_font=dict(
            size=16,
            color=Colors.black,
        ),
        title_y=0.87,
        title_x=0.03,
        xaxis=dict(
            showgrid=False,
            tickangle=-45,
        ),
        yaxis=dict(
            visible=False,
        ),
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        annotations=[
            dict(
                x=0.93,
                y=2.45,
                text=f'''<b>{df.sort_values('Paid Fees', ascending=False).Consultant.iloc[0]}</b>''',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=16,
                    color=Colors.black,
                ),
            ),
            dict(
                x=0.93,
                y=2.15,
                text=f'''<b>{df['Paid Fees'].max()/1e6}M</b>''',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=18,
                    color=Colors.black,
                ),
            ),
            dict(
                x=0.97,
                y=1.85,
                text=f'<b>Top selling Consultant</b>',
                showarrow=False,
                xref='paper',
                yref='paper',
                font=dict(
                    size=10,
                    color=Colors.grey,
                ),
            ),
        ],
    )

    return fig


def plot_advertisements(value):
    fig = go.Figure()

    dt = 'Month' if data.sp.data.Month.unique().size > 1 else 'Day'
    df = data.sp.data.groupby([dt, 'Advertisement'], as_index=False)['Paid Fees'].sum()

    colors = __get_colors(df.Advertisement)

    for i, advertisement in enumerate(df.Advertisement.dropna().unique()[:value]):
        advertisement_part = df.query('Advertisement == @advertisement')
        fig.add_trace(
            go.Scatter(
                x=advertisement_part[dt],
                y=advertisement_part['Paid Fees'],
                marker_color=colors[i],
                mode='lines',
                name=advertisement,
            ),
        )

    fig.update_layout(
        showlegend=True,
        margin=dict(l=10, r=10, t=55, b=25),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        height=224,
        title=f'''<b>Advertisement <span style='color: {Colors.grey}; font-size: 14px;'><br>by total sales</span></b>''',
        title_font=dict(
            size=16,
            color=Colors.black,
        ),
        title_y=0.9,
        title_x=0.03,
        yaxis=dict(
            range=[0, df['Paid Fees'].max() * 1.25],
            gridcolor=Colors.grey.opacity(0.5),
            dtick=df['Paid Fees'].max() / 5,
        ),
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        hovermode='x unified',
    )

    return fig


def plot_training_levels_courses():
    fig = go.Figure()

    df = (
        data.sp.data.groupby('Training Levels', as_index=False)['Enrolled Courses']
        .sum()
        .sort_values(by='Training Levels', ascending=False)
    )

    fig.add_trace(
        go.Scatter(
            x=df['Training Levels'],
            y=df['Enrolled Courses'],
            mode='lines+markers',
            marker_color=Colors.blue,
            line_color=Colors.blue,
        ),
    )

    fig.update_layout(
        title='''<b>Enrolled Courses by Training Levels</b>''',
        title_font=dict(
            size=13,
            family='Inter',
            color=Colors.grey,
        ),
        title_y=0.9,
        showlegend=False,
        margin=dict(l=20, r=20, t=50, b=0),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        yaxis=dict(
            range=[0, df['Enrolled Courses'].max() * 1.25],
            gridcolor=Colors.grey.opacity(0.5),
            dtick=df['Enrolled Courses'].max() / 5,
            showticklabels=False,
        ),
        xaxis=dict(
            tickangle=-45,
        ),
        height=224,
    )

    return fig


def plot_training_levels_fees():
    fig = go.Figure()

    df = (
        data.sp.data.groupby('Training Levels', as_index=False)['Paid Fees']
        .count()
        .sort_values(by='Training Levels', ascending=False)
    )

    fig.add_trace(
        go.Bar(
            x=df['Paid Fees'],
            y=df['Training Levels'],
            orientation='h',
            marker_color=Colors.blue,
        ),
    )

    fig.update_layout(
        title='''<b>Training Level's Fees</b>''',
        title_font=dict(
            size=16,
            family='Inter',
            color=Colors.grey,
        ),
        title_y=0.9,
        bargap=0.6,
        showlegend=False,
        height=224,
        margin=dict(l=70, r=20, t=50, b=0),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        xaxis=dict(
            visible=False,
        ),
    )

    return fig


def plot_average_call():
    fig = go.Figure()

    dt = 'Month' if data.sp.data.Month.unique().size > 1 else 'Day'
    df = (
        pd.concat(
            [
                data.sp.data.query('`Paid Fees` > 0')[dt],
                pd.to_datetime(
                    data.sp.data.query('`Paid Fees` > 0')['Average call duration'],
                    format='%H:%M:%S',
                ),
            ],
            axis=1,
        )
        .groupby(dt, as_index=False)
        .mean()
    )

    min_call = df['Average call duration'].min()
    max_call = df['Average call duration'].max()

    fig.add_trace(
        go.Scatter(
            x=df[dt],
            y=df['Average call duration'],
            mode='markers',
            marker_color=Colors.blue,
            marker_size=10,
            name='Average',
        ),
    )

    fig.add_trace(
        go.Scatter(
            x=[df[df['Average call duration'] == min_call][dt].values[0]],
            y=[min_call],
            mode='markers',
            marker_color=Colors.green,
            marker_size=10,
            name='Min',
        ),
    )

    fig.add_trace(
        go.Scatter(
            x=[df[df['Average call duration'] == max_call][dt].values[0]],
            y=[max_call],
            mode='markers',
            marker_color=Colors.red,
            marker_size=10,
            name='Max',
        ),
    )

    fig.update_layout(
        showlegend=False,
        height=224,
        margin=dict(l=20, r=20, t=10, b=50),
        width=366,
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        font=dict(
            family='Inter',
            color=Colors.grey,
        ),
        xaxis=dict(
            tickangle=-45,
        ),
        yaxis=dict(
            gridcolor=Colors.grey.opacity(0.5),
            gridwidth=1,
            griddash='dot',
            tickformat='%M:%S',
        ),
    )

    return [
        fig,
        df['Average call duration'].mean().strftime('%M:%S'),
        df['Average call duration'].min().strftime('%M:%S'),
        df['Average call duration'].max().strftime('%M:%S'),
        dt,
    ]


def pie_factory(c, h, column, k1, k2, color):
    return go.Pie(
        values=[
            k1,
            k2 - k1,
        ],
        labels=[f'{column}', 'Total'],
        domain={
            'x': [0 + c, 1 - c],
            'y': [0 + c, 1 - c],
        },
        hole=h,
        sort=False,
        marker={
            'colors': [
                color,
                Colors.grey.opacity(0.3),
            ],
        },
        showlegend=False,
        # rotation=180,
        textinfo='none',
        name=column,
    )


def plot_advertisement_channel():
    fig = go.Figure()

    df = data.sp.data.groupby('Advertising Channel')['Paid Fees'].sum().sort_values(ascending=False).head(6)

    colors = __get_colors(df.index)

    fig.add_trace(pie_factory(0.000, 0.93, df.index[0], df.iloc[0], df.sum(), colors[0]))
    fig.add_trace(pie_factory(0.050, 0.91, df.index[1], df.iloc[1], df.sum(), colors[1]))
    fig.add_trace(pie_factory(0.105, 0.89, df.index[2], df.iloc[2], df.sum(), colors[2]))
    fig.add_trace(pie_factory(0.160, 0.87, df.index[3], df.iloc[3], df.sum(), colors[3]))
    fig.add_trace(pie_factory(0.215, 0.85, df.index[4], df.iloc[4], df.sum(), colors[4]))
    fig.add_trace(pie_factory(0.270, 0.83, df.index[5], df.iloc[5], df.sum(), colors[5]))

    fig.update_layout(
        title='<b>Advertising Channels</b>',
        title_x=0.03,
        title_y=0.95,
        height=255,
        margin=dict(l=0, r=0, t=35, b=0),
        paper_bgcolor=Colors.transparent,
        plot_bgcolor=Colors.transparent,
        annotations=[
            dict(
                text=f'<b>{df.sum()/1e9:.1f}B</b>',
                x=0.5,
                y=0.45,
                showarrow=False,
                font=dict(
                    size=20,
                ),
            ),
            dict(
                text=f'<b>Paid<br>Advertisement</b>',
                x=0.5,
                y=0.55,
                showarrow=False,
                font=dict(
                    size=8,
                ),
            ),
        ],
    )

    return fig
