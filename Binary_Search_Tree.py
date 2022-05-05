class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        #If the tree is empty
        if self.root is None:
            self.root = new_node
            return True
        #To access the parent node (root) across the branches
        temp = self.root
        #To iterate over the branches 
        while True:
            #For identical values
            if new_node.value == temp.value:
                return False
            # less than we go left 
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True 
                temp = temp.left
            # greater than we go right 
            else:
                if temp.right is None:
                    temp.right  = new_node
                    return True 
                temp = temp.right     
        
        


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)




 