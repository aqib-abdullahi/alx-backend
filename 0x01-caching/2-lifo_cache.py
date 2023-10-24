#!/usr/bin/python3
"""LIFOCaching task 2
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inheriting from the BaseCaching
    """
    def __init__(self):
        """Initializer
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """assigns to the dictionary the ITEM value
        for the key.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """gets value linked to passed key
        """
        if key and self.cache_data[key]:
            value = self.cache_data[key]
            return value
        return None
