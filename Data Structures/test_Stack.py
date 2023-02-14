from unittest import TestCase
from random import sample, randint
from Stack import Stack


class TestStack(TestCase):
    def setUp(self):
        self.size = 8
        self.s = Stack(self.size)

    def test_push(self):
        values = sample(range(self.size*3), self.size)

        self.assertEqual(-1, self.s.top)

        for i, v in enumerate(values):
            self.s.push(v)
            self.assertEqual(i, self.s.top)

        self.assertEqual(self.size - 1, self.s.top)

        rand_val = randint(0, self.size*3)
        self.s.push(rand_val)
        self.assertEqual(self.size - 1, self.s.top)

    def test_pop(self):
        values = sample(range(self.size*3), self.size)

        for v in values:
            self.s.push(v)

        self.assertEqual(self.size - 1, self.s.top)

        #########

        for i in range(self.size):
            self.assertEqual(self.size - (i + 1), self.s.top)
            self.s.pop()

        self.assertEqual(-1, self.s.top)
        self.s.pop()
        self.assertEqual(-1, self.s.top)
