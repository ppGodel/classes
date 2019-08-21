from functools import lru_cache
from typing import Dict, Tuple
from pandas import DataFrame, read_csv, Series, MultiIndex

from util.constants import attendance_list_dict_type

folder_path = "../../back_end/csv_files"
class_student_csv_path = "{}/{}".format(folder_path, 'class_students.csv')
class_csv_path = "{}/{}".format(folder_path, 'class_info.csv')
attendance_csv_path = "{}/{}".format(folder_path, 'class_attendance.csv')


def parse_csv_df(csv_path: str, **kwargs) -> DataFrame:
    return read_csv(csv_path, **kwargs)


def get_df_from_csv(csv_path: str, **kwargs) -> DataFrame:
    return parse_csv_df(csv_path, **kwargs)


def get_df_from_csv_by_query(csv_path: str, query: str, **kwargs) -> DataFrame:
    return get_df_from_csv(csv_path, **kwargs).query(query)


def create_attendance_list_for_date(class_id: str,
                                    attendance_date: str) -> DataFrame:
    class_list_df = get_student_names(class_id).reset_index('student_id')
    if class_list_df.empty:
        raise ValueError("class not found {}".format(class_id))
    index_list = [(class_id, attendance_date, student_row[1]['student_id'])
                        for student_row in class_list_df.iterrows()]
    attendance_list = DataFrame(data=[False]*len(index_list),
                                index=MultiIndex.from_tuples(index_list, names=('class_id', 'date', 'student_id')),
                                columns=['attendance'])
    save_attendance_list(attendance_list)
    return attendance_list


def update_class_attendance(class_attendance_list: DataFrame, student_attendance: Series):
    class_attendance_list.loc[
        (student_attendance['class_id'],
         student_attendance['date'],
         student_attendance['student_id']), 'attendance'] = student_attendance['attendance']


def save_attendance_list(attendance_list: DataFrame) -> bool:
    class_attendance_list = get_df_from_csv(attendance_csv_path, sep=',', index_col=[0, 1, 2])
    attendance_list_df = attendance_list.reset_index(['class_id', 'date', 'student_id'])
    attendance_date = attendance_list_df['date'][0]
    class_id = attendance_list_df['class_id'][0]
    try:
        if not class_attendance_list.loc[(class_id, attendance_date), ].empty:
            [update_class_attendance(class_attendance_list, student_attendance[1])
             for student_attendance in attendance_list_df.iterrows()]
    except (KeyError, TypeError):
        class_attendance_list = class_attendance_list.append(attendance_list)
    class_attendance_list.to_csv(attendance_csv_path)
    return True


def save_attendance_dict(attendance_dict: Dict) -> bool:
    return save_attendance_list(transform_dict_to_attendance_list(attendance_dict))


def get_attendance_list_by_class_date(class_id, date: str) -> DataFrame:
    return get_df_from_csv_by_query(attendance_csv_path,
                                    'class_id=="{}" and date=="{}"'.format(class_id, date),
                                    sep=',', index_col=[0, 1,2])


@lru_cache(maxsize=None)
def get_student_names(class_id: str) -> DataFrame:
    return get_df_from_csv_by_query(class_student_csv_path,
                                    'class_id=="{}" and status==True'.format(class_id), sep=',', index_col=[0, 1])


@lru_cache(maxsize=None)
def get_class_info(class_id: str) -> DataFrame:
    return get_df_from_csv_by_query(class_csv_path,
                                    'class_id=="{}"'.format(class_id), sep=',', index_col=[0])


def student_dict(student: Series, student_names: DataFrame) -> Dict[str, str]:
    return {'student_id': student['student_id'],
            'full_name': student_names.loc[student['student_id'], 'full_name'],
            'attendance': 'checked' if student['attendance'] else ''}


def transform_attendance_list_to_dict(attendance_list: DataFrame) -> attendance_list_dict_type:
    attendance_df = attendance_list.reset_index('student_id')
    class_id, attendance_date = attendance_df.index.get_values()[0]
    student_names = get_student_names(class_id).reset_index('class_id')
    class_info = get_class_info(class_id)

    student_attendance_dict = [student_dict(student[1], student_names) for student in attendance_df.iterrows()]
    return {'class_id': class_id, 'class_name': class_info['class_name'][0], 'teacher': class_info['teacher'][0],
            'date': attendance_date, 'students': student_attendance_dict}


def student_tuple(class_id:str, date: str, student_attendance: Series, attendance_list: Dict) -> Tuple[str, str, str, str]:
    return (class_id,
            date,
            student_attendance['student_id'],
            attendance_list.get(str(student_attendance['student_id']), False)
            )


def transform_dict_to_attendance_list(attendance_list: Dict) -> DataFrame:
    class_id = attendance_list['class_id']
    date = attendance_list['date']
    student_names = get_student_names(class_id).reset_index('student_id')
    attendance_list_tuple = [student_tuple(class_id, date, student_class_info[1], attendance_list)
                             for student_class_info in student_names.iterrows()]
    return DataFrame.from_records(data=attendance_list_tuple, columns=['class_id', 'date', 'student_id', 'attendance'])\
        .set_index(['class_id', 'date', 'student_id'])

