from datetime import date
from typing import Dict, Optional

from back_end.web_app.api_querier import get_response_json, map_parameters, send_post_get_response_text


def get_class_attendance_list_url(base_url: str, class_name: str, attendance_date: date) -> str:
    return '{}/classes/api/get_class_list?{}'\
        .format(base_url, map_parameters(class_name=class_name, attendance_date=attendance_date))


def send_class_attendance_list_url(base_url: str):
    return '{}/classes/api/send_class_attendance_list'.format(base_url)


def get_class_attendance_list(base_url: str, class_name: str, attendance_date: date) -> Optional[Dict]:
    url = get_class_attendance_list_url(base_url, class_name, attendance_date)
    return get_response_json(url)


def send_class_attendance_list(base_url: str, class_attendance_list: Dict) -> str:
    url = send_class_attendance_list_url(base_url)
    return send_post_get_response_text(url, class_attendance_list)




