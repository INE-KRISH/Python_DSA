class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
        
#create root
root = Node(1)

'''
following is the tree after above statement

    1
   / \ 
None None
'''

root.left = Node(2);
root.right = Node(3);

'''
2 and 3 become left and right chidern of 1

    1                        N = Node
   / \ 
  2   3
 / \ / \ 
N  N N  N
'''

root.left.left = Node(4);
'''
        1                   N = Node
       / \ 
      2   3  
     / \ / \ 
    4  N N  N  
'''