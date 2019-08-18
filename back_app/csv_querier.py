from functools import partial
from typing import Dict

from pandas import DataFrame, read_csv, Series


folder_path = "csv_files"
classes_csv_path = "{}/{}".format(folder_path, 'class_students.csv')
attendance_csv_path = "{}/{}".format(folder_path, 'class_attendance.csv')


def parse_csv_df(csv_path: str, **kwargs) -> DataFrame:
    return read_csv(csv_path, **kwargs)


def get_df_from_csv(csv_path: str, **kwargs) -> DataFrame:
    return parse_csv_df(csv_path, **kwargs)


def get_df_from_csv_by_query(csv_path: str, query: str, **kwargs) -> DataFrame:
    return get_df_from_csv(csv_path, **kwargs).query(query)


def create_attendance_list_for_date(class_id: str,
                                    attendance_date: str) -> DataFrame:
    class_list_df = get_df_from_csv_by_query(classes_csv_path,  # type: DataFrame
                                             'class=="{}" and status=True'
                                             .format(class_id), sep=',', index_col=[0, 1])
    if class_list_df.empty:
        raise ValueError("class not found {}".format(class_id))
    attendance_list = class_list_df.loc[['student_id', 'full_name'],]
    attendance_list['class_id'] = class_id
    attendance_list['date'] = attendance_date
    attendance_list['attendance'] = False
    save_attendance_list(class_id, attendance_date, attendance_list)
    return attendance_list


def update_class_atendance(class_attendance_list: DataFrame, student_attendance: Series):
    class_attendance_list.loc[
        (student_attendance['class_id'],
         student_attendance['date'],
         student_attendance['student_id'], 'attendance')] = student_attendance['attendance']


def save_attendance_list(class_id: str, attendance_date: str,
                         attendance_list: Dict) -> bool:
    class_attendance_list = get_df_from_csv(attendance_csv_path, sep=',', index_col=[0,1,2])
    try:
        if not class_attendance_list.loc[(class_id, attendance_date),].empty:
            class_attendance_list.append(attendance_list)
    except KeyError:
        [update_class_atendance(class_attendance_list, student_attendance) for student_attendance in attendance_list]
    class_attendance_list.write_csv(attendance_csv_path)
    return True

