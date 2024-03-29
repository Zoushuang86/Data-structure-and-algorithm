from queue import Queue
from collections import Counter
import time


class BST:

    class __Node:
        def __init__(self, key, value, node=None):
            if not node:
                self.key = key
                self.value = value
                self.left = None
                self.right = None
            else:
                self.key = node.key
                self.value = node.value
                self.left = node.left
                self.right = node.right

    def __init__(self):
        self.__root = None
        self.__count = 0

    def size(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0

    def __insert(self, node: __Node, key, value):
        if not node:
            self.__count += 1
            return self.__Node(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left = self.__insert(node.left, key, value)
        else:
            node.right = self.__insert(node.right, key, value)
        return node

    def insert(self, key, value):
        self.__root = self.__insert(self.__root, key, value)

    def __contain(self, node: __Node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self.__contain(node.left, key)
        else:
            return self.__contain(node.right, key)

    def contain(self, key):
        return self.__contain(self.__root, key)

    def __search(self, node: __Node, key):
        if not node:
            return None
        if key == node.key:
            return node.value
        elif key < node.key:
            return self.__search(node.left, key)
        else:
            return self.__search(node.right, key)

    def search(self, key):
        return self.__search(self.__root, key)

    def __pre_order(self, node: __Node):
        if node:
            print(node.key)
            self.__pre_order(node.left)
            self.__pre_order(node.right)

    def pre_order(self):
        self.__pre_order(self.__root)

    def __in_order(self, node: __Node):
        if node:
            self.__in_order(node.left)
            print(node.key)
            self.__in_order(node.right)

    def in_order(self):
        self.__in_order(self.__root)

    def __post_order(self, node: __Node):
        if node:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.key)

    def post_order(self):
        self.__post_order(self.__root)

    def destroy(self, node: __Node):
        if node:
            self.destroy(node.left)
            self.destroy(node.right)
            del node
            self.__count -= 1

    def level_order(self):
        q = Queue()
        q.put(self.__root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    def __minimum(self, node: __Node):
        if not node.left:
            return node
        return self.__minimum(node.left)

    def minimum(self):
        assert self.__count != 0
        min_node = self.__minimum(self.__root)
        return min_node

    def __maximum(self, node: __Node):
        if not node.right:
            return node
        return self.__maximum(node.right)

    def maximum(self):
        assert self.__count != 0
        max_node = self.__maximum(self.__root)
        return max_node

    def __remove_min(self, node: __Node):
        if not node.left:
            right_node = node.right
            del node
            self.__count -= 1
            return right_node
        node.left = self.__remove_min(node.left)
        return node

    def remove_min(self):
        if self.__root:
            self.__root = self.__remove_min(self.__root)

    def __remove_max(self, node: __Node):
        if not node.right:
            left_node = node.left
            del node
            self.__count -= 1
            return left_node
        node.right = self.__remove_max(node.right)
        return node

    def remove_max(self):
        if self.__root:
            self.__root = self.__remove_max(self.__root)

    def __remove(self, node: __Node, key):
        # 终止条件
        if not node:
            return None
        # 首先找到待删除的节点
        if key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        else:
            # 仅有一个孩子或者没有孩子的情况
            if not node.left:
                right_node = node.right
                del node
                self.__count -= 1
                return right_node
            if not node.right:
                left_node = node.left
                del node
                self.__count -= 1
                return left_node
            # 待删除节点都有左右孩子
            # 找到待删除节点右子树最小节点，即后驱为将要替换的节点
            successor = self.__Node(node=self.__minimum(node.right))
            self.__count += 1
            # 后驱的右子树是删除最小值后返回的右子树根节点
            successor.right = self.__remove_min(node.right)
            # 后驱的左子树是待删除节点的左子树
            successor.left = node.left
            del node
            self.__count -= 1
            # 返回删除节点后子树的根节点
            return successor

    def remove(self, key):
        self.__root = self.__remove(self.__root, key)


if __name__ == "__main__":
    f = open("bible.txt", "r")
    replace = [".", ",", ":", "(", ")", "?", "!", "-", ";", "\n"]
    content = f.read().lower()
    f.close()
    for e in replace:
        content = content.replace(e, "")
    content = content.replace("'", " ")
    content = content.split(" ")
    print(len(content))
    c = Counter(content)
    print(c.get("god"))
    bst = BST()
    for key in c.keys():
        bst.insert(key, c.get(key))
    start = time.time()
    print(bst.search("god"))
    end = time.time()
    print("time: {:0.6f} s".format(end-start))





