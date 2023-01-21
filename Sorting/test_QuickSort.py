from unittest import TestCase
from random import sample
from Sorting.QuickSort import QuickSort


class TestQuickSort(TestCase):
    def test_partition(self):
        nb_tests = 100
        qs = QuickSort

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), nb_tests)
            pivot = ls[len(ls)-1]

            # get an index of a pivot (it should be located in a place where it should be in a sorted list)
            my_index = qs.partition(ls, 0, len(ls)-1)
            # pivot index = index in a sorted list
            ls_sorted = sorted(ls)
            pivot_index = ls_sorted.index(pivot)

            self.assertTrue(pivot_index == my_index)
