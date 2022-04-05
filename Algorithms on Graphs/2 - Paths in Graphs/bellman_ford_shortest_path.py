def Bellman_Ford(adjacency_list, cost_list, start):
    distance = [float('inf') for _ in range(len(adjacency_list))]
    distance[start] = 0
    for _ in range(len(adjacency_list) - 1):
        for u in range(len(adjacency_list)):
            for v in adjacency_list[u]:
                index = adjacency_list[u].index(v)
                if distance[v] > distance[u] + cost_list[u][index]:
                    distance[v] = distance[u] + cost_list[u][index]
                    
    reserved = list(distance)
    
    for _ in range(2):
        for i in range(len(adjacency_list)):
            for j in adjacency_list[i]:
                index = adjacency_list[i].index(j)
                if distance[j] > distance[i] + cost_list[i][index]:
                    distance[j] = distance[i] + cost_list[i][index]

    return reserved, distance

def shortest_path(reserved, distance, start):
    for i in range(len(reserved)):
        if reserved[i] != distance[i]:
            print('-')
        elif i == start:
            print(0)
        elif distance[i] == float('inf'):
            print('*')
        else:
            print(distance[i])

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    start = int(input())
    start -= 1
    adjacency_list = [[] for _ in range(vertex)]
    cost_list = [[] for _ in range(vertex)]
    for a, b, w in edges:
        adjacency_list[a - 1].append(b - 1)
        cost_list[a - 1].append(w)
    reserved = Bellman_Ford(adjacency_list, cost_list, start)[0]
    distance = Bellman_Ford(adjacency_list, cost_list, start)[1]
    shortest_path(reserved, distance, start)