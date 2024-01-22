class MyHashMap(object):
    def __init__(self):
        self.size = 1024
        self.num_of_keys = 0
        self.max_load_factor = 0.75
        self.hash_table = [[] for _ in range(self.size)]

    def hash_func(self, key):
        return 31 * key % self.size

    def put(self, key, value):
        hash_value = self.hash_func(key)
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.hash_table[hash_value][i][1] = value
                return
        self.hash_table[hash_value].append([key, value])
        self.num_of_keys += 1
        self.rehash()

    def get(self, key):
        hash_value = self.hash_func(key)
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                return self.hash_table[hash_value][i][1]
        return -1

    def remove(self, key):
        hash_value = self.hash_func(key)
        for i in range(len(self.hash_table[hash_value])):
            if self.hash_table[hash_value][i][0] == key:
                self.hash_table[hash_value].pop(i)
                return

    def rehash(self):
        if self.num_of_keys / self.size > self.max_load_factor:
            temp = self.hash_table.copy()
            self.num_of_keys = 0
            self.size *= 2
            self.hash_table = [[] for _ in range(self.size)]
            for i in temp:
                for k, v in i:
                    self.put(k, v)
                    
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Alternative solution

class MyHashMap1(object):
    size = 20000
    prime = 19997 
    max_load_factor = 0.70

    def __init__(self):
        self.num_of_keys = 0
        self.table = [None] * self.size

    def hash_func(self, key):
        return key % self.size
    
    def double_hash(self, key):
        return self.prime - key % self.prime

    def put(self, key, value):
        hash_val = self.hash_func(key)
        if self.table[hash_val] is None:
            self.table[hash_val] = (key, value)
            self.num_of_keys += 1
            #self.rehash(self.table)
            return
        i = 1
        while self.table[hash_val] is not None and self.table[hash_val] != -1:
            if self.table[hash_val][0] == key:
                self.table[hash_val] = (key, value)
                return
            hash_val += i * self.double_hash(key)
            hash_val = hash_val % self.size
            i += 1
        self.table[hash_val] = (key, value)
        self.num_of_keys += 1
        #self.rehash(self.table)

    def get(self, key):
        hash_val = self.hash_func(key)
        i = 1
        while self.table[hash_val] is not None:
            if self.table[hash_val] != -1 and self.table[hash_val][0] == key:
                return self.table[hash_val][1]
            hash_val += i * self.double_hash(key)
            hash_val = hash_val % self.size
            i += 1
        return -1

    def remove(self, key):
        hash_val = self.hash_func(key)
        i = 1
        while self.table[hash_val] is not None and self.table[hash_val] != -1:
            if self.table[hash_val][0] == key:
                self.table[hash_val] = -1
                return
            hash_val += i * self.double_hash(key)
            hash_val = hash_val % self.size
            i += 1
    
    def rehash(self, table):
        load_factor = self.num_of_keys / self.size
        if load_factor > self.max_load_factor:
            self.num_of_keys = 0
            temp = self.table
            self.size *= 2
            self.table = [None] * self.size
            for i in temp:
                if i != None or i != -1:
                    self.put(i[0], i[1])
