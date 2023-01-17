# Cormen; page: 34; exercise: 1.3-5
# returns an index of a value in a list
# return false when there is not such value
def bisect_value_index(ls, value, p, q):
    m = int((p+q)/2)
    if ls[m] == value:
        return m
    if p == q:
        return False
    elif value < ls[m]:
        m = bisect_value_index(ls, value, p, m)
    else:
        m = bisect_value_index(ls, value, m + 1, q)
    return m


# a list has to be sorted
# return an index where a value should be inserted so that a list is still sorted
def bisect_index_insert(ls, value, p, q):
    m = int((p+q)/2)
    if ls[m] == value or ls[m-1] < value < ls[m] or (value < ls[m] and m == 0):
        return m
    elif ls[m-1] < value and p == len(ls)-1:
        return m + 1
    elif value < ls[m]:
        m = bisect_index_insert(ls, value, p, m)
    else:
        m = bisect_index_insert(ls, value, m+1, q)
    return m
