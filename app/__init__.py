from flask import Flask
from app.routes import register_routes
from app.loghandler import init_log
from app.errorhandler import init_errorhandler
from app.db import db
from app.initializers import init_setup


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)
    init_setup(app)
    register_routes(app)
    db.init_app(app)
    init_errorhandler(app)
    init_log(app)
    return app

