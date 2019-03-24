from node import Node


N = 10


if __name__ == "__main__":
    # Create an empty tree
    tree = Node()

    # Run the simulations
    print(f"Running {N} simulations.")
    for _ in range(N):
        tree.simulate()

    print(tree.pretty_string())
