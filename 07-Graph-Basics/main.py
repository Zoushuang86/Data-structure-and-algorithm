from read_graph import ReadGraph
from dense_garph import DenseGraph
from sparse_graph import SparseGraph
from component import Component

if __name__ == "__main__":

    N1 = 13
    filename1 = "testG1.txt"
    g1 = SparseGraph(N1, False)
    ReadGraph1 = ReadGraph(g1, "testG1.txt")
    component1 = Component(g1)
    # g1.printGraph()
    print("TestG1.txt, Componet Count:", component1.count())

    N2 = 7
    filename2 = "testG2.txt"
    g2 = SparseGraph(N2, False)
    ReadGraph2 = ReadGraph(g2, "testG1.txt")
    component2 = Component(g2)
    # g2.printGraph()
    print("TestG2.txt, Componet Count:", component1.count())
