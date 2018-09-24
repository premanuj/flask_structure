from flask import Flask
from app.routes import register_routes
from raven.contrib.flask import Sentry
from app.loghandler import init_log


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile("config.py")
    app.config.from_json("config.json")
    if is_test:
        app.config.from_json("test_config.json")
    print(app.config)
    register_routes(app)
    init_log(app)
    return app

