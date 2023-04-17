class UnionFind1:
    def __init__(self, n):
        # 初始化都不相连接
        self.__id = [i for i in range(n)]
        self.__count = n

    def find(self, p):
        assert (p >= 0) and (p < self.__count)
        return self.__id[p]

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id != q_id:
            for i in range(self.__count):
                if self.__id[i] == p_id:
                    self.__id[i] = q_id
