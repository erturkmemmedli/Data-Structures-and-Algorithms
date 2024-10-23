from typing import Union, List, Optional


class SegmentTreeNode:
    def __init__(self, start: int, end: int, val: int = None, left: int = None, right: int = None) -> None:
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right
        
    
class SegmentTree:
    def __init__(self, array: List[int], op: Union[min, max, sum]) -> Optional[SegmentTreeNode]:
        assert op in [min, max, sum]
        
        self.op = op
        self.base_val = -float('inf') if op == max else float('inf') if op == min else 0
        
        def build_tree(array: List[int], left: int, right: int) -> Optional[SegmentTreeNode]:
            if left > right:
                return
            
            if left == right:
                node = SegmentTreeNode(left, right, array[left])
                return node
                
            mid = (left + right) // 2
            root = SegmentTreeNode(left, right, self.base_val)
            root.left = build_tree(array, left, mid)
            root.right = build_tree(array, mid + 1, right)
            root.val = self.op([root.left.val, root.right.val])
            return root 

        self.root = build_tree(array, 0, len(array) - 1)
        
       
    def update(self, idx: int, val: int) -> int:
        def update_tree(root: Optional[SegmentTreeNode], idx: int, val: int) -> int:
            if root.start == root.end:
                root.val = val
                return val
            
            mid = (root.start + root.end) // 2
            
            if idx <= mid:
                update_tree(root.left, idx, val)
            else:
                update_tree(root.right, idx, val)
            
            root.val = self.op([root.left.val, root.right.val])
            return root.val
        
        return update_tree(self.root, idx, val)
        
    def query(self, start: int, end: int) -> int:
        def query_tree(root: Optional[SegmentTreeNode], start: int, end: int) -> int:
            if root.start == start and root.end == end:
                return root.val
            
            mid = (root.start + root.end) // 2
            
            if end <= mid:
                return query_tree(root.left, start, end)
            elif start >= mid + 1:
                return query_tree(root.right, start, end)
            else:
                return self.op([query_tree(root.left, start, mid), query_tree(root.right, mid + 1, end)])
            
        return query_tree(self.root, start, end)


if __name__ == '__main__':
    arr = [5,2,6,8,5,12,6,1,2,3,7]
    min_seg_tree = SegmentTree(arr, min)
    min_seg_tree.update(5, 7)
    print("Minimum in range [1,4]: ", min_seg_tree.query(1,4))
    
    max_seg_tree = SegmentTree(arr, max)
    max_seg_tree.update(3, 31)
    print("Maximum in range [4,7]: ", max_seg_tree.query(4,7))

    sum_seg_tree = SegmentTree(arr, sum)
    sum_seg_tree.update(2, 1)
    print("Maximum of range [1,6]: ", sum_seg_tree.query(1,6))
