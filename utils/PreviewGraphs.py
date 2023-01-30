import plotly.graph_objects as go

from .Colors import Colors


class PreviewGraphs:
    """Preview graphs for different projects with dummy data"""

    def __init__(self):
        self._videogame_sales: go.Figure = self.__videogame_sales()
        self._hr_analytics: go.Figure = self.__hr_analytics()
        self._sales_performance: go.Figure = self.__sales_performance()

    def __videogame_sales(self) -> go.Figure:
        vg = go.Figure()
        vg.update_layout(
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),
        )

        vg.add_trace(
            go.Scatter(
                x=[2001, 2002, 2003, 2004, 2005, 2006],
                y=[10, 20, 33, 100, 70, 120],
                name='Sony',
                stackgroup='one',
            ),
        )

        vg.add_trace(
            go.Scatter(
                x=[2001, 2002, 2003, 2004, 2005, 2006],
                y=[100, 100, 77, 20, 115, 25],
                name='Electronic Arts',
                stackgroup='one',
            ),
        )

        vg.add_trace(
            go.Scatter(
                x=[2001, 2002, 2003, 2004, 2005, 2006],
                y=[50, 105, 115, 135, 70, 150],
                name='Nintendo',
                stackgroup='one',
            ),
        )

        vg.update_layout(
            legend=dict(
                orientation='h',
                y=0,
            ),
            yaxis=dict(
                tickprefix='$',
                ticksuffix='M',
                visible=False,
            ),
            xaxis=dict(
                visible=False,
            ),
            paper_bgcolor=Colors.transparent,
            plot_bgcolor=Colors.transparent,
            dragmode=False,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(
                family='Inter',
                size=14,
                color=Colors.black,
            ),
        )

        return vg

    def __hr_analytics(self) -> go.Figure:
        hr = go.Figure()

        hr.add_trace(
            go.Pie(
                labels=['HR', 'Sales', 'R&D'],
                values=[40, 90, 130],
                sort=True,
                direction='clockwise',
                textposition='inside',
                textinfo='label+percent',
                textfont=dict(
                    color=Colors.white,
                ),
            ),
        )

        hr.update_layout(
            showlegend=False,
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(
                family='Inter',
                size=16,
                color=Colors.white,
            ),
            paper_bgcolor=Colors.transparent,
            plot_bgcolor=Colors.transparent,
            dragmode=False,
        )

        return hr

    def __sales_performance(self) -> go.Figure:
        sp = go.Figure()

        sp.update_layout(
            height=200,
            margin=dict(l=0, r=0, t=15, b=0),
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
                    range=[0, 105 * 1.15],
                    dtick=105 * 0.4,
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

        sp.add_trace(
            go.Scatterpolar(
                r=[105, 90, 95, 50, 75, 105],
                theta=['<b>A1</b>', '<b>A2</b>', '<b>B1</b>', '<b>B2</b>', '<b>C1</b>', '<b>A1</b>'],
                fill='toself',
                fillcolor=Colors.green.opacity(0.1),
                mode='lines',
                name='Area Code',
            ),
        )

        return sp

    @property
    def videogame_sales(self) -> go.Figure:
        return self._videogame_sales

    @property
    def hr_analytics(self) -> go.Figure:
        return self._hr_analytics

    @property
    def sales_performance(self) -> go.Figure:
        return self._sales_performance


preview_graphs = PreviewGraphs()
