from waitress import serve
import api_app.app as app

serve(app.app, host='0.0.0.0', port=5001)