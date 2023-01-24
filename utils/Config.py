import plotly.graph_objects as go
from pydantic import BaseSettings

from utils.PreviewGraphs import preview_graphs as pg


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
            button_text='Examine',
            icon='people-group',
        ),
    ]

    videogame_sales_data_path: str = 'data/vgsales.csv'
    videogame_sales_top_n_publishers_default: int = 5
    videogame_sales_top_n_games_default: int = 10

    hr_analytics_data_path: str = 'data/HR Data.csv'


config = Config()
