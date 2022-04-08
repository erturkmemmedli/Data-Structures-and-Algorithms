import heapq

def Dijkstra(adjacency_list, cost_list, start, end):
    distance = [float('inf') for _ in range(len(adjacency_list))]
    distance[start] = 0
    H = [(distance[start], start)]
    heapq.heapify(H)
    while len(H) != 0:
        item = heapq.heappop(H)
        vertex = item[1]
        for i in range(len(adjacency_list[vertex])):
            if distance[adjacency_list[vertex][i]] > distance[vertex] + cost_list[vertex][i]:
                distance[adjacency_list[vertex][i]] = distance[vertex] + cost_list[vertex][i]
                heapq.heappush(H, (distance[adjacency_list[vertex][i]], adjacency_list[vertex][i]))
        if vertex == end:
            return item[0]
    return -1

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    adjacency_list = [[] for _ in range(vertex)]
    cost_list = [[] for _ in range(vertex)]
    for a, b, w in edges:
        adjacency_list[a - 1].append(b - 1)
        cost_list[a - 1].append(w)
    print(Dijkstra(adjacency_list, cost_list, start, end))
