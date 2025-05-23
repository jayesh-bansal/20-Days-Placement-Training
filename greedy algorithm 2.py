# max no of meeting possible
# start = list(map(int,input().split()))
# end = list(map(int,input().split()))
# l = [[start[i],end[i]] for i in range(len(start))] # creating in the tuple form
# l.sort(key = lambda x: x[1]) # sorting with end
# c = 0
# prev = 0
# for i,j in l:
#     if prev <= i: # comparing start with the previous meet end
#         c += 1 # possible meet
#         prev = j # new meet end
# print(c)

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
arr = list(map(int,input().split()))
k = int(input())
c = 0
s = 0
i = 0
j = 0
m = 0
while j < len(arr):
    if s < k: # add till sum is less than k
        s += arr[j]
        j += 1
    else:
        m = max(m,j-i+1) # compare len count with the max len count
        s -= arr[i] # removing the first element so that new elements can be added
        i += 1 # incrementing the subarray first index
print(m)