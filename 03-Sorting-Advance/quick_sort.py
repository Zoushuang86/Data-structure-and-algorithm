from typing import TypeVar, List, Generic
from sort_test_helper import *
from insertion_sort import *
T = TypeVar("T")    # Can be anything
import random
import sys
sys.setrecursionlimit(100000)
# 改进前
# 对arr[left,right]进行partition操作
# 返回索引p，使得arr[left,p-1]<arr[p] and arr[p]<arr[p,right]
def __partition(arr, left, right):
    v = arr[left]
    # arr[left,p-1]<arr[p] and arr[p]<arr[p,right)
    # 初始化时，两个区间都为空
    j = left
    for i in range(left+1, right+1):
        if arr[i] < v:
            arr[j+1], arr[i] = arr[i], arr[j+1]
            j += 1
    arr[left], arr[j] = arr[j], arr[left]
    return j


# 对arr[left:right+1]进行快速排序
def __quick_sort(arr, left, right):
    if left >= right:
        return
    p = __partition(arr, left, right)
    __quick_sort(arr, left, p-1)
    __quick_sort(arr, p+1, right)


def quick_sort(arr: List[Generic[T]], n: int):
    __quick_sort(arr, 0, n-1)


def __partition_new(arr, left, right):

    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]

    v = arr[left]

    j = left
    for i in range(left+1, right+1):
        if arr[i] < v:
            arr[j+1], arr[i] = arr[i], arr[j+1]
            j += 1
    arr[left], arr[j] = arr[j], arr[left]
    return j


# 对arr[left:right+1]进行快速排序
def __quick_sort_new(arr, left, right):
    # if left >= right:
    #     return
    if right-left<=15:
        # print(arr)
        insertion_sort_new(arr, left, right)
        return

    p = __partition_new(arr, left, right)
    __quick_sort_new(arr, left, p-1)
    __quick_sort_new(arr, p+1, right)


# 改进后
# 1. 当数组很小时，使用插入排序
def quick_sort_new(arr: List[Generic[T]], n: int):
    __quick_sort_new(arr, 0, n - 1)


if __name__ == "__main__":
    n = 10000
    arr = generate_random_list(n, 0, n)
    arr2 = arr.copy()
    # print(arr)
    # quick_sort(arr, n)
    # print(arr)
    test_sort("Quick Sort", quick_sort, arr, len(arr))
    test_sort("Quick Sort New", quick_sort_new, arr2, len(arr2))
