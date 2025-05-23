# possible to reach end
# arr = list(map(int,input().split()))
# k = 0
# for i in arr:
#     k = max(k,i) # updating to the better value
#     k -= 1 # subtracting for moving to the next step
#     if k < 0: # if the best value is negative, not possible
#         print("Not Possible")
#         break
# else: # reached end means possible
#     print("Possible")

# shortest job scheduling
# arr = list(map(int,input().split()))
# arr.sort()
# c = 0
# for i in range(len(arr)):
#     c += (arr[i] * (len(arr)-1-i)) # shortcut formula for sum of the prefix sum
# print(c//len(arr))

# demand and supply
# demand = list(map(int,input().split()))
# supply = list(map(int,input().split()))
# demand.sort(reverse = True) # sorting demand in desc
# supply.sort(reverse = True) # sorting supply in desc
# i = 0
# j = 0
# c = 0
# while i < len(demand):
#     if demand[i] <= supply[j]: # if highest of supply == highest of demand then increase both else increase only demand
#         c += 1
#         j += 1
#     i += 1
# print(c)