from enum import Enum

class EvictionPolicy(Enum):
    OLDEST_FIRST=1
    NEWEST_FIRST=2
    REJECT=3