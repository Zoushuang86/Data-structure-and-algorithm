class UnionFind2:
    def __init__(self, n):
        self.__parent = [i for i in range(n)]
        self.__count = n

    def find(self, p):
        assert (p >= 0) and (p < self.__count)
        while p != self.__parent[p]:
            p = self.__parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root != q_root:
            self.__parent[p_root] = q_root

