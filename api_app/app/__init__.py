from flask import Flask

app = Flask(__name__)

from api_app.app import classes_api

if __name__ == "__main__" or __name__ == "api_app.app":
    app.run(debug=True, port=5001, host='0.0.0.0')
