class UnionFind5:
    def __init__(self, n):
        self.__parent = [i for i in range(n)]
        self.__count = n
        self.__rank = [1] * n #以i为根的集合的层数

    def find(self, p):
        assert (p >= 0) and (p < self.__count)
        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        if p_root != q_root:
            if self.__rank[p_root] < self.__rank[q_root]:
                self.__parent[p_root] = q_root
            elif self.__rank[q_root] < self.__rank[p_root]:
                self.__parent[q_root] = p_root
            else:
                self.__parent[p_root] = q_root
                self.__rank[q_root] += 1
