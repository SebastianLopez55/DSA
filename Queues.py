from numpy import MAY_SHARE_BOUNDS


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first 
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def en_queue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
           self.last.next = new_node
           self.last = new_node
        self.length += 1
    

my_queue = Queue(0)
my_queue.en_queue(1)
my_queue.en_queue(2)

my_queue.print_queue()
