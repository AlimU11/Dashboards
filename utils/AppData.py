import os

import pandas as pd
import yaml

with open('global_config.yaml', 'r') as f:
    config = yaml.safe_load(f)
    for key, value in config.items():
        os.environ[key] = str(value)


class AppData:
    def __init__(self) -> None:
        self.__videogame_sales: dict = {
            'data': None,
            'top_n_publishers': None,
            'top_n_games': None,
            'region': None,
            'years_range': None,
        }

        self.read_data()
        self.videogame_sales_update()

    def read_data(self):
        self.__videogame_sales['data'] = pd.read_csv(os.environ.get('VIDEOGAME_SALES_DATA_PATH'))
        self.__videogame_sales['top_n_publishers'] = int(os.environ.get('VIDEOGAME_SALES_TOP_N_PUBLISHERS_DEFAULT'))
        self.__videogame_sales['top_n_games'] = int(os.environ.get('VIDEOGAME_SALES_TOP_N_GAMES_DEFAULT'))

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


app_data = AppData()
