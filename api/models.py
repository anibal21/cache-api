from utils.EvictionPolicy import EvictionPolicy
from pendulum import now
import json

class Object:

    left= None
    right= None    

    def __init__(self, key, value, ttl):
        self.timezone = "America/Santiago"

        self.key = key
        self.value = value
        self.ttl = ttl if isinstance(ttl, int) else int(ttl, 10)
        self.creationDate = now(tz=self.timezone)

    def isValid(self):
        if self.ttl == 0:
            return True

        now_datetime = now(tz=self.timezone)
        max_datetime = self.creationDate.add(seconds=self.ttl)

        return False if now_datetime > max_datetime else True

    def toJSON(self):
        return {
            "key": self.key,
            "value": json.loads(self.value),
            "left": self.left,
            "right": self.right
        }
    
class ObjectDoublyLinkedList:

    def __init__(self, ep, sn):
        self.head = None
        self.tail = None
        self.objectList = {}
        self.ep = ep
        self.capacity = sn

    def get(self, key):
        if key not in self.objectList.keys():
            return None
        else:           
            return self.objectList[key]

    def obtain(self, key):
        return self.objectList[key].toJSON()

    def add(self, key, value, ttl):
        objects_length = len(self.objectList)
        evicted = False

        new_object = Object(key, value, ttl)

        # Length Validation
        if objects_length == self.capacity:
            if self.ep == EvictionPolicy.OLDEST_FIRST:
                """print("paso1")
                evicted_key = self.tail
                previous_object_key = None
                print("paso2")
                # Update links
                if objects_length > 1:
                    print("test")
                    print(self.tail)
                    previous_object_key = self.objectList[self.tail].left
                    print("previous")
                    self.objectList[previous_object_key].right = new_object.key
                if self.head == self.tail:
                    self.head = new_object.key
                    self.last = new_object.key
                print("paso4")
                # Evict object
                self.objectList.pop(evicted_key)
                print("paso5")
                new_object.left = previous_object_key
                self.objectList[key] = new_object
                print("paso6")
                evicted = True
                print(self.objectList.keys())"""                
                pass
            elif self.ep == EvictionPolicy.NEWEST_FIRST:
                pass
                """
                # Update links
                if objects_length > 1:
                    previous_object_key = self.objectList[self.tail].left
                    self.objectList[previous_object_key].right = new_object.key

                # Update the new object
                self.objectList[self.tail] = new_object

                if self.head == self.tail:
                    self.head = new_object.key

                # Update the new last
                self.tail = new_object.key"""
            else:
                return None
        else:
            # The first object added
            if self.head is None:
                self.head = key
                self.tail = key
            else:
                # Update links
                if self.objectList[self.tail].left is not None:
                    previous_object_key = self.objectList[self.tail].left
                    self.objectList[previous_object_key].right = key
                else:
                    self.objectList[self.head].right = key
                    new_object.left = self.head
                self.tail = key

        # Add new object
        if not evicted:
            self.objectList[key] = new_object

        print("__________")
        print(self.head)
        print(self.tail)
        print("__________")
        print(self.objectList.keys())
        return new_object

    def update(self, key, value):
        if key not in self.objectList.keys():
            return None
        else:
            self.objectList[key].value = value
            return self.objectList[key]


    def remove(self, key):
        if key not in self.objectList.keys():
            return None
        else:
            if len(self.objectList) == 1:
                self.head = None
                self.last = None
            else:
                left_key = self.objectList[key].left
                right_key = self.objectList[key].right
                if left_key != None and right_key != None:
                    self.objectList[left_key].right = right_key
                    self.objectList[right_key].left = left_key
                elif left_key == None:
                    self.objectList[right_key].left = None
                    self.head = self.objectList[right_key]
                else:
                    self.objectList[left_key].right = None
                    self.last = self.objectList[left_key]

            # Remove object
            removed = self.objectList.pop(key)

            return removed


 





