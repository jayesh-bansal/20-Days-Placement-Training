# all binary numbers from 0 to n using recursion
# import math
# n = int(input())
# def binary(n,length,k):
#     if n == -1:
#         return n
#     if len(k) == length: # reaching the required length for given n
#         print(k)
#         n -= 1 # subtracting k after printing the possible binary number
#         return n
#     n = binary(n,length,k + '0') # adding the string with 0 bit
#     n = binary(n,length,k + '1') # adding the string with 1 bit
#     return n
# binary(n,int(math.log(n,2))+1,"")

# reverse using recursion
# def rev(n,re):
#     if n == 0:
#         return re
#     return rev(n//10,re * 10 + n % 10) # updating in the parameters
# n = 153
# print(rev(n,0))

# even sum using recursion
# def even_sum(x,i):
#     if i == len(x): # base condtion
#         return 0
#     if x[i] % 2 == 0: # even condtion check
#         return x[i] + even_sum(x,i + 1) # add and recursive even
#     else:
#         return even_sum(x,i + 1) # just returning if not even
# z = [2,5,6,7,2,1,4,3,6]
# print(even_sum(z,0))

# count of prime numbers in a single function
# def prime(a,i,t,c):
#     if i == len(a): # reached the end of the array
#         return c
#     if a[i] == 2: # exception of prime number 2 incrementing
#         return prime(a,i+1,2,c+1)
#     if a[i] % t == 0: # checking if a number is prime or not
#         return prime(a,i+1,2,c)
#     if t == a[i]//2 + 1: # exiting if the number is prime and incrementing count
#         return prime(a,i+1,2,c+1)
#     return prime(a,i,t+1,c) # increasing dividing value to see it the number is prime or not
# print(prime([2,5,6,7,2,12,4,3,6],0,2,0))

# check if a number reaches 1 by subtracting 3 and 5 (count,paths)
# (possible wrong code)
# def check(n,c,l):
#     if n < 1:
#         # return -1
#         return []
#     if n == 1:
#         # return c
#         return l
#     # return max(check(n-5,c+1,l + [5]), check(n-3,c+1,l + [3]))
#     return (check(n-5,c+1,l + [5]) or check(n-3,c+1,l + [3]))

# def check(n,c,l):
#     if n < 1:
#         return -1
#     if n % 3 == 1: # if number remainder is 1 then subtract everytime with 3
# #         return c + n//3
#         return l + [3] * (n//3)
#     if n % 5 == 1: # if number remainder is 1 then subtract everytime with 3
# #         return c + n//5
#         return l + [5] * (n//5)
#     return check(n-3, c + 1,l + [3]) or check(n-5, c + 1,l + [5]) # check both possibility

# print(check(int(input()),0,[]))

# Generate Parenthesis
# res = []
# def paren(n,left,right,s):
#     if len(s) == 2 * n: # len is equal to both open and close bracket
#         res.append(s)
#         return
#     if left < n: # all count of open
#         paren(n,left + 1,right,s + '(')
#     if left > right: # open > closing
#         paren(n,left,right + 1,s + ')')
# paren(int(input()),0,0,"")
# print(res)