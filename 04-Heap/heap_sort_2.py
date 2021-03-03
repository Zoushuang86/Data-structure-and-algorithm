from max_heap import MaxHeap
from sort_test_helper import *


def heap_sort_2(arr, n):
    maxheap = MaxHeap(capacity=n, arr=arr)
    for i in range(n-1, -1, -1):
        arr[i] = maxheap.extructMax()


if __name__ == "__main__":
    n = 10
    arr = generate_random_list(n, 0, n)
    print(arr)
    heap_sort_2(arr, n)
    print(arr)
    # test_sort("Quick Sort", heap_sort_1, arr, len(arr))