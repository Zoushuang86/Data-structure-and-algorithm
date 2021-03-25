from union_find_1 import UnionFind1
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


if __name__ == "__main__":
    testUF1(10000)
