from collections import namedtuple


class Algorithm:

    def __init__(self):
        self.steps = []
        self.Step = namedtuple('Step', 'description state')

