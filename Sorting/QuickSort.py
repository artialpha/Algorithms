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
        ls[r], ls[i] = ls[i], ls[r]
        return i

    @classmethod
    def quick_sort(cls, ls, p, r):
        if p < r:
            q = cls.partition(ls, p, r)
            # print(f'p: {p}, q: {q}, r:{r}')
            cls.quick_sort(ls, p, q-1)
            cls.quick_sort(ls, q+1, r)
