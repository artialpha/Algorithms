from unittest import TestCase
from random import randint
from Math.Binary import Binary


class TestBinary(TestCase):
    def test_add_binary(self):
        number_of_tests = 100

        for _ in range(number_of_tests):
            nb1 = randint(10, 100)
            nb2 = randint(10, 100)
            res = nb1 + nb2
            res_bin = bin(res)
            print('python calculation:', res, res_bin, type(res_bin))

            binary = Binary()
            my_res = binary.add_binary(bin(nb1), bin(nb2))

            print('my calculation:', my_res, type(my_res), '\n')
            self.assertEqual(res_bin, my_res)


