from queue import Queue


class BST:

    class __Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def __insert(self, node: __Node, key, value):
        if node == None:
            self.count += 1
            return self.__Node(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)
        return node

    def insert(self, key, value):
        self.root = self.__insert(self.root, key, value)

    def __contain(self, node: __Node, key):
        if node == None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.__contain(node.left, key)
        else:
            return self.__contain(node.right, key)

    def contain(self, key):
        return self.__contain(self.root, key)

    def __pre_order(self, node: __Node):
        if node != None:
            print(node.key)
            self.__pre_order(node.left)
            self.__pre_order(node.right)

    def pre_order(self):
        self.__pre_order(self.root)

    def __in_order(self, node: __Node):
        if node != None:
            self.__in_order(node.left)
            print(node.key)
            self.__in_order(node.right)

    def in_order(self):
        self.__in_order(self.root)

    def __post_order(self, node: __Node):
        if node != None:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.key)

    def post_order(self):
        self.__post_order(self.root)

    def destroy(self, node: __Node):
        if node != None:
            self.destroy(node.left)
            self.destroy(node.right)
            del node
            self.count -= 1

    def level_order(self):
        q = Queue()
        q.put(self.root)
        while q.empty() == False:
            node = q.get()
            print(node.key)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def __minimum(self, node: __Node):
        if node.left == None:
            return node
        return self.__minimum(node.left)

    def minimum(self):
        assert self.count != 0
        min_node = self.__minimum(self.root)
        return min_node.key

    def __maximum(self, node: __Node):
        if node.right == None:
            return node
        return self.__maximum(node.right)

    def maximum(self):
        assert self.count != 0
        max_node = self.__maximum(self.root)
        return max_node.key

    def __remove_min(self, node: __Node):
        if node.left == None:
            right_node = node.right
            del node
            self.count -= 1
            return right_node
        node.left = self.__remove_min(node.left)
        return node

    def remove_min(self):
        if self.root != None:
            self.root = self.__remove_min(self.root)

    def __remove_max(self, node: __Node):
        if node.right == None:
            left_node = node.left
            del node
            self.count -= 1
            return left_node
        node.right = self.__remove_max(node.right)
        return node

    def remove_max(self):
        if self.root != None:
            self.root = self.__remove_max(self.root)


if __name__ == "__main__":
    pass