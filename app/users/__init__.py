from flask import Blueprint
from flask import current_app

users_bp = Blueprint("users", __name__)


@users_bp.route("/")
def user():
    result = {"name": "anuj"}
    # current_app.logger.critical(result)

    return result

