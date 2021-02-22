from selection_sort import selection_sort
from insertion_sort import *
from bubble_sort import *
from sort_test_helper import *

"""
Insertion Sort : 6.74 s
Selection Sort : 3.02 s
Bubble Sort : 7.94 s

Insertion Sort : 0.09 s
Selection Sort : 3.01 s
Bubble Sort : 4.01 s

Insertion Sort : 0.00 s
Selection Sort : 3.02 s
Bubble Sort : 0.00 s
"""
if __name__ == "__main__":
    n = 10000
    arr = generate_random_list(n, 0, n)
    arr2 = arr.copy()
    arr3 = arr.copy()

    test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort, arr3, len(arr3))

    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    test_sort("Insertion Sort", insertion_sort_new, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort_new, arr3, len(arr3))

    arr = generate_nearly_ordered_array(n, 0)
    arr2 = arr.copy()
    arr3 = arr.copy()
    test_sort("Insertion Sort", insertion_sort_new, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort_new, arr3, len(arr3))
