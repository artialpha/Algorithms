from unittest import TestCase
from random import sample, randint, shuffle
from Math.Find_pair import find_pair


class Test(TestCase):

    def test_find_pair(self):
        def generate_list_with_sums(s, range_list, size_list):
            half = s/2

            # random distances from a half of the sum
            ls = sorted(sample(range(range_list), size_list))

            ls_pairs = []
            for index, nb in enumerate(ls):
                if index % 2 == 0:
                    res = round(half + nb)
                else:
                    res = round(half - nb)
                ls_pairs.append(res)

            nb = ls[0]
            while nb in ls:
                nb = randint(0, range_list) if s % 2 == 0 else randint(0, range_list) + 0.5
            pair = [int(half-nb), int(half+nb)]
            print(f'this is pair: {pair}')
            ls_pairs.extend(pair)
            shuffle(ls_pairs)
            ls_pairs.sort()

            return ls_pairs

        nb_tests = 100
        for _ in range(nb_tests):
            s = randint(100, 1000)
            ls = generate_list_with_sums(s=s, range_list=int(s/3), size_list=int(s/4))
            print(ls)
            a_index, b_index = find_pair(ls, s)
            print(ls[a_index], ls[b_index], f'sum: {ls[a_index] + ls[b_index]}')
            self.assertEqual(s, ls[a_index] + ls[b_index])
