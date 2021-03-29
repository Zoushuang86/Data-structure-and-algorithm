# 没有自环边，但有可能有平行边

class SparseGraph:
    def __init__(self, n, directed):
        self.__n = n  # 结点数
        self.__m = 0  # 边数
        self.__directed = directed  # 是否是有向图
        self.__g = []
        for i in range(self.__n):
            self.__g.append([])

    def V(self):
        return self.__n

    def E(self):
        return self.__m

    def add(self, v, w):
        assert (v >= 0) and (v < self.__n)
        assert (w >= 0) and (w < self.__n)
        self.__g[v].append(w)
        if (not self.__directed) and (v != w):
            self.__g[w].append(v)
        self.__m += 1

    def hasEdge(self, v, w):
        assert (v >= 0) and (v < self.__n)
        assert (w >= 0) and (w < self.__n)
        for i in range(len(self.__g[v])):
            if self.__g[v][i] == w:
                return True
        return False

    def printGraph(self):
        for i in range(self.__n):
            print("{}->{}".format(i, self.__g[i]))

    def adj(self, v):
        assert (v >= 0) and (v < self.__n)
        it = iter(self.__g[v])
        return it, len(self.__g[v])

