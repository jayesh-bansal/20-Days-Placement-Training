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

arr = list(map(int,input().split()))
root = None
for i in arr:
    root = bstadd(root,Node(i)) 
