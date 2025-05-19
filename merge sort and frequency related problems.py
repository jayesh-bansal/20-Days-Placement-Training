# sorting 2 sorted array
# arr = list(map(int,input().split()))
# arr2 = list(map(int,input().split()))
# i = 0
# j = 0
# arr3 = []
# while i < len(arr) and j < len(arr2):
#     if arr[i] > arr2[j]:
#         arr3.append(arr2[j])
#         j += 1
#     else:
#         arr3.append(arr[i])
#         i += 1
# while i < len(arr):
#         arr3.append(arr[i])
#         i += 1
# while j < len(arr2):
#         arr3.append(arr2[j])
#         j += 1
# print(arr3)

# merge sort
# def merge(arr,l,h,mid):
#     n1 = mid - l + 1
#     n2 = h - mid
#     L = [0] * n1
#     R = [0] * n2
#     for i in range(n1):
#         L[i] = arr[l + i]
#     for i in range(n2):
#         R[i] = arr[mid + 1 + i]

#     i = 0
#     j = 0
#     k = l
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
    
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
    
# def mergesort(arr,l,h):
#     if l >= h:
#          return
#     mid = (l + h) // 2
#     mergesort(arr,l,mid)
#     mergesort(arr,mid+1,h)
#     merge(arr,l,h,mid)
# l = list(map(int,input().split()))
# mergesort(l,0,len(l)-1)
# print(l)

# kth largest element
# (O(n))
# arr = list(map(int,input().split()))
# l = [0] * (max(arr) + 1)
# k = int(input())
# for i in arr:
#     l[i] += 1
# i = len(l) - 1
# print(l)
# while True:
#     # print(i)
#     k -= l[i]
#     if k <= 0:
#         break
#     i -= 1
# print(i)

# O(nlogn) we use merge sort and the find the largest k position from last

# finding the largest frequency element
# arr = list(map(int,input().split()))
# d = {}
# for i in arr:
#     d[i] = d.get(i,0) + 1
# m = 0
# k = 0
# for i in d:
#     if d[i] < m:
#         m = d[i]
#         k = i
# print(i)

# finding the kth highest frequency element
# arr = list(map(int,input().split()))
# d = {}
# k = int(input())
# for i in arr:
#     d[i] = d.get(i,0) + 1
# m = max(d.values())
# l = [0] * (m+1)
# for i,j in d.items():
#     l[j] = i
# i = len(l) - 1
# while True:
#     if l[i] != 0:
#         k -= 1
#     if k == 0:
#         break
# print(l[i])

# find the kth values frequency
# arr = list(map(int,input().split()))
# d = {}
# l = []
# k = int(input())
# for i in arr:
#     d[i] = d.get(i,0) + 1
# for i in d:
#     if d[i] == k:
#         l.append(i)
# print(l)

# find the majority element
# using dictonary
# arr = list(map(int,input().split()))
# d = {}
# for i in arr:
#     d[i] = d.get(i,0) + 1
# for i in d:
#     if  d[i] > len(arr)//2:
#         print(i)
#         break

# more voting algorithm
# arr = list(map(int,input().split()))
# c = 0
# for i in arr:
#     if c == 0:
#         k = i
#     if i == k:
#         c += 1
#     else:
#         c -= 1
# print(k)

# linear search last occurence
# arr = list(map(int,input().split()))
# k = int(input())
# for i in range(len(arr) - 1,-1,-1):
#     if arr[i] == k:
#         print(i)
#         break
# else:
#     print(-1)

# binary search
# arr = list(map(int,input().split()))
# l = 0
# r = len(arr) - 1
# k = int(input())
# while l <= r:
#     m = (l + r) // 2
#     if arr[m] == k:
#         print(m)
#         break
#     elif arr[m] > k:
#         r = m - 1
#     else:
#         l = m + 1
# else:
#     print(-1)

# binary search last occurence
# arr = list(map(int,input().split()))
# k = int(input())
# l = 0
# r = len(arr) - 1
# t = -1
# while l <= r:
#     m = (l + r) // 2
#     if arr[m] == k:
#         t = m
#         l = m + 1
#     elif arr[m] > k:
#         r = m - 1
#     else:
#         l = m + 1
# print(t)

# inserting in a sorted array
arr = list(map(int,input().split()))
k = int(input())
l = 0
r = len(arr) - 1
while l <= r:
    m = (l + r) // 2
    if arr[m] == k:
        break
    elif arr[m] > k:
        r = m - 1
    else:
        l = m + 1
print(m)