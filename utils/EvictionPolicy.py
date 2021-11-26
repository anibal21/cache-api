from enum import Enum

"""
@Description: Eviction Policy Enum
@Author: arodriguez
@Date: 2021-11-26
"""

class EvictionPolicy(Enum):
    OLDEST_FIRST=1
    NEWEST_FIRST=2
    REJECT=3