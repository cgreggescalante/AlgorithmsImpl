from utils.random_array import random_array


class BinaryTree:
    def __init__(self, value, parent=None, data_type=None):
        self._value = value
        self._left = None
        self._right = None
        self._parent = parent
        self._data_type = data_type

    def get_value(self):
        return self._value

    def set_value(self, value):
        if self._data_type:
            if not isinstance(value, self._data_type):
                raise ValueError(f"Value {value} must be of type {self._data_type}")
        self._value = value

    value = property(get_value, set_value)

    def get_left(self):
        return self._left

    def set_left(self, left):
        self._left = left

    left = property(get_left, set_left)

    def get_right(self):
        return self._right

    def set_right(self, right):
        self._right = right

    right = property(get_right, set_right)

    def add_value(self, *values):
        for value in values:
            if self._data_type:
                if not isinstance(value, self._data_type):
                    raise ValueError(f"Value {value} must be of type {self._data_type}")
            if val < self._value:
                if self._left is None:
                    self._left = BinaryTree(value, self)
                else:
                    self._left.add_value(value)
            else:
                if self._right is None:
                    self._right = BinaryTree(value, self)
                else:
                    self._right.add_value(value)

    def inorder(self):
        arr = []
        if self._left:
            arr.extend(self._left.inorder())
        arr.append(self._value)
        if self._right:
            arr.extend(self._right.inorder())
        return arr

    def preorder(self):
        arr = [self._value]
        if self._left:
            arr.extend(self._left.preorder())
        if self._right:
            arr.extend(self._right.preorder())
        return arr

    def postorder(self):
        arr = []
        if self._left:
            arr.extend(self._left.postorder())
        if self._right:
            arr.extend(self._right.postorder())
        arr.append(self._value)
        return arr

    def __contains__(self, item):
        if self._value == item:
            return True
        if self._left and item in self._left:
            return True
        if self._right and item in self._right:
            return True

    def depth(self):
        l, r = 0, 0
        if self._left:
            l = self._left.depth()
        if self._right:
            r = self._right.depth()
        return 1 + max((l, r))

    def search(self, value):
        if self._data_type:
            if not isinstance(value, self._data_type):
                raise ValueError(f"Value {value} must be of type {self._data_type}")
        if self.value == value:
            return self
        l, r = None, None
        if self._left:
            l = self._left.search(value)
        if self._right:
            r = self._right.search(value)
        if l:
            return l
        return r

    def inorder_successor(self):
        successor = self._right
        while successor.left:
            successor = successor.left
        return successor

    def remove(self, value=None):
        if value:
            node = self.search(value)
        else:
            node = self
        left = node == node._parent.left
        if node:
            if node._left and node._right:
                successor = self.inorder_successor()
                self._value = successor.value
                successor.remove()
            elif node._left:
                if left:
                    node._parent.left = node._left
                else:
                    node._parent.right = node._left
            elif node._right:
                if left:
                    node._parent.left = node._right
                else:
                    node._parent.right = node._right
            else:
                if left:
                    node._parent.left = None
                else:
                    node._parent.right = None


if __name__ == '__main__':
    tree = BinaryTree(10, data_type=int)

    for val in random_array(1, 100, 20):
        tree.add_value(val)
    tree.add_value(20)

    print(tree.preorder())
    print(tree.depth())
    tree.remove(20)
    print(tree.preorder())
