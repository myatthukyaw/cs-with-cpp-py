

def normal_factorial(n):
    total = 1
    for i in range(n):
        total *= (i + 1)
    return total

def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n-1)

def tail_recursive_factorial(n, total=1):
    if n == 0:
        return total
    return tail_recursive_factorial(n-1, total * n)

def tail_recursive_factorial_with_index(n, index=0, total=1):
    if n==index or n==0:
        return total
    index = index + 1
    return tail_recursive_factorial_with_index(n, index, total*index)


print(normal_factorial(3))
print(tail_recursive_factorial(3))
print(tail_recursive_factorial_with_index(3))