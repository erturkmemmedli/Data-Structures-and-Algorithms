import math
import heapq

def Prim(n, adj, cost):
    price = [float('inf') for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    price[0] = 0
    H = [(price[0], 0)]
    heapq.heapify(H)
    while len(H) != 0:
        item = heapq.heappop(H)
        vertex = item[1]
        for i in range(n - 1):
            if visited[adj[vertex][i]] == False:
                if price[adj[vertex][i]] > cost[vertex][i]:
                    price[adj[vertex][i]] = cost[vertex][i]
                    parent[adj[vertex][i]] = vertex
                    heapq.heappush(H, (price[adj[vertex][i]], adj[vertex][i]))
        visited[vertex] = True          
    return sum(price)

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        u, w = list(map(int, input().split()))
        x.append(u)
        y.append(w)
    edges = []
    for i in range(0, n):
        for j in range(i + 1, n):
            weight = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((i, j, weight))
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]   
    for a, b, w in edges:
        adj[a].append(b)
        adj[b].append(a)
        cost[a].append(w)
        cost[b].append(w)
    print("{0:.9f}".format(Prim(n, adj, cost)))