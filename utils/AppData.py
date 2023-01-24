import pandas as pd
from pandas import DataFrame

from .Config import config


class AppData:
    def __init__(self) -> None:
        self.__videogame_sales: dict = {
            'data': None,
            'top_n_publishers': None,
            'top_n_games': None,
            'region': None,
            'years_range': None,
        }

        self.__hr_analytics: dict = {
            'data': None,
            'attrition': None,
            'education': None,
            'education_list': None,
        }

        self.read_data()
        self.videogame_sales_update()

    def read_data(self):
        self.__videogame_sales['data'] = pd.read_csv(
            config.videogame_sales_data_path,
        )
        self.__videogame_sales['top_n_publishers'] = int(
            config.videogame_sales_top_n_publishers_default,
        )
        self.__videogame_sales['top_n_games'] = int(
            config.videogame_sales_top_n_games_default,
        )

        self.__hr_analytics['data'] = pd.read_csv(
            config.hr_analytics_data_path,
        )
        self.__hr_analytics['attrition'] = self.__hr_analytics['data'].query(
            'Attrition == "Yes"',
        )
        self.__hr_analytics['education_list'] = self.__hr_analytics['data'].Education.unique()

    def videogame_sales_update(self):
        columns = ['Name', 'Platform', 'Year', 'Genre', 'Publisher']

        df_region = pd.DataFrame(
            columns=columns + ['Region'],
        )

        for sales in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']:
            df_part = self.__videogame_sales['data'][columns + [sales]].copy()
            df_part.columns = columns + ['Sales']
            df_part.loc[:, 'Region'] = sales.split('_')[0]

            df_region = pd.concat(
                [
                    df_region,
                    df_part,
                ],
            )

        self.__videogame_sales['data_region'] = df_region

    @property
    def videogame_sales(self) -> dict:
        return self.__videogame_sales

    @videogame_sales.setter
    def videogame_sales(self, value: dict) -> None:
        self.__videogame_sales = value

    @property
    def hr_analytics(self) -> dict:
        return self.__hr_analytics

    @property
    def hr_analytics_data(self) -> DataFrame:
        return self.__hr_analytics['data'][
            self.__hr_analytics['data'].Education.isin(
                [self.__hr_analytics['education']]
                if self.__hr_analytics['education'] != 'All'
                else self.__hr_analytics['education_list'],
            )
        ]

    @property
    def hr_attrition(self) -> DataFrame:
        return self.__hr_analytics['attrition'][
            self.__hr_analytics['attrition'].Education.isin(
                [self.__hr_analytics['education']]
                if self.__hr_analytics['education'] != 'All'
                else self.__hr_analytics['education_list'],
            )
        ]

    @property
    def hr_education(self) -> list:
        return self.__hr_analytics['data']['Education'].unique().tolist()

    @hr_analytics.setter
    def hr_analytics(self, value: dict) -> None:
        self.__hr_analytics = value


app_data = AppData()
