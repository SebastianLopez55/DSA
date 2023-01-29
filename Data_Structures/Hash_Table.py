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

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None 


    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data[i][j][0])
        return all_keys            


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('\n')

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))

print('\n')

my_hash_table.print_table()

