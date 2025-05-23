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
# i = k # starting from the kth element
# while i < len(arr) - k: # base exit condition
#     j = k # starting from the last kth element
#     while j < len(arr) - k - i - 1: # bubble sort condition
#         if arr[j] > arr[j+1]:
#           arr[j],arr[j+1] = arr[j+1],arr[j]
#         j += 1
#     i += 1
# print(arr)

#finding kth largest element
# arr = list(map(int,input().split()))
# k = int(input())
# for i in range(k): # running k times to find the kth largest element
#     flag = False
#     for j in range(len(arr)-i-1):
#         if arr[j] > arr[j+1]:
#             flag = True
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#     if not flag:
#         break
# print(arr[-k]) # print the kth element from the last

#sorting by 2nd element of a 2d matrix
# arr = [list(map(int,input().split())) for i in range(5)]
# for i in range(5): # no of rows
#     flag = False
#     for j in range(4-i): # no of rows - 1 - i and bubble sort
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
#     for j in range(len(s)-i-1): # bubble sort by comparing the first element
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
# primes = [] # saving all primes position
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if prime(arr[i][j]): # checking if a no is prime in a list
#             primes.append(j)
#             break
# for i in range(len(arr)):
#     flag = True
#     for j in range(len(arr)-j-1):
#         if arr[j][primes[j]] > arr[j+1][primes[j+1]]: # bubble sort with prime number index
#             flag = False
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             primes[i],primes[j+1] = primes[j+1],primes[j]
#     if flag:
#         break
# print(arr)

# sort according to length
# arr = input().split()
# length = list(map(len,arr)) # saving length of string
# for i in range(len(arr)):
#     flag = True
#     for j in range(len(arr)-i-1):
#         if length[j] > length[j+1]: # bubble sort with length
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
#     d[i] = d.get(i,0) + 1 # counting the frequency
# d = list(d.items()) # saving as pair of tuple in list
# for i in range(len(d)):
#     flag = True
#     for j in range(len(d)-1-i): # bubble sort of the 2nd element of a tuple of a list
#         if d[j][1] > d[j+1][1]:
#             d[j],d[j+1] = d[j+1],d[j]
#             flag = False
#     if flag:
#         break
# arr = []
# for i,j in d:
#     arr += ([i]*j) # adding and multiplying by frequency
# print(arr)

# bucket sort
# arr = list(map(int,input().split()))
# bucket = [[] for i in range(len(arr))] # empty array
# mini = min(arr) # min value
# maxi = max(arr) # max value
# for i in arr:
#     index = (i - mini) * (len(arr) - 1) // (maxi - mini) # finding on the basis of the min value
#     bucket[index].append(i) # appending in that position
# for i in bucket:
#     i.sort() # sorting in ascending order to add properly in the last
# arr = []
# for i in bucket:
#     arr += i # add all the lists together
# print(arr)