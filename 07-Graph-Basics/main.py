from sparse_graph import SparseGraph
from dense_garph import DenseGraph
import random

if __name__ == "__main__":
    N = 20
    M = 100

    # Sparse Graph
    g1 = DenseGraph(N, False)
    g2 = SparseGraph(N, False)
    for i in range(M):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        # print(a, b)
        g1.add(a, b)
        g2.add(a, b)

    # g1.printGraph()
    # print("\n")

    # O(E)
    for v in range(N):
        print("{} :".format(v), end=" ")
        it, num = g1.adj(v)
        for i in range(num):
            print("{}".format(next(it)), end=" ")
        print("")

    # Dense Graph
    g2 = SparseGraph(N, False)
    for i in range(M):
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        # print(a, b)
        g2.add(a, b)

    # g1.printGraph()
    # print("\n")

    # O(V^2)
    for v in range(N):
        print("{} :".format(v), end=" ")
        it, num = g2.adj(v)
        for i in range(num):
            print("{}".format(next(it)), end=" ")
        print("")

