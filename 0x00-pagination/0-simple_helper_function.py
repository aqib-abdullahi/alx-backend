#!/usr/bin/env python
"""index range module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """return a tuple of size two containing
    a start index and an end index corresponding to 
    the range of indexes to return in a list 
    """
    start_index = (page - 1) * page_size
    end_index = page_size * page
    return (start_index, end_index)
