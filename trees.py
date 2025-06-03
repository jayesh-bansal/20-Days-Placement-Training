class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def bstadd(root,node):
    if not root:
        return node
    if root.data > node.data:
        root.left = bstadd(root.left,node)
    else:
        root.right = bstadd(root.right,node)
    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end = ' ')
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.data,end = ' ')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end = ' ')

# parameteried
def sumall(root,s):
    if not root:
        return s
    s = s + root.data
    s = sumall(root.left,s)
    s = sumall(root.right,s)
    return s

# function call
# def sumall(root):
#     if not root:
#         return 0
#     return root.data + sumall(root.left) + sumall(root.right)

def sumeven(root):
    if not root:
        return 0
    if root.data % 2 == 0:
        k = root.data
    else:
        k = 0
    return k + sumeven(root.left) + sumeven(root.right)

# parameterised
def height(root,m):
    if not root:
        return m
    return max(height(root.left,m+1),height(root.right,m+1))

# function call
def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right)) + 1

def searching(root,target):
    if not root:
        return -1
    if root.data == target:
        return root
    if root.data > target:
        return searching(root.left,target)
    else:
        return searching(root.right,target)

def countleafnode(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return countleafnode(root.left) + countleafnode(root.right)

def paths(root,l):
    if not root:
        return []
    if not root.left and not root.right:
        return [l + [root.data]] 
    return paths(root.left,l+[root.data]) + paths(root.right,l+[root.data])

def levelorder(root):
    if not root:
        return
    q = [root]
    k = []
    while q:
        l = []
        n = len(q)
        for i in range(n):
            item = q.pop(0)
            l.append(item.data)
            if item.left:
                q.append(item.left)
            if item.right:
                q.append(item.right)
        k.append(l)

def verticalorder(root):
    if not root:
        return
    q = [[root,0]]
    d = {}
    while q:
        n = len(q)
        for i in range(n):
            item = q.pop(0)

            if item[1] not in d:
                d[item[1]] = [item[0].data]
            else:
                d[item[1]] += [item[0].data]
            if item[0].left:
                q.append([item[0].left,item[1]-1])
            if item[0].right:
                q.append([item[0].right,item[1]+1])

def topview(root):
    if not root:
        return
    q = [[root,0]]
    d = {}
    while q:
        n = len(q)
        for i in range(n):
            item = q.pop(0)
            if item[1] not in d:
                d[item[1]] = item[0].data
            if item[0].left:
                q.append([item[0].left,item[1]-1])
            if item[0].right:
                q.append([item[0].right,item[1]+1])

def bottomview(root):
    if not root:
        return
    q = [[root,0]]
    d = {}
    while q:
        n = len(q)
        for i in range(n):
            item = q.pop(0)
            d[item[1]] = item[0].data
            if item[0].left:
                q.append([item[0].left,item[1]-1])
            if item[0].right:
                q.append([item[0].right,item[1]+1])

def leftview(root):
    if not root:
        return
    q = [root]
    l = []
    while q:
        n = len(q)
        for i in range(n):
            item = q.pop(0)
            if i == 0:
                l.append(item.data)
            if item[0].left:
                q.append(item.left)
            if item[0].right:
                q.append(item.right)

def rightview(root):
    if not root:
        return
    q = [root]
    l = []
    while q:
        n = len(q)
        for i in range(n):
            item = q.pop(0)
            if i == n-1:
                l.append(item.data)
            if item[0].left:
                q.append(item.left)
            if item[0].right:
                q.append(item.right)

def topviewrecur(root,d,c):
    if root:
        return
    if c not in d:
        d[c] = root.data
    topviewrecur(root.left,d,c+1)
    topviewrecur(root.right,d,c-1)

def bottomviewrecur(root,d,c):
    if root:
        return
    d[c] = root.data
    topviewrecur(root.left,d,c+1)
    topviewrecur(root.right,d,c-1)

def leftviewrecur(root,d,c):
    if root:
        return
    if c not in d:
        d[c] = root.data
    leftviewrecur(root.left,d,c+1)
    leftviewrecur(root.right,d,c+1)

def rightviewrecur(root,d,c):
    if root:
        return
    d[c] = root.data
    rightviewrecur(root.left,d,c+1)
    rightviewrecur(root.right,d,c+1)

def lsa(root,a,b):
    if root.data >= a and root.data <= b:
        return root.data
    if root.data <= a:
        return lsa(root.right,a,b)
    return lsa(root.left,a,b)

def balanced(root,c):
    if not root:
        return True
    if -1 < c > 1:
        return False
    if root.left:
        if root.right:
            return balanced(root.left,c) and balanced(root.right,c)
        else:
            return balanced(root.left,c-1)
    else:
        if root.right:
            return balanced(root.right,c+1)
    
arr = list(map(int,input().split()))
root = None
for i in arr:
    root = bstadd(root,Node(i)) 
print(balanced(root,0))