from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything

from sort_test_helper import *
from insertion_sort import *

# 对arr的闭区间[left, middle]、[middle, right]进行排序
def __merge(arr, left, middle, right):
    aux = arr[left:right + 1].copy()
    i, j = left, middle + 1
    for k in range(left, right + 1):
        # 判断索引合法性
        if i > middle:
            arr[k] = aux[j-left]
            j += 1
        elif j > right:
            arr[k] = aux[i-left]
            i += 1
        elif aux[i-left] < aux[j-left]:
            arr[k] = aux[i-left]
            i += 1
        else:
            arr[k] = aux[j-left]
            j += 1


# 对arr的闭区间[left, right]进行排序
def __merge_sort(arr, left, right):
    if left >= right:
        return
    middle = (left+right) // 2
    __merge_sort(arr, left, middle)
    __merge_sort(arr, middle+1, right)
    __merge(arr, left, middle, right)


# 改进前：递归方法自上而下
def merge_sort(arr: List[Generic[T]], n: int):
    __merge_sort(arr, 0, n-1)


# 改进后
"""
1. 当左边子数组的最大值小于右边子数组的最小值，已经无需排序。这种方法有可能有效。
2. 当n很小时，可以使用插入排序代替：
   (1) 当n很小时，数组近乎是有序的概率较大，插入排序有优势；
   (2) 当n很小时，由于插入排序xO(n^2)中x比归并排序yO(nlogn)的y小，因此插入排序和归并排序性能差距不大。
"""
def __merge_sort_new(arr, left, right):
    # if left >= right:
    #     return
    if right - left <= 15:
        insertion_sort_new(arr, left, right)
    middle = (left+right) // 2
    __merge_sort(arr, left, middle)
    __merge_sort(arr, middle+1, right)
    if arr[middle] > arr[middle+1]:
        __merge(arr, left, middle, right)


def merge_sort_new(arr: List[Generic[T]], n: int):
    __merge_sort_new(arr, 0, n - 1)


def merge_sort_bottom_to_up(arr: List[Generic[T]], n: int):
    # 生成size列表
    size_list = []
    i = 1
    while i <= n:
        size_list.append(i)
        i += i
    # 遍历size大小的子数组
    for size in size_list:
        for i in range(0, n - size, size+size):
            # 保证后面数组存在
            # 对arr[i,i+size-1]和arr[i+size, i+size+size-1]进行归并
            # min()保证当不足size大小时不会越界
            __merge(arr, i, i+size-1, min(i+size+size-1, n-1))


def merge_sort_bottom_to_up_new(arr: List[Generic[T]], n: int):
    # 对于小数组, 使用插入排序优化
    for i in range(0, n, 16):
        # print(arr)
        insertion_sort_new(arr, i, min(i+15, n-1))
    # print(arr)
    # 生成size列表
    size_list = []
    i = 16
    while i <= n:
        size_list.append(i)
        i += i
    # 遍历size大小的子数组
    for size in size_list:
        for i in range(0, n - size, size+size):
            # 保证后面数组存在
            # 对arr[i,i+size-1]和arr[i+size, i+size+size-1]进行归并
            # min()保证当不足size大小时不会越界
            # 对于arr[mid] <= arr[mid+1]的情况,不进行merge
            if arr[i+size-1] > arr[i+size]:
                __merge(arr, i, i+size-1, min(i+size+size-1, n-1))


if __name__ == "__main__":
    n = 50000
    """
    
    """
    # arr = generate_nearly_ordered_array(n, 10)
    """
    
    """
    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    # print(arr)
    # merge_sort_bottom_to_up_new(arr, len(arr))
    # print(arr)
    """
    Merge Sort : 0.2599 s
    Merge Sort New : 0.2711 s
    Merge Sort Bottom to Up : 0.2620 s
    Merge Sort Bottom to Up New : 0.2155 s
    """
    test_sort("Merge Sort", merge_sort, arr, len(arr))
    test_sort("Merge Sort New", merge_sort_new, arr2, len(arr2))
    test_sort("Merge Sort Bottom to Up", merge_sort_bottom_to_up, arr3, len(arr3))
    test_sort("Merge Sort Bottom to Up New", merge_sort_bottom_to_up_new, arr4, len(arr4))

