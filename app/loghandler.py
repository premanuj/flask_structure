import logging
from logging.handlers import TimedRotatingFileHandler


def init_log(app):
    log = logging.getLogger(__name__)
    formatter = logging.Formatter(app.config["LOGGING_FORMAT"])
    log.setLevel(logging.DEBUG)

    error_handler = TimedRotatingFileHandler(
        "logs/errors.log", when="midnight", interval=1, backupCount=10
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    debug_handler = TimedRotatingFileHandler(
        "logs/debug.log", when="midnight", interval=1, backupCount=10
    )
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)

    warning_handler = TimedRotatingFileHandler(
        "logs/warning.log", when="midnight", interval=1, backupCount=10
    )
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)

    critical_handler = TimedRotatingFileHandler(
        "logs/critical.log", when="midnight", interval=1, backupCount=10
    )
    critical_handler.setLevel(logging.CRITICAL)
    critical_handler.setFormatter(formatter)

    # log.addHandler(debug_handler)
    # log.addHandler(error_handler)
    # log.addHandler(warning_handler)
    # log.addHandler(critical_handler)

    app.logger.addHandler(debug_handler)
    app.logger.addHandler(error_handler)
    app.logger.addHandler(warning_handler)
    app.logger.addHandler(critical_handler)
