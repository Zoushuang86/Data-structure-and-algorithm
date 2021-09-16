from typing import TypeVar, List, Generic
from sort_test_helper import *
from quick_sort import quick_sort_new
from insertion_sort import *
T = TypeVar("T")    # Can be anything
import random
import sys
sys.setrecursionlimit(100000)


def __partition_2(arr, left, right):

    random_index = random.randint(left, right)
    arr[left], arr[random_index] = arr[random_index], arr[left]

    v = arr[left]

    # arr[left+1,i) <= v, arr[i,right) >= v
    i, j = left+1, right
    while True:
        while (i <= right) and (arr[i] < v):    # 多了个等号的判断也会造成两棵子树不平衡
            i += 1
        while (j >= left+1) and (arr[j] > v):
            j -= 1
        if i > j:
            break
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    arr[left], arr[j] = arr[j], arr[left]

    return j


# 对arr[left:right+1]进行快速排序
def __quick_sort_2(arr, left, right):
    # if left >= right:
    #     return
    if right-left <= 15:
        # print(arr)
        insertion_sort_new(arr, left, right)
        return

    p = __partition_2(arr, left, right)
    __quick_sort_2(arr, left, p-1)
    __quick_sort_2(arr, p+1, right)


# 改进后
# 1. 当数组很小时，使用插入排序
def quick_sort_2(arr: List[Generic[T]], n: int):
    __quick_sort_2(arr, 0, n - 1)


if __name__ == "__main__":
    n = 20
    arr = generate_random_list(n, 0, 1)
    arr2 = arr.copy()
    # print(arr)
    # quick_sort_2(arr, n)
    # print(arr)
    test_sort("Quick Sort", quick_sort_new, arr, len(arr))
    test_sort("Quick Sort 2", quick_sort_2, arr2, len(arr2))
