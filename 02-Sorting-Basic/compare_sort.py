from selection_sort import selection_sort
from insertion_sort import insertion_sort
from sort_test_helper import *

if __name__ == "__main__":
    n = 10000
    arr = generate_random_list(n, 0, 3)
    arr2 = arr.copy()
    """
    改进前：
    Insertion Sort : 5.14 s
    Selection Sort : 3.12 s
    改进后：
    Insertion Sort : 2.87 s
    Selection Sort : 3.11 s
    """
    test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))

    """
    #当数组基本有序，插入排序远远比选择排序快
    Insertion Sort : 0.12 s
    Selection Sort : 3.39 s
    """
    arr = generate_nearly_ordered_array(n, 100)
    arr2 = arr.copy()
    test_sort("Insertion Sort", insertion_sort, arr, len(arr))
    test_sort("Selection Sort", selection_sort, arr2, len(arr2))
