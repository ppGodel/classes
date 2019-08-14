from datetime import date
from typing import Dict, Union

from flask import render_template, request, url_for

from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/class_list', methods=['GET'])
def class_list():
    arguments = request.args  # type: Dict
    class_name = arguments['class_name']
    attendance_date = arguments.get('date', date.today())
    class_info = get_classes_dict(class_name, attendance_date)
    return render_template('class_list.html', title=class_info['name'], class_info=class_info, date=attendance_date,
                           response_url=url_for('class_response'))


def get_classes_dict(class_name: str, attendance_date: date) -> Dict[str, Union[str, Dict[str, str]]]:
    classes_info = {
        'automata': {
            'name': 'Automata Theory',
            'teacher': 'JAHS',
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


@app.route('/class_list/response', methods=['POST'])
def class_response():
    if request.method == 'POST':
        result = request.form  # type: Dict
        return render_template("list_accepted.html", result=result)
