from flasgger import Swagger
from flask import Flask
from flask_restful import Api

from werkzeug import exceptions

from config.envConfig import env_config
from routes.default import DefaultRoute
from routes.object import ObjectRoute
from utils import errors

"""
@Description: API config
@Author: arodriguez
@Date: 2021-11-26
"""

api = Api()

def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(env_config[config_name])

    # register api
    api.init_app(app)

    # swagger component definition
    Swagger(app)

    """API Error handlers"""

    app.register_error_handler(exceptions.NotFound, errors.handle_404_errors)

    app.register_error_handler(
        exceptions.InternalServerError, errors.handle_server_errors
    )

    app.register_error_handler(exceptions.BadRequest, errors.handle_400_errors)

    app.register_error_handler(FileNotFoundError, errors.handle_400_errors)

    app.register_error_handler(TypeError, errors.handle_400_errors)

    app.register_error_handler(KeyError, errors.handle_404_errors)

    app.register_error_handler(AttributeError, errors.handle_400_errors)

    app.register_error_handler(ValueError, errors.handle_400_errors)

    app.register_error_handler(AssertionError, errors.handle_400_errors)

    return app


"""Routes definition"""

# register url for objects
api.add_resource(ObjectRoute, "/v1/objects/<int:key>", endpoint="object")   

# register url for default
api.add_resource(DefaultRoute, "/", endpoint="home")