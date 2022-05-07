from unittest import result


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
        #To access the parent node (root) across the branches. TO TRAVERSE THROUGH THE TREE
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

    def contains(self, value):
        # Variable temp to iterate through the loop
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right 
            else:
                return True 
        return False

    #Searching algos:

    def breadth_first_search(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results 

    def deepth_BS_pre_order(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def deepth_BS_post_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    def deepth_BS_in_order(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)

if my_tree.contains(47):
    print("Success!")

print(f'\nOutput using BFS: {my_tree.breadth_first_search()}')
print(f'\nOutput using DFS pre_order: {my_tree.deepth_BS_pre_order()}')
print(f'\nOutput using DFS post_order: {my_tree.deepth_BS_in_order()}')
print(f'\nOutput using DFS in_order: {my_tree.deepth_BS_in_order()}')