# Mock interview with Bahruz Abil (Microsoft)

'''
Id allocator. Capacity 0-N.
int Allocate() : returns avilable ID within 0-N range.
int Release(int ID) : releases given ID and that ID becomes available for allocation.
boolean isAllocated(int ID)

Client:
    run(){
        var idAlloc = new IdAllocator(100);

        int id1 = idAlloc.allocate(); // 0
        int id2 = idAlloc.allocate(); // 1

        idAlloc.isAllocated( 5 ); // false
    }
'''

# We assume release(id) call is always valid.

# Trade-Off 1: Checking whether ID is allocated Time: O(n); Space: O(1).
class IdAllocator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freeIDs = list(range(capacity))
        
    def allocate(self):
        return self.freeIDs.pop()
    
    def release(self, id):
        self.freeIDs.append(id) 
    
    def isAllocated(self, id):
        for num in self.freeIDs:
            if num == id: return True
        return False
    
# Trade-Off 2: Checking whether ID is allocated Time: O(1); Space: O(n).
class IdAllocator:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freeIDs = list(range(capacity))
        self.usedIDs = set()
        
    def allocate(self):
        allocated = self.freeIDs.pop()
        self.usedIDs.add(allocated)
        return allocated
    
    def release(self, id):
        self.usedIDs.remove(id)
        self.freeIDs.append(id)
    
    def isAllocated(self, id):
        return id in self.usedIDs
