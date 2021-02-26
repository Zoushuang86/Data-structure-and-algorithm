from typing import TypeVar, List, Generic
from sort_test_helper import *
from quick_sort import quick_sort_new
from insertion_sort import *
T = TypeVar("T")    # Can be anything
import random
import sys
sys.setrecursionlimit(100000)


def __partition_3(arr, left, right):

    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]

    v = arr[left]

    lt = left       # arr在[left+1, lt]<v
    gt = right+1    # arr在[gt, right]>v
    i = left+1      # arr在[right+1, i-1]=v
    while i < gt:
        if arr[i] < v:
            arr[i], arr[lt+1] = arr[lt+1], arr[i]
            lt += 1
            i += 1
        elif arr[i] > v:
            arr[i], arr[gt-1] = arr[gt-1], arr[i]
            gt -= 1
        else:
            i += 1
    arr[left], arr[lt] = arr[lt], arr[left]
    return lt, gt


# 对arr在区间[left,right]进行快速排序
# 将arr[left:right+1]分为<v、=v、>v三个部分
# 之后只需将>v和<v两个部分进行三路快速排序
def __quick_sort_3(arr, left, right):
    if right-left <= 15:
        insertion_sort_new(arr, left, right)
        return

    lt, gt = __partition_3(arr, left, right)
    __quick_sort_3(arr, left, lt-1)
    __quick_sort_3(arr, gt, right)


# 改进后
# 1. 当数组很小时，使用插入排序
def quick_sort_three_ways(arr: List[Generic[T]], n: int):
    __quick_sort_3(arr, 0, n - 1)


if __name__ == "__main__":
    n = 10
    arr = generate_random_list(n, 0, 10)
    arr2 = arr.copy()
    print(arr)
    quick_sort_three_ways(arr, n)
    print(arr)
    # test_sort("Quick Sort", quick_sort_new, arr, len(arr))
    # test_sort("Quick Sort 2", quick_sort_three_ways, arr2, len(arr2))
