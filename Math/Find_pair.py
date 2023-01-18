from FindInList.Bisect import bisect_value_index


# Cormen; page: 34; exercise: 1.3-7
def find_pair(ls, s):
    for a_index, a in enumerate(ls):
        b = s - a
        if b_index := bisect_value_index(ls, b, 0, len(ls)-1):
            return a_index, b_index
