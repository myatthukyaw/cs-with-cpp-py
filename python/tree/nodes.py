class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

def print_tree(node, level=0):
    print(" " * level + str(node.value))
    for child in node.children:
        print_tree(child, level + 2)