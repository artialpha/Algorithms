from unittest import TestCase
from random import randint, sample
from string import ascii_letters
from math import sqrt
from HashTable import HashTableModulo, HashTableMultiplication, HashTableLinearAddressing


class TestHashTable(TestCase):
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

            ht_linear_addressing = HashTableLinearAddressing(size, modulo)

            number_of_pairs = 200
            pairs = []
            keys = sample(range(1000), number_of_pairs)

            # test __setitem__ - set a value for a given key

            for key in keys:
                value = ''.join(sample(ascii_letters, k=10))
                pairs.append((key, value))

                ht_modulo[key] = value
                ht_multiplication[key] = value

            # test __getitem__ - get a value for a certain key - check if it gives a correct value!

            for key, value in pairs:
                self.assertEqual(value, ht_modulo[key])
                self.assertEqual(value, ht_multiplication[key])

            # test __setitem__ - replace an old value with a new one

            new_pairs_to_replace = sample(pairs, int(number_of_pairs/4))
            pairs.clear()
            for key, _ in new_pairs_to_replace:
                new_value = ''.join(sample(ascii_letters, k=7))
                pairs.append((key, new_value))

                ht_modulo[key] = new_value
                ht_multiplication[key] = new_value

            for key, value in pairs:
                self.assertEqual(value, ht_modulo[key])
                self.assertEqual(value, ht_multiplication[key])

            # test __delitem__ - a key that has been deleted should return None

            pairs_to_delete = sample(pairs, int(number_of_pairs/4))
            for key, _ in pairs_to_delete:
                del ht_multiplication[key]
                del ht_modulo[key]

            for key, _ in pairs_to_delete:
                self.assertIsNone(ht_modulo[key])
                self.assertIsNone(ht_multiplication[key])

    ################################################################################

    @staticmethod
    def linear_addressing_different_indices():
        ht = HashTableLinearAddressing(size=6)

        ht[12] = 'child'
        ht[37] = 'monkey'
        ht[62] = 'dog'
        ht[123] = 'cat'
        ht[28] = 'rat'
        ht[71] = 'mouse'

        predicted_table = [(12, 'child'), (37, 'monkey'), (62, 'dog'), (123, 'cat'), (28, 'rat'), (71, 'mouse')]

        return ht, predicted_table

    @staticmethod
    def linear_addressing_one_index():
        ht = HashTableLinearAddressing(size=6)

        # 45 mod 6 = 3
        ht[45] = 'child'
        ht[57] = 'monkey'
        ht[9] = 'dog'
        ht[75] = 'cat'
        ht[123] = 'rat'
        ht[39] = 'mouse'

        predicted_table = [(75, 'cat'), (123, 'rat'), (39, 'mouse'), (45, 'child'), (57, 'monkey'), (9, 'dog')]

        return ht, predicted_table

    @staticmethod
    def linear_addressing_indices_both_cases():
        ht = HashTableLinearAddressing(size=6)

        # 45 mod 6 = 3
        ht[14] = 'child'
        ht[12] = 'monkey'
        ht[61] = 'dog'
        ht[45] = 'cat'
        ht[123] = 'rat'
        ht[57] = 'mouse'

        predicted_table = [(12, 'monkey'), (61, 'dog'), (14, 'child'), (45, 'cat'), (123, 'rat'), (57, 'mouse')]

        return ht, predicted_table

    def test_hash_linear_addressing_set_different_indices(self):
        ht, predicted_table = TestHashTable.linear_addressing_different_indices()

        self.assertEqual(12, ht.table[0][0])
        self.assertEqual(37, ht.table[1][0])
        self.assertEqual(62, ht.table[2][0])
        self.assertEqual(123, ht.table[3][0])
        self.assertEqual(28, ht.table[4][0])
        self.assertEqual(71, ht.table[5][0])

        self.assertEqual('child', ht.table[0][1])
        self.assertEqual('monkey', ht.table[1][1])
        self.assertEqual('dog', ht.table[2][1])
        self.assertEqual('cat', ht.table[3][1])
        self.assertEqual('rat', ht.table[4][1])
        self.assertEqual('mouse', ht.table[5][1])

        self.assertEqual(ht.table, predicted_table)

    def test_hash_linear_addressing_set_one_index(self):
        ht, predicted_table = TestHashTable.linear_addressing_one_index()

        self.assertEqual(45, ht.table[3][0])
        self.assertEqual(57, ht.table[4][0])
        self.assertEqual(9, ht.table[5][0])
        self.assertEqual(75, ht.table[0][0])
        self.assertEqual(123, ht.table[1][0])
        self.assertEqual(39, ht.table[2][0])

        self.assertEqual('child', ht.table[3][1])
        self.assertEqual('monkey', ht.table[4][1])
        self.assertEqual('dog', ht.table[5][1])
        self.assertEqual('cat', ht.table[0][1])
        self.assertEqual('rat', ht.table[1][1])
        self.assertEqual('mouse', ht.table[2][1])

        self.assertEqual(ht.table, predicted_table)

    def test_hash_linear_addressing_set_mix(self):
        ht, predicted_table = TestHashTable.linear_addressing_indices_both_cases()

        self.assertEqual(12, ht.table[0][0])
        self.assertEqual(61, ht.table[1][0])
        self.assertEqual(14, ht.table[2][0])
        self.assertEqual(45, ht.table[3][0])
        self.assertEqual(123, ht.table[4][0])
        self.assertEqual(57, ht.table[5][0])

        self.assertEqual('monkey', ht.table[0][1])
        self.assertEqual('dog', ht.table[1][1])
        self.assertEqual('child', ht.table[2][1])
        self.assertEqual('cat', ht.table[3][1])
        self.assertEqual('rat', ht.table[4][1])
        self.assertEqual('mouse', ht.table[5][1])

        self.assertEqual(ht.table, predicted_table)

    def test_hash_linear_addressing_get_different_indices(self):
        ht, predicted_table = TestHashTable.linear_addressing_different_indices()

        self.assertEqual('child', ht[12])
        self.assertEqual('monkey', ht[37])
        self.assertEqual('dog', ht[62])
        self.assertEqual('cat', ht[123])
        self.assertEqual('rat', ht[28])
        self.assertEqual('mouse', ht[71])

    def test_hash_linear_addressing_get_one_index(self):
        ht, predicted_table = TestHashTable.linear_addressing_one_index()

        self.assertEqual('child', ht[45])
        self.assertEqual('monkey', ht[57])
        self.assertEqual('dog', ht[9])
        self.assertEqual('cat', ht[75])
        self.assertEqual('rat', ht[123])
        self.assertEqual('mouse', ht[39])

    def test_hash_linear_addressing_get_mix(self):
        ht, predicted_table = TestHashTable.linear_addressing_indices_both_cases()

        self.assertEqual('child', ht[14])
        self.assertEqual('monkey', ht[12])
        self.assertEqual('dog', ht[61])
        self.assertEqual('cat', ht[45])
        self.assertEqual('rat', ht[123])
        self.assertEqual('mouse', ht[57])

    def test_hash_linear_addressing_del_different_indices(self):
        ht, predicted_table = TestHashTable.linear_addressing_different_indices()

        del ht[12]
        self.assertIsNone(ht[12])
        self.assertEqual('monkey', ht[37])
        self.assertEqual('dog', ht[62])
        self.assertEqual('cat', ht[123])
        self.assertEqual('rat', ht[28])
        self.assertEqual('mouse', ht[71])

        del ht[71]
        self.assertIsNone(ht[12])
        self.assertEqual('monkey', ht[37])
        self.assertEqual('dog', ht[62])
        self.assertEqual('cat', ht[123])
        self.assertEqual('rat', ht[28])
        self.assertIsNone(ht[71])

        del ht[123]
        self.assertIsNone(ht[12])
        self.assertEqual('monkey', ht[37])
        self.assertEqual('dog', ht[62])
        self.assertIsNone(ht[123])
        self.assertEqual('rat', ht[28])
        self.assertIsNone(ht[71])

        del ht[62]
        self.assertIsNone(ht[12])
        self.assertEqual('monkey', ht[37])
        self.assertIsNone(ht[62])
        self.assertIsNone(ht[123])
        self.assertEqual('rat', ht[28])
        self.assertIsNone(ht[71])

        del ht[37]
        self.assertIsNone(ht[12])
        self.assertIsNone(ht[37])
        self.assertIsNone(ht[62])
        self.assertIsNone(ht[123])
        self.assertEqual('rat', ht[28])
        self.assertIsNone(ht[71])

        del ht[28]
        self.assertIsNone(ht[12])
        self.assertIsNone(ht[37])
        self.assertIsNone(ht[62])
        self.assertIsNone(ht[123])
        self.assertIsNone(ht[28])
        self.assertIsNone(ht[71])

        self.assertEqual(ht.table, ['deleted', 'deleted', 'deleted', 'deleted', 'deleted', 'deleted'])

    def test_hash_linear_addressing_del_one_index(self):
        ht, predicted_table = TestHashTable.linear_addressing_one_index()

        del ht[45]
        self.assertIsNone(ht[45])
        self.assertEqual('monkey', ht[57])
        self.assertEqual('dog', ht[9])
        self.assertEqual('cat', ht[75])
        self.assertEqual('rat', ht[123])
        self.assertEqual('mouse', ht[39])

        del ht[39]
        self.assertIsNone(ht[45])
        self.assertEqual('monkey', ht[57])
        self.assertEqual('dog', ht[9])
        self.assertEqual('cat', ht[75])
        self.assertEqual('rat', ht[123])
        self.assertIsNone(ht[39])

        del ht[9]
        self.assertIsNone(ht[45])
        self.assertEqual('monkey', ht[57])
        self.assertIsNone(ht[9])
        self.assertEqual('cat', ht[75])
        self.assertEqual('rat', ht[123])
        self.assertIsNone(ht[39])

        del ht[75]
        self.assertIsNone(ht[75])
        del ht[123]
        del ht[57]

        self.assertEqual(ht.table, ['deleted', 'deleted', 'deleted', 'deleted', 'deleted', 'deleted'])

    def test_hash_linear_addressing_del_mix(self):
        ht, predicted_table = TestHashTable.linear_addressing_indices_both_cases()

        del ht[12]
        self.assertEqual('child', ht[14])
        self.assertIsNone(ht[12])
        self.assertEqual('dog', ht[61])
        self.assertEqual('cat', ht[45])
        self.assertEqual('rat', ht[123])
        self.assertEqual('mouse', ht[57])

        del ht[57]
        self.assertEqual('child', ht[14])
        self.assertIsNone(ht[12])
        self.assertEqual('dog', ht[61])
        self.assertEqual('cat', ht[45])
        self.assertEqual('rat', ht[123])
        self.assertIsNone(ht[57])

        del ht[45]
        del ht[123]
        self.assertEqual('child', ht[14])
        self.assertIsNone(ht[12])
        self.assertEqual('dog', ht[61])
        self.assertIsNone(ht[45])
        self.assertIsNone(ht[123])
        self.assertIsNone(ht[57])

        del ht[14]
        del ht[61]
        self.assertEqual(ht.table, ['deleted', 'deleted', 'deleted', 'deleted', 'deleted', 'deleted'])

    def test_hash_linear_addressing_replace_different_indices(self):
        ht, predicted_table = TestHashTable.linear_addressing_different_indices()

        ht[12] = 'different child'
        ht[71] = 'not mouse'
        ht[62] = 'cerberus'

        self.assertEqual('different child', ht[12])
        self.assertEqual('not mouse', ht[71])
        self.assertEqual('cerberus', ht[62])

    def test_hash_linear_addressing_replace_one_index(self):
        ht, predicted_table = TestHashTable.linear_addressing_one_index()

        ht[45] = 'different child'
        ht[39] = 'not mouse'
        ht[9] = 'cerberus'

        self.assertEqual('different child', ht[45])
        self.assertEqual('not mouse', ht[39])
        self.assertEqual('cerberus', ht[9])

    def test_hash_linear_addressing_replace_mix(self):
        ht, predicted_table = TestHashTable.linear_addressing_indices_both_cases()

        ht[12] = 'different monkey'
        ht[57] = 'not mouse'
        ht[45] = 'jerry'

        self.assertEqual('different monkey', ht[12])
        self.assertEqual('not mouse', ht[57])
        self.assertEqual('jerry', ht[45])

    def test_hash_linear_addressing_set_full_table(self):
        ht_different, rest = TestHashTable.linear_addressing_different_indices()
        ht_one, rest = TestHashTable.linear_addressing_one_index()

        with self.assertRaises(IndexError):
            ht_different[20] = 'demon'

        # a key giving an index that is already taken
        with self.assertRaises(IndexError):
            ht_one[21] = 'demon'

        # a key giving a free index
        with self.assertRaises(IndexError):
            ht_one[22] = 'demon'

    def test_hash_linear_addressing_get_full_table(self):
        ht_different, rest = TestHashTable.linear_addressing_different_indices()
        ht_one, rest = TestHashTable.linear_addressing_one_index()

        # there is no key 20 in a ht_different
        self.assertIsNone(ht_different[20])

        # key 21 gives index 3 that is taken
        self.assertIsNone(ht_one[21])

        # key 22 given index 4 that is free but the whole table is taken
        self.assertIsNone(ht_one[22])

    def test_hash_linear_addressing_del_full_table(self):
        ht_different, rest = TestHashTable.linear_addressing_different_indices()
        ht_one, rest = TestHashTable.linear_addressing_one_index()

        del ht_different[20]
        self.assertIsNone(ht_different[20])

        del ht_one[21]
        del ht_one[22]
        self.assertIsNone(ht_one[21])
        self.assertIsNone(ht_one[22])








