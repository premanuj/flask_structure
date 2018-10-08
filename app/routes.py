from app.users import users_bp


def register_routes(app):
    app.register_blueprint(users_bp, url_prefix="/users")
    # app.register_blueprint(app.routes)

