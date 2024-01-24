class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[node]

        return node

    def union(self, node_a, node_b):
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b

        if self.rank[root_a] == self.rank[root_b]:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
