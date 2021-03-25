from union_find_1 import UnionFind1
from union_find_2 import UnionFind2
from union_find_3 import UnionFind3
from union_find_4 import UnionFind4
from union_find_5 import UnionFind5
from union_find_6 import UnionFind6
import random
import time


def testUF1(n):
    uf = UnionFind1(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind1, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


def testUF2(n):
    uf = UnionFind2(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind2, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


def testUF3(n):
    uf = UnionFind3(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind3, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


def testUF4(n):
    uf = UnionFind4(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind4, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


def testUF5(n):
    uf = UnionFind5(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind5, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


def testUF6(n):
    uf = UnionFind6(n)
    start = time.time()

    # 进行n次操作, 每次随机选择两个元素进行合并操作
    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.union(a, b)

    for i in range(n):
        a = random.randint(0, n - 1)
        b = random.randint(0, n - 1)
        uf.is_connected(a, b)

    end = time.time()
    print("UnionFind6, {ops} ops, {time:.4f} s".format(ops=2*n, time=end-start))


if __name__ == "__main__":
    # UnionFind1, 20000 ops, 6.1260 s
    # UnionFind2, 20000 ops, 1.3700 s
    # UnionFind3, 20000 ops, 0.0840 s
    # UnionFind4, 20000 ops, 0.0843 s
    # rank方法不一定比size方法好，需要遇到特殊情况
    n = 1000000
    # testUF1(n)
    # testUF2(n)
    # testUF3(n)
    # UnionFind4, 2000000 ops, 8.9237 s
    # UnionFind5, 2000000 ops, 8.5868 s
    # UnionFind6, 2000000 ops, 9.1249 s
    testUF4(n)
    testUF5(n)
    testUF6(n)
