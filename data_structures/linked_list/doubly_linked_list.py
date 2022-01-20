class Node:
    def __init__(self, value, previous=None):
        self._value = value
        self._previous = previous
        self._next = None

    def get_value(self):
        return self._value

    value = property(get_value)

    def get_next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node

    next = property(get_next, set_next)

    def get_previous(self):
        return self._previous

    def set_previous(self, previous_node):
        self._previous = previous_node

    previous = property(get_previous, set_previous)

    def add_value(self, value):
        if self._value:
            if self._next:
                self._next.add_value(value)
            else:
                self._next = Node(value, self)
        else:
            self._value = value

    def remove(self, value):
        if self.next:
            if self.next.value == value:
                self.next = self.next.next
            else:
                self.next.remove(value)

    def pop(self, index):
        if index == 1:
            if self.next:
                node = self.next
                self.next = self.next.next
                node.next = None
                return node
            return
        elif self.next:
            return self.next.pop(index - 1)
        return

    def __str__(self):
        if self._next:
            return f"{self._value}, {self._next}"
        else:
            return f"{self._value}"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_value(self, value):
        if self.head:
            self.head.add_value(value)
        else:
            self.head = Node(value)
            self.tail = self.head

    def remove(self, value):
        if self.head:
            if self.head.value == value:
                self.head = self.head.next
            else:
                self.head.remove(value)

    def pop(self, index: int) -> Node:
        if index:
            return self.head.pop(index)
        else:
            node = self.head
            self.head = self.head.next
            node.next = None
            return node

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __len__(self):
        return len(tuple(self))

    def __str__(self):
        if self.head:
            return f"DoublyLinkedList[{self.head}]"
        else:
            return "DoublyLinkedList"


if __name__ == '__main__':
    linked = DoublyLinkedList()
    for i in range(10):
        linked.add_value(i)
    print(linked.pop(5))
    print(linked)
