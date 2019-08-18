from typing import Dict

from flask import request, jsonify

from app import app
from back_app.api_responser import get_classes_dict
from util.date_formatter import convert_str_date


@app.route('/classes/api/get_class_list', methods=['GET'])
def api_get_attendance_list():
    if request.method == 'GET':#type request
        arguments = request.args  # type: Dict
        class_name = arguments.get('class_name')
        attendance_date = convert_str_date(arguments.get('attendance_date'))
        class_info = get_classes_dict(class_name, attendance_date)
        return jsonify(class_info)


@app.route('/classes/api/send_class_attendance_list', methods=['POST'])
def api_send_class_attendance_list():
    if request.method == 'POST':#type request
        attendance_list = request.form  # type: Dict
        response = save_attendance_list(attendance_list)
        return response


