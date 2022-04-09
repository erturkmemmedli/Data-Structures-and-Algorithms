import math

class Node:
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.rank = 0   

def MakeSet(i, x, y, nodes):
    nodes.append(Node(x[i], y[i], i))
    
def Find(i, nodes):
    if i != nodes[i].parent:
        nodes[i].parent = Find(nodes[i].parent, nodes)
    return nodes[i].parent

def Union(i, j, nodes):
    i_id = Find(i, nodes)
    j_id = Find(j, nodes)
    if i_id == j_id:
        return
    if nodes[i_id].rank > nodes[j_id].rank:
        nodes[j_id].parent = i_id
    else:
        nodes[i_id].parent = j_id
        if nodes[i_id].rank == nodes[j_id].rank:
            nodes[j_id].rank += 1
            
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def Kruskal(n, x, y, k):
    MST = []
    nodes = []
    for i in range(0, n):
        MakeSet(i, x, y, nodes)
    edges = []
    for i in range(0, n):
        for j in range(i + 1, n):
            weight = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append(Edge(i, j, weight))
    edges = sorted(edges, key = lambda e: e.weight)
    for edge in edges:
        if Find(edge.u, nodes) != Find(edge.v, nodes):
            MST.append(edge)
            Union(edge.u, edge.v, nodes)
    return MST[-(k-1)].weight

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        x.append(a)
        y.append(b)
    k = int(input())
    print("{0:.9f}".format(Kruskal(n, x, y, k)))