import plotly.graph_objects as go


class PreviewGraphs:
    def __init__(self):
        self._videogame_sales: go.Figure = self.__videogame_sales()
        self._hr_analytics: go.Figure = self.__hr_analytics()

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
                y=1.2,
            ),
            yaxis=dict(
                tickprefix='$',
                ticksuffix='M',
                visible=False,
            ),
            xaxis=dict(
                visible=False,
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            dragmode=False,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(
                family='Inter',
                size=14,
                color='#000000',
            ),
        )

        return vg

    def __hr_analytics(self) -> go.Figure:
        hr_analytics = go.Figure()

        hr_analytics.add_trace(
            go.Pie(
                labels=['HR', 'Sales', 'R&D'],
                values=[40, 90, 130],
                sort=True,
                direction='clockwise',
                textposition='inside',
                textinfo='label+percent',
            ),
        )

        hr_analytics.update_layout(
            showlegend=False,
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),
            font=dict(
                family='Inter',
                size=16,
                color='#FFFFFF',
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            dragmode=False,
        )

        return hr_analytics

    @property
    def videogame_sales(self) -> go.Figure:
        return self._videogame_sales

    @property
    def hr_analytics(self) -> go.Figure:
        return self._hr_analytics


preview_graphs = PreviewGraphs()
