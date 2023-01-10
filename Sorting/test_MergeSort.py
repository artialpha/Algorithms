import random
from unittest import TestCase
from Sorting.MergeSort import MergeSort


class TestMergeSort(TestCase):
    def test_merge(self):
        number_of_tests = 100
        size = 8
        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = random.sample(range(size), size)
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
        size = 8
        for _ in range(number_of_tests):
            merge = MergeSort()
            ls = random.sample(range(size), size)
            ls_copy = ls[:]

            ls_sorted = sorted(ls)
            p = 0
            r = len(ls_copy) - 1
            merge.sort(ls_copy, p, r)

            self.assertEqual(ls_sorted, ls_copy)
