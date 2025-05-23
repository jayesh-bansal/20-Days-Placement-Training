# Max Difference between 2 elements
# arr = list(map(int,input().split()))
# mini = float('inf')
# final = 0
# for i in arr:
#     mini = min(mini,i) # minimum value
#     final = max(i - mini,final) # comparing by subtracting current index and minimum at the current situation and stored value
# print(final)

# Larget Even and Smallest Odd
# me = -float('inf')
# so = float('inf')
# arr = list(map(int,input().split()))
# for i in arr:
#     if i % 2 == 0: # check even
#         me = max(me,i) # store max even
#     else: # check odd
#         so = min(so,i) # min odd
# print(f"Max Even: {me} Min Odd: {so}")

#2nd largest Number
m = 0
m2 = 0
arr = list(map(int,input().split()))
for i in arr:
    if i >= m: # compare with the max value
        m2 = m # prev max = current max
        m = i # current max = new max
print(m2) # prev max