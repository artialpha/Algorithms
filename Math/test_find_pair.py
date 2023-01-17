from unittest import TestCase
from random import sample, randint, shuffle
from Math.find_pair import find_pair


class Test(TestCase):

    def test_find_pair(self):
        nb_tests = 100

        def generate_pairs_even(s):
            """
            I want to generate a list of numbers which have only one pair of numbers that add up to a given sum

            :param s:
            sum which is supposed to be obtained by adding two numbers that can be found in a list
            :return:
            list of numbers which contains one pair that can be added to get a desired sum
            """
            half = s/2

            ls = sorted(sample(range(3*nb_tests), nb_tests))

            ls_pairs = []
            for index, nb in enumerate(ls):
                if index % 2 == 0:
                    res = half + nb
                else:
                    res = half - nb
                ls_pairs.append(res)

            nb = ls[0]
            while nb in ls:
                nb = randint(0, 3*nb_tests)
            pair = [half-nb, half+nb]

            ls_pairs.extend(pair)
            shuffle(ls_pairs)
            ls_pairs.sort()

            return ls_pairs

        s = 1000
        for _ in range(nb_tests):
            ls = generate_pairs_even(s)
            a_index, b_index = find_pair(ls, s)
            self.assertEqual(s, ls[a_index] + ls[b_index])
