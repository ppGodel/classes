from flask import Flask

app = Flask(__name__)

from web_app.app import classes_html_app

if __name__ == "__main__" or __name__ == "web_app.app":
    app.run(debug=True, port=5000, host='0.0.0.0')
