# bubble sort
# arr = list(map(int,input().split()))
# for i in range(len(arr)):
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j],arr[j+1] = arr[j+1],arr[j]
# print(arr)

#sorting between first k and last k
# arr = list(map(int,input().split()))
# k = int(input())
# i = k
# while i < len(arr) - k:
#     j = k
#     while j < len(arr) - k - i - 1:
#         if arr[j] > arr[j+1]:
#           arr[j],arr[j+1] = arr[j+1],arr[j]
#         j += 1
#     i += 1
# print(arr)

#finding kth largest element
# arr = list(map(int,input().split()))
# k = int(input())
# for i in range(k):
#     flag = False
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             flag = True
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#     if not flag:
#         break
# print(arr[-k])

#sorting by 2nd element of a 2d matrix
# arr = [list(map(int,input().split())) for i in range(5)]
# for i in range(5):
#     flag = False
#     for j in range(4-i):
#         if arr[j][1] > arr[j+1][1]:
#             flag = True
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#     if not flag:
#         break
# print(arr)

#lexographical of first 2 letters of an element in a string and ignoring the if more than 2 letters are same
# s = input().split()
# for i in range(len(s)):
#     flag = True
#     for j in range(len(s)-i-1):
#         if s[j][0] > s[j+1][0]:
#             flag = False
#             s[j],s[j+1] = s[j+1],s[j]
#         elif s[j][0] == s[j+1][0]:
#             if s[j][1] > s[j+1][1]:
#                 flag = False
#                 s[j],s[j+1] = s[j+1],s[j]
#             else:
#                 break
#      if flag:
#           break
# print(s)

#sort according to prime numbers where the prime numbers can be in any col and there is only one prime in a row
# def prime(n):
#     for i in range(int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True
# arr = [list(map(int,input().split())) for i in range(5)]
# primes = []
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if prime(arr[i][j]):
#             primes.append(j)
#             break
# for i in range(len(arr)):
#     flag = True
#     for j in range(len(arr)-j-1):
#         if arr[j][primes[j]] > arr[j+1][primes[j+1]]:
#             flag = False
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             primes[i],primes[j+1] = primes[j+1],primes[j]
#     if flag:
#         break
# print(arr)

# sort according to length
# arr = input().split()
# length = list(map(len,arr))
# for i in range(len(arr)):
#     flag = True
#     for j in range(len(arr)-i-1):
#         if length[j] > length[j+1]:
#             length[j],length[j+1] = length[j+1],length[j]
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             flag = False
#     if flag:
#         break
# print(arr)

# sort by frequency
# arr = list(map(int,input().split()))
# d = {}
# for i in arr:
#     d[i] = d.get(i,0) + 1
# d = list(d.items())
# for i in range(len(d)):
#     flag = True
#     for j in range(len(d)-1-i):
#         if d[j][1] > d[j+1][1]:
#             d[j],d[j+1] = d[j+1],d[j]
#             flag = False
#     if flag:
#         break
# arr = []
# for i,j in d:
#     arr += ([i]*j)
# print(arr)

# bucket sort
# arr = list(map(int,input().split()))
# bucket = [[] for i in range(len(arr))]
# mini = min(arr)
# maxi = max(arr)
# for i in arr:
#     index = (i - mini) * (len(arr) - 1) // (maxi - mini)
#     bucket[index].append(i)
# for i in bucket:
#     i.sort()
# arr = []
# for i in bucket:
#     arr += i
# print(arr)