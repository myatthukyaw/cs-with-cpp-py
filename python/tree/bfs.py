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


def bfs_with_queue(n):
    queue = [n]

    while queue:
        node = queue[0]
        queue = queue[1:]
        # same as queue.pop(0) dequeue from front
        print(node.value)
        for child in node.children:
            queue.append(child)

def bfs(n):
    if not n:
        return
    
    for child in n.chiildren:
        bfs(child)

bfs_with_queue(root)