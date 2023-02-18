from unittest import TestCase
from random import randint, sample, random
from string import ascii_letters
from math import sqrt
from HashTable import HashTableModulo, HashTableMultiplication


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

            key = randint(0, 1000)
            value = ''.join(sample(ascii_letters, k=10))

            ht_modulo[key] = value
            self.assertEqual(value, ht_modulo[key])

            ht_multiplication[key] = value
            self.assertEqual(value, ht_multiplication[key])


