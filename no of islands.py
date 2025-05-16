# No of Islands
# def island(l,i,j):
#     if i < 0 or j < 0 or i >= len(l) or j >= len(l[0]) or l[i][j] == 2 or l[i][j] == 0:
#         return 1
#     l[i][j] = 2
#     island(l,i+1,j)
#     island(l,i-1,j)
#     island(l,i,j+1)
#     island(l,i,j-1)
#     return 1
# arr = []
# for i in range(6):
#     arr.append(list(map(int,input().split())))
# c = 0

# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == 1:
#             c += island(arr,i,j)

# No of Trees
# def trees(l,i,j):
#     if i < 0 or j < 0 or i >= len(l) or j >= len(l[0]) or l[i][j] == 2 or l[i][j] == 0:
#         return 1
#     l[i][j] = 2
#     trees(l,i+1,j)
#     trees(l,i-1,j)
#     trees(l,i,j+1)
#     trees(l,i,j-1)
#     return 1

# arr = []
# for i in range(6):
#     arr.append(list(map(int,input().split())))
# c = 0
# trees(arr,i,j)
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == 1:
#             c += 1
# print(c)

# Frog Jump
k = int(input())
blocks = [list(map(int,input().split())) for i in range(4)]
n, m = list(map(int,input().split()))

def paths(i,j,k):
    if [i,j] in blocks:
        return 0
    if i == k and j == k:
        return 1
    if i == k and j != k:
        return paths(i,j + 1,k)
    if j == k and i != k:
        return paths(i + 1,j,k)
    
    return paths(i + 1,j,k) + paths(i,j + 1,k)
print(paths(n,m,k))