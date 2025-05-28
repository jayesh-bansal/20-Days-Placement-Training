# evaluate an expression
# value = input().split(',')
# l = []
# for i in value:
#     if i.isdigit():
#         l.append(float(i))
#     else:
#         if i == '+':
#             l.append(l.pop()+l.pop())
#         if i == '*':
#             l.append(l.pop()*l.pop())
#         if i == '**':
#             a = l.pop()
#             b = l.pop()
#             l.append(b**a)
#         if i == '-':
#             a = l.pop()
#             b = l.pop()
#             l.append(b-a)
#         if i == '/':
#             a = l.pop()
#             b = l.pop()
#             l.append(b/a)
# print(l.pop())

# balance parenthesis
# value = input()
# l = []
# for i in value:
#     if i == ")":
#         if '(' != l.pop():
#             print("False")
#             break
#     elif i == '}':
#         if '{' != l.pop():
#             print("False")
#             break
#     else:
#         l.append(i)
# else:
#     if len(l) != 0:
#         print("False")
#     else:
#         print("True")

# higher element in right in arr2
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
# O(n*m)
# l = []
# for i in arr1:
#     j = len(arr2) - 1
#     k = -1
#     while arr2[j] != i:
#         if arr2[j] > i:
#             k = arr2[j]
#         j -= 1
#     l.append(k)
# print(l)
# O(n+m)
l = []
d = {}
for i in arr2:
    while l and l[-1] < i:
        d[l.pop()] = i
    l.append(i)
while l:
    d[l.pop()] = -1
for i in arr1:
    l.append(d[i])
print(l)