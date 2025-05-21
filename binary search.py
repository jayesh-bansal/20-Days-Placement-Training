# sqrt of a number
# n = int(input())
# t = 0
# l = 0
# r = n //2
# while l <= r:
#     m = (l + r) // 2
#     if m * m < n:
#         t = m
#         l = m + 1
#     else:
#         r = m - 1
# print(t)

# index of the rotated sorted array
arr = list(map(int,input().split()))
l = 0 
r = len(arr) - 1
while l <= r:
    m = (l + r) // 2
    print(m)
    if arr[m] < arr[m-1]:
        print(m)
        break
    elif arr[m] > arr[l]:
        l = m + 1
    else:
        r = m - 1
else:
    print(0)

# find all the peaks
# arr = list(map(int,input().split()))
# def peaks(arr,l,r,c):
#     if l > r:
#         return c
#     m = (l + r) // 2
#     if m + 1 < len(arr) and arr[m] > arr[m+1] and m > -2 and arr[m] > arr[m-1]:
#         c += 1
#     c=peaks(arr,l,m-1,c) 
#     c=peaks(arr,m+1,r,c)
#     return c
# print(peaks(arr,0,len(arr)-1,0))