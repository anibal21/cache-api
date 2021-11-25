import os
from flask import request
from http import HTTPStatus
from flask_restful import Resource, request
import json

from api.models import ObjectDoublyLinkedList
from utils.EvictionPolicy import EvictionPolicy

env_sn = os.getenv("OBJECTS_SLOT_NUMBER")
env_ttl = os.getenv("OBJECTS_TIME_TO_LIVE")
env_ep = os.getenv("OBJECTS_EVICTION_POLICY")

class ObjectResource(Resource):

    # Environment variables
    ttl = 3600 if not env_ttl else int(env_ttl)
    sn = 10000 if not env_sn else int(env_sn)
    ep = EvictionPolicy.REJECT if not env_ep else EvictionPolicy[env_ep]

    in_memory = ObjectDoublyLinkedList(ep, sn)

    #def __init__(self):
    #    # Cache store as DoubleLinkedList


    def get(self, key):
        found_object = self.in_memory.get(key)

        if found_object is None:

            response = "The object doesn't exist"
            estadoHTTP = HTTPStatus.NOT_FOUND
        elif found_object.isValid() is False:

            response = "The object has expired"
            estadoHTTP = HTTPStatus.NOT_FOUND
        else:

            response = self.in_memory.obtain(key)
            estadoHTTP = HTTPStatus.OK

        return {"data" : response}, estadoHTTP

    def post(self, key):
        args = request.args
        
        object_ttl = args["ttl"] if 'ttl' in args.keys() else self.ttl

        json_data = request.get_json(force=True)
        object_value = json.dumps(json_data, separators=(',', ':'))

        object_added = self.in_memory.add(key, object_value, object_ttl)

        if object_added is None:
            response = "There's no space available to store more objects on the server"
            estadoHTTP = HTTPStatus.INSUFFICIENT_STORAGE
        else:
            response = object_added.toJSON()
            estadoHTTP = HTTPStatus.OK

        return {"written": response}, estadoHTTP

    def put(self, key):
        args = request.args
        if 'ttl' in args.keys():
            print(args["ttl"])

        json_data = request.get_json(force=True)

        json_data = request.get_json(force=True)
        object_value = json.dumps(json_data, separators=(',', ':'))

        self.in_memory.update(key, object_value)

        return {"updated": self.in_memory.obtain(key)}, HTTPStatus.OK

    def delete(self, key):
        removed = self.in_memory.remove(key)
        return {"removed": removed.toJSON()}, HTTPStatus.OK