class Node:
    def __init__(self, value):
        self.value = value
        self.next = None #arrow pointing right
        self.prev = None #arrow pointing left
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # Pointing the tail of the last node added to the list to the "new_node"
            new_node.prev = self.tail # The pointer to the previous node "prev" will point where "tail" is pointing 
            self.tail = new_node
        self.length += 1
        return True 

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev # the previous relative to what tail was pointing 
            self.tail.next = None # Break the connection ->
            temp.prev = None # Break the connection <-
        self.length -= 1
        return temp

    def print_list(self): # Add the temp.value to check the value inside the nodes
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)
my_doubly_linked_list.pop()
my_doubly_linked_list.pop()
my_doubly_linked_list.pop()

my_doubly_linked_list.print_list()




