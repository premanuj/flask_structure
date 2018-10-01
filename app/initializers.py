def init_setup(app):
    if app.config["ENV"] == "development":
        app.config.from_object("config.DevelopmentConfig")
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    app.config.from_pyfile("config.py")
    if app.config["TESTING"]:
        app.config.from_json("test_config.json")
