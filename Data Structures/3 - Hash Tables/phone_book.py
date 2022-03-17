class HashTable():
    size = 10000001
    prime = 9999991
    max_load_factor = 0.75
    
    def __init__(self):
        self.num_of_keys = 0
        self.table = [None] * self.size
         
    def hashing(self, key):
        return key % self.size
    
    def double_hashing(self, key):
        return self.prime - key % self.prime
    
    def insert(self, key, value):
        self.num_of_keys += 1
        hashed_key = self.hashing(key)
        if self.table[hashed_key] == None:
            self.table[hashed_key] = (key, value)
            self.rehash(self.table)
            return
        i = 1
        while self.table[hashed_key] != None and self.table[hashed_key] != -1:
            if self.table[hashed_key][0] == key:
                self.table[hashed_key] = (key, value)
                return
            hashed_key += i * self.double_hashing(key)
            hashed_key = hashed_key % self.size
            i += 1 
        self.table[hashed_key] = (key, value)
        self.rehash(self.table)

    def find(self, key):
        hashed_key = self.hashing(key)
        i = 1
        while self.table[hashed_key] != None:
            if self.table[hashed_key] != -1 and self.table[hashed_key][0] == key:
                print(self.table[hashed_key][1])
                return
            hashed_key += i * self.double_hashing(key)
            hashed_key = hashed_key % self.size
            i += 1
        print('not found')
        return
        
    def delete(self, key):
        hashed_key = self.hashing(key)
        i = 1
        while self.table[hashed_key] != None and self.table[hashed_key] != -1:
            if self.table[hashed_key][0] == key:
                self.num_of_keys -= 1
                self.table[hashed_key] = -1
                return
            hashed_key += i * self.double_hashing(key)
            hashed_key = hashed_key % self.size
            i += 1
            
    def rehash(self, table):
        load_factor = self.num_of_keys / self.size
        if load_factor > self.max_load_factor:
            self.num_of_keys = 0
            temp = self.table
            self.size *= 2
            self.table = [None] * self.size
            for i in temp:
                if i != None and i != -1:
                    self.insert(i[0], i[1])
                
if __name__ == '__main__':
    phone_book = HashTable()
    n = int(input())
    for _ in range(n):
        query = input().split()
        if query[0] == 'add':
            phone_book.insert(int(query[1]), query[2])
        elif query[0] == 'del':
            phone_book.delete(int(query[1]))
        elif query[0] == 'find':
            phone_book.find(int(query[1]))
        else:
            assert(0)
