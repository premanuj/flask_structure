from flask import request, jsonify, make_response, Response
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.utils.custom_exception import DataNotFound, DbException
import json


def init_errorhandler(app):
    @app.errorhandler(404)
    def not_found(error=None):
        message = {"message": "Not Found: " + request.url}
        return jsonify(message), 400

    @app.errorhandler(500)
    def internal_error(error=None):
        message = {"message": "Something went wrong" + request.url}

        return jsonify(message), 500

    @app.errorhandler(ValidationError)
    def required_not_found(error=None, data=None):
        message = {"message": "Not Found: "}
        return jsonify(message), 500

    @app.errorhandler(IntegrityError)
    def aleardy_exixts(error=None):
        message = {"message": "{} already exist".format(str(error.messages)).split(".")[-1]}
        return jsonify(message), 500

    @app.errorhandler(DataNotFound)
    def data_not_found(error=None):
        message = {"message": error.messages}
        return jsonify(message), 500

    @app.errorhandler(401)
    def custom_401(error):
        return Response(
            "<Why access is denied string goes here...>",
            401,
            {"WWWAuthenticate": 'Basic realm="Login Required"'},
        )

