import random
from typing import TypeVar, Generic
T = TypeVar("T")


class IndexMaxHeap:
    def __init__(self, capacity: int, arr=None):
        if arr == None:
            # index=0不存储
            self.__data = [Generic[T]] * (capacity+1)
            self.__count = 0
            self.__capacity = capacity
            self.__indexes = [Generic[T]] * (capacity+1)
            self.__reverse = [0] * (capacity+1)
        else:
            self.__data = [Generic[T]] * (capacity+1)
            self.__indexes = [Generic[T]] * (capacity + 1)
            self.__reverse = [0] * (capacity + 1)
            self.__capacity = capacity
            for i in range(self.__capacity):
                self.__data[i+1] = arr[i]
            self.__count = capacity

            for i in range(self.__count // 2, 0, -1):
                self.__shiftDown(i)

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def __shiftUp(self, k):
        while k > 1 and self.__data[self.__indexes[k//2]] < self.__data[self.__indexes[k]]:
            self.__indexes[k // 2], self.__indexes[k] = self.__indexes[k], self.__indexes[k // 2]
            self.__reverse[self.__indexes[k // 2]] = k // 2
            self.__reverse[self.__indexes[k]] = k
            k = k // 2

    # 传入的i对用户而言，是从0索引的
    def insert(self, i, item):
        assert self.__count + 1 <= self.__capacity
        assert i+1 >= 1 and 1+1 <= self.__capacity
        i += 1
        self.__data[i] = item
        self.__indexes[self.__count+1] = i
        self.__reverse[i] = self.__count+1
        self.__count += 1
        self.__shiftUp(self.__count)

    def __shiftDown(self, k):
        while 2*k <= self.__count:
            # 在此轮循环中，data[k]和data[j]交换位置
            j = 2*k
            if j+1 <= self.__count and self.__data[self.__indexes[j+1]] > self.__data[self.__indexes[j]]:
                j += 1
            if self.__data[self.__indexes[k]] >= self.__data[self.__indexes[j]]:
                break
            else:
                self.__indexes[k], self.__indexes[j] = self.__indexes[j], self.__indexes[k]
                self.__reverse[self.__indexes[k]] = k
                self.__reverse[self.__indexes[j]] = j
                k = j

    def extructMax(self):
        assert self.__count > 0
        ret = self.__data[self.__indexes[1]]
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__reverse[self.__indexes[1]] = 1
        self.__reverse[self.__indexes[self.__count]] = 0
        self.__count -= 1
        self.__shiftDown(1)
        return ret

    def extructMaxIndex(self):
        assert self.__count > 0
        ret = self.__indexes[1] - 1
        self.__indexes[1], self.__indexes[self.__count] = self.__indexes[self.__count], self.__indexes[1]
        self.__reverse[self.__indexes[1]] = 1
        self.__reverse[self.__indexes[self.__count]] = 0
        self.__count -= 1
        self.__shiftDown(1)
        return ret

    def getItem(self, i):
        assert self.__contain(i)
        return self.__data[i+1]

    def __contain(self, i):
        assert (i + 1 >= 1) and (i + 1 <= self.__capacity)
        return self.__reverse[i+1] != 0

    def change(self, i, newItem):
        assert self.__contain(i)
        i += 1
        self.__data[i] = newItem
        # 找到indexes[j]=i，j表示data[i]在堆中的位置
        # 之后shiftUP(j), 再shiftDown(j)
        # for j in range(1, self.__count+1):
        #     if self.__indexes[j] == i:
        #         self.__shiftUp(j)
        #         self.__shiftDown(j)
        j = self.__reverse[i]
        self.__shiftUp(j)
        self.__shiftDown(j)


if __name__ == "__main__":
    n = 20
    maxheap = IndexMaxHeap(100)
    for i in range(n):
        maxheap.insert(random.randint(0, 99))
    maxheap.printHeap()
    # while maxheap.isEmpty() == False:
    maxheap.extructMax()
    maxheap.printHeap()
