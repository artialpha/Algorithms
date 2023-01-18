from unittest import TestCase
from random import sample
from Sorting.HeapSort import HeapSort


class TestHeapSort(TestCase):

    def test_heap_sort(self):
        nb_tests = 10
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), nb_tests)

            # sorted by python
            ls_sorted_copy = sorted(ls)

            # sorted by my heapsort
            print(f'before my heap sort: {ls}')
            hp.heapsort(ls)
            print(f'after my heap sort: {ls}\n')

            # check if they are equal as they should be
            self.assertEqual(ls_sorted_copy, ls)
