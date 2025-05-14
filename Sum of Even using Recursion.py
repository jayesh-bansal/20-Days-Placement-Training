def even_sum(x,i):
    if i == len(x):
        return 0
    if x[i] % 2 == 0:
        return x[i] + even_sum(x,i + 1)
    else:
        return even_sum(x,i + 1)
z = [2,5,6,7,2,1,4,3,6]
print(even_sum(z,0))