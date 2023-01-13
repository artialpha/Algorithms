def bisect(ls, value, p, q):
    m = int((p+q)/2)
    if ls[m] == value:
        return m
    elif value < ls[m]:
        m = bisect(ls, value, p, m)
    else:
        m = bisect(ls, value, m+1, q)
    return m
