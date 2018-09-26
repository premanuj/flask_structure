from flask import request, jsonify


def init_errorhandler(app):
    @app.errorhandler(404)
    def not_found(error=None):
        message = {"status": 404, "message": "Not Found: " + request.url}
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    @app.errorhandler(500)
    def internal_error(error=None):
        message = {"status": 500, "message": "Something went wrong" + request.url}
        resp = jsonify(message)
        resp.status_code = 500

        return resp
