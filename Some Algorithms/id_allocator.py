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

        idAlloc.isAllocated( 5 ); false
    }
'''
