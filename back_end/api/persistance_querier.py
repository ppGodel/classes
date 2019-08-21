from datetime import datetime
from util.constants import attendance_list_dict_type
from typing import Dict, Callable
from pandas import DataFrame
from util.date_formatter import convert_date_str


def get_attendance_list_from_mock(class_name: str, attendance_date: datetime.date) -> attendance_list_dict_type:
    date_today = convert_date_str(datetime.combine(attendance_date, datetime.min.time()))  # type: str
    classes_info = {
        'automata': {
            'class_id': 'TDA_AD_19',
            'name': 'Automata Theory',
            'teacher': 'JAHS',
            'date': date_today,
            'students': [
                {
                    'student_id': '1000001',
                    'full_name': 'student1',
                    'attendance': 'checked'
                },
                {
                    'student_id': '1000002',
                    'full_name': 'student2',
                    'attendance': ''
                }
            ]
        },
        'db': {
            'class_id': 'DB_AD_19',
            'class_name': 'Database',
            'teacher': 'JAHS',
            'date': date_today,
            'students': [
                {
                    'student_id': '0000001',
                    'full_name': 'student1',
                    'attendance': ''
                },
                {
                    'student_id': '0000002',
                    'full_name': 'student2',
                    'attendance': ''
                }
            ]
        }
    }
    return classes_info[class_name]


def get_attendance_list_from(get_attendance_df_by_class_date: Callable[[str, str], DataFrame],
                             create_attendance_df_class_date: Callable[[str, str], DataFrame],
                             transform_attendance_list_to_dict: Callable[[DataFrame], Dict],
                             class_name: str, attendance_date: datetime.date) -> attendance_list_dict_type:
    attendance_list = get_attendance_df_by_class_date(class_name, attendance_date)
    if attendance_list.empty:
        attendance_list = create_attendance_df_class_date(class_name, attendance_date)
    return transform_attendance_list_to_dict(attendance_list)


def save_attendance_dict(save_attendance_df: Callable[[Dict], str], attendance_dict: Dict) -> str:
    return save_attendance_df(attendance_dict)