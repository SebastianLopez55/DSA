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
        self.length +=1
        return True 

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
  

my_doubly_linked_list = DoublyLinkedList(7)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()




