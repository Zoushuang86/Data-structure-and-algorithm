import sys
import types
sys.setrecursionlimit(999999999)

class Component:
    def __init__(self, graph):
        self.__graph = graph
        self.__visit = [False] * graph.V()   # 记录节点是否被访问
        self.__ccount = 0   # 记录连通分量数量

        for i in range(graph.V()):
            if self.__visit[i] is False:
                self.__tramp(self.__dfs, i)
                self.__ccount += 1

    def count(self):
        return self.__ccount

    def __dfs(self, v):
        self.__visit[v] = True
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
