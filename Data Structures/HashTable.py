from math import floor


class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = None

    def __str__(self):
        return str(self.table)

    def hash_index(self, key):
        pass


class HashTableSeparateChaining(HashTable):

    def __init__(self, size):
        super().__init__(size)
        self.table = [list() for _ in range(size)]

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


class HashTableOpenAddressing(HashTable):

    def __init__(self, size):
        super().__init__(size)
        self.table = [None for _ in range(size)]
        self.increment = None

    def __setitem__(self, key, value):
        index = self.hash_index(key)
        cont = True

        while cont:
            pair = self.table[index]

            if not pair or pair[0] == key:
                self.table[index] = (key, value)
                cont = False
            else:
                index += self.increment

    def __getitem__(self, key):
        index = self.hash_index(key)
        cont = True

        if not self.table[index]:
            return None

        while cont:
            if not self.table[index]:
                return None
            elif self.table[index][0] == key:
                return self.table[index][1]
            else:
                index += self.increment

    def __delitem__(self, key):
        index = self.hash_index(key)
        cont = True

        while cont:
            if self.table[index][0] == key:
                del self.table[index]
                cont = False
            else:
                index += self.increment


class HashTableLinearAddressing(HashTableOpenAddressing):

    def __init__(self, size, modulo):
        super().__init__(size)
        self.modulo = modulo
        self.increment = 1

    def hash_index(self, key):
        return key % self.modulo
