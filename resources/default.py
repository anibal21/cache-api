
from flask_restful import Resource


class DefaultResource(Resource):
    """Handle default route."""

    def get(self):
        """Get request for home page or response."""
        return {
            "status": "success",
            "data": {
                "msg": "Welcome to Cache API by CBInsights"
            }
        }


