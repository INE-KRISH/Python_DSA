class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        
        new_node.next = self.head
        
        self.head = new_node
        
    def search(self, li, key):
        if(not li):
            return False
        
        if(li.data == key):
            return True
        
        return self.search(li.next, key)
    
if __name__ == '__main__':
    
    li = LinkedList()
    
    li.push(10)
    li.push(30)
    li.push(11)
    li.push(21)
    li.push(14)
    
    x = int(input('Enter the number to be searched:'))
    
    if li.search(li.head, x):
        print('Yes')
        
    else:
        print('No')
        
        
        
    