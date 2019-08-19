from flask import Flask

app = Flask(__name__)

from app import classes_html_app, classes_api

if __name__ == "__main__" or __name__ == "app":
    app.run(debug=True, port=5000, host='0.0.0.0')
