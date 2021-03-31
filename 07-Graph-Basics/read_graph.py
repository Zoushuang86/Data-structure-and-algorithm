
class ReadGraph:

    def __init__(self, graph, filename):

        self.__readFile(filename)

        V = int(self.context[0].split(" ")[0])
        if V < 0:
            assert Exception("number of vertices in a Graph must be nonnegative")
        assert V == graph.V()

        E = int(self.context[0].split(" ")[1])
        if E < 0:
            assert Exception("number of edges in a Graph must be nonnegative")

        for i in range(E):
            v = int(self.context[i + 1].split(" ")[0])
            w = int(self.context[i + 1].split(" ")[1])
            assert (v >= 0) and (v < V)
            assert (w >= 0) and (w < V)
            graph.add(v, w)

    def __readFile(self, filename):
        assert filename is not None
        with open(filename, "r") as f:
            self.context = f.read().split("\n")