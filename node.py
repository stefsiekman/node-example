class Node:

    def __init__(self, parent=None):
        self.count = 0
        self.parent: Node = parent

    def simulate_random(self):
        pass

    def back_propagate(self):
        self.count += 1

        if self.parent:
            self.parent.back_propagate()
