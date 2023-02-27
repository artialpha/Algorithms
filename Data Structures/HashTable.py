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

    def __setitem__(self, key, value):
        index_in_table = self.hash_index(key)
        index_first_element_in_series = index_in_table
        index_in_series = 1
        cont = True

        while cont:
            pair = self.table[index_in_table]

            if not pair or pair[0] == key:
                self.table[index_in_table] = (key, value)
                cont = False
            else:
                index_in_table = self.calculate_next_index(index_first_element_in_series, index_in_series) % self.size
                index_in_series += 1

                if index_in_series > self.size:
                    raise IndexError("there is no free space to set another item in a table")

    def __getitem__(self, key):
        index_in_table = self.hash_index(key)
        index_first_element_in_series = index_in_table
        index_in_series = 1
        cont = True

        if not self.table[index_in_table]:
            return None

        while cont:
            if not self.table[index_in_table]:
                return None
            elif self.table[index_in_table][0] == key:
                return self.table[index_in_table][1]
            elif index_in_series > self.size:
                return None
            else:
                index_in_table = self.calculate_next_index(index_first_element_in_series, index_in_series) % self.size
                index_in_series += 1

    def __delitem__(self, key):
        index_in_table = self.hash_index(key)
        index_first_element_in_series = index_in_table
        index_in_series = 1
        cont = True

        while cont:
            if self.table[index_in_table][0] == key:
                self.table[index_in_table] = 'deleted'
                cont = False
            elif index_in_series > self.size:
                return None
            else:
                index_in_table = self.calculate_next_index(index_first_element_in_series, index_in_series) % self.size
                index_in_series += 1

    @staticmethod
    def calculate_next_index(index_in_table, index_in_series):
        pass


class HashTableLinearAddressing(HashTableOpenAddressing):

    def __init__(self, size, modulo=None):
        super().__init__(size)
        self.increment = 1

    @staticmethod
    def calculate_next_index(index_in_table, index_in_series):
        return index_in_table + index_in_series

    def hash_index(self, key):
        return key % self.size


class HashTableQuadraticAddressing(HashTableOpenAddressing):

    def __init__(self, size, modulo):
        super().__init__(size)
        self.modulo = modulo

    def hash_index(self, key):
        return key % self.modulo
