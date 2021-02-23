from selection_sort import selection_sort
from insertion_sort import insertion_sort_new
from bubble_sort import bubble_sort_new
from sort_test_helper import *
from shell_sort import shell_sort
"""
比较SelectionSort, InsertionSort和BubbleSort和ShellSort四种排序算法的性能效率
ShellSort是这四种排序算法中性能最优的排序算法

Insertion Sort : 3.6380 s
Selection Sort : 2.9979 s
Bubble Sort : 7.1005 s
Shell Sort : 3.5282 s
=========================
Insertion Sort : 0.1088 s
Selection Sort : 2.9277 s
Bubble Sort : 3.8425 s
Shell Sort : 0.1026 s
=========================
Insertion Sort : 0.0040 s
Selection Sort : 2.8623 s
Bubble Sort : 0.0010 s
Shell Sort : 0.0050 s
"""
if __name__ == "__main__":
    n = 10000

    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    test_sort("Insertion Sort", insertion_sort_new, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort_new, arr3, len(arr3))
    test_sort("Shell Sort", shell_sort, arr4, len(arr4))
    print("=========================")
    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    test_sort("Insertion Sort", insertion_sort_new, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort_new, arr3, len(arr3))
    test_sort("Shell Sort", shell_sort, arr4, len(arr4))
    print("=========================")
    arr = generate_nearly_ordered_array(n, 0)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    test_sort("Insertion Sort", insertion_sort_new, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
    test_sort("Bubble Sort", bubble_sort_new, arr3, len(arr3))
    test_sort("Shell Sort", shell_sort, arr4, len(arr4))
