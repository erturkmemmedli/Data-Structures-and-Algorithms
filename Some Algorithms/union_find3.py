class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
        
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
