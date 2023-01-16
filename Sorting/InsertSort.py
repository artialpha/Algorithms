from Algorithm import Algorithm


class InsertSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self, ls):
        for index in range(1, len(ls)):
            context = {'index': index, 'element': ls[index]}
            msg = f'I want to find a place of an element {ls[index]} at index {index} in a sorted sublist'
            step = self.Step(msg=msg, state=ls[:], context=context)
            self.steps.append(step)

            self.insert(ls, index)

            msg = 'This is the list after inserting'
            step = self.Step(msg=msg, state=ls[:], context=context)
            self.steps.append(step)

    def insert(self, ls, index):
        for i in range(index, 0, -1):
            # ls[i] is the element for which I want to find a place - it's "key"
            if ls[i] < ls[i-1]:
                context = {'key_element': ls[i], 'sorted_element': ls[i-1]}
                msg = 'I want swap two elements in a list because ' \
                      'I am looking for a place for an element to maintain order. \n' \
                      'Elements to swap:\n' \
                      f'Key element: {ls[i]}. ' \
                      f'\nElement from a sorted sublist: {ls[i-1]}'
                step = self.Step(msg=msg, state=ls[:], context=context)
                self.steps.append(step)

                ls[i], ls[i-1] = ls[i-1], ls[i]

                msg = 'This is the list after swapping elements. \n' \
                      'The elements that were swapped:\n' \
                      f'{ls[i-1]} was put before {ls[i]}'
                step = self.Step(msg=msg, state=ls[:], context=context)
                self.steps.append(step)

    def sort_recursively(self, ls, index):
        if index < len(ls):
            self.insert(ls, index)
            self.sort_recursively(ls, index+1)

    def show_steps(self):
        for index, step in enumerate(self.steps):
            print(f'Step {index+1}')
            print(f"State of a list: {step.state}")
            print(step.msg, end='\n\n')

