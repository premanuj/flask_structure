import json

from flask import Blueprint, current_app, jsonify, request
from flask_httpauth import HTTPBasicAuth
from marshmallow import ValidationError

from app.users import service as user_service
from app.users.schema import user_schema, users_schema


auth = HTTPBasicAuth()


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
    result = users_schema.dump(result)
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


@users_bp.route("/token", methods=["GET"])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    response = jsonify({"token": token.decode("ascii")})
    return response

