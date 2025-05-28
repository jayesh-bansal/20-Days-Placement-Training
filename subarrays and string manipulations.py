# reverse the consonant of a string
# s = input()
# l = []
# v = 'aeiou'
# for i in range(len(s)):
#     if s[i] not in v: # appending all consonants
#         l.append(i)
# k = ''
# j = 0
# for i in range(len(s)):
#     if i == l[j]: # if consonant, then reverse add from the list
#         k += s[l[-j-1]]
#         j += 1
#     else: # else add vowels
#         k += s[i]
# print(k)

# max sum of a sub array
# arr = list(map(int,input().split()))
# k = int(input())
# c = 0
# for i in range(k):
#     c += arr[i] # som of first k
# s = c
# for i in range(k,len(arr)):
#     s += arr[i] - arr[i - k] # sum of the next window
#     c = max(c,s) # update the max sum window
# print(c)

# longest subarray with sum less than equal to k
# arr = list(map(int,input().split()))
# k = int(input())
# c = 0
# s = 0
# i = 0
# j = 0
# m = 0
# while j < len(arr):
#     if s < k: # add till sum is less than k
#         s += arr[j]
#         j += 1
#     else:
#         m = max(m,j-i+1) # compare len count with the max len count
#         s -= arr[i] # removing the first element so that new elements can be added
#         i += 1 # incrementing the subarray first index
# print(m)

# longest substring palindrome
# def palindrome(s,left,right):
#     k = ''
#     if left == right:
#         k = s[left]
#         left -= 1
#         right += 1
#     while left > -1 and right < len(s) and s[left] == s[right]:
#         k = s[left] + k + s[right]
#         left -= 1
#         right += 1
#     return k
# s = input()
# k = ''
# for i in range(len(s)):
#     k = max(k,palindrome(s,i,i),palindrome(s,i,i+1),key = len)
# print(k)

# count of all palindrome substring
# import math
# def palindrome(s,left,right):
#     while left > -1 and right < len(s) and s[left] == s[right]:
#         left -= 1
#         right += 1
#     return math.ceil((right-left)/2)
# s = input()
# k = 0
# for i in range(len(s)):
#     k += palindrome(s,i,i) + palindrome(s,i,i+1)
# print(k)

# non repeating longest substring
# O(n) (Using Sets)
# s = input()
# l = 0
# r = 0
# k = set()
# m = 0
# while r < len(s):
#     if s[r] not in k:
#         k.add(s[r])
#     else:
#         m = max(m,len(k))
#         while s[r] != s[l]:
#             k.remove(s[l])
#             l += 1
#         l += 1
#     r += 1
# print(max(m,len(k)))

# O(n) (lesser time) (Using Dict)
# s = input()
# d = {}
# m = 0
# prev = 0
# for i in range(s):
#     if s[i] in d:
#         c = max(c,i-prev)
#         prev = max(prev,d[s[i]]+1)
#     d[s[i]] = i
# print(max(c,i-prev))

# longest non repeating substring and should have 2 characters
# s = input()
# d = {}
# m = 0
# a,b = map(int,input())
# prev = 0
# for i in range(s):
#     if a in d and b in d:
#         if s[i] in d:
#             c = max(c,i-prev)
#             prev = max(prev,d[s[i]]+1)
#     d[s[i]] = i
# print(max(c,i-prev) if prev > 0 else -1)

# remove k points from arrays to have max points
# arr = list(map(int,input().split()))
# k = int(input())
# s = sum(arr)
# i = 0
# j = len(arr) - 1
# for a in range(k):
#     if arr[i] > arr[j]:
#         s -= arr[j]
#         j -= 1
#     elif arr[i] == arr[j]:
#         x = i + 1
#         y = j - 1
#         while x < y and arr[x] == arr[y]:
#             x += 1
#             y -= 1
#         if arr[x] > arr[y]:
#             s -= arr[j]
#             j -= 1
#         else:
#             s -= arr[i]
#             i += 1
#     else:
#         s -= arr[i]
#         i += 1
# print(s)

# remove k numbers to have highest value
# O(2^k) (Using recursion)
# arr = list(map(int,input().split()))
# k = int(input())
# def total(arr,i,j,k,s):
#     if k == 0:
#         return s
#     return max(total(arr,i+1,j,k-1,s+arr[i]),total(arr,i,j-1,k-1,s+arr[j]))
# print(total(arr,0,len(arr)-1,k,0))

# O(k) (Using Sliding window/Two pointer)
arr = list(map(int,input().split()))
k = int(input())
m = left = sum(arr[:k])
for i in range(k):
    left -= arr[~i+k]
    left += arr[~i]
    m = max(m,left)
print(m)