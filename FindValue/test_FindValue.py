from unittest import TestCase
import random
from FindValue.Bisect import bisect
from FindValue.FindLowestLinear import find_lowest_linear


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
            # print(f' before sort: {test}')
            test.sort()
            # print(f' after sort: {test}\n')
            x = random.choice(test)
            self.assertEqual(test.index(x), bisect(test, x, 0, len(test)-1))

    def test_find_lowest_linear(self):
        for test in self.tests:
            # print(test)
            self.assertEqual(min(test), find_lowest_linear(test)[1])
