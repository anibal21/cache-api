from http import HTTPStatus
from to.response import ResponseTO

"""
@Description: Define custom error handlers for application
@Author: arodriguez
@Date: 2021-11-26
"""

def handle_server_errors(error):
    """Handle all 500 server errors in code."""
    return ResponseTO(error, HTTPStatus.INTERNAL_SERVER_ERROR)

def handle_404_errors(error):
    """Handle wrong url requests with custom message."""
    return ResponseTO(error, HTTPStatus.NOT_FOUND)

def handle_400_errors(error):
    """Handle 400 errors in resources."""
    return ResponseTO(error, HTTPStatus.BAD_REQUEST)
