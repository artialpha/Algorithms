from os import listdir
from random import sample
from Sorting.InsertSort import InsertSort

print("Hello, this script allows to pick one of the algorithms and check how "
      "they work on a list that either you provide or is random")

work = True
sorting = listdir(r'Sorting')
print(sorting)
sorting = [name.rstrip('.py') for name in sorting if name[:4] != 'test']
sorting = [f'{name[:-4]} {name[-4:]}'.lower() for name in sorting]

# get rid of __pycache__
sorting.pop()

while work:
    print("Commands:")
    print("1. Sorting\n"
          "2. Exit")
    answer = input()

    if answer == '1':
        print(f'available algorithms: {sorting}')
        print("Which do you want to see?")
        for i, alg in enumerate(sorting, 1):
            print(f'{i}: {alg}')
        answer = input()

        if answer == '2':
            print("We will use a random list")
            ls = sample(range(20), 10)
            ins = InsertSort()
            ins.sort(ls)
            ins.show_steps()
            answer = None

    if answer == '2':
        print("So I exit!")
        work = False
