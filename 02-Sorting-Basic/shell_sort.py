from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything

from sort_test_helper import *


# 改进前
def shell_sort(arr: List[Generic[T]], n: int) -> List[Generic[T]]:
    # 计算 increment sequence: 1, 4, 13, 40...
    h = 1
    while h < n / 3:
        h = 3 * h + 1   # +1为了保证最后一次进行插入排序
    h = 1
    while h >= 1:
        # h-sort the array
        for i in range(h, n):
            # 对arr[i], arr[i-h], arr[i-2*h]...使用插入排序
            e = arr[i]
            for j in range(i, h-2, -h): # -2：一是为了能够取到h，二是保证取到h大小数组的第一个数
                if e < arr[j-h]:
                    arr[j] = arr[j-h]
                else:
                    break
            arr[j] = e
        h = h // 3
    return arr


if __name__ == "__main__":
    n = 10
    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    print(arr)
    print(shell_sort(arr, len(arr)))
    """
    Bubble Sort : 4.18 s
    Bubble Sort New : 3.76 s
    """
    # test_sort("Bubble Sort", shell_sort, arr, len(arr))
    # test_sort("Bubble Sort New", shell_sort_new, arr2, len(arr2))

