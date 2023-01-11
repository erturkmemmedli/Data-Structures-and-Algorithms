class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += 1
            i += i & -i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & -i
        return r

# hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}
# tree = BinaryIndexedTree(len(hashTable))
