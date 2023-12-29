# Using O(N) Extra space
#using vector to store all node and then search in it.

class Node:
    def __init__(self,key):
        self.key = key
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_key):
        new_node = Node(new_key)
        new_node.next = self.head
        self.head = new_node
        
llist = LinkedList()

llist.push(10)
llist.push(30)
llist.push(11)
llist.push(21)
llist.push(14)

x = int(input("Enter element to be searched:"))

temp = llist.head

v = []

while(temp):
    v.append(temp.key)
    temp = temp.next
    
if x in v:
    print("YES")
else:
    print("NO")
    
    
#Time complexity: O(N), to travese the linked list.
#auxiliary Space: O(N), to store the values.