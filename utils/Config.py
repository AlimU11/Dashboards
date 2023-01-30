import plotly.graph_objects as go
from pydantic import BaseSettings

from .PreviewGraphs import preview_graphs as pg


class Config(BaseSettings):
    class Project(BaseSettings):
        name: str
        fig: go.Figure
        description: str
        button_text: str
        icon: str

    projects: list[Project] = [
        Project(
            name='VideoGame Sales',
            fig=pg.videogame_sales,
            description='Analysis of video game sales data from 1980 to 2020',
            button_text='Explore',
            icon='gamepad',
        ),
        Project(
            name='HR Analytics',
            fig=pg.hr_analytics,
            description='Analysis of employees\' attrition',
            button_text='Inspect',
            icon='people-group',
        ),
        Project(
            name='Sales Performance',
            fig=pg.sales_performance,
            description='Analysis of sales performance of a company',
            button_text='View',
            icon='phone-volume',
        ),
    ]

    vg_data_path: str = 'https://raw.githubusercontent.com/AlimU11/Dashboards/master/data/vgsales.csv'
    vg_default_top_n_publishers: int = 5
    vg_default_top_n_games: int = 10

    hr_data_path: str = 'https://raw.githubusercontent.com/AlimU11/Dashboards/master/data/HR%20data.csv'
    hr_default_bin_size: int = 3

    sp_data_path: str = 'https://github.com/AlimU11/Dashboards/blob/master/data/sp%20data.xlsx?raw=true'
    sp_default_total_advetisement: int = 5


config = Config()
