def check(n,c,l):
    if n < 1:
        # return -1
        return []
    if n == 1:
        # return c
        return l
    # return max(check(n-5,c+1,l + [5]), check(n-3,c+1,l + [3]))
    return (check(n-5,c+1,l + [5]) or check(n-3,c+1,l + [3]))

# def check(n,c,l):
#     if n < 1:
#         return -1
#     if n % 3 == 1:
# #         return c + n//3
#         return l + [3] * (n//3)
#     if n % 5 == 1:
# #         return c + n//5
#         return l + [5] * (n//5)
#     return check(n-3, c + 1,l + [3]) or check(n-5, c + 1,l + [5])

print(check(int(input()),0,[]))