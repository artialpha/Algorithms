from unittest import TestCase
from random import choices
from collections import namedtuple
from Sorting.CountSort import CountSort


class TestCountSort(TestCase):
    def test_counting_sort(self):
        nb_tests = 100
        rng = 50
        for _ in range(nb_tests):
            ls = choices(range(rng), k=2*rng)

            lsc = sorted(ls)
            res = CountSort.sort(ls, rng)

            self.assertEqual(lsc, res)

    def test_find_digit1(self):
        test = 9876543210
        test_str = str(test)

        for digit in test_str[::-1]:
            res = CountSort.find_digit(test, int(digit)+1)
            self.assertEqual(int(digit), res)

    def test_find_digit2(self):
        TestDigit = namedtuple('TestDigit', ['number', 'place', 'digit'])
        tests = list()

        tests.append(TestDigit(5, 1, 5))
        tests.append(TestDigit(93, 2, 9))
        tests.append(TestDigit(467, 2, 6))
        tests.append(TestDigit(200, 1, 0))
        tests.append(TestDigit(999, 3, 9))
        tests.append(TestDigit(987, 2, 8))

        for test in tests:
            res = CountSort.find_digit(test.number, test.place)
            self.assertEqual(res, test.digit)

    def test_counting_d1(self):
        nb_tests = 100

        for _ in range(nb_tests):
            ls = choices(range(10), k=nb_tests)

            lsc = sorted(ls)
            res = CountSort.counting_sort_by_digit(ls, 10)

            self.assertEqual(lsc, res)

    def test_counting_d2(self):
        nb_tests = 100
        for _ in range(nb_tests):
            ls = choices(range(10), k=nb_tests)
            ls = [nb*10 for nb in ls]

            lsc = sorted(ls)
            res = CountSort.counting_sort_by_digit(ls, 10, 2)

            self.assertEqual(lsc, res)

    def test_counting_d22(self):
        nb_tests = 100

        def my_key(x):
            return CountSort.find_digit(x, 2)

        for _ in range(nb_tests):
            ls = choices(range(10, 100), k=nb_tests)
            ls2 = choices(range(40, 50), k=3)
            ls.extend(ls2)

            lsc = sorted(ls, key=my_key)
            res = CountSort.counting_sort_by_digit(ls, 10, 2)

            self.assertEqual(lsc, res)

    def test_counting_d3(self):
        nb_tests = 100

        def my_key(x):
            return CountSort.find_digit(x, 3)

        for _ in range(nb_tests):
            ls = choices(range(100, 1000), k=nb_tests)
            ls2 = choices(range(400, 500), k=3)
            ls.extend(ls2)

            lsc = sorted(ls, key=my_key)
            res = CountSort.counting_sort_by_digit(ls, 10, 3)

            self.assertEqual(lsc, res)




