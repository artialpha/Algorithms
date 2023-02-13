from Algorithm import Algorithm
from CountSort import CountSort


class RadixSort(Algorithm):

    @staticmethod
    def sort(ls, digits):
        for d in range(digits):
            ls = CountSort.counting_sort_by_digit(ls, 10, d+1)
        return ls
