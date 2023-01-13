def polynomial(pol, x):
    res = 0
    for i, n in enumerate(pol):
        res += n * x**i
    return res


def polynomial2(pol, x):
    res = pol[0]
    temp = 1

    for n in pol[1:]:
        temp *= x
        res += n * temp
    return res