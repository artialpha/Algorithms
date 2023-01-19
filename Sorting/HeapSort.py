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
                return False
        return True

    @classmethod
    def heapify(cls, heap, i, stop=inf):
        heap_size = len(heap) - 1
        left = cls.heap_left_child_index(i)
        right = cls.heap_right_child_index(i)
        largest = i
        if i < stop:
            if left <= heap_size and left <= stop and heap[left] > heap[largest]:
                largest = left
            if right <= heap_size and right <= stop and heap[right] > heap[largest]:
                largest = right
            if largest != i:
                heap[largest], heap[i] = heap[i], heap[largest]
                cls.heapify(heap, largest, stop)

    @classmethod
    def build_heap(cls, ls):
        size = len(ls) - 1
        half = int(round(size/2))
        for i in range(half, -1, -1):
            cls.heapify(ls, i)

    @classmethod
    def heapsort(cls, ls):
        cls.build_heap(ls)
        size = len(ls) - 1

        for i in range(size, 0, -1):
            ls[i], ls[0] = ls[0], ls[i]
            size -= 1
            # resize list, without last
            cls.heapify(ls, 0, size)

    @classmethod
    def heap_extract_max(cls, heap):
        mx = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        cls.heapify(heap, 0)
        return mx

    @classmethod
    def heap_insert(cls, heap, value):
        i = len(heap) - 1
        while i > 0 and heap[cls.heap_parent_index(i)] < value:
            heap[i] = heap[cls.heap_parent_index(i)]
            i = cls.heap_parent_index(i)
        heap[i] = value
