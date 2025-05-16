import math
n = int(input())
def binary(n,length,k):
    if n == -1:
        return n
    if len(k) == length:
        print(k)
        n -= 1
        return n
    n = binary(n,length,k + '0')
    n = binary(n,length,k + '1')
    return n

binary(n,int(math.log(n,2))+1,"")