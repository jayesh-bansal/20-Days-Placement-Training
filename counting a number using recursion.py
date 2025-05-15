l = list(map(int,input().split()))
target = int(input())

def counting(l,i,target,c):
    if i == len(l):
        return c
    if l[i] == target:
        return counting(l,i+1,target,c+1)
    return counting(l,i+1,target,c)
print(counting(l,0,target,0))


def find_frequency(d,target,l,i):
    if d[l[i]] == target:
        return l[i]
    return find_frequency(d,target,l,i+1) 

def find_by_frequency(l,i,target,d):
    if i == len(l):
        return find_frequency(d,target,list(d.keys()),0)
    if l[i] in d:
        d[l[i]] += 1
    else:
        d[l[i]] = 1
    return find_by_frequency(l,i+1,target,d)
print(find_by_frequency(l,0,target,{}))
