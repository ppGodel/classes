from datetime import date
from functools import partial
from typing import Dict
from back_end.api import csv_querier, persistance_querier
from util.constants import attendance_list_dict_type

# get_attendance_list_from = persistance_querier.get_attendance_list_from_mock

get_attendance_list_from = partial(
    persistance_querier.get_attendance_list_from,
    csv_querier.get_attendance_list_by_class_date,
    csv_querier.create_attendance_list_for_date,
    csv_querier.transform_attendance_list_to_dict)

save_attendance_list_fn = partial(persistance_querier.save_attendance_dict, csv_querier.save_attendance_dict)


def get_classes_dict(class_name: str, attendance_date: date) -> attendance_list_dict_type:
    return get_attendance_list_from(class_name, attendance_date)


def save_attendance_list(attendance_list: Dict):
    try:
        save_result = save_attendance_list_fn(attendance_list)
        return 'List Accepted, {}'.format(save_result)
    except Exception as e:
        return 'Error'.format(e)
