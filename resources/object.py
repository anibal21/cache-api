import os
from http import HTTPStatus
from flask_restful import Resource, request

env_ttl = os.getenv("OBJECTS_TIME_TO_LIVE")

class ObjectResource(Resource):

    ttl = 3600 if not env_ttl else env_ttl
    in_memory = {}

    def get(self, key):
        print(self.ttl)
        return {"test": self.in_memory}, HTTPStatus.OK

    def post(self, key):
        args = request.args
        if 'ttl' in args.keys():
            print(args["ttl"])

        test= self.in_memory[key] = "testito"
        return {"test": test}, HTTPStatus.OK