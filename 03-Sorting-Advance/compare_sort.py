from quick_sort import *
from sort_test_helper import *
from merge_sort import *
"""
Merge Sort : 0.0376 s
Quick Sort : 0.0445 s
Random Quick Sort : 0.0437 s
===================================
Merge Sort : 0.0263 s
Quick Sort : 0.1329 s
Random Quick Sort : 0.1139 s
"""
if __name__ == "__main__":
    n = 10000

    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    # test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr2, len(arr2))
    test_sort("Quick Sort", quick_sort, arr3, len(arr3))
    test_sort("Random Quick Sort", quick_sort_new, arr4, len(arr4))
    print("===================================")
    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    # test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr2, len(arr2))
    test_sort("Quick Sort", quick_sort, arr3, len(arr3))
    test_sort("Random Quick Sort", quick_sort_new, arr4, len(arr4))
#