from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything

from sort_test_helper import *


# 改进前
def shell_sort(arr: list, n: int):
    # 计算 increment sequence: 1, 4, 13, 40...分组数量
    h = 1
    while h < n / 3:
        h = 3 * h + 1   # +1为了保证最后一次进行插入排序

    while h >= 1:
        print("h=", h)
        # h-sort the array
        for i in range(h, n):
            # 对arr[i], arr[i-h], arr[i-2*h]...使用插入排序
            e = arr[i]
            j = i
            for j in range(i, h-2, -h): # -2：一是为了能够取到h，二是保证取到h大小数组的第一个数
                if e < arr[j-h]:
                    arr[j] = arr[j-h]
                else:
                    break
            arr[j] = e
            print("arr:", arr)
        h = h // 3
        print(arr)

def shell_sort_2(arr: list, n: int):
    # 先初始化每组2个元素的增量
    step = n >> 1
    while step:
        # 使用插入排序对组内进行排序
        for i in range(step, n):
            j = i
            while j-step >= 0 and arr[j] < arr[j-step]:
                arr[j], arr[j-step] = arr[j-step], arr[j]
                j -= step
        print("增量{}的排序：{}".format(step,arr))
        # 增量减少一半
        step = step >> 1

if __name__ == "__main__":
    n = 10
    arr = generate_random_list(n, 0, 100)
    arr2 = arr.copy()
    print(arr)
    shell_sort_2(arr, len(arr))
    print(arr)
    """
    Bubble Sort : 4.18 s
    Bubble Sort New : 3.76 s
    """
    # test_sort("Bubble Sort", shell_sort, arr, len(arr))
    # test_sort("Bubble Sort New", shell_sort_new, arr2, len(arr2))

