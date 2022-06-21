from numpy import MAY_SHARE_BOUNDS

class HashTable: #Will built the list (Table)
    def __init__(self, size = 7):
        self.data_map = [None] * size
    
    def __hash(self, key):
        '''Returns the hash table index'''
        my_hash = 0
        for char in key:
            # Mode to fin in the hash table
            # Multiply by prime number 23 to reduce the chances of collisions?
            my_hash = (my_hash + ord(char) * 23) % len(self.data_map) 
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def print_table(self):
        '''Prints the values of the hash table'''
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
my_hash_table = HashTable()
my_hash_table.print_table()
