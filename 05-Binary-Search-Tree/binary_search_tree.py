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

if __name__ == "__main__":
    pass
