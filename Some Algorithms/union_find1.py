class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n+1)
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] == -1:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        elif root_a < root_b:
            self.parent[root_a] = root_b
            self.rank[root_b] += 1
            return True
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
            return True
