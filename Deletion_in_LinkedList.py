class Node:
    def __init__(self,data):
        self.data  = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    
    
    #deletion in linked list from the beginning
    
    def del_first(self):
        temp = self.head
        self.head = self.head.next
        del(temp)   
        
    def del_end(self):
        if not self.head:
            print("The linked list is empty.")
            return

        if not self.head.next:
            # If there is only one node in the list, set the head to None
            self.head = None
            return

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node.next = None
         


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    
    llist.head.next = second ;
    second.next = third ;
    third.next = fourth ;
    
    #llist.printList()
    
    #llist.del_first()
    #llist.printList()
    
    llist.del_end()
    llist.printList()