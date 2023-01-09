import random
from unittest import TestCase
from Sorting.MergeSort import MergeSort


class TestMergeSort(TestCase):
    def test_merge(self):
        number_of_tests = 100
        size = 11
        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = random.sample(range(size), size)
            ls1 = sorted(ls[:int(size/2)])
            ls2 = sorted(ls[int(size/2):])
            # print(f'ls1: {ls1}')
            # print(f'ls2: {ls2}')

            ls_sorted = sorted(ls)
            ls_merged = merge.merge(ls1, ls2)

            print(f'ls merged: {ls_merged}')
            self.assertEqual(ls_sorted, ls_merged)
