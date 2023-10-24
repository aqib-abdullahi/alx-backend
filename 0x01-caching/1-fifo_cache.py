#!/usr/bin/python3
"""FIFOCache task 1
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inheriting from BaseCaching
    """
    def __init__(self):
        """Initializer
        """
        super().__init__()
        # self.history = []

    def put(self, key, item):
        """puts items into dictionary with associated
        keys
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            old = next(iter(self.cache_data))
            del self.cache_data[old]
            print("DISCARD:", old)

    def get(self, key):
        """gets value linked to passed key
        """
        if key and self.cache_data[key]:
            value = self.cache_data[key]
            return value
        return None
