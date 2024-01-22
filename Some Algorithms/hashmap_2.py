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
