"""Using stacks using two different data structures: deque from the collections module and a regular Python list"""

from collections import deque

# --------- Using deque as a stack ---------
print("== Using deque as a stack ==")

example_stack = deque()
print("Initial stack (deque):", example_stack)

example_stack.append(10)
example_stack.append("ABC")
example_stack.append(1.0)
print("Stack after pushing elements:", example_stack)

print("Bottom of the stack (index 0):", example_stack[0])
print("Top of the stack (last element):", example_stack[-1])
print("Current stack size:", len(example_stack))

# Pop the top element
popped_element = example_stack.pop()
print(f"Popped the top element: {popped_element}")
print("Stack after popping one element:", example_stack)

# Check if the stack is empty
if not example_stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")

print("\n")

# --------- Using list as a stack ---------
print("== Using list as a stack ==")

list_stack = []
print("Initial stack (list):", list_stack)

list_stack.append(20)
list_stack.append("XYZ")
list_stack.append(1.0)
print("Stack after pushing elements:", list_stack)

print("Popping elements:")
print("Popped:", list_stack.pop())
print("Popped:", list_stack.pop())
print("Popped:", list_stack.pop())

if not list_stack:
    print("Stack is empty.")
else:
    print("Stack is not empty.")
