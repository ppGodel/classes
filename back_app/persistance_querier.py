from datetime import datetime
from typing import Optional, Dict, Callable, Union
from pandas import DataFrame
from util.date_formatter import convert_date_str
attendance_list_dict = Dict[str, Union[str, Dict[str, str]]]


def get_attendance_list_from_mock(class_name: str, attendance_date: datetime.date) -> attendance_list_dict:
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


def get_student_names(class_id: str) -> DataFrame:
    pass


def get_class_info(class_id) -> Dict:
    pass


def transform_attendance_list_to_dict(attendance_list: DataFrame) -> attendance_list_dict:
    attendance_df = attendance_list.reset_index('student_id')
    class_id, attendance_date = attendance_df.index.get_values()[0]
    attendance_df[attendance_df['attendance'], 'attendance'] = 'checked'
    attendance_df[not attendance_df['attendance'], 'attendance'] = ''
    student_names = get_student_names(class_id)
    student_attendance_list = student_names.join(attendance_df, on='student_id')
    class_info = get_class_info(class_id)
    return {'name': class_info['name'], 'teacher': class_info['teacher'], 'date': attendance_date, 'students': student_attendance_list }


def transform_dict_to_attendance_list(attendance_list: Dict) -> DataFrame:
    pass


def get_attendance_list_from(get_df_by_date_class: Callable[[str, str], DataFrame],
                             create_attendance_list_for_date: Callable[[str, str], DataFrame],
                             class_name: str, attendance_date: datetime.date) -> \
        Optional[Dict[str, str]]:
    attendance_list = get_df_by_date_class(class_name, attendance_date)
    if attendance_list.empty:
        attendance_list = create_attendance_list_for_date(class_name, attendance_date)
    return transform_attendance_list_to_dict(attendance_list)

