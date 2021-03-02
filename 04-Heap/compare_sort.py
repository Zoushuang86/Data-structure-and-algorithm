from quick_sort import *
from sort_test_helper import *
from merge_sort import *
from quick_sort_2 import quick_sort_2
from quick_sort_three_ways import quick_sort_three_ways
from heap_sort import heap_sort
"""
================随机数组=================
Merge Sort : 0.0355 s
Quick Sort : 0.0283 s
Random Quick Sort : 0.0279 s
Random Quick Sort 2 : 0.0244 s
Random Quick Sort 3 : 0.0409 s
============随机重复元素数组=============
Merge Sort : 0.0347 s
Quick Sort : 0.2317 s
Random Quick Sort : 0.2514 s
Random Quick Sort 2 : 0.4194 s
Random Quick Sort 3 : 0.0073 s
==============几乎有序数组===============
Merge Sort : 0.0251 s
Quick Sort : 0.0940 s
Random Quick Sort : 0.0322 s
Random Quick Sort 2 : 0.0229 s
Random Quick Sort 3 : 0.0421 s
"""
if __name__ == "__main__":
    n = 10000
    print("================随机数组=================")
    arr = generate_random_list(n, 0, n)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 3", heap_sort, arr6, len(arr6))
    print("============随机重复元素数组=============")
    arr = generate_random_list(n, 0, 10)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 3", heap_sort, arr6, len(arr6))
    print("==============几乎有序数组===============")
    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 3", heap_sort, arr6, len(arr6))
