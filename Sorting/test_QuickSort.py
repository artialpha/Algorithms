from unittest import TestCase
from random import sample, choices
from Sorting.QuickSort import QuickSort


class TestQuickSort(TestCase):
    def test_partition(self):
        nb_tests = 100
        qs = QuickSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests*3), nb_tests)
            pivot = ls[len(ls)-1]

            # get an index of a pivot (it should be located in a place where it should be in a sorted list)
            my_index = qs.partition(ls, 0, len(ls)-1)
            # pivot index = index in a sorted list
            ls_sorted = sorted(ls)
            pivot_index = ls_sorted.index(pivot)

            self.assertTrue(pivot_index == my_index)

            before_pivot = ls[:pivot_index]
            after_pivot = ls[pivot_index+1:]

            print('pivot: ', pivot)
            print('ls after partitioning: ', ls)
            print('pivot:', pivot)
            print('before pivot:', before_pivot)
            for nb in before_pivot:
                self.assertTrue(nb < pivot)

            print('pivot:', pivot)
            print('after pivot:', after_pivot, '\n')
            for nb in after_pivot:
                self.assertTrue(pivot < nb)

    def test_partition_small_list(self):
        nb_tests = 100
        qs = QuickSort()
        size = list(range(1, 3))

        for s in size:
            for _ in range(nb_tests):
                ls = sample(range(nb_tests), s)
                pivot = ls[len(ls)-1]

                # get an index of a pivot (it should be located in a place where it should be in a sorted list)
                my_index = qs.partition(ls, 0, len(ls)-1)
                # pivot index = index in a sorted list
                ls_sorted = sorted(ls)
                pivot_index = ls_sorted.index(pivot)

                self.assertTrue(pivot_index == my_index)

    def test_quick_sort(self):
        nb_tests = 100
        rng = range(100)
        size = 30

        qs = QuickSort()

        for _ in range(nb_tests):
            ls = sample(rng, 30)

            # sorted by python; sorted returns a new list, doesn't change the original one
            ls_copy = sorted(ls)

            # sorted by my quick sort
            qs.quick_sort(ls, 0, len(ls)-1)

            self.assertEqual(ls_copy, ls)

    def test_sort_with_repetition(self):
        nb_tests = 100
        rng = range(100)
        size = 30

        qs = QuickSort()

        for _ in range(nb_tests):
            ls = choices(rng, k=size)

            result_python = sorted(ls)
            qs.quick_sort(ls, 0, len(ls)-1)

            self.assertEqual(result_python, ls)