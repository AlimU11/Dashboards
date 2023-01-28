import plotly.graph_objects as go

from utils.AppData import data


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
                color='#DC3912',
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
                x=0.75,
                y=0.85,
                xref='paper',
                yref='paper',
                text='<b>Calls</b>',
                showarrow=False,
                font=dict(
                    size=11,
                    color='#7F7F7F',
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
        width=274,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
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
        height=222,
        width=288,
        margin=dict(l=0, r=0, t=50, b=25),
        paper_bgcolor='rgba(0,0,0,0)',
        polar=dict(
            bgcolor='rgba(0,0,0,0)',
            radialaxis=dict(
                side='counterclockwise',
                showline=False,
                linewidth=1,
                gridcolor='rgb(153, 153, 153)',
                gridwidth=1,
                showticklabels=False,
            ),
        ),
    )

    fig.add_trace(
        go.Scatterpolar(
            r=df.values.tolist() + [df.values[0]],
            theta=df.index.tolist() + [df.index[0]],
            # TODO: change fill color
            fill='toself',
            fillcolor='rgba(0, 204, 150, 0.1)',
            mode='lines',
        ),
    )

    fig.update_polars(sector=[-180, 180], angularaxis=dict(direction='clockwise', rotation=90))

    return fig


def plot_fees_by_model_team():
    df = data.sp.data.groupby(['Sale Team', 'Training Models'], as_index=False)['Paid Fees'].sum()

    fig = go.Figure(
        [
            go.Bar(
                x=df[df['Training Models'] == model][['Sale Team', 'Training Models']].T,
                y=df[df['Training Models'] == model]['Paid Fees'],
                name=model,
                marker_color='#636EFA',
            )
            for model in df['Training Models'].unique()
        ],
    )

    fig.update_layout(
        title='''<b>Training Models Fees <span style='color: rgb(153,153,153)'>by Sales Team</span></b>''',
        title_font=dict(
            size=15,
        ),
        title_x=0,
        bargap=0.6,
        showlegend=False,
        yaxis=dict(
            visible=False,
        ),
        xaxis=dict(
            # TODO: disable separator
        ),
        width=360,
        height=224,
        margin=dict(l=0, r=35, t=25, b=70),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family='Inter',
            size=12,
        ),
    )

    fig.update_xaxes(tickangle=0)
    return fig
