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

    def __str__(self):
        return f"Node(count={self.count})"

    def pretty_string(self, depth=1):
        # Add this node to the string
        string = str(self) + '\n'

        # Then add all the children
        for nr in range(MAX_CHILDREN):
            # Skip non-existing children
            if not self.children[nr]:
                continue

            # Recursive indentation
            string += "    " * depth

            # The child itself, also called recursively
            string += f"#{nr}: {self.children[nr].pretty_string(depth + 1)}\n"

        # The string should not end with a newline
        return string[:-1]
