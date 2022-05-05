from tempfile import tempdir

#This class acts as a dictionary. Stores the values and pointer of the Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True 
             
    def pop(self, value):
        if self.head ==0:
            return None
        temp = self.head 
        pre = self.head 
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp 

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # New node is pointing where Head was pointing to.
            new_node.next = self.head
            #Head is pointing to the new_node
            self.head = new_node
        self.length +=1
        return True 
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail  = None
        return temp
    
    def get(self,index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.prepend(0)
my_linked_list.pop_first()
index = 2
print(f"\nValue at index {index}:", my_linked_list.get(index))

my_linked_list.print_list()


