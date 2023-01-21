from Algorithm import Algorithm


class QuickSort(Algorithm):

    @staticmethod
    def partition(ls, p, r):
        pivot = ls[r]
        i = p
        j = r

        while i < j:
            if ls[i] > pivot:
                if ls[j] < pivot:
                    ls[i], ls[j] = ls[j], ls[i]
                else:
                    j -= 1
            else:
                i += 1
        ls[r], ls[i] = ls[r], ls[i]
        return i