# sqrt of a number
# n = int(input())
# t = 0
# l = 0 # number can be 0
# r = n //2 # number can be n/2
# while l <= r:
#     m = (l + r) // 2
#     if m * m < n: # check if middle is less than n and store the potential value and increase to right subarray
#         t = m
#         l = m + 1
#     else:
#         r = m - 1
# print(t)

# index of the rotated sorted array
# arr = list(map(int,input().split()))
# l = 0 
# r = len(arr) - 1
# while l <= r:
#     m = (l + r) // 2
#     if arr[m] < arr[m-1]: # rotated array value should be less than previous value
#         print(m)
#         break
#     elif arr[m] > arr[0]: # if middle value is greater, it is in original and we have to search in left subarray
#         l = m + 1
#     else:
#         r = m - 1
# else: # not rotated
#     print(0)

# count of all the peaks
# arr = list(map(int,input().split()))
# def peaks(arr,l,r,c):
#     if l > r: # binary search base condition
#         return c
#     m = (l + r) // 2 # check if mid is peak or not
#     if m + 1 < len(arr) and arr[m] > arr[m+1] and m > -2 and arr[m] > arr[m-1]: check peak condition and increment
#         c += 1
#     c=peaks(arr,l,m-1,c) # check left subarray
#     c=peaks(arr,m+1,r,c) # check right subarray
#     return c
# print(peaks(arr,0,len(arr)-1,0))