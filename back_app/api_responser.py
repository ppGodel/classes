from datetime import date
from functools import partial
from typing import Dict, Union
from pandas import DataFrame
from back_app import persistance_querier, csv_querier

get_attendance_list_from = partial(persistance_querier.get_attendance_list_from,
                                   csv_querier.get_df_from_csv_by_query,
                                   csv_querier.create_attendance_list_for_date)


def get_classes_dict(class_name: str, attendance_date: date) -> Dict[str, Union[str, Dict[str, str]]]:
    return get_attendance_list_from(class_name, attendance_date)



def save_attendance_list(attendance_list: DataFrame):
    csv_querier.save_attendance_list(attendance_list)
    return 'List Accepted'
