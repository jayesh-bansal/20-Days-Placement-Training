# frog jump
# arr = list(map(int,input().split()))
# dp = [0] * (len(arr) + 1)
# dp[2] = arr[1] - arr[0]
# for i in range(3,len(arr) + 1):
#     dp[i] = min(abs(arr[i-1] - arr[i-2]) + dp[i-1],abs(arr[i-1] - arr[i-3]) + dp[i-2])
# print(dp[-1])

# frog k jump
# arr = list(map(int,input().split()))
# k = int(input())
# dp = [float('inf')] * (len(arr) + 1)
# for i in range(2,len(arr) + 1):
#     for j in range(1,min(i,k)):
#         dp[i] = min(abs(arr[i-1] - arr[i-j-1]) + dp[i-j],dp[i])
# print(dp[-1])

# job sheduling
# arr1 = eval(input())
# arr2 = list(map(int,input().split()))
# dp = [0] * (arr1[-1][1]+1)
# for i in range(len(arr1)):
#     if dp[arr1[i][1]] < dp[arr1[i][0]] + arr2[i]:
#         for j in range(i,len(arr1)):
#             dp[arr1[i][1]] = dp[arr1[i][0]] + arr2[i]
# print(dp)
# print(dp[-1])

# longest common subsequence
# O(m + n)
# s1 = input()
# s2 = input()
# d = {}
# for i in s1:
#     d[i] = d.get(i,0) + 1
# k = ''
# for i in s2:
#     if i in d and d[i] > 0:
#         k += i
#         d[i] -= 1
# print(k)

# O(m * n)
s1 = input()
s2 = input()