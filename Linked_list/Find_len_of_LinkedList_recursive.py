class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def getCountRec(self, node):
        if(not node):
            return 0
        else:
            return 1+ self.getCountRec(node.next)
        
    def getCount(self):
        return self.getCountRec(self.head)
    
if __name__ =='__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    
    print('Count of node is :', llist.getCount())
    
    
#Time complexity : O(N)
#Auxiliary Space : O(N)

 