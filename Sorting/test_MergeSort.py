from random import sample, shuffle, choices
from unittest import TestCase
from Sorting.MergeSort import MergeSort


class TestMergeSort(TestCase):
    def test_merge(self):
        number_of_tests = 100
        size = 8
        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = sample(range(size), size)
            ls_copy = ls[:]
            p = 0
            r = len(ls_copy) - 1
            q = int((p+r)/2)
            ls_copy = sorted(ls_copy[p:q+1]) + sorted(ls_copy[q+1:r+1])

            #print(f'ls: {ls_copy}')
            #print(f'p: {p}, q: {q}, r: {r}')
            print(f'ls1: {ls_copy[p:q+1]}; ls2: {ls_copy[q+1:r+1]}')

            ls_sorted = sorted(ls)
            merge.merge(ls_copy, p, q, r)

            print(f'ls merged: {ls_copy}\n')
            self.assertEqual(ls_sorted, ls_copy)

    def test_merge2(self):
        merge = MergeSort()
        ls = [6, 0]
        p = 0
        r = len(ls) - 1
        q = int((p+r)/2)
        ls_merged = merge.merge(ls, p, q, r)
        print(f'p: {p}, q: {q}, q+1: {q+1} r {r}')
        print(f'ls merged: {ls}')
        self.assertEqual([0, 6], ls)

    def test_sort(self):
        number_of_tests = 100
        size = 21
        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = sample(range(size), size)
            ls_copy = ls[:]

            # sorted by python and by my algorithm
            ls_sorted = sorted(ls)
            print(f'Before sorting: {ls_copy}')
            merge.sort(ls_copy, 0, len(ls_copy) - 1)
            print(f'After sorting: {ls_copy}\n')

            self.assertEqual(ls_sorted, ls_copy)

    def test_sort_with_repetition(self):
        number_of_tests = 100
        rng = range(100)
        size = 30

        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = choices(rng, k=size)
            ls_copy = ls[:]

            python_result = sorted(ls)
            merge.sort(ls_copy, 0, len(ls_copy) - 1)

            self.assertEqual(python_result, ls_copy)

    def test_show_steps(self):
        size = 8
        ls = list(range(size))
        shuffle(ls)
        print(f'ls before sorting: {ls}')

        merge = MergeSort()
        merge.sort(ls, 0, len(ls)-1)

        print(f'ls after sorting: {ls}\n')
        merge.show_steps()

