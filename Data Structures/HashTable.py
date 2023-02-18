from math import floor


class HashTable:

    def __init__(self, size):
        self.size = size


class HashTableSeparateChaining(HashTable):

    def __init__(self, size):
        super().__init__(size)
        self.table = [list() for _ in range(size)]

    def hash_index(self, key):
        pass

    def __getitem__(self, key):
        for k, value in self.table[self.hash_index(key)]:
            if k == key:
                return value

    def __setitem__(self, key, value):
        pair = (key, value)
        if self[key]:
            to_remove = None
            for i, (k, _) in enumerate(self.table[self.hash_index(key)]):
                if k == key:
                    to_remove = i
            del self.table[self.hash_index(key)][to_remove]
        self.table[self.hash_index(key)].append(pair)

    def __delitem__(self, key):
        to_remove = None
        for i, (k, _) in enumerate(self.table[self.hash_index(key)]):
            if k == key:
                to_remove = i
        del self.table[self.hash_index(key)][to_remove]

    def __str__(self):
        return str(self.table)


class HashTableModulo(HashTableSeparateChaining):

    def __init__(self, size, modulo=None):
        super().__init__(size)
        self.modulo = modulo if modulo else size

    def hash_index(self, key):
        return key % self.modulo


class HashTableMultiplication(HashTableSeparateChaining):

    def __init__(self, size, a, m):
        super().__init__(size)
        self.a = a
        self.m = m

    def hash_index(self, key):
        return floor(self.m * ((key * self.a) % 1)) % self.size
