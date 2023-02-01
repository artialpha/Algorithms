from Algorithm import Algorithm


class QuickSort(Algorithm):

    def partition(self, ls, p, r):
        pivot = ls[r]
        i = p
        j = r

        msg = f"I am performing partitioning\n" \
              f"pivot taken from the right: {pivot}\n" \
              f"i: {i}; j: {j}\n" \
              f"List state: {ls}\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        while i < j:
            if ls[i] > pivot:
                msg = f"'i' met an element that is bigger than a pivot\n" \
                      f"pivot: {pivot}\n" \
                      f"element index: {i}; element value: {ls[i]}\n"
                step = self.Step(msg=msg, state=ls[:], context={})
                self.steps.append(step)

                if ls[j] < pivot:
                    msg = f"'j' met an element that is smaller than a pivot\n" \
                          f"pivot: {pivot}\n" \
                          f"element index: {j}; element value: {ls[j]}\n"
                    step = self.Step(msg=msg, state=ls[:], context={})
                    self.steps.append(step)

                    msg = f"List before swap: \n{ls}\n" \
                          f"Element on the left to swap (bigger than pivot). Index: {i}, value: {ls[i]}\n" \
                          f"Element on the right to swap (smaller than pivot). Index: {j}, value: {ls[j]}\n"
                    step = self.Step(msg=msg, state=ls[:], context={})
                    self.steps.append(step)

                    ls[i], ls[j] = ls[j], ls[i]

                    msg = f"List after swap: \n{ls}\n"
                    step = self.Step(msg=msg, state=ls[:], context={})
                    self.steps.append(step)
                else:
                    msg = f"Index j: {j}; element: {ls[j]}\n" \
                          f"This is not smaller than pivot: {pivot}\n" \
                          f"So I decrease index from {j} to {j-1}\n"
                    step = self.Step(msg=msg, state=ls[:], context={})
                    self.steps.append(step)
                    j -= 1
            else:
                msg = f"Index i: {i}; element: {ls[i]}\n" \
                      f"This is not bigger than pivot: {pivot}\n" \
                      f"So I increase index from {i} to {i+1}\n"
                step = self.Step(msg=msg, state=ls[:], context={})
                self.steps.append(step)
                i += 1

        msg = f"List before final swap: {ls}" \
              f"Indices meet at the same position: {i}\n" \
              f"Now I swap the element at this place with a pivot\n" \
              f"Index: {i}; Element: {ls[i]}\n" \
              f"Pivot index: {r}; pivot value: {ls[r]}\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        ls[r], ls[i] = ls[i], ls[r]

        msg = f"List after final swap: {ls}\n" \
              f"I return pivot index: {i}\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        return i

    def quick_sort(self, ls, p, r):
        if p < r:
            msg = f"I am about to perform partition on a list\n" \
                  f"p: {p}; r: {r}\n" \
                  f"List state: {ls}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

            q = self.partition(ls, p, r)
            msg = f"Pivot from partitioning: {q}\n" \
                  f"List state: {ls}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

            # print(f'p: {p}, q: {q}, r:{r}')
            self.quick_sort(ls, p, q-1)
            self.quick_sort(ls, q+1, r)

    def show_steps(self):
        print(f'ls at the start: {self.steps[0].state}')
        for index, step in enumerate(self.steps):
            print(step.msg)

