# Larget Even and Smallest Odd
# me = -float('inf')
# so = float('inf')
# arr = list(map(int,input().split()))
# for i in arr:
#     if i % 2 == 0:
#         me = max(me,i)
#     else:
#         so = min(so,i)
# print(f"Max Even: {me} Min Odd: {so}")

#2nd largest Number
m = 0
m2 = 0
arr = list(map(int,input().split()))
for i in arr:
    if i >= m:
        m2 = m
        m = i
print(m2)