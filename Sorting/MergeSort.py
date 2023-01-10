from Algorithm import Algorithm


class MergeSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self, ls, p, r):
        q = int((p+r)/2)
        #print(f'before if')
        print(f'p: {p}, q: {q}, r {r}')
        if p < r:
            #print(f'before dividing')
            #print(f'p: {p}, q: {q}, r {r}')
            self.sort(ls, p, q)
            self.sort(ls, q+1, r)
            #print(f'the whole list: {ls}')
            #print(f'p: {p}, q: {q}, r {r}')
            #print(f'before merge: ls1: {ls[p:q]}; ls2: {ls[q:r]}')
            self.merge(ls, p, q, r)
            #print(f'after merge:')
            #print(f'ls {ls[p:r]}\n')

    def merge(self, ls, p, q, r):
        temp = []
        start = p
        half = q

        #print(f'whole list: {ls[p:r+1]}')

        while p <= half and (q+1) <= r:
            #print(f'p: {p}, half: {half}, q+1: {q+1} , r {r}. TEMP: {temp}')
            if ls[p] < ls[q+1]:
                #print(f'element to add: {ls[p]}')
                temp.append(ls[p])
                p += 1
            else:
                #print(f'element to add: {ls[q]}')
                temp.append(ls[q+1])
                q += 1
            #print(f'p: {p}, half: {half}, q+1: {q+1} , r {r}. TEMP: {temp}\n')
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

        #print(f'temp before last merge: {temp}')
        if half-p > r-(q+1):
            #print(f'i add left: {ls[p:half+1]}')
            temp.extend(ls[p:half+1])
        else:
            #print(f'i add right: {ls[q+1:r+1]}')
            temp.extend(ls[q+1:r+1])

        ls[start:r+1] = temp

