from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything


from sort_test_helper import generate_random_list, test_sort, is_sorted

# 改进前
def insertion_sort(arr: List[Generic[T]], n: int):
    for i in range(1, n):
        # 寻找元素arr[i]合适的插入位置
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                t = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = t
            else:
                break
            j -= 1

# 改进后
def insertion_sort_new(arr: List[Generic[T]], n: int):
    for i in range(1, n):
        # 寻找元素arr[i]合适的插入位置
        j = i
        e = arr[i]
        for j in range(i, -1, -1):
            if e < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = e


def insertion_sort_new(arr: List[Generic[T]], left: int, right: int):
    for i in range(left+1, right+1):
        # 寻找元素arr[i]合适的插入位置
        e = arr[i]
        for j in range(i, left-1, -1):
            if e < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                break
        arr[j] = e

if __name__ == "__main__":
    n = 20
    arr = generate_random_list(n, 0, 10)
    print(arr)
    insertion_sort_new(arr, 5, 9)
    print(arr)
    # test_sort("Insertion Sort", insertion_sort, arr, len(arr))
