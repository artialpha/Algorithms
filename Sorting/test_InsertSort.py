import random
from unittest import TestCase
from Sorting.InsertSort import InsertSort


class TestInsertSort(TestCase):
    def test_insert(self):
        tests = [
            {
                'in': ([2, 6, 7, 3, 1, 4, 5], 3),
                'out': [2, 3, 6, 7, 1, 4, 5]
            },
            {
                'in': ([2, 3, 6, 7, 1, 4, 5], 4),
                'out': [1, 2, 3, 6, 7, 4, 5]
            },
            {
                'in': ([1, 2, 3, 6, 7, 4, 5], 5),
                'out': [1, 2, 3, 4, 6, 7, 5]
            },
            {
                'in': ([1, 2, 3, 4, 6, 7, 5], 6),
                'out': [1, 2, 3, 4, 5, 6, 7]
            }
        ]

        for test in tests:
            insert_sort = InsertSort()
            insert_sort.insert(test['in'][0], test['in'][1])
            self.assertEqual(test['out'], test['in'][0])
            print(test['in'][0])

    def test_sort(self):
        number_of_tests = 100
        size_of_list = 10
        insert_sort = InsertSort()

        for _ in range(number_of_tests):
            ls = list(range(size_of_list))
            result = sorted(ls[:])
            random.shuffle(ls)

            print(f'ls before: {ls}')
            insert_sort.sort(ls)
            self.assertEqual(result, ls)
            print(f'ls after: {ls}\n')

    def test_steps(self):
        insert_sort = InsertSort()
        ls = list(range(10))
        random.shuffle(ls)
        insert_sort.sort(ls)
        for step in insert_sort.steps:
            print(step)