from app.db import db
from flask import Flask
from app.loghandler import init_log
from flask_migrate import Migrate
from app.routes import register_routes
from app.initializers import init_setup
from app.errorhandler import init_errorhandler
from app.users.models import User, Contact

from app.marshmallow_schema import ma
from flask_cors import CORS


def create_app(is_test=False):
    app = Flask(__name__, instance_relative_config=True)
    init_setup(app)
    CORS(app)
    register_routes(app)
    db.init_app(app)
    ma.init_app(app)
    Migrate(app, db)
    init_errorhandler(app)
    init_log(app)
    return app

