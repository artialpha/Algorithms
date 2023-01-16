def find_lowest_linear(ls):
    nb = ls[0]
    i = 0

    for index, n in enumerate(ls[1:], 1):
        if n < nb:
            nb = n
            i = index
    return i, nb
