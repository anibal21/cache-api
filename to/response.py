from http import HTTPStatus

"""
@Description: Transfer Object for the endpoints
response mapping
@Author: arodriguez
@Date: 2021-11-26
"""

class ResponseTO:
    
    def __init__(self, msg=None):
        self.msg = msg

    def success(self, data):
        return data, HTTPStatus.OK
    
    def error(self, estado = HTTPStatus.INTERNAL_SERVER_ERROR):
        return { "error": self.msg }, estado
