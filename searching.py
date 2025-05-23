# search in a 2d matrix
# arr = [list(map(int,input().split())) for i in range(int(input()))]
# k = int(input())
# flag = True
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == k: # linear search
#             flag = False
#             print(f"Found the element at {i+1}th row and {j+1}th column")
#             break
#     if not flag:
#         break
# else:
#     print("Element Not Found")

# finding an element in a sorted array
# arr = [list(map(int,input().split())) for i in range(int(input()))]
# k = int(input())
# l = 0
# r = len(arr) * len(arr[0])
# while l <= r:
#     m = (l + r) // 2
#     if arr[min(m//len(arr[0]),len(arr)-1)][min(m%len(arr[0]),len(arr[0])-1)] == k: # directly sorting and finding index by dividing with rows
#         print(f"Found the element at {m//len(arr)+1}th row and {m%len(arr)+1}th column")
#         break
#     elif arr[min(m//len(arr[0]),len(arr)-1)][min(m%len(arr[0]),len(arr[0])-1)] > k:
#         r = m - 1
#     else:
#         l = m + 1
# else:
#     print("Element Not Found")

# 2 pointer sum
arr = list(map(int,input().split()))
k = int(input())
arr.sort()
i = 0
j = len(arr) - 1
while i < j:
    if arr[i] + arr[j] > k: # sum greater, we are reducing
        j -= 1
    elif arr[i] + arr[j] < k: # sum less, we are increasing
        i += 1
    else:
        print(f"At Index {i} and Index {j}, Sum is equal to Target")
        break
else:
    print("Target Sum Not Possible")