class Queue:

    def __init__(self, size):
        self.size = size
        self.arr = [None for _ in range(size)]
        self.p = 0
        self.q = 0

    def push(self, value):
        if self.q == self.p and self.arr[self.q]:
            print("Queue is full so I can't push anything")
        else:
            self.arr[self.q] = value
            if self.q < self.size - 1:
                self.q += 1
            else:
                self.q = 0

    def pop(self):
        if self.p == self.q and not self.arr[self.q]:
            print("Queue is empty, so I can't pop!"
                  )
        else:
            self.arr[self.p] = None
            if self.p < self.size - 1:
                self.p += 1
            else:
                self.p = 0

    def __str__(self):
        return str(self.arr)