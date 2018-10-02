from flask import Blueprint, current_app, jsonify, request
from app.users import service as user_service

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["POST"])
def user():
    data = request.get_json() or {}
    print(data)
    result = user_service.new_user(data)
    response = jsonify(result)
    response.status_code = 200
    return response


@users_bp.route("/", methods=["GET"])
def all_users():
    result = user_service.get_all_user()
    for user in result:
        print(user.username, user.email_address)
    response = jsonify(result)
    response.status_code = 200
    return response

