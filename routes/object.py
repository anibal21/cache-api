import os
from flask import request
from http import HTTPStatus
from flask_restful import Resource, request
import json

from controllers.object import ObjectDoublyLinkedList
from to.response import ResponseTO
from utils.EvictionPolicy import EvictionPolicy

"""
@Description: Object Route definition
This Route has CRUD operations for the Cached Data
saved on memory
@Author: arodriguez
@Date: 2021-11-26
"""

env_sn = os.getenv("OBJECTS_SLOT_NUMBER")
env_ttl = os.getenv("OBJECTS_TIME_TO_LIVE")
env_ep = os.getenv("OBJECTS_EVICTION_POLICY")

class ObjectRoute(Resource):

    # Environment variables
    ttl = 3600 if not env_ttl else int(env_ttl)
    sn = 10000 if not env_sn else int(env_sn)
    ep = EvictionPolicy.REJECT if not env_ep else EvictionPolicy[env_ep]

    in_memory = ObjectDoublyLinkedList(ep, sn)

    def get(self, key):
        found_object = self.in_memory.get(key)

        if found_object is None:
            response = ResponseTO("The object doesn't exist").error(HTTPStatus.NOT_FOUND)
        elif found_object.isValid() is False:
            response = ResponseTO("The object has expired").error(HTTPStatus.NOT_FOUND)
        else:
            response = ResponseTO().success(found_object.toJSON())
        return response

    def post(self, key):
        args = request.args
        
        object_ttl = args["ttl"] if 'ttl' in args.keys() else self.ttl

        json_data = request.get_json(force=True)
        object_value = json.dumps(json_data, separators=(',', ':'))

        object_added = self.in_memory.add(key, object_value, object_ttl)

        if object_added is None:
            response = ResponseTO("There's no space available to store more objects on the server").error(HTTPStatus.INSUFFICIENT_STORAGE)
        else:
            response = ResponseTO().success(object_added.toJSON())

        return response

    def put(self, key):
        args = request.args
        if 'ttl' in args.keys():
            print(args["ttl"])

        json_data = request.get_json(force=True)

        object_value = json.dumps(json_data, separators=(',', ':'))

        self.in_memory.update(key, object_value)

        return ResponseTO().success(self.in_memory.get(key).toJSON())

    def delete(self, key):
        removed = self.in_memory.remove(key)
        return ResponseTO().success(removed.toJSON())
