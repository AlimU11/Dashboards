import plotly.graph_objects as go


class PreviewGraphs:
    # TODO: add preview graphs
    def __init__(self):
        self._videogame_sales: go.Figure = self.__videogame_sales()
        self._hr_analytics: go.Figure = self.__hr_analytics()

    def __videogame_sales(self) -> go.Figure:
        videogame_sales = go.Figure()
        videogame_sales.update_layout(
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),
        )

        return videogame_sales

    def __hr_analytics(self) -> go.Figure:
        hr_analytics = go.Figure()
        hr_analytics.update_layout(
            height=200,
            margin=dict(l=0, r=0, t=0, b=0),
        )

        return hr_analytics

    @property
    def videogame_sales(self) -> go.Figure:
        return self._videogame_sales

    @property
    def hr_analytics(self) -> go.Figure:
        return self._hr_analytics


preview_graphs = PreviewGraphs()
