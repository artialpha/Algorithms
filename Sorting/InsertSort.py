from Algorithm import Algorithm


class InsertSort(Algorithm):

    def __init__(self):
        super().__init__()

    @classmethod
    def sort(cls, ls):
        for index in range(1, len(ls)):
            cls.insert(ls, index)

    @staticmethod
    def insert(ls, index):
        for i in range(index, 0, -1):
            if ls[i] < ls[i-1]:
                ls[i], ls[i-1] = ls[i-1], ls[i]
