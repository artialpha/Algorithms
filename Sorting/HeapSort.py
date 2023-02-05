from Algorithm import Algorithm
from math import inf


class HeapSort(Algorithm):

    @staticmethod
    def heap_parent_index(i):
        parent_index = int((i+1)/2) - 1
        return parent_index

    @staticmethod
    def heap_left_child_index(i):
        left_index = ((i+1) * 2) - 1
        return left_index

    @staticmethod
    def heap_right_child_index(i):
        right_index = (i+1) * 2
        return right_index

    @classmethod
    def check_heap(cls, heap):
        for index, node in enumerate(heap[1:], 1):
            parent_index = cls.heap_parent_index(index)
            if heap[parent_index] < node:
                print("check heap claims that this is not a heap")
                print(f'parent index: {parent_index}, parent value: {heap[parent_index]}')
                print(f'node index: {index}, node value: {node}')
                return False
        return True

    def heapify(self, ls, i, stop=inf):
        heap_size = len(ls) - 1
        left = self.heap_left_child_index(i)
        right = self.heap_right_child_index(i)
        largest = i
        if i < stop:
            if left <= heap_size and left <= stop and ls[left] > ls[largest]:
                largest = left
            if right <= heap_size and right <= stop and ls[right] > ls[largest]:
                largest = right
            if largest != i:
                msg = f"The heap property at index: {i} is not satisfied so I need to swap elements\n" \
                      f"Largest index: {largest}, largest value: {ls[largest]}\n" \
                      f"Parent index: {i}, parent value: {ls[i]}"
                step = self.Step(msg=msg, state=ls[:], context={})
                self.steps.append(step)

                ls[largest], ls[i] = ls[i], ls[largest]
                self.heapify(ls, largest, stop)

    def build_heap(self, ls):
        size = len(ls) - 1
        half = int(round(size/2))
        for i in range(half, -1, -1):
            self.heapify(ls, i)

    def heapsort(self, ls):
        msg = f"I want to sort this list: {ls}\n" \
              f"At first I will build a heap from it.\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        self.build_heap(ls)
        size = len(ls) - 1

        msg = f"The heap built from the list:\n" \
              f"{self.print_heap(ls)}\n"
        step = self.Step(msg=msg, state=ls[:], context={})
        self.steps.append(step)

        for i in range(size, 0, -1):
            msg = f"List before swap:\n" \
                  f"{ls}\n" \
                  f"I swap the first element with the last (for the current size: {size}):\n" \
                  f"First element: {ls[0]}, last element: {ls[i]}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

            ls[i], ls[0] = ls[0], ls[i]
            size -= 1

            msg = f"List after swap:\n" \
                  f"{ls}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

            msg = f"After the swap I need to heapify\n" \
                  f"{self.print_heap(ls)}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)
            # resize list, without last
            self.heapify(ls, 0, size)

            msg = f"Heap after heapify: \n" \
                  f"{self.print_heap(ls)}\n"
            step = self.Step(msg=msg, state=ls[:], context={})
            self.steps.append(step)

    @classmethod
    def heap_extract_max(cls, heap):
        mx = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        cls.heapify(heap, 0)
        return mx

    @classmethod
    def heap_insert(cls, heap, value):
        heap.append(value)
        i = len(heap) - 1

        while i > 0 and heap[cls.heap_parent_index(i)] < value:
            heap[i] = heap[cls.heap_parent_index(i)]
            i = cls.heap_parent_index(i)
        heap[i] = value

    @classmethod
    def swap_with_parent(cls, heap, i, value):
        while i > 0 and heap[cls.heap_parent_index(i)] < value:
            heap[i] = heap[cls.heap_parent_index(i)]
            i = cls.heap_parent_index(i)
        heap[i] = value

    @classmethod
    def heap_increase_value(cls, heap, i, value):
        heap[i] = max(heap[i], value)
        cls.swap_with_parent(heap, i, value)

    @classmethod
    def heap_delete(cls, heap, i):
        last_index = len(heap) - 1
        if i == last_index:
            heap.pop()
        else:
            heap[i] = heap[last_index]
            heap.pop()
            if heap[i] > heap[cls.heap_parent_index(i)]:
                cls.swap_with_parent(heap, i, heap[i])
            else:
                cls.heapify(heap, i)

    @classmethod
    def merge_lists(cls, lists):
        pass

    @classmethod
    def print_heap(cls, ls):
        def get_indices(ls_):
            a1 = 1
            q = 2
            len_ls = len(ls_)
            n = 1
            temp = []

            while (geo_sum := int(a1 * ((1-q**n)/(1-q)))) < len_ls:
                temp.append((geo_sum - (2**(n-1)), geo_sum))
                n += 1
            temp.append((geo_sum - (2**(n-1)), len_ls))
            return temp

        indices = get_indices(ls)
        msg = ''
        line_length = 130

        for i, (start, end) in enumerate(indices):
            elements = ls[start:end]
            for el in elements:
                msg += f'{el:^{int(line_length/(2**i))}}'
            msg += f'\n'
            for _ in range(len(elements)):
                b = '/'
                f = '\\'
                msg += f'{b:^{int(line_length/((2**i)*2))}}{f:^{int(line_length/((2**i)*2))}}'
            msg += f'\n'

        # remove last line two lines
        msg = "\n".join(msg.split("\n")[0:-2])
        return msg

    def show_steps(self):
        print(f'ls at the start: {self.steps[0].state}')
        for index, step in enumerate(self.steps):
            print(step.msg)




