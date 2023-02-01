from unittest import TestCase
from Sorting.SelectSort import SelectSort
from random import sample, choices


class TestSelectSort(TestCase):
    def test_find_lowest(self):
        number_of_tests = 100
        size_list = 11
        range_list = 100

        for _ in range(number_of_tests):
            ls = sample(range(range_list), size_list)
            select = SelectSort()
            self.assertEqual(min(ls), select.find_lowest(ls)[1])

    def test_sort(self):
        number_of_tests = 100
        size_list = sample(range(number_of_tests), number_of_tests)

        for size in size_list:
            ls = sample(range(size), size)
            select = SelectSort()
            print(size)
            #print(f'sorted list: {sorted(ls)} but ls is not changed: {ls}')
            self.assertEqual(sorted(ls), select.sort(ls[:]))

    def test_sort_with_repetition(self):
        number_of_tests = 100
        size = 30

        for _ in range(number_of_tests):
            ls = choices(range(number_of_tests), k=size)
            select = SelectSort()

            python_result = sorted(ls)
            my_result = select.sort(ls)

            self.assertEqual(python_result, my_result)
