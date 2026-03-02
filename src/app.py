from flask import Flask

app: Flask | None = None

def run_app():
    global app
    app = Flask('app', static_folder='static', template_folder='templates')
    from .routes import init_routes
    init_routes()
    app.run(debug=True)
