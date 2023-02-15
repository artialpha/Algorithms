
class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def __str__(self):
        msg = ''
        node = self.head
        while node:
            msg += f'{node.value} -> '
            node = node.next
        return msg[:-3]

    def insert_start(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node

    def insert_end(self, node):
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def check_in_list(self, value):
        node = self.head

        if isinstance(value, int):
            while node:
                if node.value == value:
                    return True
                node = node.next
            return False
        elif isinstance(value, Node):
            while node:
                if node is value:
                    return True
                node = node.next
            return False

    def find_node(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

    def delete_node(self, target):
        node = self.head
        while node:
            if node is target:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next
