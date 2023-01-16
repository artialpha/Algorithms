# Cormen; page: 24; exercise: 1.1-3
def find_index(ls, value):
    for index, v in enumerate(ls):
        if v == value:
            return index
