from random import random, randint
from typing import List

MAX_CHILDREN = 2


class Node:

    def __init__(self, parent=None):
        self.count = 0
        self.parent: Node = parent
        self.children: List[Node] = [None] * MAX_CHILDREN

    def simulate(self):
        # 1/4 chance of termination
        if random() < .25:
            self.back_propagate()
            return

        # Otherwise, continue with a random child (might have to be created)
        child_nr = randint(0, MAX_CHILDREN - 1)
        if not self.children[child_nr]:
            self.children[child_nr] = Node(self)
        self.children[child_nr].simulate()


    def back_propagate(self):
        self.count += 1

        if self.parent:
            self.parent.back_propagate()
