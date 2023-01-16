from Algorithm import Algorithm


class MergeSort(Algorithm):

    def __init__(self):
        super().__init__()

    def sort(self, ls, p, r):
        q = int((p+r)/2)
        if p < r:
            msg = f"I divide the list: \n{ls[p:r+1]}\ninto two sub-lists:\n" \
                  f"Left sublist: {ls[p:q+1]}\n" \
                  f"Right sublist: {ls[q+1:r+1]}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

            self.sort(ls, p, q)
            self.sort(ls, q+1, r)

            msg = f"Now I want to merge two sub-lists:\n" \
                  f"Left sublist: {ls[p:q+1]}\n" \
                  f"Right sublist: {ls[q+1:r+1]}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)
            self.merge(ls, p, q, r)

    def merge(self, ls, p, q, r):
        temp = []
        start = p
        half = q

        msg = f"I am merging two sub-lists:\n" \
              f"Left: {ls[p:q+1]}. Index at start: {p}\n" \
              f"Right: {ls[q+1:r+1]}. Index at start: {q+1}\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        while p <= half and (q+1) <= r:
            if ls[p] < ls[q+1]:
                temp.append(ls[p])
                p += 1

                msg = f"Value in the left sub-list is smaller, I add it to a temporary list\n" \
                      f"{ls[p-1]} < {ls[q+1]}\n" \
                      f"{ls[p-1]} has been added to a temp list: {temp}\n" \
                      f"I have increase index in the left sub-list from {p-1} to {p}\n"
                step = self.Step(msg=msg, state=ls[:], context={})
                self.steps.append(step)
            else:
                temp.append(ls[q+1])
                q += 1

                msg = f"Value in the right sub-list is smaller, I add it to a temporary list\n" \
                      f"{ls[q]} < {ls[p]}\n" \
                      f"{ls[q]} has been added to a temp list: {temp}\n" \
                      f"I have increase index in the left sub-list from {q-1} to {q}\n"
                step = self.Step(msg=msg, state=ls[:], context={})
                self.steps.append(step)

        if half-p > r-(q+1):
            temp.extend(ls[p:half+1])

            msg = f"I have added the rest of the elements from the left sub-list to a temporary list:\n" \
                  f"{ls[p:half+1]} to temp {temp}"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)
        else:
            temp.extend(ls[q+1:r+1])

            msg = f"I have added the rest of the elements from the right sub-list to a temporary list:\n" \
                  f"{ls[q+1:r+1]} to temp {temp}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)
        ls[start:r+1] = temp

    def show_steps(self):
        print(f'ls at the start: {self.steps[0].state}')
        for index, step in enumerate(self.steps):
            print(step.msg)




