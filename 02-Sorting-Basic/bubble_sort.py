from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything

from sort_test_helper import *


# 改进前
def bubble_sort(arr: List[Generic[T]], n: int):
    for i in range(1, n):
        for j in range(0, n-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 改进后
# 记录最后交换位置，之后的元素在下一轮不再交换
def bubble_sort_new(arr: List[Generic[T]], n: int):
    new_n = 1
    while new_n > 0:
        new_n = 0
        for i in range(1, n):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                new_n = i
        n = new_n


if __name__ == "__main__":
    n = 10000
    arr = generate_nearly_ordered_array(n, 10)
    arr2 = arr.copy()
    # print(arr)
    # bubble_sort_new(arr, len(arr))
    # print(arr)
    """
    Bubble Sort : 4.18 s
    Bubble Sort New : 3.76 s
    """
    test_sort("Bubble Sort", bubble_sort, arr, len(arr))
    test_sort("Bubble Sort New", bubble_sort_new, arr2, len(arr2))

