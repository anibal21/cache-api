from pendulum import now
import json

"""
@Description: Transfer Object for the items of the
data cached in memory
@Author: arodriguez
@Date: 2021-11-26
"""

class ObjectTO:

    left= None
    right= None    

    def __init__(self, key, value, ttl):
        self.timezone = "America/Santiago"

        self.key = key
        self.value = value
        self.ttl = ttl if isinstance(ttl, int) else int(ttl, 10)
        self.creationDate = now(tz=self.timezone)

    def isValid(self):
        """Valid if the object is expired"""
        if self.ttl == 0:
            return True

        now_datetime = now(tz=self.timezone)
        max_datetime = self.creationDate.add(seconds=self.ttl)

        return False if now_datetime > max_datetime else True

    def toJSON(self):
        """Map the object to JSON"""
        return {
            "key": self.key,
            "value": json.loads(self.value)
        }