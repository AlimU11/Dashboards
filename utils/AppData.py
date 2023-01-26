from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from pandas import DataFrame, Series

from .Config import config


class AppData:
    @dataclass
    class VideogameSales:

        data: DataFrame
        data_region: DataFrame
        ranged_data: DataFrame
        top_n_publishers: int
        top_n_games: int
        region: str
        years_range: list[int]

        def __init__(self) -> None:
            self.__read_data()
            self.__vg_transform_sales()

        def __read_data(self) -> None:
            self.data = pd.read_csv(config.videogame_sales_data_path)
            self.top_n_publishers = int(config.videogame_sales_top_n_publishers_default)
            self.top_n_games = int(config.videogame_sales_top_n_games_default)

        def __vg_transform_sales(self) -> None:
            """
            Transform sales data from a format where each column represents all sales for a given region,
            to a format where each row represents the sales for a single region.
            """

            columns = ['Name', 'Platform', 'Year', 'Genre', 'Publisher']
            df_region = pd.DataFrame(columns=columns + ['Region'])

            for sales in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']:
                df_part = self.data[columns + [sales]].copy()
                df_part.columns = columns + ['Sales']
                df_part.loc[:, 'Region'] = sales.split('_')[0]
                df_region = pd.concat([df_region, df_part])

            self.data_region = df_region

    @dataclass
    class HrAnalytics:

        data: DataFrame
        is_attrition: Series[bool]
        _education: str
        education_list: list[str]
        _attrition: DataFrame
        _by_education: DataFrame

        def __init__(self) -> None:
            self.__read_data()

        def __read_data(self) -> None:
            self.data = pd.read_csv(config.hr_analytics_data_path)
            self.is_attrition = self.data.Attrition == 'Yes'
            self.education_list = self.data.Education.unique().tolist()

        @property
        def by_education(self) -> DataFrame:
            return self._by_education

        @property
        def attrition(self) -> DataFrame:
            return self._attrition

        @property
        def education(self) -> str:
            return self._education

        @education.setter
        def education(self, value: str) -> None:
            self._education = value

            self._attrition = self.data[self.is_attrition][
                self.data[self.is_attrition].Education.isin(
                    [self.education] if self.education != 'All' else self.education_list,
                )
            ]

            self._by_education = self.data[
                self.data.Education.isin(
                    [self.education] if self.education != 'All' else self.education_list,
                )
            ]

    def __init__(self) -> None:
        self.__vg: AppData.VideogameSales = AppData.VideogameSales()
        self.__hr: AppData.HrAnalytics = AppData.HrAnalytics()

    @property
    def vg(self) -> AppData.VideogameSales:
        return self.__vg

    @property
    def hr(self) -> AppData.HrAnalytics:
        return self.__hr


data = AppData()
