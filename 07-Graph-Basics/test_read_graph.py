from read_graph import ReadGraph
from dense_garph import DenseGraph
from sparse_graph import SparseGraph


if __name__ == "__main__":

    N = 13
    filename = "testG1.txt"
    g1 = SparseGraph(N, False)
    readGraph1 = ReadGraph(g1, "testG1.txt")
    g1.printGraph()

    g2 = DenseGraph(N, False)
    readGraph2 = ReadGraph(g2, filename)
    g2.printGraph()
