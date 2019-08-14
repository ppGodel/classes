from datetime import date
from typing import Dict

from flask import render_template, request

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
    classes_info = {
        'automata': {
            'name': 'Automata Theory',
            'teacher': 'JAHS',
            'students': [
                {
                    'student_id': '1000001',
                    'full_name': 'student1',
                    'attendance': False
                },
                {
                    'student_id': '1000002',
                    'full_name': 'student2',
                    'attendance': False
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
                    'attendance': False
                },
                {
                    'student_id': '0000002',
                    'full_name': 'student2',
                    'attendance': False
                }
            ]
        }
    }
    class_info = classes_info[class_name]
    return render_template('class_list.html', title=class_info['name'], class_info=class_info, date=attendance_date)


@app.route('/class_list/response', methods=['POST'])
def class_response():
    if request.method == 'POST':
        result = request.form  # type: Dict
        return render_template("list_accepted.html", result=result)
