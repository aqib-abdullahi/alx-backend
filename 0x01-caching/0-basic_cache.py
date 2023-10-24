#!/usr/bin/python3
"""BasicCache task 0
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inheriting from BasicCaching
    """
    def __init__(self):
        """initialize
        """
        super().__init__()

    def put(self, key, item):
        """Assigns to the dictionary, items and keys
        If key or item is None, method shouldn't do anything
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """gets item associated with given key
        """
        if key:
            if self.cache_data.get(key):
                value = self.cache_data.get(key)
                return value
            return None
        return None
