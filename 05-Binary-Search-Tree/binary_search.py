from sort_test_helper import *

def binary_search(arr, n, target):
    """
    二分查找法，在有序数组arr中，查找target
    如果找到target，返回相应的索引index
    如果没有找到target，返回-1
    """
    # arr在[left, right]区间查找target
    left, right = 0, n-1
    while left <= right:
        # middle = (left+right) // 2 加法可能导致溢出
        middle = left + (right - left) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return -1


def __binary_search_recursion(arr, left, right, target):
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return __binary_search_recursion(arr, left, mid-1, target)
    else:
        return __binary_search_recursion(arr, mid+1, right, target)


def binary_search_recursion(arr, n, target):
    return __binary_search_recursion(arr, 0, n-1, target)


if __name__ == "__main__":
    n = 1000000000
    arr = generate_nearly_ordered_array(n, 0)
    target = arr[n//4]
    # print(arr)
    # test_search("binary_search", binary_search, arr, n, target)
    # test_search("binary_search_recursion", binary_search_recursion, arr, n, target)
