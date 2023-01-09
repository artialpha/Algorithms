from Algorithm import Algorithm


class MergeSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self):
        pass

    def merge(self, ls1, ls2):
        temp = []
        i = 0
        j = 0

        while i < len(ls1) and j < len(ls2):
            if ls1[i] < ls2[j]:
                temp.append(ls1[i])
                i += 1
            else:
                temp.append(ls2[j])
                j += 1
        '''
        Here I had i > j
        But there could be a situation when i and j were equal
        and there was still on element in ls2 (because the second list had one more element)
        and then this element was not added to temp list
        eg:
        ls1: [0, 1, 6, 7, 9]
        ls2: [2, 3, 4, 5, 8, 10]
        ls merged: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        when the condition in while is not fulfilled then i and j are both equal to 5
        but there is still one element in ls2
        if the condition below is 'i>j' then this element would not be added
        that's why I have i >= j 
        '''

        if i >= j:
            temp.extend(ls2[j:])
        else:
            temp.extend(ls1[i:])

        return temp
