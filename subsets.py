# Create a Subset
# l = list(map(int,input().split()))
# def subset(l,i,res):
#     if i == len(l):
#         return [res]
#     return subset(l,i+1,res+[l[i]]) + subset(l,i+1,res)
# print(subset(l,0,[]))

#subset sum is equal to k
# l = list(map(int,input().split()))
# target = int(input())
# def subset(l,i,res,s,target):
#     if s == target:
#         return [res]
#     if i == len(l) or s > target:
#         return []
#     return subset(l,i+1,res+[l[i]],s + l[i],target) + subset(l,i+1,res,s,target)
# print(subset(l,0,[],0,target))

#min length subset
l = list(map(int,input().split()))
target = int(input())
def subset(l,i,c,target,m):
    if 0 == target:
        return min(c,m)
    if i == len(l) or target < 0:
        return float('inf')
    return min(subset(l,i+1,c + 1,target - l[i],m), subset(l,i+1,c,target,m))
k = subset(l,0,0,target,float('inf'))
print(k if k != float('inf') else -1)