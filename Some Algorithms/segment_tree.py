import math
from typing import List, Callable, Union


class SegmentTree:
    def __init__(self, array: List[int]) -> None:
        self.array = array
        self.length = len(array)
        self.segment_length = 2 * 2 ** math.ceil(math.sqrt(self.length)) - 1
        self.segment_tree = [math.inf] * self.segment_length
        self.lazy = [0] * self.segment_length
        
    def build(self, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        if high == None:
            high = self.length - 1

        if low == high:
            self.segment_tree[pos] = self.array[low]
            return

        mid = low + (high - low) // 2
        
        self.build(low, mid, pos * 2 + 1, op)
        self.build(mid + 1, high, pos * 2 + 2, op)

        self.segment_tree[pos] = op([self.segment_tree[pos * 2 + 1], self.segment_tree[pos * 2 + 2]])
        
    def update(self, left: int, right: int, delta: int, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        if high == None:
            high = self.length - 1
            
        if self.lazy[pos] != 0:
            self.segment_tree[pos] += self.lazy[pos]
            if low != high:
                self.lazy[pos * 2 + 1]  += self.lazy[pos]
                self.lazy[pos * 2 + 2] += self.lazy[pos]
            self.lazy[pos] = 0
            
        if low >= left and high <= right: # total overlap
            self.segment_tree[pos] += delta
            if low != high:
                self.lazy[pos * 2 + 1]  += self.lazy[pos]
                self.lazy[pos * 2 + 2] += self.lazy[pos]
            return
        
        if high < left or low > right: # no overlap
            return
        
        mid = low + (high - low) // 2
        
        self.update(left, right, delta, low, mid, pos * 2 + 1, op)
        self.update(left, right, delta, mid + 1, high, pos * 2 + 2, op)

        self.segment_tree[pos] = op([self.segment_tree[pos * 2 + 1], self.segment_tree[pos * 2 + 2]])
        
        
    def range_query(self, left: int, right: int, low: int = 0, high: int = None, pos: int = 0, op: Callable = None, factor: float = None) -> Union[int, float]:
        if high == None:
            high = self.length - 1

        if self.lazy[pos] != 0:
            self.segment_tree[pos] += self.lazy[pos]
            if low != high:
                self.lazy[pos * 2 + 1]  += self.lazy[pos]
                self.lazy[pos * 2 + 2] += self.lazy[pos]
            self.lazy[pos] = 0
        
        if low >= left and high <= right: # total overlap
            return self.segment_tree[pos]
        
        if high < left or low > right: # no overlap
            return factor
        
        mid = low + (high - low) // 2
        
        l = self.range_query(left, right, low, mid, pos * 2 + 1, op, factor)
        r = self.range_query(left, right, mid + 1, high, pos * 2 + 2, op, factor)
        
        return op([l, r])
      
    
class SegmentTreeMinimum(SegmentTree):
    def build(self, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().build(low, high, pos, min)
    
    def update(self, left: int, right: int, delta: int, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().update(left, right, delta, low, high, pos, min)
        
    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, min, math.inf)


class SegmentTreeMaximum(SegmentTree):
    def build(self, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().build(low, high, pos, max)
    
    def update(self, left: int, right: int, delta: int, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().update(left, right, delta, low, high, pos, max)
        
    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, max, -math.inf)
      
    
class SegmentTreeSum(SegmentTree):
    def build(self, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().build(low, high, pos, sum)
    
    def update(self, left: int, right: int, delta: int, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        super().update(left, right, delta, low, high, pos, sum)
        
    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, sum, 0)


arr = [0, 2, 4, -1, 8, -3, 1, 5]

s = SegmentTreeMinimum(arr)
s.build()
print(s.segment_tree)
print(s.range_query(0, 4))

t = SegmentTreeMaximum(arr)
t.build()
print(t.segment_tree)
print(t.range_query(1, 7))

z = SegmentTreeSum(arr)
z.build()
print(z.segment_tree)
print(z.range_query(0, 3))
