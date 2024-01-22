'''
To update tree, we need to update next element step-by-step. Procedure is as follows:
    1. Find 2's complement of index -> -idx
    2. AND it with original index -> idx & -idx
    3. Add them together to get next index -> idx + (idx & -idx)

To find sum until given index, we need to traverse toward root node. Procedure is as follows:
    1. Find 2's complement of index -> -idx
    2. AND it with original index -> idx & -idx
    3. Subtract them to find parent index -> idx - (idx & -idx)
'''

class BinaryIndexedTree(object):
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def sum(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result
    
    def update(self, idx, val):
        while idx < len(self.tree):
            self.tree[idx] += val
            idx += idx & -idx


# arr = [3,1,2,5,6,5,2,-3,4,8]
# bit = BinaryIndexedTree(len(arr))

# for i, val in enumerate(arr):
#     bit.update(i + 1, val)

# print(bit.tree)
# print(bit.sum(7))
