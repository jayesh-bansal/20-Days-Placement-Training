def prime(a,i,t,c):
    if i == len(a):
        return c
    if a[i] == 2:
        return prime(a,i+1,2,c+1)
    if a[i] % t == 0:
        return prime(a,i+1,2,c)
    if t == a[i]//2 + 1:
        return prime(a,i+1,2,c+1)
    return prime(a,i,t+1,c)
print(prime([2,5,6,7,2,12,4,3,6],0,2,0))