#!/usr/bin/env python3
"""index range module
helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing
       a start index and an end index corresponding range
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return (start_index, end_index)
