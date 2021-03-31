import sys
import types
sys.setrecursionlimit(999999999)


class Component:
    def __init__(self, graph):
        self.__graph = graph
        self.__visit = [False] * graph.V()   # 记录节点是否被访问
        self.__ccount = 0   # 记录连通分量数量
        self.__id = [-1] * graph.V()  # 节点之间是否相连

        for i in range(graph.V()):
            if self.__visit[i] is False:
                self.__tramp(self.__dfs, i)
                self.__ccount += 1

    def count(self):
        return self.__ccount

    def __dfs(self, v):
        self.__visit[v] = True
        self.__id[v] = self.__ccount
        it, num = self.__graph.adj(v)
        for i in range(num):
            item = next(it)
            if self.__visit[item] is False:
                yield self.__dfs(i)

    # 尾递归优化Trampline
    def __tramp(self, gen, arg):
        g = gen(arg)
        while isinstance(g, types.GeneratorType):
            g = g.__next__()

    def isConnected(self, v, w):
        assert (v >= 0) and (v < self.__graph.V())
        assert (w >= 0) and (w < self.__graph.V())
        return self.__id[v] == self.__id[w]