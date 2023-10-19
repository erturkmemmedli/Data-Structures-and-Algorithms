class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()

        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        item = self.array[self.size - 1]
        print(item)
        self.array[self.size - 1] = None
        self.size -= 1
        return item

    def resize(self) -> None:
        self.capacity *= 2
        self.new_array = [None] * self.capacity

        for i in range(len(self.array)):
            self.new_array[i] = self.get(i)
        
        self.array = self.new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
