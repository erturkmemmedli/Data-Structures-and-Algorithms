import heapq
import math

def A_Star(adjacency_list, cost_list, coordinates, start, end):
        
    distance =[float('inf') for _ in range(len(adjacency_list))]
    distance[start] = 0
    
    parent = [None for _ in range(len(adjacency_list))]
    
    potential = [float('inf') for _ in range(len(adjacency_list))]
    potential[start] = 0
    
    H = [(potential[start], start)]
    heapq.heapify(H)
    
    while len(H) != 0:
        item = heapq.heappop(H)
        vertex = item[1]
        
        for i in range(len(adjacency_list[vertex])):
            if distance[adjacency_list[vertex][i]] > distance[vertex] + cost_list[vertex][i]:
                distance[adjacency_list[vertex][i]] = distance[vertex] + cost_list[vertex][i]
                heuristic = Heuristic(coordinates, adjacency_list[vertex][i], end, 'Euclidean')
                potential[adjacency_list[vertex][i]] = distance[vertex] + cost_list[vertex][i] + heuristic
                parent[adjacency_list[vertex][i]] = vertex
                heapq.heappush(H, (potential[adjacency_list[vertex][i]], adjacency_list[vertex][i]))       

        if vertex == end:
            return distance[vertex]
        
    return -1

def Heuristic(coordinates, vertex, end, kind):
    if kind == 'Euclidean':
        x1 = coordinates[vertex][0]
        y1 = coordinates[vertex][1]
        x2 = coordinates[end][0]
        y2 = coordinates[end][1]
        heuristic = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        
    if kind == 'Manhattan':
        x1 = coordinates[vertex][0]
        y1 = coordinates[vertex][1]
        x2 = coordinates[end][0]
        y2 = coordinates[end][1]
        heuristic = abs(x1-x2) + abs(y1-y2)
        
    if kind == 'Chebyshev':
        x1 = coordinates[vertex][0]
        y1 = coordinates[vertex][1]
        x2 = coordinates[end][0]
        y2 = coordinates[end][1]
        heuristic = max(abs(x1-x2), abs(y1-y2))
        
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
        
    for start, end in queries:
        if start == end:
            print(0)
        else:
            print(A_Star(adjacency_list, cost_list, coordinates, start - 1, end - 1))