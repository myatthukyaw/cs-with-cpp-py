from collections import deque

example_stack = deque()
print(example_stack)

example_stack.append(10)
example_stack.append("ABC")
example_stack.append(1.0)
print(example_stack)
print(example_stack[0])
print(example_stack[-1])
print(len(example_stack))

example_stack.pop()

if not example_stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")


list_stack = []
print(list_stack)

list_stack.append(20)
list_stack.append("XYZ")
list_stack.append(1.0)
print(list_stack)

list_stack.pop()
list_stack.pop()
list_stack.pop()

if not list_stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")