import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv("SECRET")
    LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    SQLALCHEMY_DATABASE_URI = database_file
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/test_db"
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""

    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False


app_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
