#!/usr/bin/python3
"""LRUCache task 3
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache implementation inheriting from
    BaseCaching
    """
    def __init__(self):
        """Initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assigns to the dictionary key and itmes from the
        passed arguments
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                least_used_key, _ = self.cache_data.popitem()
                print("DISCARD:", least_used_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets item associated with passed key
        """
        if key and key in self.cache_data:
            return self.cache_data.move_to_end(key, last=False)
        return None
