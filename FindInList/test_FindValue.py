from unittest import TestCase
import random
from FindInList.Bisect import bisect_value_index, bisect_index_insert
from FindInList.FindLowestLinear import find_lowest_linear
from FindInList.FindIndex import find_index
from bisect import bisect_left


class Test(TestCase):

    def setUp(self) -> None:
        nb_tests = 100
        test_range = 100
        test_size_list = 20
        # those values are supposed to be in the list
        self.tests = []

        # those values are not supposed to be in the list
        self.tests_fail = []

        for _ in range(nb_tests):
            self.tests.append(random.sample(range(test_range), test_size_list))

        for _ in range(int(nb_tests/2)):
            self.tests_fail.append(random.sample(range(test_range, 2*test_range), test_size_list))

        for _ in range(int(nb_tests/2)):
            self.tests_fail.append(random.sample(range((-2)*test_range, -10), test_size_list))

    def test_bisect_value_index(self):
        for test in self.tests:
            test.sort()
            x = random.choice(test)
            self.assertEqual(test.index(x), bisect_value_index(test, x, 0, len(test) - 1))

        for test_is, test_not in zip(self.tests, self.tests_fail):
            test_is.sort()
            x = random.choice(test_not)
            self.assertFalse(bisect_value_index(test_is, x, 0, len(test_is) - 1))

    def test_bisect_index_insert(self):
        for test in self.tests:
            test.sort()
            x = random.choice(test)
            self.assertEqual(bisect_left(test, x), bisect_index_insert(test, x, 0, len(test) - 1))

    def test_find_index(self):
        for test in self.tests:
            test.sort()
            x = random.choice(test)
            self.assertEqual(test.index(x), find_index(test, x))

    def test_find_lowest_linear(self):
        for test in self.tests:
            self.assertEqual(min(test), find_lowest_linear(test)[1])

