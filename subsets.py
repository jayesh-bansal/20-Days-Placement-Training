# Create a Subset
# l = list(map(int,input().split()))
# def subset(l,i,res):
#     if i == len(l): # check if reached the end
#         return [res] # return in the form of nested list
#     return subset(l,i+1,res+[l[i]]) + subset(l,i+1,res) # add the returned nested list forming a bigger list
# print(subset(l,0,[]))

#subset sum is equal to k
# l = list(map(int,input().split()))
# target = int(input())
# def subset(l,i,res,s,target):
#     if s == target: # check if sum == target
#         return [res] # skipping the rest and returning
#     if i == len(l) or s > target: # checking if reached end or sum is greater than target
#         return [] #returning empty as it is not required
#     return subset(l,i+1,res+[l[i]],s + l[i],target) + subset(l,i+1,res,s,target) # adding all possible subset set equal to target
# print(subset(l,0,[],0,target))

#min length subset sum
l = list(map(int,input().split()))
target = int(input())
def subset(l,i,c,target,m):  
    if 0 == target: # if sum of subset = target
        return min(c,m) # returning min of existing value and the length of subset
    if i == len(l) or target < 0: # if sum > target or reached end
        return float('inf') # returning max value so i can be ignored by min function
    return min(subset(l,i+1,c + 1,target - l[i],m), subset(l,i+1,c,target,m)) # checking all possibles and finding the min value
k = subset(l,0,0,target,float('inf')) # saving the min value in k
print(k if k != float('inf') else -1)