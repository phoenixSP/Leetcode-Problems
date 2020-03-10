# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 22:41:30 2020

@author: shrey
"""

from collections import OrderedDict
#OrderedDict is implemented using DLL

class LRUCache:

    def __init__(self, capacity: int):
        self.ordered_dict = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.ordered_dict:
            self.ordered_dict.move_to_end(key, last = False)
            return self.ordered_dict[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        self.ordered_dict[key] = value
        self.ordered_dict.move_to_end(key, last = False)
        if len(self.ordered_dict) > self.capacity:
            return self.ordered_dict.popitem()
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)