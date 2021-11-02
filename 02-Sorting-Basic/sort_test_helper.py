import numpy as np
import time
from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything

import random

def generate_random_list(n, rangeL, rangeR):
    """
    生成有n个元素的随机数组，
    每个元素的随即范围为[rangL, rangeR]
    """
    assert rangeR >= rangeL
    arr = np.random.randint(rangeL, rangeR+1, n).tolist()
    return arr


def test_sort(sort_name, sort, arr: List[Generic[T]], n: int):
    start_time = time.time()
    sort(arr, n)
    end_time = time.time()
    print("{} : {:.4f} s".format(sort_name, end_time-start_time))


def test_search(sort_name, sort, arr: List[Generic[T]], n: int, target: int):
    start_time = time.time()
    sort(arr, n, target)
    end_time = time.time()
    print("{} : {:.8f} s".format(sort_name, end_time-start_time))


def is_sorted(arr: List[Generic[T]], n: int) -> bool:
    for i in range(n):
        if arr[i] > arr[i+1]:
            return False
    return True

def generate_nearly_ordered_array(n, swap_times):
    arr = [i for i in range(n)]
    swap_index_1 = random.sample(arr, swap_times)
    swap_index_2 = random.sample(arr, swap_times)
    for i in range(swap_times):
        x = swap_index_1[i]
        y = swap_index_2[i]
        t = arr[x]
        arr[x] = arr[y]
        arr[y] = t
    return arr
