from nodes import Node, print_tree

root = Node("root")
child1 = Node("child1")
child2 = Node("child2")
child11 = Node("child1.1")
child12 = Node("child1.2")
child21 = Node("child2.1")
child22 = Node("child2.2")

child1.add_child(child11)
child1.add_child(child12)
child2.add_child(child21)
child2.add_child(child22)
root.add_child(child1)
root.add_child(child2)


print_tree(root)