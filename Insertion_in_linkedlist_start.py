from Linked_list import Node


def push(self, new_data):
    
    new_node = Node(new_data)
    
    new_node.next = self.head
    
    self.head = new_node
    
'''
Import error 
'''