class Node():
    
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None   

class MaxStack():
            
    def __init__(self):
        self.head_stack = None
        self.tail_stack = None
        
        self.head_queue = None
        self.tail_queue = None

    def push(self, key):
        node_stack = Node(key)      
        
        node_stack.next = self.head_stack
        node_stack.prev = None

        if self.head_stack == None:
            self.head_stack = node_stack
            self.tail_stack = node_stack
            
        else:
            node_stack.next = self.head_stack
            self.head_stack = node_stack
        
        node_queue = Node(key)
        
        if self.head_queue == None:
            self.head_queue = node_queue
            self.tail_queue = node_queue
            node_queue.next = None
            node_queue.prev = None    
            
        else:
            temp = self.head_queue
            
            while temp != None and temp.key > node_queue.key:
                temp = temp.next   
                
            if temp != None:
                if temp == self.head_queue:
                    node_queue.next = temp
                    temp.prev = node_queue
                    self.head_queue = node_queue
                    node_queue.prev = None
                    
                else:
                    node_queue.prev = temp.prev.next
                    temp.prev.next = node_queue
                    node_queue.next = temp
                    temp.prev = node_queue
                    
            else:
                node_queue.prev = self.tail_queue
                self.tail_queue.next = node_queue
                self.tail_queue = node_queue
                node_queue.next = None          
    
    def pop(self):
        popped = self.head_stack
        
        if self.head_stack == self.tail_stack:
            self.head_stack = None
            self.tail_stack = None
            
        else:
            self.head_stack = self.head_stack.next
            self.head_stack.prev = None
        
        if self.head_queue == self.tail_queue:
            self.head_queue = None
            self.tail_queue = None
            
        else:
            temp = self.head_queue
            
            while temp != None and temp.key != popped.key:
                temp = temp.next
                
            if temp == self.head_queue:
                self.head_queue = self.head_queue.next
                self.head_queue.prev = None
                
            elif temp == self.tail_queue:
                self.tail_queue = self.tail_queue.prev
                self.tail_queue.next = None
                   
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
            
    def maximum(self):
        print(self.head_queue.key, end = '\n')
        
    def test_print(self):
        temp1 = self.head_stack
        if temp1 == None:
            print('Empty')
        while temp1 != None:
            print(temp1.key, end = ' ')
            temp1 = temp1.next
        print('\n')
        
        temp2 = self.head_queue
        if temp2 == None:
            print('Empty')
        while temp2 != None:
            print(temp2.key, end = ' ')
            temp2 = temp2.next
        print('\n')

if __name__ == '__main__':
    stack = MaxStack()
    n = int(input())
    for i in range(n):
        query = input().split()
        if query[0] == 'push':
            stack.push(query[1])
        elif query[0] == 'pop':
            stack.pop()
        elif query[0] == 'max':
            stack.maximum()
        else:
            assert(0)