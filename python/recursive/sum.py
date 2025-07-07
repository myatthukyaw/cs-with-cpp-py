def normal_sun(n):
    total_sum = 0 
    for i in range(n+1):
        total_sum += i
    return total_sum

def recursive_sum(n):
    if n == 0:
        return 0
    total_sum = n + recursive_sum(n - 1)
    return total_sum


def tail_recursive_sum(n, total_sum=0):
    if n == 0:
        return total_sum
    return tail_recursive_sum(n - 1, total_sum + n)

def tail_recursive_sum_with_indexing(n, index=0, total_sum=0):
    if index == n:
        return total_sum + index
    return tail_recursive_sum_with_indexing(n, index+1, total_sum + index)

print(normal_sun(10))
print(recursive_sum(10))
print(recursive_sum_with_indexing(10))
print(tail_recursive_sum(10))