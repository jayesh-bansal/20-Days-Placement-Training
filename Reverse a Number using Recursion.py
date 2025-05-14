def rev(n,re):
    if n == 0:
        return re
    return rev(n//10,re * 10 + n % 10)

n = 153
print(rev(n,0))