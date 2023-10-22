#!/usr/bin/env python3
"""Hypermedia pagination
task 2
"""
import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing
       a start index and an end index corresponding range
    """
    start_index = (page - 1) * page_size
    end_index = page_size + start_index
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns appropriate page for dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index > len(data):
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns page information
        """
        hypermedia = self.get_page(page, page_size)
        total_page = math.ceil(len(self.__dataset) / page_size)
        start_index, end_index = index_range(page, page_size)
        result = {
            'page_size': len(hypermedia),
            'page': page,
            'data': hypermedia,
            'next_page': page + 1 if end_index < len(self.__dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_page,
        }
        return result
