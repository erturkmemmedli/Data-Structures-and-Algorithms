def Bellman_Ford(adjacency_list, cost_list):
    distance = [10**19 for _ in range(len(adjacency_list))]
    distance[0] = 0
    for _ in range(len(adjacency_list) - 1):
        for u in range(len(adjacency_list)):
            for v in adjacency_list[u]:
                index = adjacency_list[u].index(v)
                if distance[v] > distance[u] + cost_list[u][index]:
                    distance[v] = distance[u] + cost_list[u][index]
                    
    reserved = list(distance)
                    
    for i in range(len(adjacency_list)):
        for j in adjacency_list[i]:
            index = adjacency_list[i].index(j)
            if distance[j] > distance[i] + cost_list[i][index]:
                distance[j] = distance[i] + cost_list[i][index]

    return 0 if reserved == distance else 1

if __name__ == '__main__':
    vertex, edge = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge)]
    adjacency_list = [[] for _ in range(vertex)]
    cost_list = [[] for _ in range(vertex)]
    for a, b, w in edges:
        adjacency_list[a - 1].append(b - 1)
        cost_list[a - 1].append(w)
    print(Bellman_Ford(adjacency_list, cost_list))
