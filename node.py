from random import random, randint
from typing import List


MAX_CHILDREN = 2


class Node:

    def __init__(self, parent=None):
        self.count = 0
        self.parent: Node = parent
        self.children: List[Node] = [None] * MAX_CHILDREN

    def simulate(self):
        """
        Run a random simulation. This means the tree is traversed with a 1/4
        chance at each node of termination, which leads to back propagation of
        a counter increase. In the other case, the algorithm chooses a random
        child to simulate from again.
        :return: Nothing
        """

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
        """
        Increases the counter of the Node and all its ancestors.
        :return: Nothing
        """

        self.count += 1

        # Apply to the ancestors
        if self.parent:
            self.parent.back_propagate()

    def __str__(self):
        return f"Node(count={self.count})"

    def pretty_string(self, depth=1):
        """
        Create a pretty representation of the tree structure from this node.
        This includes all the (existing) children on the node. Indentation is
        added to clearly show which Nodes are children of which Nodes.
        :param depth: The recursion depth (default for root)
        :return: Pretty string representation of the tree starting at this Node
        """
        
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
