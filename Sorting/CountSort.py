from Algorithm import Algorithm


class CountSort(Algorithm):

    @staticmethod
    def sort(ls, rng):
        temp = [0] * rng
        ls_ret = [0] * len(ls)

        for nb in ls:
            temp[nb] += 1

        for i in range(1, rng):
            temp[i] = temp[i] + temp[i-1]

        for nb in ls:
            ls_ret[temp[nb]-1] = nb
            temp[nb] -= 1

        return ls_ret

    @staticmethod
    def find_digit(number, n):
        return (number // 10**(n-1)) % 10

    @classmethod
    def counting_sort_by_digit(cls, ls, rng, digit=1):
        temp = [0] * rng
        ls_ret = [0] * len(ls)

        for nb in ls:
            d = cls.find_digit(nb, digit)
            temp[d] += 1

        for i in range(1, rng):
            temp[i] = temp[i] + temp[i-1]

        for nb in ls[::-1]:
            d = cls.find_digit(nb, digit)
            ls_ret[temp[d]-1] = nb
            temp[d] -= 1

        return ls_ret
