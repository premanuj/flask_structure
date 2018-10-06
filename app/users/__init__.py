import json
from flask import Blueprint, current_app, jsonify, make_response, request
from marshmallow import ValidationError

import app
from app.users import service as user_service
from app.users.schema import user_schema, users_schema, profile_schema, profiles_schema

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["POST"])
def user():
    data = request.get_json() or {}
    try:
        result = user_schema.load(data)
    except ValidationError as e:
        raise ValidationError(e)
    else:
        result = user_service.new_user(result)
    response = jsonify(result)
    response.status_code = 200
    return response


@users_bp.route("/", methods=["GET"])
def all_users():
    result = user_service.get_all_user()
    print("AAAAAA", result)
    result = users_schema.dump(result)
    print("BBBB", result)
    response = jsonify(result)
    response.status_code = 200
    return response


@users_bp.route("/<int:id>", methods=["GET"])
def user_details(id):
    result = user_service.get_user(id)
    result = user_schema.dump(result)
    response = jsonify(result)
    response.status_code = 200
    return response


@users_bp.route("/login")
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response(
            "Could not verify", 201, {"WWW-Authenticate": "Basic-relam: Login required"}
        )

    token = user_service.login(auth)
    response = jsonify({"token": token.decode("UTF-8")})
    response.status_code = 200
    return response


@users_bp.route("/<int:user_id>/user_profile", methods=["POST"])
def user_profile(user_id):
    print("HERE")
    data = request.get_json() or {}
    data.update({"user_id": user_id})
    try:
        result = profile_schema.load(data)
    except ValidationError as e:
        print(e)
        raise ValidationError(e)
    else:
        result = user_service.user_profile(result)
    response = jsonify(result)
    response.status_code = 200
    return response


@users_bp.route("/user_profiles", methods=["GET"])
def get_all_profile():
    result = user_service.get_all_profile()
    result = profiles_schema.dump(result)
    response = jsonify(result)
    response.status_code = 200
    return response
