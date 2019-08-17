from datetime import datetime
from functools import partial
from typing import Optional, Dict
from pandas import DataFrame, read_csv
from util.date_formatter import convert_date_str


def get_df_from_csv(csv_path: str) -> DataFrame:
    return parse_csv_df(csv_path)


def get_df_from_csv_by_query(csv_path: str, query: str) -> DataFrame:
    return get_df_from_csv(csv_path).query(query)


folder_path = "csv_files"
classes_csv_path = "{}/{}".format(folder_path, 'classes.csv')
attendance_csv_path = "{}/{}".format(folder_path, 'class_attendance.csv')
get_df_by_query = partial(get_df_from_csv_by_query, classes_csv_path)


def get_attendance_list_from_mock(class_name: str, attendance_date: datetime.date):
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


def create_attendance_list_for_date(attendance_date):
    pass


def get_attendance_list_from_csv(class_name: str, attendance_date: datetime.date) -> \
        Optional[Dict[str, str]]:
    try:
        attendance_list = get_df_by_query('date={}'.format(attendance_date))
        if not attendance_date or attendance_list.empty:
            attendance_list = create_attendance_list_for_date(attendance_date)
        return attendance_list
    except Exception:
        return None

def save_attendance_list(csv_path: str, attendance_list: Dict) -> bool:
    existing_attendance_list = get_df_from_csv(csv_path)
    existing_attendance_list.query('')
    return True
    # df.all(attendance_list)
    # df.to_csv(folder_path)


def parse_csv_df(csv_path: str) -> DataFrame:
    return read_csv(csv_path)

