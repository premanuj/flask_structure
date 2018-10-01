from flask import request, jsonify, make_response


def init_errorhandler(app):
    @app.errorhandler(404)
    def not_found(error=None):
        message = {"message": "Not Found: " + request.url}
        return jsonify(message), 400

    @app.errorhandler(500)
    def internal_error(error=None):
        message = {"message": "Something went wrong" + request.url}

        return jsonify(message), 500
