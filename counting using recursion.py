l = list(map(int,input().split()))
target = int(input())

# find the frequency of the target
def counting(l,i,target,c):
    if i == len(l):
        return c
    if l[i] == target: # check if index value == target
        return counting(l,i+1,target,c+1) # increment both count and index
    return counting(l,i+1,target,c) # increment only index
print(counting(l,0,target,0))

# find the value which has frequency equal to target
def find_frequency(d,target,l,i):
    if d[l[i]] == target: # frequency = target
        return l[i] # return key
    return find_frequency(d,target,l,i+1) # increment the index

def find_by_frequency(l,i,target,d):
    if i == len(l): # reached the end of the array
        return find_frequency(d,target,list(d.keys()),0) # check the frequency with target
    if l[i] in d: # creating an dict for frequency
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    return find_by_frequency(l,i+1,target,d) # incrementing the count to reach the end
print(find_by_frequency(l,0,target,{}))
