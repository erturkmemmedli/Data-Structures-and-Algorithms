class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [i for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
            x =  self.parent[x]
        return x

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        elif root_a < root_b:
            self.parent[root_a] = root_b
            self.rank[root_b] += self.rank[root_a]
            return True
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += self.rank[root_b]
            return True
