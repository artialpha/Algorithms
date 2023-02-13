from unittest import TestCase
from random import random
from BucketSort import BucketSort


class TestBucketSort(TestCase):
    def test_sort(self):
        nb_tests = 100
        size = 15

        for _ in range(nb_tests):
            ls = [random() for _ in range(size)]

            lsc = sorted(ls)
            res = BucketSort.sort(ls)

            self.assertEqual(lsc, res)
