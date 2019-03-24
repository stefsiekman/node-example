# Node Example

Example of a class based tree in python.

Each node is part of a tree. They can have `N` children, as defined in `node.py`, which are identified by there index.

I had to make the code some something, so I added something that slightly resembles Monte Carlo Tree Search. For each
simulation run the program goes down the tree selection a random child Node of the `N` possible children. At each node
there is a `1/4` change that the traversal will terminate. When this termination happens, the `count` of that node is
incremented. This incrementation is then back propagated to all the ancestors.

Additionally there is code to recursively create a string representation of the tree structure. This is mainly just to
aid with debugging, but it also shows a way to implement a recursive algorithm with a class.

The output of the program is random, but it might be the following to give an example.

```
Running 10 simulations...
Node(count=10)
    #0: Node(count=5)
        #0: Node(count=2)
            #0: Node(count=1)
            #1: Node(count=1)
        #1: Node(count=3)
            #1: Node(count=3)
                #0: Node(count=1)
                #1: Node(count=1)
                    #1: Node(count=1)
    #1: Node(count=3)
        #0: Node(count=1)
            #0: Node(count=1)
                #0: Node(count=1)
                    #1: Node(count=1)
        #1: Node(count=1)
```