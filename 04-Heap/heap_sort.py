import random
from sort_test_helper import *


def __shiftDown(arr, n, k):
    while 2 * k + 1 < n:
        # 在此轮循环中，arr[k]和arr[j]交换位置
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if arr[k] >= arr[j]:
            break
        else:
            arr[k], arr[j] = arr[j], arr[k]
            k = j


def heap_sort(arr, n):
    # Heapify过程
    for i in range((n-1-1)//2, -1, -1):
        __shiftDown(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        __shiftDown(arr, i, 0)


if __name__ == "__main__":
    n = 10
    arr = generate_random_list(n, 0, n)
    print(arr)
    test_sort("Heap Sort 3", heap_sort, arr, len(arr))
    print(arr)
