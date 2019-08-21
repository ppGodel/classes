from waitress import serve
import web_app as app
serve(app, host='0.0.0.0', port=5000)