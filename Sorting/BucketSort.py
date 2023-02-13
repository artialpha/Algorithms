from Algorithm import Algorithm
from CountSort import CountSort


class BucketSort(Algorithm):

    @staticmethod
    def sort(ls):
        length = len(ls)
        temp = [[] for i in range(length)]
        ret_ls = []

        for v in ls:
            temp[int(v*length)].append(v)

        for l in temp:
            ret_ls.extend(sorted(l))

        return ret_ls
