from quick_sort import *
from sort_test_helper import *
from merge_sort import *
from quick_sort_2 import quick_sort_2
from quick_sort_three_ways import quick_sort_three_ways
from heap_sort_1 import heap_sort_1
from heap_sort_2 import heap_sort_2
from heap_sort import heap_sort

"""
================随机数组=================
Merge Sort : 0.0405 s
Quick Sort : 0.0300 s
Random Quick Sort : 0.0333 s
Random Quick Sort 2 : 0.0294 s
Random Quick Sort 3 : 0.0604 s
Heap Sort 1 : 0.0939 s
Heap Sort 2 : 0.0991 s
Heap Sort 3 : 0.0633 s
============随机重复元素数组=============
Merge Sort : 0.0405 s
Quick Sort : 0.2492 s
Random Quick Sort : 0.2832 s
Random Quick Sort 2 : 0.0221 s
Random Quick Sort 3 : 0.0088 s
Heap Sort 1 : 0.0984 s
Heap Sort 2 : 0.0829 s
Heap Sort 3 : 0.0598 s
==============几乎有序数组===============
Merge Sort : 0.0299 s
Quick Sort : 0.1143 s
Random Quick Sort : 0.0351 s
Random Quick Sort 2 : 0.0267 s
Random Quick Sort 3 : 0.0575 s
Heap Sort 1 : 0.1495 s
Heap Sort 2 : 0.1026 s
Heap Sort 3 : 0.0685 s
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
    arr7 = arr.copy()
    arr8 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 1", heap_sort_1, arr6, len(arr6))
    test_sort("Heap Sort 2", heap_sort_2, arr7, len(arr7))
    test_sort("Heap Sort 3", heap_sort, arr8, len(arr8))
    print("============随机重复元素数组=============")
    arr = generate_random_list(n, 0, 10)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()
    arr7 = arr.copy()
    arr8 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 1", heap_sort_1, arr6, len(arr6))
    test_sort("Heap Sort 2", heap_sort_2, arr7, len(arr7))
    test_sort("Heap Sort 3", heap_sort, arr8, len(arr8))
    print("==============几乎有序数组===============")
    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    arr6 = arr.copy()
    arr7 = arr.copy()
    arr8 = arr.copy()
    test_sort("Merge Sort", merge_sort_bottom_to_up_new, arr, len(arr))
    test_sort("Quick Sort", quick_sort, arr2, len(arr2))
    test_sort("Random Quick Sort", quick_sort_new, arr3, len(arr3))
    test_sort("Random Quick Sort 2", quick_sort_2, arr4, len(arr4))
    test_sort("Random Quick Sort 3", quick_sort_three_ways, arr5, len(arr5))
    test_sort("Heap Sort 1", heap_sort_1, arr6, len(arr6))
    test_sort("Heap Sort 2", heap_sort_2, arr7, len(arr7))
    test_sort("Heap Sort 3", heap_sort, arr8, len(arr8))
