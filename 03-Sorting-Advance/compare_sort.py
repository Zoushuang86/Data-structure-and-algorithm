from insertion_sort import insertion_sort
from sort_test_helper import *
from merge_sort import *
"""
"""
if __name__ == "__main__":
    n = 10000

    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    # arr3 = arr.copy()
    # arr4 = arr.copy()
    test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Merge Sort", merge_sort_new, arr2, len(arr2))
    # print("=========================")
    # arr = generate_nearly_ordered_array(n, 100)
    # arr2 = arr.copy()
    # # arr3 = arr.copy()
    # # arr4 = arr.copy()
    # test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    # test_sort("Merge Sort", merge_sort, arr2, len(arr2))
    # print("=========================")
    # arr = generate_nearly_ordered_array(n, 0)
    # arr2 = arr.copy()
    # # arr3 = arr.copy()
    # # arr4 = arr.copy()
    # test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    # test_sort("Merge Sort", merge_sort, arr2, len(arr2))
