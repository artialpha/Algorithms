from unittest import TestCase
from random import sample, randint
from heapq_max import heapify_max
from Sorting.HeapSort import HeapSort


class TestHeapSort(TestCase):

    def test_parent_index(self):
        hp = HeapSort()
        self.assertEqual(0, hp.heap_parent_index(1))
        self.assertEqual(0, hp.heap_parent_index(2))
        self.assertEqual(1, hp.heap_parent_index(3))
        self.assertEqual(1, hp.heap_parent_index(4))
        self.assertEqual(2, hp.heap_parent_index(5))
        self.assertEqual(2, hp.heap_parent_index(6))
        self.assertEqual(3, hp.heap_parent_index(7))
        self.assertEqual(3, hp.heap_parent_index(8))
        self.assertEqual(4, hp.heap_parent_index(9))
        self.assertEqual(4, hp.heap_parent_index(10))
        self.assertEqual(5, hp.heap_parent_index(11))
        self.assertEqual(5, hp.heap_parent_index(12))
        self.assertEqual(6, hp.heap_parent_index(13))
        self.assertEqual(6, hp.heap_parent_index(14))

    def test_left_index(self):
        hp = HeapSort()
        self.assertEqual(1, hp.heap_left_child_index(0))
        self.assertEqual(3, hp.heap_left_child_index(1))
        self.assertEqual(5, hp.heap_left_child_index(2))
        self.assertEqual(7, hp.heap_left_child_index(3))
        self.assertEqual(9, hp.heap_left_child_index(4))
        self.assertEqual(11, hp.heap_left_child_index(5))
        self.assertEqual(13, hp.heap_left_child_index(6))

    def test_right_index(self):
        hp = HeapSort()
        self.assertEqual(2, hp.heap_right_child_index(0))
        self.assertEqual(4, hp.heap_right_child_index(1))
        self.assertEqual(6, hp.heap_right_child_index(2))
        self.assertEqual(8, hp.heap_right_child_index(3))
        self.assertEqual(10, hp.heap_right_child_index(4))
        self.assertEqual(12, hp.heap_right_child_index(5))
        self.assertEqual(14, hp.heap_right_child_index(6))

    def test_check_heap_reverse_sorted(self):
        hp = HeapSort()
        nb_tests = 100
        size = 10

        for _ in range(nb_tests):
            ls = sorted(sample(range(size), size), reverse=True)
            self.assertTrue(hp.check_heap(ls))

    # https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
    def test_check_heap_list_from_heapify_true(self):
        hp = HeapSort()
        nb_tests = 100
        size = 10

        for _ in range(nb_tests):
            ls = sample(range(size), size)
            heapify_max(ls)
            self.assertTrue(hp.check_heap(ls))

    def test_check_heap_list_from_heapify_false(self):
        hp = HeapSort()
        nb_tests = 100
        size = 10

        for _ in range(nb_tests):
            ls = sample(range(size), size)
            heapify_max(ls)

            index1 = randint(1, size-1)
            parent_index = hp.heap_parent_index(index1)
            ls[parent_index], ls[index1] = ls[index1], ls[parent_index]

            self.assertFalse(hp.check_heap(ls))

    def test_heapify_heap_height_one(self):
        size = 3
        nb_tests = 100
        hp = HeapSort()

        for s in range(size):
            for n in range(nb_tests):
                ls = sample(range(nb_tests), size-1)
                nb = randint(nb_tests+1, nb_tests*2)
                ls.insert(s, nb)
                hp.heapify(ls, 0)
                self.assertTrue(hp.check_heap(ls))

    def test_heapify_swap_parent_child(self):
        size = 10
        nb_tests = 100
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), size)
            heapify_max(ls)

            index1 = randint(1, size-1)
            parent_index = hp.heap_parent_index(index1)
            ls[parent_index], ls[index1] = ls[index1], ls[parent_index]
            self.assertFalse(hp.check_heap(ls))
            hp.heapify(ls, parent_index)
            self.assertTrue(hp.check_heap(ls))

    def test_heapify_swap_grandparent_child(self):
        size = 10
        nb_tests = 100
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), size)
            heapify_max(ls)

            index1 = randint(3, size-1)
            parent_index = hp.heap_parent_index(index1)
            grandparent_index = hp.heap_parent_index(parent_index)
            ls[parent_index], ls[index1] = ls[index1], ls[parent_index]
            ls[parent_index], ls[grandparent_index] = ls[grandparent_index], ls[parent_index]

            self.assertFalse(hp.check_heap(ls))
            hp.heapify(ls, grandparent_index)
            self.assertTrue(hp.check_heap(ls))

    # there i use my own method to build a heap
    def test_build_heap(self):
        nb_tests = 100
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), nb_tests)
            hp.build_heap(ls)
            self.assertTrue(hp.check_heap(ls))

    def test_heap_sort(self):
        nb_tests = 100
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

    def test_heap_extract_max(self):
        nb_tests = 100
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), nb_tests)
            hp.build_heap(ls)
            mx = hp.heap_extract_max(ls)

            self.assertTrue(mx > max(ls))
            self.assertTrue(hp.check_heap(ls))

    def test_heap_insert(self):
        nb_tests = 100
        hp = HeapSort()

        for _ in range(nb_tests):
            ls = sample(range(nb_tests), nb_tests)
            hp.build_heap(ls)
            value = randint(int(nb_tests/2), nb_tests)
            hp.heap_insert(ls, value)
            self.assertTrue(ls)