from itertools import zip_longest


class Binary:

    @staticmethod
    def add_binary(nb1, nb2):
        nb1 = list(nb1)[2:]
        nb1 = nb1[::-1]

        nb2 = list(nb2)[2:]
        nb2 = nb2[::-1]

        temp = 0
        res = []
        for n1, n2 in zip_longest(nb1, nb2):
            n1 = int(n1) if n1 else 0
            n2 = int(n2) if n2 else 0
            sum = n1 + n2 + temp
            if sum >= 2:
                sum -= 2
                temp = 1
            else:
                temp = 0
            res.append(sum)
        if temp:
            res.append(1)
        res = [str(n) for n in res]
        res = f"0b{''.join(res[::-1])}"
        return res
