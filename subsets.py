l = list(map(int,input().split()))
def subset(l,i,res):
    if i == len(l):
        return [res]
    return subset(l,i+1,res+[l[i]]) + subset(l,i+1,res)
print(subset(l,0,[]))