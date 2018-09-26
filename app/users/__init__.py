from flask import Blueprint
from flask import current_app
from flask import jsonify

users_bp = Blueprint("users", __name__)


@users_bp.route("/")
def user():
    result = {"name": "anuj"}
    response = jsonify(result)
    response.status_code = 200
    return response

