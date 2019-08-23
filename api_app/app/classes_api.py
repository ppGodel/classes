from typing import Dict

from flask import request, jsonify

from api_app.app import app
from back_end.api.api_responser import get_attendance_class_dict, save_attendance_list, get_classes_info


@app.route('/classes/api/get_class_attendance_list', methods=['GET'])
def api_get_attendance_list():
    if request.method == 'GET':
        arguments = request.args  # type: Dict
        class_name = arguments.get('class_name')
        attendance_date = arguments.get('attendance_date')
        class_info = get_attendance_class_dict(class_name, attendance_date)
        return jsonify(class_info)


@app.route('/classes/api/send_class_attendance_list', methods=['POST'])
def api_send_class_attendance_list():
    if request.method == 'POST':
        attendance_list = request.form  # type: Dict
        response = save_attendance_list(attendance_list)
        return response


@app.route('/classes/api/get_classes_info', methods=['GET'])
def api_get_classes_info():
    if request.method == 'GET':
        return jsonify({'data': get_classes_info()})

