class Stack:

    def __init__(self, size):
        self.size = size
        self.arr = [None for _ in range(size)]
        self.top = -1

    def check_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, value):
        if self.top < self.size - 1:
            self.arr[self.top + 1] = value
            self.top += 1
        else:
            print("Stack is full and I can't add anything")

    def pop(self):
        if self.check_empty():
            print("I can't pop anything because stack is empty")
        else:
            self.arr[self.top] = None
            self.top -= 1
