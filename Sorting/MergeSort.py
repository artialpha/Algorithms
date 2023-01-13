from Algorithm import Algorithm


class MergeSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self, ls, p, r):
        q = int((p+r)/2)
        if p < r:
            self.sort(ls, p, q)
            self.sort(ls, q+1, r)
            self.merge(ls, p, q, r)

    def merge(self, ls, p, q, r):
        temp = []
        start = p
        half = q

        while p <= half and (q+1) <= r:
            if ls[p] < ls[q+1]:
                temp.append(ls[p])
                p += 1
            else:
                temp.append(ls[q+1])
                q += 1

        if half-p > r-(q+1):
            temp.extend(ls[p:half+1])
        else:
            temp.extend(ls[q+1:r+1])

        ls[start:r+1] = temp
