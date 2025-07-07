from nodes import Node, print_tree

root = Node(0)
child1 = Node(1)
child2 = Node(2)
child3 = Node(3)
child4 = Node(4)
child5 = Node(5)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)
child4.add_child(child5)

print_tree(root)

def dfs_stack(node):
    stack = [node]
    while stack:
        node = stack.pop()
        # do processing
        print(node.value)
        for child in node.children:
            stack.append(child)

    print(stack)


def dfs_recursive(n):
    if n is None:
        return 
    # do processing eg search...
    print(n.value)
    for child in n.children:
        dfs_recursive(child)

dfs_stack(root)
dfs_recursive(root)
