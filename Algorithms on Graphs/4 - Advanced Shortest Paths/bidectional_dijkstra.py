import heapq

def BiderectionalDijkstra(adj, adj_rev, cost, cost_rev, start, end):
    dist = [float('inf') for _ in range(len(adj))]
    dist_rev = [float('inf') for _ in range(len(adj))]
    prev = [None for _ in range(len(adj))]
    prev_rev = [None for _ in range(len(adj))]
    dist[start] = 0
    dist_rev[end] = 0
    proc = []
    proc_rev = []
    H = [(dist[start], start)]
    H_rev = [(dist_rev[end], end)]
    heapq.heapify(H)
    heapq.heapify(H_rev)
    while len(H) != 0 and len(H_rev) != 0:
        item = heapq.heappop(H)
        vertex = item[1]
        for i in range(0, len(adj[vertex])):
            if dist[adj[vertex][i]] > dist[vertex] + cost[vertex][i]:
                dist[adj[vertex][i]] = dist[vertex] + cost[vertex][i]
                prev[adj[vertex][i]] = vertex
                heapq.heappush(H, (dist[adj[vertex][i]], adj[vertex][i]))
        proc.append(vertex)
        if vertex in proc_rev:
            return shortest_path(start, dist, prev, proc, end, dist_rev, prev_rev, proc_rev)
        item = heapq.heappop(H_rev)
        vertex = item[1]
        for j in range(0, len(adj_rev[vertex])):
            if dist_rev[adj_rev[vertex][j]] > dist_rev[vertex] + cost_rev[vertex][j]:
                dist_rev[adj_rev[vertex][j]] = dist_rev[vertex] + cost_rev[vertex][j]
                prev_rev[adj_rev[vertex][j]] = vertex
                heapq.heappush(H_rev, (dist_rev[adj_rev[vertex][j]], adj_rev[vertex][j]))
        proc_rev.append(vertex)
        if vertex in proc:
            return shortest_path(start, dist, prev, proc, end, dist_rev, prev_rev, proc_rev)
    return -1

def shortest_path(start, dist, prev, proc, end, dist_rev, prev_rev, proc_rev):
    distance = float('inf')
    u_best = None
    for u in set(proc + proc_rev):
        if dist[u] + dist_rev[u] < distance:
            u_best = u
            distance = dist[u] + dist_rev[u]
    return distance

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    query = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(query)]
    adj = [[] for _ in range(vertex)]
    cost = [[] for _ in range(vertex)]
    adj_rev = [[] for _ in range(vertex)]
    cost_rev = [[] for _ in range(vertex)]
    for a, b, w in edges:
        adj[a - 1].append(b - 1)
        adj_rev[b - 1].append(a - 1)
        cost[a - 1].append(w)
        cost_rev[b - 1].append(w)
    for q1, q2 in queries:
        print(BiderectionalDijkstra(adj, adj_rev, cost, cost_rev, q1 - 1, q2 - 1))
