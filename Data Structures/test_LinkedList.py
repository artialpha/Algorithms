from unittest import TestCase
from random import randint, sample, randrange
from LinkedList import LinkedList, Node


class TestLinkedList(TestCase):

    def setUp(self):
        self.size = 8
        self.a = 0
        self.b = 100
        self.rng = range(self.a, self.b)
        self.nb_test = 20

    def random_node(self):
        value = randint(self.a, self.b)
        return Node(value)

    def random_linked_list(self, get_values=False):
        ll = LinkedList()
        values = sample(self.rng, self.size)

        for v in reversed(values):
            node = Node(v)
            ll.insert_start(node)

        if get_values:
            return ll, values
        else:
            return ll


    def test_general(self):
        node = self.random_node()
        ll = LinkedList(node)
        self.assertIs(node, ll.head)
        print(ll)

    def test_insert_start(self):
        first_node = self.random_node()
        ll = LinkedList(first_node)
        print('first node: ',  first_node)

        node = self.random_node()
        ll.insert_start(node)
        print('next node: ', node)

        self.assertIs(node.next, first_node)
        print('linked list: ', ll)

    def test_check_in_list(self):
        ll = LinkedList()
        values = []

        for i in range(self.size):
            node = self.random_node()
            ll.insert_start(node)
            values.append(node.value)

        for v in values:
            self.assertTrue(ll.check_in_list(v))

        while self.nb_test > 0:
            if (r := randint(self.a, self.b)) not in values:
                self.assertFalse(ll.check_in_list(r))
                self.nb_test -= 1

    def test_insert_start2(self):
        ll = LinkedList()
        head = None
        tail = None

        for i in range(self.size):
            node = self.random_node()
            if i == 0:
                tail = node
            elif i == self.size- 1:
                head = node
            ll.insert_start(node)
            print(ll)

        self.assertIs(ll.head, head)
        self.assertIs(ll.tail, tail)

    def test_find_node(self):
        for _ in range(self.nb_test):
            ll, values = self.random_linked_list(True)

            index = randrange(1, self.size-1)
            node = ll.find_node(values[index])

            self.assertEqual(values[index-1], node.prev.value)
            self.assertEqual(values[index+1], node.next.value)

    def test_delete_node(self):
        for _ in range(self.nb_test):

            ll, values = self.random_linked_list(True)

            index = randrange(1, self.size-1)
            node = ll.find_node(values[index])
            prev = node.prev
            next_ = node.next

            self.assertTrue(ll.check_in_list(node))
            self.assertTrue(ll.check_in_list(prev))
            self.assertTrue(ll.check_in_list(next_))

            ll.delete_node(node)

            self.assertFalse(ll.check_in_list(node))
            self.assertTrue(ll.check_in_list(prev))
            self.assertTrue(ll.check_in_list(next_))
            self.assertIs(prev.next, next_)
            self.assertIs(next_ .prev, prev)
