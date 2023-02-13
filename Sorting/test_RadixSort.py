from unittest import TestCase
from random import sample
from RadixSort import RadixSort


class TestRadixSort(TestCase):
    def test_radix_1digit(self):
        nb_tests = 100

        a = 0
        b = 10
        rng = range(a, b)
        size = 5

        for _ in range(nb_tests):
            ls = sample(rng, size)

            lsc = sorted(ls)
            res = RadixSort.sort(ls, 1)

            self.assertEqual(lsc, res)

    def test_radix_digits(self):
        nb_tests = 100

        digits = 10
        a = 10 ** (digits-1)
        b = 10 ** digits
        rng = range(a, b)
        size = 100

        for _ in range(nb_tests):
            ls = sample(rng, size)

            lsc = sorted(ls)
            res = RadixSort.sort(ls, digits)

            self.assertEqual(lsc, res)
