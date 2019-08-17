from datetime import date
from typing import Dict, Union
from back_app import csv_querier

get_attendance_list_from = csv_querier.get_attendance_list_from_mock


def get_classes_dict(class_name: str, attendance_date: date) -> Dict[str, Union[str, Dict[str, str]]]:
    return get_attendance_list_from(class_name, attendance_date)



def save_attendance_list(attendance_list: Dict):
    return 'List Accepted'
