from enum import Enum, auto


class IdHolder(Enum):
    home = auto()

    UNDEFINED = auto()

    # Videogame Sales

    videogame_sales = auto()
    vg_callback_dispatcher = auto()

    vg_sales_amount_title = auto()
    vg_sales_amount_description = auto()

    vg_top_game_title = auto()
    vg_top_game_description = auto()

    vg_top_freq_platform_title = auto()
    vg_top_freq_platform_description = auto()

    vg_trending_genre_title = auto()
    vg_trending_genre_description = auto()

    vg_by_publisher_title = auto()
    vg_by_publisher = auto()

    vg_by_genre_title = auto()
    vg_by_genre = auto()

    vg_top_games_title = auto()
    vg_top_games = auto()

    vg_genre_by_year_title = auto()
    vg_genre_by_year = auto()

    vg_genre_by_platform_title = auto()
    vg_genre_by_platform = auto()

    vg_rank_by_year_title = auto()
    vg_rank_by_year = auto()

    vg_region_platform_genre_title = auto()
    vg_region_platform_genre = auto()

    vg_years_range = auto()
    vg_top_n_publishers = auto()
    vg_top_n_games = auto()
    vg_region = auto()

    vg_genre_1_title = auto()
    vg_genre_2_title = auto()
    vg_genre_3_title = auto()
    vg_genre_4_title = auto()
    vg_genre_5_title = auto()
    vg_genre_6_title = auto()
    vg_genre_7_title = auto()
    vg_genre_8_title = auto()
    vg_genre_9_title = auto()
    vg_genre_10_title = auto()
    vg_genre_11_title = auto()
    vg_genre_12_title = auto()

    vg_genre_1 = auto()
    vg_genre_2 = auto()
    vg_genre_3 = auto()
    vg_genre_4 = auto()
    vg_genre_5 = auto()
    vg_genre_6 = auto()
    vg_genre_7 = auto()
    vg_genre_8 = auto()
    vg_genre_9 = auto()
    vg_genre_10 = auto()
    vg_genre_11 = auto()
    vg_genre_12 = auto()

    ###

    market_prices = auto()
    market_prices_graph = auto()

    #  HR Analytics
    hr_analytics = auto()

    hr_callback_dispatcher = auto()
    hr_education_dropdown = auto()
    hr_bin_slider_container = auto()
    hr_bin_slider = auto()

    hr_employee_count_title = auto()
    hr_attrition_count_title = auto()
    hr_attrition_rate_title = auto()
    hr_active_employee_count_title = auto()
    hr_average_age_title = auto()
    hr_average_income_title = auto()

    hr_employee_count = auto()
    hr_attrition_count = auto()
    hr_attrition_rate = auto()
    hr_active_employee_count = auto()
    hr_average_age = auto()
    hr_average_income = auto()

    hr_attrition_by_gender_title = auto()
    hr_attrition_by_gender_graph = auto()

    hr_attrition_by_department_title = auto()
    hr_attrition_by_department_graph = auto()

    hr_employees_by_age_group_title = auto()
    hr_employees_by_age_group_graph = auto()

    hr_job_satisfaction_title = auto()
    hr_job_satisfaction_table = auto()

    hr_attrition_by_education_title = auto()
    hr_attrition_by_education_graph = auto()

    hr_attrition_by_gender_age_title = auto()
    hr_attrition_by_gender_age_graph = auto()

    # Sales Performance
    sales_performance = auto()

    sp_callback_dispatcher = auto()

    sp_avg_calls_graph = auto()
