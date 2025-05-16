# generate Parenthesis
res = []
def paren(n,left,right,s):
    if len(s) == 2 * n:
        res.append(s)
        return
    if left < n:
        paren(n,left + 1,right,s + '(')
    if left > right:
        paren(n,left,right + 1,s + ')')
paren(int(input()),0,0,"")
print(res)