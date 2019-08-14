from flask import Flask

app = Flask(__name__)

from app import classes_info

app.run(debug=True, port=5000, host='0.0.0.0')
