
from flask_restful import Resource
from to.response import ResponseTO

"""
@Description: Default route for every case not declared for the API
@Author: arodriguez
@Date: 2021-11-26
"""

class DefaultRoute(Resource):
    """Handle default route."""

    def get(self):
        return ResponseTO().success("Route not found")
