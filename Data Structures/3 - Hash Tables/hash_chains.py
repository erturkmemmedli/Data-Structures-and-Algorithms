class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push_front(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
        if self.tail == None:
            self.tail = self.head
    
    def pop_front(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next
        if self.head == None:
            self.tail = self.head
    
    def find_key(self, key):
        temp = self.head
        while(temp != None and temp.key != key):
            temp = temp.next
        if self.head == None or temp == None:
            print('no')
        else:
            print('yes')          

    def delete_key(self, key):
        temp = self.head
        if temp == None:
            return
        elif temp.key == key:
            self.pop_front()
        else:
            while(temp.next != None and temp.next.key != key):
                temp = temp.next
            if temp.next == None and temp.key != key:
                return
            else:
                if temp.next.next != None:
                    temp.next = temp.next.next
                else:
                    self.tail = temp
                    temp.next = None
    
    def print_linked_list(self):
        temp = self.head
        if temp == None:
            print()
        while(temp != None):
            if temp != self.tail:
                print(temp.key, end = ' ')
            else:
                print(temp.key)
            temp = temp.next
        
class HashChainTable:
    multiplier = 263
    prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.hash_table = [None] * self.bucket_count
        for i in range(self.bucket_count) :
            self.hash_table[i] = LinkedList()
        
    def hash_func(self, string):
        hash_value = 0
        for i in range(len(string)):
            hash_value = (hash_value + ord(string[i]) * (self.multiplier ** i)) % self.prime
        return hash_value % self.bucket_count
    
    def insert(self, string):
        index = self.hash_func(string)
        self.hash_table[index].push_front(string)

    def find(self, string):
        index = self.hash_func(string)
        self.hash_table[index].find_key(string)
        
    def delete(self, string):
        index = self.hash_func(string)
        self.hash_table[index].delete_key(string)
                
    def print_chain(self, index):
        self.hash_table[index].print_linked_list()

if __name__ == '__main__':
    bucket_count = int(input())
    chain = HashChainTable(bucket_count)
    elements = []
    query_count = int(input())
    for i in range(query_count):
        query = input().split()
        if query[0] == 'add':
            if query[1] not in elements:
                chain.insert(query[1])
                elements.append(query[1])
        elif query[0] == 'del':
            if query[1] in elements:
                chain.delete(query[1])
                elements.remove(query[1])
        elif query[0] == 'find':
            chain.find(query[1])
        elif query[0] == 'check':
            chain.print_chain(int(query[1]))
        else:
            assert(0)
