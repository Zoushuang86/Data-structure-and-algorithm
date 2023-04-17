from union_find_test_helper import *


if __name__ == "__main__":
    n = 10000
    # UnionFind1, 20000 ops, 5.4345 s
    testUF1(n)
    # UnionFind2, 20000 ops, 1.1780 s
    testUF2(n)
