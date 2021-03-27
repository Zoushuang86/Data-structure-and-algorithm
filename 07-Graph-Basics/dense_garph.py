class DenseGraph:
    def __init__(self, n, directed):
        self.__n = n    # 节点数
        self.__m = 0    # 边数
        self.__directed = directed  # 是否是有向图
        for i in range(n):
            self.__g = [[False] * n] * n

    def V(self):
        return self.__n

    def E(self):
        return self.__m

    def add(self, v, w):
        assert (v >= 0) and (v < self.__n)
        assert (w >= 0) and (w < self.__n)
        if self.hasEdge(v, w):
            return
        self.__g[v][w] = True
        if not self.__directed:
            self.__g[w][v] = True
        self.__m += 1

    def hasEdge(self, v, w):
        assert (v >= 0) and (v < self.__n)
        assert (w >= 0) and (w < self.__n)
        return self.__g[v][w]
