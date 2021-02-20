import numpy as np
import time
from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything


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
    print("{} : {:.2f} s".format(sort_name, end_time-start_time))


def is_sorted(arr: List[Generic[T]], n: int) -> bool:
    for i in range(n):
        if arr[i] > arr[i+1]:
            return False
    return True
