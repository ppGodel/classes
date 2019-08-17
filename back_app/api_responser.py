from datetime import date, datetime
from typing import Dict, Union

from util.date_formatter import convert_date_str


def get_classes_dict(class_name: str, attendance_date: date) -> Dict[str, Union[str, Dict[str, str]]]:
    date_today = convert_date_str(datetime.combine(attendance_date, datetime.min.time()))  # type: str
    classes_info = {
        'automata': {
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
            'name': 'Database',
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


def save_attendance_list(attendance_list: Dict):
    return 'List Accepted'
