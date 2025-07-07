def normal_fi(n):
    if n <= 1: 
        return n
    total = 0
    total_t_minus_1 = 1
    total_t_minus_2 = 0
    for i in range(2, n+1):
        total = total_t_minus_1 + total_t_minus_2
        total_t_minus_2 = total_t_minus_1
        total_t_minus_1 = total
    return total


def a(n):
    if n<=1:
        return n
    return a(n-1) + a(n-2)

# def b(n, index=0, t=0, t1=0):
#     if index == n:
#         return t
#     return b(n, index+1, )

print(normal_fi(7))
print(a(7))
print(b(7))