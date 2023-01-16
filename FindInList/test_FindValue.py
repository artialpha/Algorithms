from unittest import TestCase
import random
from FindInList.Bisect import bisect
from FindInList.FindLowestLinear import find_lowest_linear
from FindInList.FindIndex import find_index


class Test(TestCase):

    def setUp(self) -> None:
        nb_tests = 100
        test_range = 100
        test_size_list = 20
        self.tests = []

        for _ in range(nb_tests):
            self.tests.append(random.sample(range(test_range), test_size_list))

    def test_bisect(self):
        for test in self.tests:
            test.sort()
            x = random.choice(test)
            self.assertEqual(test.index(x), bisect(test, x, 0, len(test)-1))

    def test_find_index(self):
        for test in self.tests:
            test.sort()
            x = random.choice(test)
            self.assertEqual(test.index(x), bisect(test, x, 0, len(test)-1))

    def test_find_lowest_linear(self):
        for test in self.tests:
            self.assertEqual(min(test), find_lowest_linear(test)[1])

