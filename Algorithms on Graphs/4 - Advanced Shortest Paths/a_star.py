import heapq
import math

def A_Star(adjacency_list, cost_list, start, end, heurestic):  
    distance = [float('inf') for _ in range(len(adjacency_list))]
    distance[start] = 0
    
    parent = [None for _ in range(len(adjacency_list))]
    
    potential = [float('inf') for _ in range(len(adjacency_list))]
    if len(adjacency_list[start]) != 0:
        potential[start] = heuristic[start]
    
    H = [(potential[start], start)]
    heapq.heapify(H)
    
    while len(H) != 0:  
        item = heapq.heappop(H)
        vertex = item[1]

        for i in range(len(adjacency_list[vertex])):      
            if distance[adjacency_list[vertex][i]] > distance[vertex] + cost_list[vertex][i]:      
                distance[adjacency_list[vertex][i]] = distance[vertex] + cost_list[vertex][i]
                potential[adjacency_list[vertex][i]] = distance[vertex] + cost_list[vertex][i] + heuristic[vertex]
                parent[adjacency_list[vertex][i]] = vertex
                heapq.heappush(H, (potential[adjacency_list[vertex][i]], adjacency_list[vertex][i])) 
        if vertex == end:
            return distance[vertex]   
    return -1

def Heuristic(coordinates, edges, kind):
    if kind == 'Euclidean':
        heuristic = []
        for u, v, w in edges:
            x1 = coordinates[u - 1][0]
            y1 = coordinates[u - 1][1]
            x2 = coordinates[v - 1][0]
            y2 = coordinates[v - 1][1]
            heuristic.append(math.sqrt((x1-x2)**2 + (y1-y2)**2))
        
    if kind == 'Manhattan':
        heuristic = []
        for u, v, w in edges:
            x1 = coordinates[u - 1][0]
            y1 = coordinates[u - 1][1]
            x2 = coordinates[v - 1][0]
            y2 = coordinates[v - 1][1]
            heuristic.append(abs(x1-x2) + abs(y1-y2))
        
    if kind == 'Chebyshev':
        heuristic = []
        for u, v, w in edges:
            x1 = coordinates[u - 1][0]
            y1 = coordinates[u - 1][1]
            x2 = coordinates[v - 1][0]
            y2 = coordinates[v - 1][1]
            heuristic.append(max(abs(x1-x2), abs(y1-y2)))
        
    return heuristic

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    coordinates = [tuple(map(int, input().split())) for _ in range(vertex)]
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    query = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(query)]

    adjacency_list = [[] for _ in range(vertex)]
    cost_list = [[] for _ in range(vertex)]
    for a, b, w in edges:
        adjacency_list[a - 1].append(b - 1)
        cost_list[a - 1].append(w)
        
    heuristic = Heuristic(coordinates, edges, 'Manhattan')
    
    for start, end in queries:
        if start == end:
            print(0)
        else:
            print(A_Star(adjacency_list, cost_list, start - 1, end - 1, heuristic))