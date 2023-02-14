from unittest import TestCase
from random import sample
from Queue import Queue


class TestQueue(TestCase):

    def setUp(self):
        self.size = 8
        self.q = Queue(self.size)

    def test_general(self):
        self.assertEqual(0, self.q.p)
        self.assertEqual(0, self.q.q)
        self.assertEqual(self.size, self.q.size)
        self.assertEqual(self.size, len(self.q.arr))

    def test_push(self):
        values = sample(range(5*self.size), self.size)

        self.assertEqual(0, self.q.q)

        for i, v in enumerate(values, 1):
            self.q.push(v)
            self.assertEqual(i % self.size, self.q.q)
        self.assertEqual(0, self.q.q)
        print(self.q.arr)
        self.q.push(5)
        self.assertEqual(0, self.q.q)
        print(self.q.arr)

        all_not_none = all(v is not None for v in self.q.arr)
        self.assertTrue(all_not_none)

    def test_pop(self):
        values = sample(range(5*self.size), self.size)

        for v in values:
            self.q.push(v)

        self.assertEqual(0, self.q.p)
        self.assertEqual(0, self.q.q)

        print('Before pop: ', self.q)
        for i in range(self.size):
            self.assertEqual(i % self.size, self.q.p)
            self.q.pop()
            self.assertIsNone(self.q.arr[i])
        print('After pop: ', self.q)

        all_none = all(v is None for v in self.q.arr)
        self.assertTrue(all_none)

    def test_push_pop(self):
        half = int(self.size/2)
        quarter = int(half/2)

        values = sample(range(5*self.size), self.size)

        for v in values:
            self.q.push(v)

        self.assertEqual(0, self.q.q)
        print('after pushing to full: ', self.q)

        for _ in range(half):
            self.q.pop()

        self.assertEqual(half, self.q.p)
        print('after popping half: ', self.q)


        ############

        values = sample(range(5*self.size), quarter)

        for v in values:
            self.q.push(v)

        self.assertEqual(half, self.q.p)
        self.assertEqual(quarter, self.q.q)
        print('after pushing 1/4: ', self.q)

        #############

        for _ in range(half):
            self.q.pop()

        self.assertEqual(0, self.q.p)
        print('after popping 1/2: ', self.q)

        #############

        values = sample(range(5*self.size), quarter)

        for v in values:
            self.q.push(v)

        self.assertEqual(0, self.q.p)
        self.assertEqual(half, self.q.q)
        print('after pushing 1/4: ', self.q)

        #############

        for _ in range(quarter):
            self.q.pop()

        self.assertEqual(quarter, self.q.p)
        print('after popping 1/2: ', self.q)
