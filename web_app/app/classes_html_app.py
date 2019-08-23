from datetime import datetime
from functools import partial
from typing import Dict

from flask import render_template, request, url_for

from web_app.app import app
from back_end.web_app import classes_requester
from util.date_formatter import convert_date_str

api_url = 'http://0.0.0.0:5001'
get_class_attendance_list = partial(classes_requester.get_class_attendance_list, api_url)
send_class_attendance_list = partial(classes_requester.send_class_attendance_list, api_url)
get_class_list = partial(classes_requester.get_class_list, api_url)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/classes_attendance')
def classes():
    classes_list = get_class_list()
    return render_template('classes_attendance.html', classes=classes_list)


@app.route('/class_list', methods=['GET'])
def class_list():
    arguments = request.args  # type: Dict
    class_name = arguments['class_name']  # type: str
    attendance_date = arguments.get('date', convert_date_str(datetime.now()))  # type: str
    class_info = get_class_attendance_list(class_name, attendance_date)
    if not class_info:
        class_info = {'class_name': class_name, 'date': attendance_date}
    return render_template('class_list.html', title=class_info['class_name'], class_info=class_info, date=class_info['date'],
                           response_url=url_for('class_response'))


@app.route('/class_list/response', methods=['POST'])
def class_response():
    if request.method == 'POST':
        attendance_result = request.form  # type: Dict
        result_txt = send_class_attendance_list(attendance_result)
        return render_template("list_accepted.html", result=attendance_result, result_txt=result_txt)
