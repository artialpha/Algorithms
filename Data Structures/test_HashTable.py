from unittest import TestCase
from random import randint, sample
from string import ascii_letters
from math import sqrt
from HashTable import HashTableModulo, HashTableMultiplication, HashTableLinearAddressing


class TestHashTableSeparateChaining(TestCase):
    def test_hash_modulo_general(self):
        ht = HashTableModulo(15)

        ht[100] = 'kids'
        ht[115] = 'dogs'
        ht[130] = 'vampire'

        print(ht.table)
        self.assertEqual('kids', ht[100])
        self.assertEqual('dogs', ht[115])
        self.assertEqual('vampire', ht[130])

    def test_hash_multiplication_general(self):
        ht = HashTableMultiplication(15, 0.75, 120)

        ht[98129819248] = 'kids'
        ht[115] = 'dogs'

        self.assertEqual('kids', ht[98129819248])
        self.assertEqual('dogs', ht[115])

    def test_hash_modulo_replacement(self):
        ht = HashTableModulo(5)

        ht[6] = 'kids'
        ht[11] = 'monkeys'
        print(ht)
        self.assertEqual('kids', ht[6])

        ht[6] = 'dogs'
        print(ht)
        self.assertEqual('dogs', ht[6])

    def test_hash_modulo_delete(self):
        ht = HashTableModulo(5)

        ht[6] = 'sharks'
        ht[11] = 'bulls'
        self.assertEqual('sharks', ht[6])
        self.assertEqual('bulls', ht[11])

        del ht[6]
        self.assertIsNone(ht[6])
        self.assertEqual('bulls', ht[11])

        del ht[11]
        self.assertIsNone(ht[11])

    def test_hash_random_different_keys(self):
        nb_tests = 100

        for _ in range(nb_tests):
            size = randint(0, 1000)
            modulo = randint(0, size-1)
            ht_modulo = HashTableModulo(size, modulo)

            # value recommended by Cormen
            a = (sqrt(5) - 1)/2
            m = 2 ** (randint(1, 10))
            ht_multiplication = HashTableMultiplication(size, a, m)

            number_of_pairs = 200
            pairs = []
            keys = sample(range(1000), number_of_pairs)

            for key in keys:
                value = ''.join(sample(ascii_letters, k=10))
                pairs.append((key, value))

                ht_modulo[key] = value
                ht_multiplication[key] = value

            for key, value in pairs:
                self.assertEqual(value, ht_modulo[key])
                self.assertEqual(value, ht_multiplication[key])

    ####################

    def test_hash_linear_addressing_set_get_simple(self):
        ht = HashTableLinearAddressing(size=15, modulo=13)

        ht[113] = 'children'
        print(ht)
        ht[126] = 'dogs'
        ht[139] = 'monkeys'

        print(ht)
        self.assertEqual('children', ht[113])
        self.assertEqual('dogs', ht[126])
        self.assertEqual('monkeys', ht[139])

    def test_hash_linear_addressing_replace(self):
        ht = HashTableLinearAddressing(size=15, modulo=13)

        ht[113] = 'children'
        print(ht)
        self.assertEqual('children', ht[113])

        ht[113] = 'dogs'
        print(ht)
        self.assertEqual('dogs', ht[113])

    def test_hash_linear_addressing_delete(self):
        ht = HashTableLinearAddressing(size=15, modulo=13)

        ht[113] = 'children'
        ht[126] = 'dogs'
        ht[139] = 'monkeys'

        self.assertEqual('children', ht[113])
        self.assertEqual('dogs', ht[126])
        self.assertEqual('monkeys', ht[139])

        del ht[113]
        self.assertIsNone(ht[113])
        self.assertEqual('dogs', ht[126])
        self.assertEqual('monkeys', ht[139])

        del ht[139]
        self.assertEqual('dogs', ht[126])
        self.assertIsNone(ht[139])

        del ht[126]
        self.assertIsNone(ht[126])






