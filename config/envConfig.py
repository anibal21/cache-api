import logging
import os
from logging.handlers import RotatingFileHandler

"""
@Description: Deployment Config by environment
@Author: arodriguez
@Date: 2021-11-26
"""

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # log to a file
        if not os.path.exists("logs"):
            os.mkdir("logs")
        # limit the log file size to 102MB
        file_handler = RotatingFileHandler(
            "logs/cache_api.log", maxBytes=102400, backupCount=10
        )
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Starting our Cache API")


env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
