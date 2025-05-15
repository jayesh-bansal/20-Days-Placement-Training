# Create a Subset
# l = list(map(int,input().split()))
# def subset(l,i,res):
#     if i == len(l):
#         return [res]
#     return subset(l,i+1,res+[l[i]]) + subset(l,i+1,res)
# print(subset(l,0,[]))

#subset sum is equal to k
l = list(map(int,input().split()))
target = int(input())
def subset(l,i,s,target):
    if s == target:
        return True
    if i == len(l) or s > target:
        return False
    return subset(l,i+1,s + l[i],target) or subset(l,i+1,s,target)
print(subset(l,0,0,target))