from to.object import ObjectTO
from utils.EvictionPolicy import EvictionPolicy

"""
@Description: DoublyLinkedList with a dictionary 
that represents the cache in memory store
* head: the first item of the DoublyLinkedList
* tail: the last item of the DoublyLinkedList
* objectList: the object items of the DoublyLinkedList
* ep: EvictionPolicy loaded to the store
* capacity: Limit capacity of items that the DoublyLinkedList can have
@Author: arodriguez
@Date: 2021-11-26
"""

class ObjectDoublyLinkedList:

    def __init__(self, ep, sn):
        self.head = None
        self.tail = None
        self.objectList = {}
        self.ep = ep
        self.capacity = sn

    def get(self, key):
        """Get one item from the list"""
        if key not in self.objectList.keys():
            return None
        else:           
            return self.objectList[key]

    def add(self, key, value, ttl):
        """Add item to the list"""
        objects_length = len(self.objectList)
        evicted = False

        new_object = ObjectTO(key, value, ttl)

        # Length Validation
        if objects_length == self.capacity:
            if new_object.ttl == 0:
                return None
            elif self.ep == EvictionPolicy.OLDEST_FIRST:
                evicted_key = self.tail
                previous_object_key = None
                # Update links
                if objects_length > 1:
                    previous_object_key = self.objectList[self.tail].left
                    self.objectList[previous_object_key].right = new_object.key
                if self.head == self.tail:
                    self.head = new_object.key
                    self.last = new_object.key
                # Evict object
                self.objectList.pop(evicted_key)
                new_object.left = previous_object_key
                self.objectList[key] = new_object
                evicted = True
                self.tail =  key
            elif self.ep == EvictionPolicy.NEWEST_FIRST:
                evicted_key = self.head
                next_object_key = None

                # Update links
                if objects_length > 1:
                    next_object_key = self.objectList[self.head].right
                    self.objectList[next_object_key].left = key

                if self.head == self.tail:
                    self.head = key
                    self.last = key

                # Evict object
                self.objectList.pop(evicted_key)
                new_object.right = next_object_key
                self.objectList = { **{key: new_object}, **self.objectList}
                evicted = True
                self.head =  key
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

        return new_object

    def update(self, key, value):
        """Edit item from the list"""        
        if key not in self.objectList.keys():
            return None
        else:
            self.objectList[key].value = value
            return self.objectList[key]


    def remove(self, key):
        """Delete item from the list"""
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