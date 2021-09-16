from typing import TypeVar, List, Generic
T = TypeVar("T")    # Can be anything


from sort_test_helper import generate_random_list, test_sort, is_sorted

def selection_sort(arr: List[Generic[T]], n: int):
    for i in range(n):
        # 寻找[i, n)区间里的最小值
        minIndex = i
        for j in range(i+1, n, 1):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[minIndex], arr[i] = arr[i], arr[minIndex]


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 重写>
    def __gt__(self, other):
        if self.score > other.score:
            return True
        else:
            return False

    # 重写<
    def __lt__(self, other):
        if self.score < other.score:
            return True
        else:
            return False

    # 重写print
    def __str__(self):
        return str(self.name)+":"+str(self.score)


if __name__ == "__main__":
    # arr = [1.0, 2.6, 0.3]
    # new_arry = selection_sort(arr, len(arr))
    # print(new_arry)
    #
    # arr = [4, 3, 2, 1]
    # new_arry = selection_sort(arr, len(arr))
    # print(new_arry)
    #
    # arr = ["a", "c", "b"]
    # new_arry = selection_sort(arr, len(arr))
    # print(new_arry)
    #
    # # 相同数的前后顺序不变，具有稳定性
    # arr = [Student("aaa", 90), Student("bbb", 80), Student("ccc", 70), Student("ddd", 80)]
    # new_arry = selection_sort(arr, len(arr))
    # for s in new_arry:
    #     print(s, end=" ")
    # print()
    #
    # arr = generate_random_list(10, 0, 20)
    # print(arr)
    # new_arry = selection_sort(arr, len(arr))
    # print(new_arry)

    n = 10000
    arr = generate_random_list(n, 0, n*3)
    test_sort("Selection Sort", selection_sort, arr, len(arr))
