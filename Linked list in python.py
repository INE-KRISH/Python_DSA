class node:
    def __init__(self,val):
        self.val = val
        self.next = None

head1, head2, result = None, None, None
carry = 0

def printlist(head):
    while head != None:
        print(head.val, end=" ")
        head = head.next
    
def push(val, lst):
    global head1, head2, result
    newnode = node(val)
    if lst == 1:
        newnode.next = head1
        head1 = newnode
    
    elif lst == 2:
        newnode.next = head2
        head2 = newnode
    else:
        newnode.next = result
        result = newnode
        
def addsamesize(n, m):
    global carry
    
    if n == None:
        return
    
    addsamesize(n.next, m.next)
    
    sum = n.val +m.val + carry
    carry = int(sum/10)
    sum = sum % 10
    
    push(sum , 3)
    
cur = None


def propagatecarry(head1):
    global carry, cur
    
    if head1 != cur:
        propagatecarry(head1.next)
        sum = carry + head1.val
        carry = int(sum / 10)
        sum %= 10
        
        push(sum, 3)
        
def getsize(head):
    count = 0
    while head!= None:
        count += 1
        head = head.next
    return count

def addlists():
    global head1, head2, result, carry, cur
    
    if head1 == None:
        result = head2
        return
    if head2 == None:
        result = head1
        return
    size1 = getsize(head1)
    size2 = getsize(head2)
    
    if size1 == size2:
        addsamesize(head1, head2)
        
    else:
        
        if size1 < size2:
            temp = head1
            head1 = head2
            head2 = temp
        diff = abs(size1 - size2)
        
        temp = head1
        while diff >= 0:
            cur = temp
            temp = temp.next
            diff -= 1
        
        addsamesize(cur, head2)
        
        propagatecarry(head1)
        
    if carry > 0:
        push(carry, 3)
        
head1, head2, result = None, None, None
carry = 0
arr1 = [9,9,9]
arr2 = [1,8]

for i in range(len(arr1)-1, -1, -1):
    push(arr1[i], 1)
    
    
for i in range(len(arr2)-1, -1, -1):
    push(arr2[i], 2)
    
addlists()
printlist(result)