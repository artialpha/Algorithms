from Algorithm import Algorithm


class InsertSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self, ls):
        for index in range(1, len(ls)):
            msg = f'This is the list before inserting: {ls}\nI am at index = {index} and I want to insert: {ls[index]}'
            self.steps.append(msg)
            self.insert(ls, index)
            msg = f'This is the list after inserting: {ls}\n'
            self.steps.append(msg)

    def insert(self, ls, index):
        for i in range(index, 0, -1):
            if ls[i] < ls[i-1]:
                msg = f'I swap: {ls[i]} and {ls[i-1]}'
                self.steps.append(msg)
                ls[i], ls[i-1] = ls[i-1], ls[i]
