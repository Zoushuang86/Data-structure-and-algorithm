from sort_test_helper import generate_nearly_ordered_array


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


if __name__ == "__main__":
    n = 10
    arr = generate_nearly_ordered_array(n, 0)
    print(arr)
    index = binary_search(arr, n, 8)
    print(index)
