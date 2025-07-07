from collections import deque

def is_balanced(input_str : str) -> bool:

    stack = deque()
    bracket_pairs = { '(' : ')',
                      '[' : ']',
                      '{' : '}', }

    for char in input_str:
        if char in bracket_pairs.keys():
            stack.append(char)
        elif char in bracket_pairs.values():
            if stack:
                top = stack.pop()
                if bracket_pairs[top] != char:
                    return False
            else:
                return False
        else:
            # char is not bracket, so we ignore it.
            continue
    return not stack

if __name__ == "__main__":

    input_str = "{([[]])}"
    
    if is_balanced(input_str):
        print("Input string is balanced")
    else:
        print("Input string is not balanced.")