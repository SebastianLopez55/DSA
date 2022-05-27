class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next 

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top # New node is going to point where top is pointing to 
            self.top = new_node
        self.height += 1

print('\n')

my_stack = Stack(4)
my_stack.push(1)
my_stack.print_stack()

        