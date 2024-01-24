import math
from typing import List, Callable, Union


class SegmentTree:
    def __init__(self, array: List[int]) -> None:
        self.array = array
        self.length = len(array)
        self.segment_length = 2 * 2 ** math.ceil(math.sqrt(self.length)) - 1
        self.segment_tree = [math.inf for _ in range(self.segment_length)]
        
    def build_segment_tree(self, low: int = 0, high: int = None, pos: int = 0, op: Callable = None) -> None:
        if high == None:
            high = self.length - 1

        if low == high:
            self.segment_tree[pos] = self.array[low]
            return

        mid = low + (high - low) // 2
        self.build_segment_tree(low, mid, pos * 2 + 1, op)
        self.build_segment_tree(mid + 1, high, pos * 2 + 2, op)

        self.segment_tree[pos] = op([self.segment_tree[pos * 2 + 1], self.segment_tree[pos * 2 + 2]])   
        
    def range_query(self, left, right, low = 0, high = None, pos = 0, op: Callable = None, factor: float = None) -> Union[int, float]:
        if high == None:
            high = self.length - 1
        
        if low >= left and high <= right: # total overlap
            return self.segment_tree[pos]
        if high < left or low > right: # no overlap
            return factor
        
        mid = low + (high - low) // 2
        l = self.range_query(left, right, low, mid, pos * 2 + 1, op, factor)
        r = self.range_query(left, right, mid + 1, high, pos * 2 + 2, op, factor)
        
        return op([l, r])
      
    
class SegmentTreeMinimum(SegmentTree):
    def build_segment_tree(self, low = 0, high = None, pos = 0, op = None) -> None:
        super().build_segment_tree(low, high, pos, min)

    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, min, math.inf)


class SegmentTreeMaximum(SegmentTree):
    def build_segment_tree(self, low = 0, high = None, pos = 0, op = None) -> None:
        super().build_segment_tree(low, high, pos, max)

    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, max, -math.inf)
      
    
class SegmentTreeSum(SegmentTree):
    def build_segment_tree(self, low = 0, high = None, pos = 0, op = None) -> None:
        super().build_segment_tree(low, high, pos, sum)

    def range_query(self, left, right, low = 0, high = None, pos = 0, op = None, factor = None):
        return super().range_query(left, right, low, high, pos, sum, 0)


# arr = [0, 2, 4, -1, 8, -3, 1, 5]

# s = SegmentTreeMinimum(arr)
# s.build_segment_tree()
# print(s.segment_tree)
# print(s.range_query(0, 4))

# t = SegmentTreeMaximum(arr)
# t.build_segment_tree()
# print(t.segment_tree)
# print(t.range_query(1, 7))

# z = SegmentTreeSum(arr)
# z.build_segment_tree()
# print(z.segment_tree)
# print(z.range_query(0, 3))
