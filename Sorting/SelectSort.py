# Cormen page 29: exercise: 1.2-1 add two binary numbers
class SelectSort:
    @staticmethod
    def find_lowest(ls):
        nb = ls[0]
        i = 0   
        index = 0
        for index, n in enumerate(ls[1:], 1):
            if n < nb:
                nb = n
                i = index
        return i, nb

    @classmethod
    def sort(cls, ls):
        temp = []
        while ls:
            index, nb = cls.find_lowest(ls)
            ls.pop(index)
            temp.append(nb)
        return temp
