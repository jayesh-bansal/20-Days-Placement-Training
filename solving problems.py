# possible to reach end
# arr = list(map(int,input().split()))
# k = 0
# for i in arr:
#     k = max(k,i)
#     k -= 1
#     if k < 0:
#         print("Not Possible")
#         break
# else:
#     print("Possible")

# shortest job scheduling
# arr = list(map(int,input().split()))
# arr.sort()
# c = 0
# for i in range(len(arr)):
#     c += (arr[i] * (len(arr)-1-i))
# print(c//len(arr))

# demand and supply
# demand = list(map(int,input().split()))
# supply = list(map(int,input().split()))
# demand.sort(reverse = True)
# supply.sort(reverse = True)
# i = 0
# j = 0
# c = 0
# while i < len(demand):
#     if demand[i] <= supply[j]:
#         c += 1
#         j += 1
#     i += 1
# print(c)