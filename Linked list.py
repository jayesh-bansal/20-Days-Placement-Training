class LinkedList:
    def __init__(self,value):
        self.data = value
        self.next = None

def addFirst(root,node):
    if not root:
        return node
    temp = root
    while temp.next:
        temp = temp.next
    temp.next = node
    return root

def sumevenindex(root):
    c = 1
    temp = root
    s = 0
    while temp:
        if c % 2 == 0:
            s += temp.data
        temp = temp.next
        c += 1
    return s

def find2largest(root):
    m1 = 0
    m2 = root
    temp = root.next
    while temp:
        if temp.data > m2.data:
            m1 = m2
            m2 = temp
    return m1.data

def consecutivepair(root,target):
    temp1 = root
    c = 0
    while temp1.next:
        if temp1.data + temp1.next.data == target:
            c += 1
        temp1 = temp1.next
    return c

def allsumpair(root,target):
    temp1 = root
    temp2 = root.next
    c = 0
    while True:
        if temp1.data + temp2.data < target:
            c += 1
        temp2 = temp2.next
        if not temp2:
            temp1 = temp1.next
            if not temp1.next:
                break
            temp2 = temp1.next
    return c

def secondhalf(root):
    temp1 = root
    temp2 = root
    while temp2:
        temp1 = temp1.next
        temp2 = temp2.next.next
    while temp1:
        print(temp1.data)
        temp1 = temp1.next

def kthlastnode(root,k):
    temp = root
    for i in range(k):
        temp = temp.next
    temp1 = root
    while temp:
        temp = temp.next
        temp1 = temp1.next
    return temp1.data

def deletekthlastnode(root,k):
    temp = root
    for i in range(k):
        temp = temp.next
    temp1 = root
    temp1 = temp1.next
    while temp:
        temp = temp.next
        temp1 = temp1.next
    temp.next = temp.next.next
    return root

def swapconsecutive(root):
    temp = root
    while temp and temp.next:
        temp.data,temp.next.data = temp.next.data,temp.data
        temp = temp.next.next
    return root

def bubblesort(root):
    temp = root
    temp2 = root
    flag = False
    while temp2:
        if not temp or not temp.next:
            if flag:
                break
            temp = root
            temp2 = temp2.next
            flag = False
        if temp.data > temp.next.data:
            flag = True
            temp.data,temp.next.data = temp.next.data,temp.data
        temp = temp.next

    return root

def countcyclicnodes(root):
    temp1 = root
    temp2 = root
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next.next
    temp1 = temp1.next
    c = 1
    while temp1 != temp2:
        c += 1
        temp1 = temp1.next
    return c

def flattencyclicnodes(root):
    temp1 = root
    temp2 = root
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next.next
    temp1 = root
    while temp1 != temp2:
        temp1 = temp1.next
        prev = temp2
        temp2 = temp2.next
    prev.next = None
    return root

def reverse(root):
    temp = root
    while temp.next:
        temp = temp.next
    end = temp
    while end != root:
        temp2 = root.next
        temp.next = root
        root = temp2
    return end

def palindrome(root):
    head1 = root
    head2 = root
    while head1 and head2:
        head1 = head1.next
        head2 = head2.next.next
    prev = None
    temp = head1
    while head1:
        nextnode = head1.next
        head1.next = prev
        prev = head1
        head1 = nextnode
    head1 = temp
    head2 = root
    while head1 and head2:
        if head1.data != head2.data:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

def addtwonumbers(root1,root2):
    temp1 = root1
    temp2 = root2
    c = 0
    s = 0
    while temp1 and temp2:
        c = (temp1.data+temp2.data+c)//10
        s = (temp1.data+temp2.data+c)%10
        temp1 = temp1.next
        temp2 = temp2.next
    
    while temp1:
        c = (temp1.data+c)//10
        s = (temp1.data+c)%10
        temp1 = temp1.next

    while temp2:
        c = (temp2.data+c)//10
        s = (temp2.data+c)%10
        temp2 = temp2.next

    return s

arr = list(map(int,input().split()))
root = None
for i in arr:
    root = addFirst(root,LinkedList(i))
root = bubblesort(root)
temp = root
while temp:
    print(temp.data, end = ' ')
    temp = temp.next